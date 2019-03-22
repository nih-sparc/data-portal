<template>
  <div id="browse">
    <div id="left-content-column">
      hello there
      <!-- <sparc-browse-filters> -->
    </div>
    <div id="right-content-column">
      <sparc-browse />
    </div>
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
    SparcWelcome,
    SparcBrowse
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
    display:flex;
    flex-direction: row;
  }

  #left-content-column {
    flex: 0;
    flex-basis: 250px;

  }

  #right-content-column {
    flex: 1;
    overflow:scroll;


  }

</style>
