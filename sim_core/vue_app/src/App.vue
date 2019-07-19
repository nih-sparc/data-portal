<template>
  <div id="sim-app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "sim-app",
  components: {}
};
</script>

<style lang="scss" scoped>
#sim-app {
  margin-top: 6em;
}

.simcore-page {
  padding: 2em 0;
  @media screen and (max-width: 768px) {
    padding: 2em 1em;
  }
}
</style>

