<template>
  <el-form :inline="true" :model="simcoreSearchForm" class="search-form" @submit.prevent.native="onSubmit">
    <el-form-item>
      <el-input v-model="simcoreSearchForm.search" placeholder="Type your search"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" native-type="submit" :loading="isFetching ? true : false">Search</el-button>
    </el-form-item>
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
      this.fetchDatasets(this.simcoreSearchForm.search);
    },
    ...mapActions([
      'fetchDatasets'
    ])
  }
}
</script>

<style lang="scss" scoped>
form.search-form {
  margin: 2em 0;
}
</style>