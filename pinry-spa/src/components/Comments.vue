<template>
  <div class="comment-list">
    <div class="top-title">
      <span>{{ total }} 条评论</span>
      <button type="primary" :loading="loading" @click="refreshComments">刷新评论</button>
    </div>
    <div v-for="(item, i) in comments" :key="i" class="item">
      <comment-detail :comment="item" />
      <div class="item-comment">
        <div class="message">
          <!-- 第二层回复 -->
          <button size="small" @click="showCommentModal(item.id, item.content, 2)">回复</button>
        </div>
      </div>
      <div v-for="(e, i2) in item.sub_comment" :key="i2" class="item-other">
        <comment-detail :comment="e" />
        <!-- 第三层回复 -->
        <button size="small" @click="showCommentModal(e.id, e.content, 3)">回复</button>
        <div v-for="(j, i3) in e.sub_comment" :key="i3" class="item-other">
          <comment-detail :comment="j" />
        </div>
      </div>
    </div>
<!--    <pagination-->
<!--      v-show="total>0"-->
<!--      :total="total"-->
<!--      :page.sync="listQuery.page"-->
<!--      :limit.sync="listQuery.limit"-->
<!--      @pagination="getList"-->
<!--    />-->
    <div :body-style="{ padding: '5px', height: '300px' }">
      <div slot="header">
        <span>欢迎评论：</span>
      </div>
      <!-- card body -->
      <div>
    <input v-model="form.author" placeholder="用户名" />
    <input v-model="form.content" :options="{hideModeSwitch:true,previewStyle:'tab'}" height="180px" />
    </div>
      <button type="primary" @click="onSubmit(form)">立即评论</button>
    </div>
<!--    =================================-->
    <div
      :visible.sync="seen"
      width="90%"
      @close="!seen"
    >
      <span>回复给：{{ sub_content }}</span>
       <div>
    <input v-model="sub_form.author" placeholder="用户名" />
    <input v-model="sub_form.content" :options="{hideModeSwitch:true,previewStyle:'tab'}" height="180px" />
  </div>
      <button type="primary" @click="onSubmit(sub_form)">立即回复</button>
    </div>
  </div>
</template>

<script>
import API from './api';
import CommentDetail from './CommentDetail.vue';

export default {
  name: 'Comments',
  components: { CommentDetail },
  data() {
    return {
      seen: false,
      comments: [],
      total: 0,
      id: this.pin.id,
      form: {
        content: 'sm syi**sorry**',
        author: this.user.meta.id,
        pin: this.pin.id,
      },
      sub_content: null,
      level: null,
      sub_form: {
        content: '子评论content',
        author: this.user.meta.id,
        parent_comment: null,
      },
      listQuery: {
        pin: null,
      },
      loading: false,
    };
  },
  props: ['pin', 'user'],
  created() {
    this.getList(this.listQuery);
    console.log(this.pin);
  },
  methods: {
    getList(listQuery) {
      this.listQuery.pin = this.pin.id;
      console.log(listQuery);
      this.loading = true;
      API.getComments(this.listQuery.pin).then((resp) => {
        this.comments = resp.data.results;
        console.log(this.comments);
        this.total = resp.data.total;
        console.log(this.total);
        setTimeout(() => {
          this.loading = false;
        }, 200);
      });
    },
    showCommentModal(parentCommentId, subContent, level) {
      this.sub_form.parent_comment = parentCommentId;
      this.sub_content = subContent;
      this.level = level;
      this.seen = true;
    },
    onSubmit(comment) {
      API.createComment(comment).then((resp) => {
        // this.$message({
        //   message: '保存成功',
        //   type: 'success',
        //   showClose: true,
        //   duration: 1000,
        // });
        this.seen = false;
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
      });
    },
    refreshComments() {
      this.getList(this.listQuery);
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
    padding: 20px 0 30px;
    border-bottom: 1px solid #f0f0f0;
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
          width: 40px;
          height: 40px;
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
    }
    .item-comment {
      .like {
        margin-right: 20px;
      }
    }
  }
}
.item-other {
  margin: 20px;
  padding: 10px;
  border-left: 2px solid #f0f0f0;
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
