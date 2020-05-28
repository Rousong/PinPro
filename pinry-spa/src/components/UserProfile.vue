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
<!--            <a @click="editPreferences" class='button is-primary is-outlined' href='#' id='edit-preferences' style='margin: 5px 0'>-->
<!--              Edit Preferences-->
<!--            </a>-->
            <br>
          </p>
          <p class='tagline'>
            {{editorMeta.user.meta.email}}
          </p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>{{userCnt.userLikes}}</p>
          <p class='stat-key'>{{$t("profile.likes")}}</p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>{{userCnt.userPins}}</p>
          <p class='stat-key'>{{$t("profile.pins")}}</p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>{{userCnt.userBoards}}</p>
          <p class='stat-key'>{{$t("profile.boards")}}</p>
        </div>
      </div>
    </div>
  </div>
  <hr />
  <div class="tabs is-boxed is-centered">
  <ul>
    <li  v-for="(item,index) in menuItems" :key="item.index" @click="addClass(index)"
             :class="{'is-active':position === index}"><a v-html="item"></a></li>
  </ul>
</div>
    <section class="section" v-if="position==='doc'">
    <div class="container">
      <div class="notification is-info">
        <h1 class="title">{{$t("profile.about1")}}</h1>
         <p class="subtitle" :v-html="$t('profile.about1')">
         {{$t("profile.about2")}}<a href="https://gravatar.com" target="_blank"><strong>Gravatar</strong></a>!
        {{$t("profile.about3")}}<a href=mailto:sample@163.com>sample@163.com</a>
      </p>
      </div>
      <div class="notification is-danger">
        <p class="subtitle">
        {{$t("profile.about4")}}
       </p>
      </div>
      <div class="notification is-success">
        <p class="subtitle">
        {{$t("profile.about5")}}
       </p>
      </div>
    </div>
  </section>
  <section class="section" v-if="position==='android'">
    <div class="container">
      <div class="notification is-info">
      {{$t("profile.android1")}}
      </div>
      <figure class="image docImage">
          <img src='../assets/img/android/android1.jpg' >
      </figure>
      <br/>
      <div class="notification is-info">
      {{$t("profile.android2")}}
      </div>
       <figure class="image docImage">
          <img src='../assets/img/android/android2.jpg' >
      </figure>
      <br/>
      <div class="notification is-info">
      {{$t("profile.android3")}}
      </div>
       <figure class="image docImage">
          <img src='../assets/img/android/android3.jpg' >
      </figure>
      <br/>
      <div class="notification is-info">
      {{$t("profile.android4")}}
      </div>
       <figure class="image docImage">
          <img src='../assets/img/android/android4.jpg' >
      </figure>
      <br/>
      <div class="notification is-info">
      {{$t("profile.android5")}}
      </div>
       <figure class="image docImage">
          <img src='../assets/img/android/android5.jpg' >
      </figure>
    </div>
  </section>
  <section class="section" v-if="position==='apple'">
    <div class="container">
      <br/>
      <div class="notification is-success">
     {{$t("profile.apple1")}}
      </div>
      <figure class="image docImage">
          <img src='../assets/img/IOS/ios1.jpg' >
      </figure>
      <br/>
      <div class="notification is-success">
      {{$t("profile.android2")}}
      </div>
      <figure class="image docImage">
          <img src='../assets/img/IOS/ios2.jpg' >
      </figure>
      <br/>
      <div class="notification is-success">
      {{$t("profile.android3")}}
      </div>
      <figure class="image docImage">
          <img src='../assets/img/IOS/ios3.jpg' >
      </figure>
      <br/>
      <div class="notification is-success">
      {{$t("profile.android5")}}
      </div>
      <figure class="image docImage">
          <img src='../assets/img/IOS/ios4.jpg' >
      </figure>
    </div>
  </section>
  <section class="section" v-if="position==='pc'">
    <div class="container">
      <br/>
      <div class="notification is-warning">
      {{$t("profile.pc1")}}
      </div>
      <figure class="image docImagePc">
          <img src='../assets/img/pc/pc1.jpg' >
      </figure>
      <br/>
      <div class="notification is-warning">
      {{$t("profile.pc2")}}
      </div>
      <figure class="image docImagePc">
          <img src='../assets/img/pc/pc2.jpg' >
      </figure>
      <br/>
      <div class="notification is-warning">
      {{$t("profile.pc3")}}
      </div>
      <figure class="image docImagePc">
          <img src='../assets/img/pc/pc3.jpg' >
      </figure>
      <br/>
      <div class="notification is-warning">
      {{$t("profile.pc4")}}
      </div>
      <figure class="image docImagePc">
          <img src='../assets/img/pc/pc4.jpg' >
      </figure>
      <br/>
      <div class="notification is-warning">
      {{$t("profile.pc5")}}
      </div>
      <figure class="image docImagePc">
          <img src='../assets/img/pc/pc5.jpg' >
      </figure>
      <br/>
      <div class="notification is-warning">
      {{$t("profile.pc6")}}
      </div>
      <figure class="image docImagePc">
          <img src='../assets/img/pc/pc6.jpg' >
      </figure>
    </div>
  </section>
</div>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>Powered by <a href="https://github.com/Pinpro/PinPro"><strong>PinPro</strong></a>. {{$t("profile.footer")}}
        </p>
      </div>
    </footer>
</div>
</template>

<script>
import API from './api';
import modals from './modals';

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
    menuItems: {
      doc: '<span class="icon is-small"><i class="fas fa-file-alt" aria-hidden="true"></i></span><span>About</span>',
      android: '<span class="icon is-small"><i class="fab fa-android" aria-hidden="true"></i></span><span>Andorid</span>',
      apple: '<span class="icon is-small"><i class="fab fa-apple" aria-hidden="true"></i></span><span>IOS</span>',
      pc: '<span class="icon is-small"><i class="fas fa-desktop" aria-hidden="true"></i></span><span>PC</span>',
    },
    position: 'doc',
  };
}
export default {
  name: 'UserProfile',
  data() {
    return initialData();
  },
  components: {
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
            this.$router.push({ path: '/' });
          } else {
            self.editorMeta.user.meta = user;
            self.editorMeta.user.meta.avatar = `//gravatar.com/avatar/${user.gravatar}`;
            self.editorMeta.user.loggedIn = true;
          }
        },
      );
    },
    getUserCnt(user) {
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
    addClass(index) {
      this.position = index;
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
  .docImage{
    min-width: 300px;
    max-width: 40%;
  }
  .docImagePc{
    min-width: 300px;
    max-width: 80%;
  }
</style>
