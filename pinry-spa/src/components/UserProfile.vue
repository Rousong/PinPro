<template>
  <div>
<div class="bg">
  <div class='container profile'>
    <div class='section profile-heading'>
      <div class='columns is-mobile is-multiline'>
        <div class='column is-2'>
          <figure class="image">
             <img class='avatar' :src='editorMeta.user.meta.avatar'>
          </figure>
        </div>
        <div class='column is-4-tablet is-10-mobile name'>
          <p>
            <span class='title is-bold'>{{ editorMeta.user.meta.username }}</span>
            <br>
            <a @click="editPreferences" class='button is-primary is-outlined' href='#' id='edit-preferences' style='margin: 5px 0'>
              Edit Preferences
            </a>
            <br>
          </p>
          <p class='tagline'>
            {{editorMeta.user.meta.description}}
          </p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>{{userCnt.userLikes}}</p>
          <p class='stat-key'>Likes</p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>{{userCnt.userPins}}</p>
          <p class='stat-key'>Pins</p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>{{userCnt.userBoards}}</p>
          <p class='stat-key'>Boards</p>
        </div>
      </div>
    </div>
    <div class='profile-options is-fullwidth'>
      <div class='tabs is-fullwidth is-medium'>
        <ul>
          <li class='link is-active'>
            <a>
              <span class='icon'>
                <i class='fa fa-list'></i>
              </span>
              <span>My Pins</span>
            </a>
          </li>
          <li class='link is-active'>
            <a>
              <span class='icon'>
                <i class='fa fa-thumbs-up'></i>
              </span>
              <span>My Likes</span>
            </a>
          </li>
          <li class='link'>
            <a>
              <span class='icon'>
                <i class='fa fa-search'></i>
              </span>
              <span>My Boards</span>
            </a>
          </li>
          <li class='link'>
            <a>
              <span class='icon'>
                <i class='fa fa-balance-scale'></i>
              </span>
              <span>Compare</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <UserPins></UserPins>
  </div>
</div>
    <footer class="footer">
      <div class="content has-text-centered">
        <p><strong>Bulma</strong> by <a href="https://jgthms.com">Jeremy Thomas</a>. The source code is licensed
          <a href="http://opensource.org/licenses/mit-license.php">MIT</a>. The website content
          is licensed <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY NC SA 4.0</a>.
        </p>
      </div>
    </footer>
</div>
</template>

<script>
import API from './api';
import modals from './modals';
import UserPins from './UserPins.vue';

function initialData() {
  return {
    editorMeta: {
      user: { loggedIn: false, meta: { username: null } },
    },
    userCnt: {
      userLikes: 0,
      userPins: 0,
      userBoards: 0,
    },
  };
}
export default {
  name: 'UserProfile',
  data() {
    return initialData();
  },
  components: {
    UserPins,
  },
  props: {
    filters: {
      type: Object,
      default() {
        return {
          userFilter: null,
        };
      },
    },
  },
  watch: {
    filters() {
      this.reset();
    },
  },
  methods: {
    initialize() {
      const self = this;
      API.User.fetchUserInfo().then(
        (user) => {
          if (user === null) {
            self.editorMeta.user.loggedIn = false;
            self.editorMeta.user.meta = {};
          } else {
            self.editorMeta.user.meta = user;
            self.editorMeta.user.meta.avatar = `//gravatar.com/avatar/${user.gravatar}`;
            self.editorMeta.user.loggedIn = true;
          }
        },
      );
      console.log(this.editorMeta);
    },
    getUserCnt(user) {
      console.log(user);
      API.getCnt(user).then((resp) => {
        this.userCnt.userLikes = resp.like_num;
        this.userCnt.userPins = resp.pin_num;
        this.userCnt.userBoards = resp.board_num;
        setTimeout(() => {
          this.loading = false;
        }, 200);
      });
    },
    reset() {
      const data = initialData();
      Object.entries(data).forEach(
        (kv) => {
          const [key, value] = kv;
          this[key] = value;
        },
      );
      this.initialize();
    },
    editPreferences() {
      modals.openProfileSet(
        this,
        { username: this.editorMeta.user.meta.username },
      );
    },
  },
  created() {
    this.initialize();
    this.getUserCnt(this.$route.params.username);
  },
};
</script>

<style scoped>
  .bg {
    background: rgb(245, 244, 244)
  }
  .stat-val {
    font-size: 2em;
    padding-top: 20px;
    font-weight: bold;
  }
  .stat-key {
    font-size: 1.4em;
    font-weight: 200
  }
  .section.profile-heading .column.is-2-tablet.has-text-centered + .has-text-centered {
    border-left: 1px dotted rgba(0, 0, 0, .2);
  }
  .control.is-pulled-left span.select {
    border-radius: 2px;
  }
  .modal-card .content h1 {
    padding: 40px 10px 10px;
    border-bottom: 1px solid #dadada
  }
  .container.profile .profile-options .tabs ul li.link a {
    margin-bottom: 20px;
    padding: 20px;
    background-color: #F1F1F1;
  }
</style>
