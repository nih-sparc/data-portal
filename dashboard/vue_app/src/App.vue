<template>
  <div id="dashboard">
    <sprc-stats />
    <sparc-welcome />

  </div>
</template>

<script>
import BfVega from './components/bf-vega/BfVega.vue'
import SparcWelcome from './components/sparc-welcome/SparcWelcome.vue'
import SprcStats from './components/SprcStats/SprcStats.vue'

export default {
  name: 'dashboard',
  components: {
    BfVega,
    SparcWelcome,
    SprcStats
  }
}
</script>

<style lang="scss" scoped>
#dashboard {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; 
  margin-top: 10px;
}
</style>
