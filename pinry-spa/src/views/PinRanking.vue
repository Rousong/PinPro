<template>
  <div class="home">
    <PHeader></PHeader>
    <div class="tabs">
      <ul>
        <li  v-for="(item,index) in menuItems" :key="item.index" @click="addClass(index)"
             :class="{'is-active':position === index}"><a>{{item}}</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import PHeader from '../components/PHeader.vue';

export default {
  name: 'Home',
  data() {
    return {
      menuItems: ['本周', '本月', '本年', '全部'],
      position: '',
    };
  },
  components: {
    PHeader,
  },
  methods: {
    addClass(index) {
      this.position = index;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .tabs{
    background-color: #dadada;
  }
</style>
