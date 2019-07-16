<template>
  <div class="dataset-about">
    <el-row type="flex" justify="center">
      <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
        <h3 class="dataset-about-header">About this dataset</h3>
        <div class="information">
          <p v-if="dataset.license">
            License: {{ dataset.license }}
          </p>
          <p v-if="dataset.license">
            Version: {{ dataset.version }}
          </p>
        </div>
        <div class="tags">
          <h4>Tags</h4>
          <!-- <ul> -->
            <el-tag type="warning" :key="tag" v-for="tag in dataset.tags">
              {{ tag }}
            </el-tag>
          <!-- </ul> -->
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'dataset-about',
  props: ['dataset']
}
</script>

<style lang="scss" scoped>
.dataset-about {
  padding: 3em 0em;
  overflow: hidden;
  background: #ff9e00;
  color: white;
}
h3.dataset-about-header {
  margin-bottom: 1em;
}
.el-tag {
  margin-right: 8px;
}
.information {
  font-size: 0.9em;
}
</style>

