<template>
<div class="bg">
<div class='columns'>
  <div class='container profile'>
    <div class='section profile-heading'>
      <div class='columns is-mobile is-multiline'>
        <div class='column is-2'>
          <span class='header-icon user-profile-image'>
            <img class='avatar' :src='editorMeta.user.meta.avatar'>
          </span>
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
          <p class='stat-val'>30</p>
          <p class='stat-key'>searches</p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>10</p>
          <p class='stat-key'>likes</p>
        </div>
        <div class='column is-2-tablet is-4-mobile has-text-centered'>
          <p class='stat-val'>3</p>
          <p class='stat-key'>lists</p>
        </div>
      </div>
    </div>
    <div class='profile-options is-fullwidth'>
      <div class='tabs is-fullwidth is-medium'>
        <ul>
          <li class='link'>
            <a>
              <span class='icon'>
                <i class='fa fa-list'></i>
              </span>
              <span>My Lists</span>
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
              <span>My Searches</span>
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
    <div class='box' style='border-radius: 0px;'>
      <!-- Main container -->
      <div class='columns'>
        <div class='column is-2-tablet user-property-count has-text-centered'>
          <p class='subtitle is-5'>
            <strong></strong>
            123
            <br>
            properties
          </p>
        </div>
        <div class='column is-8'>
          <p class='control has-addons'>
            <input class='input' placeholder='Search your liked properties' style='width: 100% !important' type='text'>
            <button class='button'>
              Search
            </button>
          </p>
        </div>
      </div>
    </div>
    <div class='columns is-mobile'>
      <div class='column is-3-tablet is-6-mobile'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#1</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
      <div class='column is-3-tablet is-6-mobile'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#2</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
      <div class='column is-3'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#3</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
      <div class='column is-3'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#4</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
    </div>
    <div class='columns is-mobile'>
      <div class='column is-3'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#5</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
      <div class='column is-3'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#6</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
      <div class='column is-3'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#7</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
      <div class='column is-3'>
        <div class='card'>
          <div class='card-image'>
            <figure class='image is-4by3'>
              <img alt='' src='http://placehold.it/300x225'>
            </figure>
          </div>
          <div class='card-content'>
            <div class='content'>
              <span class='tag is-dark subtitle'>#8</span>
              <p>Personal Notes on the Property (can be edited and saved automatically by clicking in and clicking out of text area) - these are unique to the user - they will show up as part of a saved listings' info here - but adding notes to a property does not automatically create a saved listing. Likewise, removing this proeprty from saved listings does not auto remove the notes.</p>
            </div>
          </div>
          <footer class='card-footer'>
            <a class='card-footer-item'>Compare</a>
            <a class='card-footer-item'>Share</a>
            <a class='card-footer-item'>Delete</a>
          </footer>
        </div>
        <br>
      </div>
    </div>
  </div>
</div>
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
  };
}
export default {
  name: 'UserProfile',
  data() {
    return initialData();
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
  },
};
</script>

<style scoped>
  .bg {
    background: rgb(245, 244, 244)
  }
  .stat-val {
    font-size: 3em;
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
  .container.profile {
    margin-top: 1%;
  }
  .control.is-pulled-left span.select {
    margin-right: 5px;
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
