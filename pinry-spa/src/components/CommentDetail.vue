<template>
  <div>
    <div class="item-header">
      <div class="author">
        <div class="avatar">
<!--          <img src="baseUrl + comment.author.gravatar" alt="avatar">-->
<!--          {{comment.author.gravatar}}-->
        </div>
      </div>
      <div class="info">
        <div class="name" data-dismiss="modal">
          <router-link :to="{ name: 'user', params: {user: comment.author} }">
            <strong @click="closeAndGoTo">{{ comment.author }}</strong>
          </router-link>
        </div>
      </div>
    </div>
    <div class="comment-detail" v-html="marked(comment.content)" />
  </div>
</template>

<script>

export default {
  props: {
    comment: {
      type: Object,
      required: true,
    },
  },
  methods: {
    marked(content) {
      return content;
    },
    closeAndGoTo() {
      this.$buefy.dialog.confirm({
        message: this.$i18n.t('comment.toUser'),
        onConfirm: () => {
          this.$parent.$parent.$parent.close();
          this.$router.push({ name: 'user', params: { user: this.comment.author } });
        },
      });
    },
  },
};
</script>

<style scoped>

</style>
