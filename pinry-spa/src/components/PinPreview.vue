<template>
  <section class="section" style="background: rgb(255,255,255)">
  <div class="container">
    <div class="columns">
      <div class="column is-6"><img :src="pinItem.large_image_url" alt="" @click="showImg">
      <div class="card-content">
            <div class="content">
                <p class="description">{{ pinItem.description }}</p>
            </div>
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="pinItem.avatar" alt="Image">
                </figure>
              </div>
              <div class="is-pulled-left">
                  <p class="title is-6 pin-meta-info"><span class="dim">{{$t("pins.PinnedBy")}}&nbsp;&nbsp;</span>
                    <span class="author">{{ pinItem.author }}</span>
                    <span v-if="hasLiked" class="icon heart" @click="deleteCollect()" style="color:Tomato">
                      <i v-show= "!loading" class="fas fa-heart fa-3x "></i><img src='../assets/loader.gif' v-show="loading"></span>
                    <span v-else class="icon heart" @click="addCollect()">
                      <i v-show= "!loading" class="far fa-heart fa-3x "></i><img src='../assets/loader.gif' v-show="loading"></span>
                      <small><span class="dim" v-show="pinItem.likes_num>0">&nbsp;&nbsp;{{ pinItem.likes_num |formatNum(pinItem.likes_num)}}</span></small>
                  </p>
                <div class="is-pulled-left">
                  <p class="subtitle is-10" v-show="pinItem.tags.length > 0">
                    <span class="subtitle dim">{{$t("pins.Tags")}}&nbsp;</span>
                    <template v-for="tag in pinItem.tags">
                      <button v-bind:key="tag" class="button is-small is-link pin-preview-tag" @click="closeAndGoToFilter(tag)">{{ tag }}</button>
                    </template>
                  </p>
                  <div class="time">
                    {{ pinItem.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
                  </div>
                </div>
              </div>
            </div>
        <hr />
            <div class="media-content">
                <div class="is-pulled-left">
                  <a :href="pinItem.referer" target="_blank">
                    <b-button
                        v-show="pinItem.referer !== null"
                        class="meta-link is-small"
                        type="is-warning">
                      {{$t("pinPreview.Referer")}}
                    </b-button>
                  </a>
                  <a :href="pinItem.original_image_url" target="_blank">
                    <b-button
                        v-show="pinItem.original_image_url !== null"
                        class="meta-link is-small"
                        type="is-link">
                        {{$t("pinPreview.OriginalImage")}}
                    </b-button>
                  </a>
                  <b-button
                      @click="closeAndGoTo"
                      class="meta-link is-small"
                      type="is-success">
                      {{$t("pinPreview.GotoPinLink")}}
                  </b-button>
                </div>
              </div>
          </div>
      </div>
      <div class="modal" :class="{ 'is-active': isActive }" @click="close">
            <div class="modal-background"></div>
            <div class="modal-content">
              <p class="image">
                <img :src="pinItem.large_image_url" alt="">
              </p>
            </div>
            <button class="modal-close is-large" aria-label="close" @click="close"></button>
        </div>
      <div class="column is-6">
          <comment-list :pin="pinItem" :user="user"></comment-list>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import API from './api';
import modals from './modals';
import commentList from './Comments.vue';

function initialData() {
  return {
    hasLiked: false,
    userLoggedIn: false,
    isActive: false,
    loading: false,
  };
}

export default {
  name: 'PinPreview',
  data() {
    return initialData();
  },
  components: { commentList },
  props: ['pinItem', 'user'],
  methods: {
    closeAndGoTo() {
      this.$parent.close();
      this.$router.push(
        { name: 'pin', params: { pinId: this.pinItem.id } },
      );
    },
    addCollect() { // 点赞
      if (!this.user.loggedIn) {
        modals.openLogin(this, this.onLoginSucceed);
      }
      this.loading = true;
      API.addLike({
        pin: this.pinItem.id,
      }).then(() => {
        this.hasLiked = true;
        this.loading = false;
        this.pinItem.likes_num += 1;
      }).catch((error) => {
        console.log(error);
      });
    },
    deleteCollect() {
    // 取消点赞
      this.loading = true;
      API.delLike(this.pinItem.id).then(() => {
        this.hasLiked = false;
        this.loading = false;
        this.pinItem.likes_num -= 1;
      }).catch((error) => {
        console.log(error);
      });
    },
    checkLikeFlg() {
      API.checkIfLike(this.pinItem.id).then(() => {
        this.hasLiked = true;
      }).catch(() => {
        console.log('Not liked');
      });
    },
    onLoginSucceed() {
      this.initializeUser(true);
    },
    closeAndGoToFilter(tag) {
      this.$parent.close();
      this.$router.push(
        { name: 'tag', params: { tag } },
      );
    },
    showImg() {
      this.isActive = true;
    },
    close() {
      this.isActive = false;
    },
  },
  created() {
    if (this.user.loggedIn) {
      this.checkLikeFlg();
    }
  },
};
</script>

<style lang="scss" scoped>
@import './utils/fonts.scss';

.meta-link {
  margin-left: 0.3rem;
}
.dim {
  @include secondary-font-color-in-dark;
}
.pin-meta-info {
  line-height: 5px;
}
.card {
  background-color: rgba(0, 0, 0, 0.6);
  .content {
    border-bottom: 1px solid #333;
  }
  .card-content {
    .author {
      @include title-font-color-in-dark;
    }
    padding: 0;
    .content {
      padding: 0.3rem;
      margin-bottom: 0;
    }
    .media {
      padding: 0.3rem;
    }
  }
  .description {
    @include title-font;
    @include title-font-color-in-dark;
    font-size: 16px;
    padding: 8px;
  }
}
.pin-preview-tag {
  margin-right: 0.2rem;
  margin-bottom: 2px;
}
/* preview size should always less then screen */
.image {
  margin: auto;
  max-width: 1000px;
}

.heart{
  margin-left: 30px;
}
</style>
