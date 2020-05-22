<template>
  <div>
  <div class='columns is-mobile is-multiline is-centered'>
    <template  v-for="item in blocks">
      <div v-bind:key="item.id"  class='column is-3-tablet is-6-mobile is-one-fifth-desktop'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
                  <EditorUI
                    :pin="item"
                    :currentUsername="editorMeta.user.meta.username"
                    :currentBoard="editorMeta.currentBoard"
                    v-on:pin-delete-succeed="reset"
                    v-on:pin-remove-from-board-succeed="reset"
                  ></EditorUI>
                  <img :src="item.url"
                     @load="onPinImageLoaded(item.id)"
                     @click="openPreview(item, editorMeta.user)"
                     alt="item.description">
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <template v-for="tag in item.tags">
              <span v-bind:key="tag" class='tag is-warning subtitle'>
                <router-link :to="{ name: 'tag', params: {tag: tag} }"
                           params="{tag: tag}">{{ tag }}</router-link>
              </span>
                </template>
              <p>Personal Notes </p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item' @click="addToBoard">添加</a>
            <a class='card-footer-item'>删除</a>
            <a class='card-footer-item'>编辑</a>
          </footer>
        </div>
      </div>
      </template>
     </div>
    <Pagination :page-config="pageConfigTotal" @changeCurrentPage="changePage"></Pagination>
  </div>
</template>

<script>
import API from './api';
import pinHandler from './utils/PinHandler';
import PinPreview from './PinPreview.vue';
import Pagination from './Pagination.vue';
import modals from './modals';
import EditorUI from './editors/PinEditorUI.vue';

function createImageItem(like) {
  const image = {};
  image.url = pinHandler.escapeUrl(like.pin.image.thumbnail.image);
  image.id = like.pin.id;
  image.owner_id = like.pin.submitter.id;
  image.private = like.pin.private;
  image.checking = like.pin.check;
  image.description = like.pin.description;
  image.tags = like.pin.tags;
  image.author = like.pin.submitter.username;
  image.avatar = `//gravatar.com/avatar/${like.pin.submitter.gravatar}`;
  image.large_image_url = pinHandler.escapeUrl(like.pin.image.image);
  image.original_image_url = like.pin.url;
  image.referer = like.pin.referer;
  image.orgianl_width = like.pin.image.width;
  image.style = {
    width: `${like.pin.image.thumbnail.width}px`,
    height: `${like.pin.image.thumbnail.height}px`,
  };
  image.published = like.pin.published;
  image.class = {};
  return image;
}

function initialData() {
  return {
    blocks: [],
    blocksMap: {},
    status: {
      loading: false,
      hasNext: true,
      offset: 0,
    },
    editorMeta: {
      currentEditId: null,
      currentBoard: {},
      user: {
        loggedIn: false,
        meta: {},
      },
    },
    listQuery: {
      page: 1,
      limit: 5,
    },
    pageConfigTotal: {
      total: 10,
      pageSize: 5,
      pageNo: 1,
    },
  };
}

