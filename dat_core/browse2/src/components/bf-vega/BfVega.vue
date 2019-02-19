<template>
  <div
    :id="id"
    :class="className"
  />
</template>

<script>
import vegaEmbed from 'vega-embed'

export default {
  name: 'bf-vega',

  props: {
    id: {
      type: String,
      default: ''
    },
    className: {
      type: String,
      default:''
    },
    spec: {
      type: Object,
      default: () => {}
    }
  },

  mounted() {
    if (this.spec && this.id) {
      vegaEmbed(`#${this.id}`, this.spec, {defaultStyle: true, actions: false})
    }
  },

  watch: {
    spec: {
      handler: function(_spec) {
        if (_spec && Object.keys(_spec).length > 0 && this.id) {
          this.$nextTick(() => {
            vegaEmbed(`#${this.id}`, _spec, {defaultStyle: true, actions: false})
          })
        }
      },
      immediate: true
    },
  }
}
</script>

<style module lang="scss">
  .vega-embed {
    padding-right: 0 !important;
  }
</style>
