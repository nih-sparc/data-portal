<template>
  <div>
    <p>
      <router-link to="/">
        <el-link type="primary" size="small">&lt; Back to search results</el-link>
      </router-link>
    </p>
    <div v-if="isFetching">
      Fetching...
    </div>
    <div v-else-if="dataset">
      <el-row :gutter="18">
        <el-col :sm="8">
          <el-image :src="dataset.banner" fit="cover" lazy></el-image>
        </el-col>
        <el-col :sm="16">
          <h2>{{ dataset.name }}</h2>
          <h3><p>{{ dataset.description }}</p></h3>
          <p>Organization: {{ dataset.organizationName }}</p>
          <p>Owner: {{ dataset.ownerName }}</p>
          <p v-if="dataset.contributors.length">
            Contributors: <span v-for="(contributor, i) in dataset.contributors" :key="contributor">{{ contributor }}{{ i === dataset.contributors.length-1 ? "." : ", "}}</span>
          </p>
        </el-col>
      </el-row>
    </div>
    <div v-else>
      <p>Sorry, we couldn't retreive the dataset for the given id.</p>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'dataset-detail',
  props: ['id'],
  computed: mapState({
    dataset(state) {
      return state.entities.datasets[this.id];
    },
    isFetching(state) {
      return state.simcoreDetail.isFetching;
    }
  }),
  methods: {
    ...mapActions([
      'fetchDataset'
    ])
  },
  created() {
    this.fetchDataset(this.id);
  }
}
</script>