export default {
  name: 'pins',
  components: {
    Pagination,
    EditorUI,
  },
  data() {
    return initialData();
  },
  props: {
    pinFilters: {
      type: Object,
      default() {
        return {
          tagFilter: null,
          userFilter: null,
          boardFilter: null,
        };
      },
    },
  },
  watch: {
    pinFilters() {
      this.reset();
    },
  },
  methods: {
    addToBoard() {
      modals.openAdd2Board(this, this.item, this.currentUsername);
    },
    editPin() {
      const props = {
        username: this.currentUsername,
        existedPin: this.pin,
        isEdit: true,
      };
      modals.openPinEdit(
        this,
        props,
      );
    },
    deletePin() {
      this.$buefy.dialog.confirm({
        message: 'Delete this Pin?',
        onConfirm: () => {
          API.Pin.deleteById(this.pin.id).then(
            () => {
              this.$buefy.toast.open('Pin deleted');
              this.$emit('pin-delete-succeed', this.pin.id);
            },
            () => {
              this.$buefy.toast.open(
                { type: 'is-danger', message: 'Failed to delete Pin' },
              );
            },
          );
        },
      });
    },
    // 是否显示审核状态标签
    shouldShowIsChecking(checking) {
      if (!this.editorMeta.user.loggedIn) {
        return false;
      }
      return checking === 0;
    },
    showEditButtons(id) {
      this.editorMeta.currentEditId = id;
    },
    hideEditButtons() {
      this.editorMeta.currentEditId = null;
    },
    onPinImageLoaded(itemId) {
      this.blocksMap[itemId].class = {
        'image-loaded': true,
      };
      this.blocksMap[itemId].style.height = 'auto';
    },
    buildBlocks(results) {
      const blocks = [];
      results.forEach(
        (like) => {
          const item = createImageItem(like);
          blocks.push(
            item,
          );
        },
      );
      return blocks;
    },
    openPreview(pinItem, user) {
      this.$buefy.modal.open(
        {
          parent: this,
          component: PinPreview,
          props: {
            pinItem,
            user,
          },
          scroll: 'keep',
          customClass: 'pin-preview-at-home',
        },
      );
    },
    shouldFetchMore(created) {
      if (!created) {
        if (this.status.loading) {
          return false;
        }
        if (!this.status.hasNext) {
          return false;
        }
      }
      return true;
    },
    initialize() {
      this.initializeMeta();
      this.getLikes();
    },
    initializeMeta() {
      const self = this;
      API.User.fetchUserInfo().then(
        (user) => {
          if (user === null) {
            self.editorMeta.user.loggedIn = false;
            self.editorMeta.user.meta = {};
          } else {
            self.editorMeta.user.meta = user;
            self.editorMeta.user.loggedIn = true;
          }
        },
      );
    },
    changePage(page) {
      this.blocks = [];
      this.listQuery.page = page;
      this.getLikes(page, this.listQuery.limit);
    },
    getLikes() {
      const promise = API.getAllLikes(this.listQuery.page, this.listQuery.limit);
      promise.then(
        (resp) => {
          const like = resp.data.items;
          this.total = resp.data.total;
          console.log('like', like);
          let newBlocks = this.buildBlocks(like);
          console.log('newBlocks', newBlocks);

          newBlocks = this.blocks.concat(newBlocks);
          this.blocks = newBlocks;
        },
      );
    },
  },
  created() {
    this.initialize();
  },
};
</script>

<style lang="scss" scoped>

/* card */
$pin-footer-position-fix: -10px;
$avatar-width: 15px;
$avatar-height: 15px;
@import './utils/fonts';
@import './utils/loader.scss';

.pin-card{
  .pin-preview-image {
    cursor: zoom-in;
    border-radius: 12px 12px 0 0;
    width: 100%;
  }
  > img {
    min-width: 100%;
    background-color: white;
    // border-radius: 25px 25px 25px 25px;
    @include loader('../assets/loader.gif');
  }
  .avatar {
    height: $avatar-height;
    width: $avatar-width;
    border-radius: 3px;
    margin-left: 5px;
  }
  .pin-tag {
    margin-right: 0.2rem;
  }
}
.pin-footer {
  position: relative;
  top: $pin-footer-position-fix;
  background-color: white;
  border-radius: 0 0 12px 12px ;
  box-shadow: 0 2px 0 #bbb;
  .description {
    @include description-font;
    padding: 5px;
    border-bottom: 1px solid #DDDDDD;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .details {
    @include secondary-font;
    padding: 2px;
    border-radius: 0 0 25px 25px;
    > .pin-info {
      line-height: 16px;
      width: 100%;
      padding-left: $avatar-width + 2px;
    }
    .pin-info a {
      font-weight: bold;
    }
  }
}

@import 'utils/grid-layout';
@include screen-grid-layout("#pins-container")

</style>
