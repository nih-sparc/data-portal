<template>
  <img
    ref="img"
    :src="bannerSrc"
    class="dataset-image"
    alt="Dataset Banner Image"
  >
</template>

<script>
export default {
  name: 'DatasetBannerImage',
  props: {
    src: {
      type: String,
      default: ''
    }
  },

  data () {
    return {
      bannerSrc: '',
      publicPath: process.env.BASE_URL
    }
  },

  computed: {
    /**
     * Compute broken image path
     * @return {String}
     */
    brokenImage: function () {
      return `${this.publicPath}images/illustrations/icon-broken-image.svg`
    }
  },

  watch: {
    src: {
      handler: function (val) {
        this.bannerSrc = val
      },
      immediate: true
    }
  },

  mounted: function () {
    // Add listener for onerror
    this.$refs.img.onerror = this.onError
  },

  methods: {
    /**
     * Set the source as the brokenImage URL
     */
    onError: function () {
      this.bannerSrc = this.brokenImage
    }
  }
}
</script>
