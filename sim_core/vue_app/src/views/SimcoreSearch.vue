<template>
  <div class="simcore-search">
    <el-row type="flex" justify="center">
      <el-col :span="18">
        <el-row>
          <el-col>
            <h2>Search and run simulations in the oSPARC platform</h2>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <SearchForm />
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <DatasetList />
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SearchForm from "../components/SimcoreSearch/SearchForm.vue";
import DatasetList from "../components/SimcoreSearch/DatasetList.vue";

export default {
  name: "simcore-search",
  components: {
    SearchForm,
    DatasetList
  }
}
</script>

<style lang="scss" scoped>
.simcore-search {
  padding-top: 7em;
}
</style>
