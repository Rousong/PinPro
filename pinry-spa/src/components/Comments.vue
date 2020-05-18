<template>
  <div class="comment-list">
    <div class="top-title">
      <span>{{ total }} 条评论</span>&nbsp;&nbsp;
      <button class="button is-primary is-small is-outlined" :loading="loading" @click="refreshComments">刷新评论</button>
    </div>
    <div v-if="this.user.loggedIn">
    <div class="field">
            <div class="control">
              <strong>{{form.author}}</strong>
              <textarea v-model="form.content" :options="{hideModeSwitch:true,previewStyle:'tab'}"  class="textarea" rows="2" placeholder="Write something..."></textarea>
              <p>{{message}}</p>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-primary is-fullwidth" @click="onSubmit(form)">Submit</button>
            </div>
          </div>
    </div>
    <div v-else>
      <button class="button is-danger is-fullwidth"  @click="logIn">登陆后评论</button>
    </div>
    <div v-for="(item, i) in comments" :key="i" class="item">
      <comment-detail :comment="item"/>
      <div class="item-comment">
          <!-- 第二层回复 -->
         <div class="time">
          {{ item.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
           <button class="button is-primary is-small is-outlined"  @click="showCommentModal(item.id, item.content, 2)">回复</button>
        </div>
      </div>
      <div v-for="(e, i2) in item.sub_comment" :key="i2" class="item-other">
        <comment-detail :comment="e" />
        <!-- 第三层回复 -->
        <div class="time">
          {{ e.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
           <button class="button is-primary is-small is-outlined"  @click="showCommentModal(e.id, e.content, 3)">回复</button>
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
      <p class="modal-card-title"><span>回复给：{{ sub_content }}</span></p>
      <button class="delete" aria-label="close" @click="close"></button>
    </header>
    <section class="modal-card-body">
      <!-- Content ... -->
      <div class="field">
            <div class="control">
              <strong>{{sub_form.author}}</strong>
              <textarea v-model="sub_form.content"  class="textarea" rows="2" placeholder="Write something..."></textarea>
              <p>{{message}}</p>
            </div>
          </div>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-primary" @click="onSubmit(sub_form)">Submit</button>
      <button class="button" @click="close()">Cancel</button>
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
    console.log('user', this.user.loggedIn);
    console.log(this.pin);
  },
  methods: {
    getList(listQuery) {
      this.listQuery.pin = this.pin.id;
      console.log(listQuery);
      this.loading = true;
      API.getComments(this.listQuery.pin, this.listQuery.page, this.listQuery.limit).then((resp) => {
        this.comments = resp.data.items;
        console.log('comments', resp.data.items);
        this.total = resp.data.total;
        this.pageConfigTotal.total = resp.data.total;
        console.log('total', resp.data.total);
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
        console.log('this.sub_contentt', this.sub_content);
      }
    },
    onSubmit(comment) {
      if (comment.content === '') {
        this.message = 'wocaomeitian';
        return;
      }
      API.createComment(comment).then((resp) => {
        // this.$message({
        //   message: '保存成功',
        //   type: 'success',
        //   showClose: true,
        //   duration: 1000,
        // });
        const data = resp.items;
        console.log('data ', data);
        if (comment.pin) {
          // 一级评论
          this.comments.unshift(data);
          console.log('add 1 level');
        } else if (this.level === 3) {
          // 三级评论
          this.comments.forEach((x, i, comments) => {
            console.log(i, x, comments);
            x.sub_comment.forEach((xs, j, c) => {
              console.log(j, xs, c);
              if (xs.id === data.parent_comment) {
                xs.sub_comment.unshift(data);
                // console.log('add 3 level')
              }
            });
          });
          console.log('level 3');
        } else if (this.level === 2) {
          // 二级评论
          this.comments.forEach((x, i, comments) => {
            console.log(i, comments);
            if (x.id === data.parent_comment) {
              x.sub_comment.unshift(data);
              console.log('add 2 level');
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
