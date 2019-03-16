<template>
  <div class="sparc-browse">
      {{ message }}
  </div>
</template>

<script>

export default {
  name: 'sparc-browse',

  props: {
    message: {
      type: String,
      default: 'The SPARC Portal will be coming soon (Summer 2019)!'
    }
       
  },

}
</script>

<style lang="scss" scoped>

</style>
