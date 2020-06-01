<template>
  <div class="search-panel">
    <div class="filter-selector">
      <div class="card-content">
         <template v-for="tag in options.HotTags">
           <button v-bind:key="tag" class="button is-light search-tag" @click="goTagFilter(tag)">{{ tag }}</button>
          </template>
          <b-field>
          <b-select :placeholder="$t('searchPanel.choose')" v-model="filterType">
            <option value="Tag">{{$t("searchPanel.tag")}}</option>
            <option value="Board">{{$t("searchPanel.board")}}</option>
          </b-select>
          <b-autocomplete
            v-show="filterType === 'Tag'"
            class="search-input"
            v-model="name"
            :data="filteredDataArray"
            :keep-first="true"
            :open-on-focus="true"
            :placeholder="$t('searchPanel.placeholderTag')"
            icon="magnify"
            @select="option => selected = option">
            <template slot="empty">{{$t("searchPanel.noResults")}}</template>
          </b-autocomplete>
          <template v-if="filterType === 'Board'">
            <b-input
              class="search-input"
              type="search"
              v-model="boardText"
              :placeholder="$t('searchPanel.placeholderBoard')"
              icon="magnify"
            >
            </b-input>
            <p class="control">
              <b-button @click="searchBoard" class="button is-warning">Search</b-button>
            </p>
          </template>
        </b-field>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'FilterSelector',
  data() {
    return {
      filterType: null,
      selectedOption: [],
      options: {
        Tag: [],
        HotTags: [],
      },
      name: '',
      boardText: '',
      selected: null,
    };
  },
  methods: {
    selectOption(filterName) {
      this.name = '';
      this.boardText = '';
      if (filterName === 'Tag') {
        this.selectedOption = this.options.Tag;
      }
    },
    searchBoard() {
      if (this.boardText === '') {
        return;
      }
      this.$emit(
        'selected',
        { filterType: this.filterType, selected: this.boardText },
      );
    },
    goTagFilter(tag) {
      this.filterType = 'Tag';
      this.name = tag;
      this.selected = tag;
    },
  },
  watch: {
    filterType(newVal) {
      this.selectOption(newVal);
    },
    selected(newVal) {
      this.$emit(
        'selected',
        { filterType: this.filterType, selected: newVal },
      );
    },
  },
  computed: {
    filteredDataArray() {
      return this.selectedOption.filter(
        (option) => {
          const ret = option
            .toString()
            .toLowerCase()
            .indexOf(this.name.toLowerCase()) >= 0;
          return ret;
        },
      );
    },
  },
  created() {
    api.Tag.fetchList().then(
      (resp) => {
        const options = [];
        resp.data.forEach(
          (tag) => {
            options.push(tag.name);
          },
        );
        this.options.Tag = options;
      },
    );
    api.Tag.fetchHotList().then(
      (resp) => {
        const hotList = [];
        resp.data.forEach(
          (tag) => {
            hotList.push(tag.name);
          },
        );
        this.options.HotTags = hotList;
      },
    );
  },
};
</script>

<style scoped="scoped" lang="scss">
  .search-panel {
    padding-top: 0.2rem;
    padding-left: 0rem;
    padding-right: 0rem;
  }
  .filter-selector {
    background-color: white;
    border-radius: 3px;
    .search-input {
      width: 100%;
    }
  }
  .search-tag {
  margin-right: 0.8rem;
  margin-bottom: 2px;
}
</style>
