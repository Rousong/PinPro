<template>
  <div id="app">
    <router-view/>
    <GoTop></GoTop>
  </div>
</template>

<script>
import GoTop from './components/GoTop.vue';

export default {
  name: 'app',
  components: { GoTop },
};
</script>

<style lang="scss">
  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";
  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
  html {
    background-color: rgb(44, 44, 44);
  }
  .body {
    font-family: 'Open Sans', sans-serif;
  }
  a:link{
    color:rgb(2, 80, 22);
  }
  a:hover,a:active{
    color:rgb(2, 80, 22);
  }
</style>
