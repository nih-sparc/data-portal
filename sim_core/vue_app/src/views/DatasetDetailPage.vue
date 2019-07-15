<template>
  <div class="simcore-page">
    <div v-if="isFetching" v-loading="true" class="loading-placeholder" element-loading-background="transparent" element-loading-text="Loading..."></div>
    <div v-else-if="dataset">
      <dataset-title v-bind:dataset="dataset" />
      <el-row type="flex" justify="center">
        <el-col :sm="18">
          <el-row>
            <el-col>
              <dataset-detail v-bind:dataset="dataset" />
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import DatasetDetail from '../components/DatasetSearch/DatasetDetail.vue';
import DatasetTitle from '../components/DatasetSearch/DatasetTitle.vue';

import { mapState, mapActions } from 'vuex';

export default {
  name: "dataset-detail-page",
  components: {
    DatasetDetail,
    DatasetTitle
  },
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

<style lang="scss" scoped>
.loading-placeholder {
  height: 300px;
}
</style>
