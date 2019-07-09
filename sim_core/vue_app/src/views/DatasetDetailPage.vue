<template>
  <div class="simcore-page">
    <el-row type="flex" justify="center">
      <el-col :sm="18">
        <el-row>
          <el-col>
            <dataset-detail v-bind:id="id" />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import DatasetDetail from '../components/DatasetSearch/DatasetDetail.vue';

export default {
  name: "dataset-detail-page",
  components: {
    DatasetDetail
  },
  props: ['id']
}
</script>

<style lang="scss" scoped>
.simcore-page {
  padding: 7em 0;
  @media screen and (max-width: 768px) {
    padding: 7em 1em;
  }
}
</style>