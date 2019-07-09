<template>
  <div class="simcore-page">
    <el-row type="flex" justify="center">
      <el-col :sm="18">
        <el-row>
          <el-col>
            <h2>Search and run simulations in the oSPARC platform</h2>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <search-form />
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <dataset-list />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SearchForm from "../components/DatasetSearch/SearchForm.vue";
import DatasetList from "../components/DatasetSearch/DatasetList.vue";

export default {
  name: "dataset-search-page",
  components: {
    SearchForm,
    DatasetList
  }
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
