<template>
  <div class="comment-list">
    <div class="top-title">
      <span>{{ total }} {{$t("comment.total")}}</span>&nbsp;&nbsp;
      <button class="button is-warning is-small is-outlined" v-show= "!loading" @click="refreshComments">{{$t("comment.reflash")}}</button>
      <img src='../assets/loading.gif' v-show="loading">
    </div>
    <div v-if="this.user.loggedIn">
    <div class="field">
            <div class="control">
              <strong>{{form.author}}</strong>
              <textarea v-model="form.content" :options="{hideModeSwitch:true,previewStyle:'tab'}"  class="textarea" rows="2" :placeholder="$t('comment.saySth')"></textarea>
              <strong style="color: #fc2e5a">{{message}}</strong>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-warning is-fullwidth" @click="onSubmit(form)">{{$t("comment.submit")}}</button>
            </div>
          </div>
    </div>
    <div v-else>
      <button class="button is-danger is-fullwidth"  @click="logIn">{{$t("comment.login")}}</button>
    </div>
    <div v-for="(item, i) in comments" :key="i" class="item">
      <comment-detail :comment="item"/>
      <div class="item-comment">
          <!-- 第二层回复 -->
         <div class="time">
          {{ item.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
           <button class="button is-warning is-small is-outlined"  @click="showCommentModal(item.id, item.content, 2)">{{$t("comment.reply")}}</button>
        </div>
      </div>
      <div v-for="(e, i2) in item.sub_comment" :key="i2" class="item-other">
        <comment-detail :comment="e" />
        <!-- 第三层回复 -->
        <div class="time">
          {{ e.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
           <button class="button is-warning is-small is-outlined"  @click="showCommentModal(e.id, e.content, 3)">{{$t("comment.reply")}}</button>
        </div>
        <div v-for="(j, i3) in e.sub_comment" :key="i3" class="item-other">
          <comment-detail :comment="j"/>
          <div class="time">
          {{ j.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
        </div>
        </div>
      </div>
    </div>
    <div>
      <Pagination :page-config="pageConfigTotal" @changeCurrentPage="changePage"></Pagination>
    </div>
    <div class="modal" :class="{ 'is-active': isActive }">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title"><span>{{$t("comment.reply")}}：{{ sub_content }}</span></p>
      <button class="delete" aria-label="close" @click="close"></button>
    </header>
    <section class="modal-card-body">
      <!-- Content ... -->
      <div class="field">
            <div class="control">
              <strong>{{sub_form.author}}</strong>
              <textarea v-model="sub_form.content"  class="textarea" rows="2" :placeholder="$t('comment.saySth')"></textarea>
              <p>{{message}}</p>
            </div>
          </div>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-warning" @click="onSubmit(sub_form)">{{$t("comment.submit")}}</button>
      <button class="button" @click="close()">{{$t("comment.cancle")}}</button>
    </footer>
  </div>
</div>
  </div>
</template>

<script>
import API from './api';
import CommentDetail from './CommentDetail.vue';
import Pagination from './Pagination.vue';
import modals from './modals';

export default {
  name: 'Comments',
  components: { CommentDetail, Pagination },
  data() {
    return {
      isActive: false,
      message: null,
      comments: [],
      total: 0,
      id: this.pin.id,
      form: {
        content: '',
        author: this.user.meta.username,
        pin: this.pin.id,
      },
      sub_content: null,
      level: null,
      sub_form: {
        content: '',
        author: this.user.meta.username,
        parent_comment: null,
      },
      pageConfigTotal: {
        total: 10,
        pageSize: 5,
        pageNo: 1,
      },
      listQuery: {
        page: 1,
        limit: 5,
        pin: null,
      },
      loading: false,
    };
  },
  props: ['pin', 'user'],
  created() {
    this.getList(this.listQuery);
  },
  methods: {
    getList() {
      this.listQuery.pin = this.pin.id;
      this.loading = true;
      API.getComments(this.listQuery.pin, this.listQuery.page, this.listQuery.limit).then((resp) => {
        this.comments = resp.data.items;
        this.total = resp.data.total;
        this.pageConfigTotal.total = resp.data.total;
        setTimeout(() => {
          this.loading = false;
        }, 200);
      });
    },
    showCommentModal(parentCommentId, subContent, level) {
      if (!this.user.loggedIn) {
        modals.openLogin(this, this.onLoginSucceed);
      } else {
        this.isActive = true;
        this.sub_form.parent_comment = parentCommentId;
        this.sub_content = subContent;
        this.level = level;
        this.sub_form.content = '';
      }
    },
    onSubmit(comment) {
      if (comment.content === '') {
        this.message = this.$i18n.t('comment.blankWarn');
        return;
      }
      API.createComment(comment).then((resp) => {
        const data = resp.items;
        if (comment.pin) {
          // 一级评论
          this.comments.unshift(data);
        } else if (this.level === 3) {
          // 三级评论
          this.comments.forEach((x) => {
            x.sub_comment.forEach((xs) => {
              if (xs.id === data.parent_comment) {
                xs.sub_comment.unshift(data);
              }
            });
          });
        } else if (this.level === 2) {
          // 二级评论
          this.comments.forEach((x) => {
            if (x.id === data.parent_comment) {
              x.sub_comment.unshift(data);
            }
          });
        }
        this.message = null;
        this.form.content = null;
        this.isActive = false;
      });
    },
    refreshComments() {
      this.getList(this.listQuery);
    },
    changePage(page) {
      this.listQuery.page = page;
      this.getList(this.listQuery.pin, page, this.listQuery.limit);
    },
    logIn() {
      modals.openLogin(this, this.onLoginSucceed);
    },
    close() {
      this.isActive = false;
    },
    onLoginSucceed() {
      this.initializeUser(true);
    },
  },
};
</script>

<style lang="scss" scoped>
.comment-list {
  text-align: center;
}
.comment-list {
  position: relative;
  text-align: left;
  padding-top: 30px;
  margin-top: 30px;
  border-top: 1px solid #eee;
  .avatar {
    position: absolute;
    left: 0px;
  }
  .el-icon-circle-plus {
    font-size: 40px;
  }
}
.clearfix {
  clear: both;
}
.comment-list {
  margin-top: 30px;
  .top-title {
    padding-bottom: 20px;
    font-size: 17px;
    font-weight: 700;
    border-bottom: 1px solid #f0f0f0;
  }
  .item {
    padding: 10px 0 15px;
    border-bottom: 1px solid #f0f0f0;
    .time {
      font-size: 12px;
      color: #969696;
    }
    .comment-detail {
      min-height: 40px;
    }
    .item-comment {
      .like {
        margin-right: 20px;
      }
    }
  }
}
.item-other {
  margin: 5px;
  padding-left: 20px;
  border-left: 1px solid #f0f0f0;
  .item-header {
    position: relative;
    padding-left: 45px;
    padding-bottom: 10px;
    .author {
      position: absolute;
      left: 0;
      display: inline-block;
      .avatar {
        display: inline-block;
        margin-right: 5px;
        width: 38px;
        height: 38px;
        vertical-align: middle;
        img {
          width: 100%;
          height: 100%;
          border-radius: 50%;
        }
      }
    }
    .info {
      display: inline-block;
      .name {
        font-size: 15px;
        color: #333;
      }
      .time {
        font-size: 12px;
        color: #969696;
      }
    }
  }
  .comment-detail {
    min-height: 40px;
    border-bottom: 1px dashed #f0f0f0;
  }
  .message {
    padding: 10px;
  }
}
</style>
