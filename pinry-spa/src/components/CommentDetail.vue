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
        <div class="name">
          <strong>{{ comment.author }}</strong>
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
  },
};
</script>

<style scoped>

</style>
