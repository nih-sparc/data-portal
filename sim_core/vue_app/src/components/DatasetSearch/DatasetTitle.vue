<template>
  <div class="header">
    <div class="gradient">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <div class="breadcrumb">
            <el-row>
              <el-col :span="24">
                Simulation Core / {{ dataset.name }}
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'dataset-title',
  props: ['dataset']
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

