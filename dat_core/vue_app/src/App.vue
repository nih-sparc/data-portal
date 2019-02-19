<template>
  <div id="browse">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <sparc-welcome />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <bf-vega id="1" class="list"></bf-vega> -->

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import BfVega from './components/bf-vega/BfVega.vue'
import SparcWelcome from './components/sparc-welcome/SparcWelcome.vue'

export default {
  name: 'browse',
  components: {
    HelloWorld,
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
