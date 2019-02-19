<template>
  <div id="browse">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <bf-vega id="1" class="list"></bf-vega>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import BfVega from './components/bf-vega/BfVega.vue'


export default {
  name: 'browse',
  components: {
    HelloWorld,
    BfVega
  }
}
</script>

<style module>
#browse {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
