<template>
  <section class="section" style="background: rgb(255,255,255)">
  <div class="container">
    <div class="columns">
      <div class="column is-6"><img :src="pinItem.large_image_url" alt="">
      <div class="card-content">
            <div class="content">
                <p class="description title">{{ pinItem.description }}</p>
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
                    <span v-if="hasLiked" class="icon heart" @click="deleteCollect()" style="color:Tomato"><i class="fas fa-heart fa-3x "></i></span>
                    <span v-else class="icon heart" @click="addCollect()"><i class="far fa-heart fa-3x "></i></span>
                  </p>
                <div class="is-pulled-left">
                  <p class="subtitle is-10" v-show="pinItem.tags.length > 0">
                    <span class="subtitle dim">in&nbsp;</span>
                    <template v-for="tag in pinItem.tags">
                      <b-tag v-bind:key="tag" type="is-info" class="pin-preview-tag">{{ tag }}</b-tag>
                    </template>
                  </p>
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

      <div class="column is-6">
         <h2 class="title has-text-centered">Comments</h2>
        <form>
          <div class="field">
            <div class="control">
              <input class="input" type="email" placeholder="Email">
            </div>
          </div>
<!--          <div class="field">-->
<!--            <div class="select is-fullwidth">-->
<!--              <select>-->
<!--                <option disabled="" selected="">Select product</option>-->
<!--                <option>Product 1</option>-->
<!--                <option>Product 2</option>-->
<!--                <option>Product 3</option>-->
<!--              </select>-->
<!--            </div>-->
<!--          </div>-->
          <div class="field">
            <div class="control">
              <textarea class="textarea" rows="3" placeholder="Write something..."></textarea>
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-primary is-fullwidth" type="submit">Submit</button>
            </div>
          </div>
        </form>
        <div>
          <hr />
          <div class="box">
            <article class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                </figure>
              </div>
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>Yao怀恩</strong> <small>@Weien</small> <small>31m</small>
                    <br>
                    澳门皇家赌场上线啦
                  </p>
                </div>
                <nav class="level is-mobile">
                  <div class="level-left">
                    <a class="level-item" aria-label="reply">
                      <span class="icon is-small">
                        <i class="fas fa-reply" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="retweet">
                      <span class="icon is-small">
                        <i class="fas fa-retweet" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="like">
                      <span class="icon is-small">
                        <i class="fas fa-heart" aria-hidden="true"></i>
                      </span>
                    </a>
                  </div>
                </nav>
              </div>
            </article>
          </div>
          <div class="box">
            <article class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                </figure>
              </div>
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>临危</strong> <small>@beforeDanger</small> <small>31m</small>
                    <br>
                    好人一生平安
                  </p>
                </div>
                <nav class="level is-mobile">
                  <div class="level-left">
                    <a class="level-item" aria-label="reply">
                      <span class="icon is-small">
                        <i class="fas fa-reply" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="retweet">
                      <span class="icon is-small">
                        <i class="fas fa-retweet" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="like">
                      <span class="icon is-small">
                        <i class="fas fa-heart" aria-hidden="true"></i>
                      </span>
                    </a>
                  </div>
                </nav>
              </div>
            </article>
          </div>
          <div class="box">
            <article class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                </figure>
              </div>
              <div class="media-content">
                <div class="content">
                  <p>
                    <strong>马啸玉</strong> <small>@LittlePony</small> <small>31m</small>
                    <br>
                    会说话就多讲两句
                  </p>
                </div>
                <nav class="level is-mobile">
                  <div class="level-left">
                    <a class="level-item" aria-label="reply">
                      <span class="icon is-small">
                        <i class="fas fa-reply" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="retweet">
                      <span class="icon is-small">
                        <i class="fas fa-retweet" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="like">
                      <span class="icon is-small">
                        <i class="fas fa-heart" aria-hidden="true"></i>
                      </span>
                    </a>
                  </div>
                </nav>
              </div>
            </article>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import API from './api';
import modals from './modals';

function initialData() {
  return {
    hasLiked: false,
    userLoggedIn: false,
  };
}

export default {
  name: 'PinPreview',
  data() {
    return initialData();
  },
  props: ['pinItem', 'loggedIn'],
  methods: {
    closeAndGoTo() {
      this.$parent.close();
      this.$router.push(
        { name: 'pin', params: { pinId: this.pinItem.id } },
      );
    },
    addCollect() { // 点赞
      if (!this.loggedIn) {
        modals.openLogin(this, this.onLoginSucceed);
      }
      API.addLike({
        pin: this.pinItem.id,
      }).then((response) => {
        console.log(response.data);
        this.hasLiked = true;
      }).catch((error) => {
        console.log(error);
      });
    },
    deleteCollect() {
    // 取消点赞
      API.delLike(this.pinItem.id).then((response) => {
        console.log(response.data);
        console.log(this.pinItem.id);
        this.hasLiked = false;
      }).catch((error) => {
        console.log(error);
      });
    },
    checkLikeFlg() {
      API.checkIfLike(this.pinItem.id).then((response) => {
        console.log(response.data);
        this.hasLiked = true;
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  created() {
    if (this.loggedIn) {
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
.card-image img {
  width: 100%;
}

.heart{
  margin-left: 30px;
}
</style>
