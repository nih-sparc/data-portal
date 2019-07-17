<template>
  <el-form :inline="true" :model="simcoreSearchForm" class="search-form" @submit.prevent.native="onSubmit">
    <el-row :gutter="8">
      <el-col :sm="16">
        <el-input v-model="simcoreSearchForm.search" placeholder="Type your search"></el-input>
      </el-col>
      <el-col :sm="8">
        <el-button class="search-button" type="warning" native-type="submit" :loading="isFetching ? true : false">Search</el-button>
      </el-col>
    </el-row>
  </el-form>
</template>

<script>
import { mapState, mapActions } from 'vuex';
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
    ...mapActions([
      'searchDatasets',
      'fetchDatasets'
    ])
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
    @media screen and (max-width: 768px) {
      margin: 1em 0;
    }
  }
}
</style>