<template>
  <div class="sim-app">
    <div class="header">
      <div class="gradient">
        <el-row type="flex" justify="center">
          <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
            <div class="breadcrumb">
              <el-row>
                <el-col :xs="24" :lg="12">
                  <h1>Simulation Core</h1>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.sim-app {
  .header {
    .gradient {
      padding: 1.5em 0;
      color: #f0f2f5;
      background-image: linear-gradient(90deg, #fe7820 0%, #fce644 100%);
    }
  }
}
</style>
