<template>
  <div>
    <p>
      <router-link to="/">
        <el-link type="primary" size="small">&lt; Back to search results</el-link>
      </router-link>
    </p>
    <div v-if="isFetching" v-loading="true" class="loading-placeholder" element-loading-background="transparent" element-loading-text="Loading..."></div>
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
          <a v-if="dataset.study" :href="'http://master.osparc.io/study/' + dataset.study.uuid" target="_blank">
            <el-button type="primary">Run simulation</el-button>
          </a>
        </el-col>
      </el-row>
      <el-row class="markdown">
        <el-col>
          <markdown :markdown="dataset.markdown" />
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
import Markdown from '../Markdown/Markdown.vue';

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
  },
  components: {
    Markdown
  }
}
</script>

<style lang="scss" scoped>
.loading-placeholder {
  height: 300px;
}
.markdown {
  margin-top: 30px;
}
</style>
