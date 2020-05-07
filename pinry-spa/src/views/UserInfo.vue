<template>
  <div class="userInfo">
    <PHeader></PHeader>
    <UserProfile :filters="filters"></UserProfile>
  </div>
</template>

<script>
import PHeader from '../components/PHeader.vue';
import UserProfile from '../components/UserProfile.vue';

export default {
  name: 'UserInfo',
  data() {
    return {
      filters: { userFilter: null },
    };
  },
  components: {
    PHeader,
    UserProfile,
  },
  beforeRouteUpdate(to, from, next) {
    this.filters = { userFilter: to.params.username };
    next();
  },
  created() {
    this.initializeProfile();
  },
  methods: {
    initializeProfile() {
      this.filters = { userFilter: this.$route.params.username };
    },
  },
};
</script>
