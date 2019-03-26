<template>
  <div id="browse-app">
      <router-view></router-view>
  </div> 
</template>

<script>

  export default {
    name: 'browse-app',
    components: {
    }
  }
</script>

<style lang="scss" scoped>
  #browse-app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50; 
    margin-top: 10px;
    display:flex;
    flex-direction: row;
  }
</style>
