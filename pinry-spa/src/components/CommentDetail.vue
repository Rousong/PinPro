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
          {{ comment.author }}
        </div>
        <div class="time">
          {{ comment.published| formatDate('yyyy-MM-dd hh:mm:ss') }}
        </div>
      </div>
    </div>
    <div class="comment-detail" v-html="marked(comment.content)" />
  </div>
<!--  <div class="box">-->
<!--            <article class="media">-->
<!--              <div class="media-left">-->
<!--                <figure class="image is-32x32">-->
<!--                  <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">-->
<!--                </figure>-->
<!--              </div>-->
<!--              <div class="media-content">-->
<!--                <div class="content">-->
<!--                  <p>-->
<!--                    <strong>{{ comment.author }}</strong> <small>{{ comment.published| formatDate('yyyy-MM-dd hh:mm:ss') }}</small>-->
<!--                    <br>-->
<!--                    {{comment.content}}-->
<!--                  </p>-->
<!--                </div>-->
<!--&lt;!&ndash;                <nav class="level is-mobile">&ndash;&gt;-->
<!--&lt;!&ndash;                  <div class="level-left">&ndash;&gt;-->
<!--&lt;!&ndash;                    <a class="level-item" aria-label="reply">&ndash;&gt;-->
<!--&lt;!&ndash;                      <span class="icon is-small">&ndash;&gt;-->
<!--&lt;!&ndash;                        <i class="fas fa-reply" aria-hidden="true"></i>&ndash;&gt;-->
<!--&lt;!&ndash;                      </span>&ndash;&gt;-->
<!--&lt;!&ndash;                    </a>&ndash;&gt;-->
<!--&lt;!&ndash;                  </div>&ndash;&gt;-->
<!--&lt;!&ndash;                </nav>&ndash;&gt;-->
<!--              </div>-->
<!--            </article>-->
<!--          </div>-->
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
