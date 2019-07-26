<template>
  <el-form :inline="true" :model="simcoreSearchForm" class="search-form" @submit.prevent.native="onSubmit">
    <el-row :gutter="8">
      <el-col :sm="14">
        <el-input v-model="simcoreSearchForm.search" placeholder="Type your search" suffix-icon="el-icon-search"></el-input>
      </el-col>
      <el-col :sm="5">
        <el-button class="search-button" type="warning" native-type="submit" :loading="isFetching ? true : false">Search</el-button>
      </el-col>
      <el-col :sm="5">
        <el-button class="search-button" @click="clearDatasets">Clear search</el-button>
      </el-col>
    </el-row>
  </el-form>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'search-form',
  data() {
    return {
      simcoreSearchForm: {
        search: ''
      }
    }
  },
  computed: mapState({
    isFetching: state => state.simcoreSearch.simcoreSearchForm.isFetching
  }),
  methods: {
    onSubmit(e) {
      if (this.simcoreSearchForm.search.length) {
        this.searchDatasets(this.simcoreSearchForm.search);
      } else {
        this.fetchDatasets();
      }
    },
    searchDatasets(query) {
      return this.$store.dispatch('searchDatasets', query);
    },
    fetchDatasets() {
      return this.$store.dispatch('fetchDatasets');
    },
    clearDatasets() {
      return this.$store.dispatch('clearDatasets');
    }
  }
}
</script>

<style lang="scss" scoped>
form.search-form {
  margin: 2em 0;
  @media screen and (max-width: 768px) {
    margin: 1em 0;
  }
  .search-button {
    width: 100%;
  }
  .el-col {
    @media screen and (max-width: 768px) {
      margin: 0.2em 0;
    }
  }
}
</style>