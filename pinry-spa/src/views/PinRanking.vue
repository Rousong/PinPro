<template>
  <div class="home">
    <PHeader></PHeader>
    <div class="tabs">
      <ul>
        <li  v-for="(item,index) in menuItems" :key="item.index" @click="addClass(index)"
             :class="{'is-active':position === index}"><a>{{item}}</a></li>
      </ul>
    </div>
    <Pins :pin-filters="filters"></Pins>
  </div>
</template>

<script>
import PHeader from '../components/PHeader.vue';
import Pins from '../components/Pins.vue';

export default {
  name: 'Home',
  data() {
    return {
      menuItems: {
        week: this.$i18n.t('rank.Week'),
        month: this.$i18n.t('rank.Month'),
        year: this.$i18n.t('rank.Year'),
        all: this.$i18n.t('rank.All'),
      },
      position: '',
      filters: { rankFilter: null },
    };
  },
  components: {
    PHeader,
    Pins,
  },
  methods: {
    addClass(index) {
      this.position = index;
      this.filters = { rankFilter: index };
    },
  },
  created() {
    this.addClass('week');
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .tabs{
    background-color: #dadada;
  }
</style>
