<template>
  <div>
    <div class="item-header">
      <div class="author">
        <div class="avatar">
          <img src="" alt="avatar">
        </div>
      </div>
      <div class="info">
        <div class="name">
          {{ comment.user }}
        </div>
        <div class="time">
          {{ comment.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
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
