<template>
  <div id="browse">
    <sparc-welcome />

  </div>
</template>

<script>
import BfVega from './components/bf-vega/BfVega.vue'
import SparcWelcome from './components/sparc-welcome/SparcWelcome.vue'
import SparcBrowse from './components/sparc-browse/SparcBrowse.vue'

export default {
  name: 'browse',
  components: {
    BfVega,
    SparcWelcome
  }
}
</script>

<style lang="scss" scoped>
#browse {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; 
  margin-top: 10px;
}
</style>
