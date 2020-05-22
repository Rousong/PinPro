<template>
  <div class="pins-for-user">
    <PHeader></PHeader>
    <LikePins :pin-filters="filters"></LikePins>
  </div>
</template>

<script>
import PHeader from '../components/PHeader.vue';
import LikePins from '../components/LikePins.vue';

export default {
  name: 'Pins4User',
  data() {
    return {
      filters: { likeFilter: null },
    };
  },
  components: {
    PHeader,
    LikePins,
  },
  created() {
    this.initializeBoard();
  },
  beforeRouteUpdate(to, from, next) {
    this.filters = { likeFilter: to.params.user };
    next();
  },
  methods: {
    initializeBoard() {
      this.filters = { likeFilter: this.$route.params.user };
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
