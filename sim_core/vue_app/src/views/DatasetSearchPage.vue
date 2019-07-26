<template>
  <div>
    <div class="header">
      <div class="gradient">
        <el-row type="flex" justify="center">
          <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
            <div class="breadcrumb">
              <el-row>
                <el-col :xs="24" :lg="12">
                  <h3>Analyses and Simulations</h3>
                  <p>A powerful computing platform called o<sup>2</sup>S<sup>2</sup>PARCenables modeling, simulation, data analysis, and visualization directly within your web browser. o<sup>2</sup>S<sup>2</sup>PARC supports simulations that predict the effects of autonomic neuromodulation on organ function. A growing list of curated computational studies from various SPARC-funded teams is available for virtual experimentation on o<sup>2</sup>S<sup>2</sup>PARC.</p>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="simcore-page">
      <el-row type="flex" justify="center">
        <el-col :sm="18">
          <el-row type="flex" justify="center">
            <el-col :sm="18" :lg="12">
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
  </div>
</template>

<script>
import SearchForm from "../components/DatasetSearch/SearchForm.vue";
import DatasetList from "../components/DatasetSearch/DatasetList.vue";

import { mapActions } from 'vuex';

export default {
  name: "dataset-search-page",
  components: {
    SearchForm,
    DatasetList
  },
  methods: mapActions([
    'firstFetch'
  ]),
  created() {
    this.firstFetch();
  }
}
</script>

<style lang="scss" scoped>
.header {
  .gradient {
    padding: 1.5em 0;
    color: #f0f2f5;
    background-image: linear-gradient(90deg, #fe7820 0%, #fce644 100%);
  }
}
</style>
