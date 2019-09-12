<template>
  <div class="carousel-view">
    <div class="carousel-controls">
      <div class="options">
        <span
          v-for="slide in slides"
          :key="slide.id"
          class="option"
       >
          <a :class="{ active: slide.heading === activeTextBlock }" href="#" @click.prevent="toggleSlide(slide.heading)"> {{ slide.heading }}</a>
          <span v-if="slide.id !== slides.length" class="dot">•</span>
        </span>
      </div>
    </div>
    <el-row type="flex" justify="center">
      <template v-for="slide in slides">
        <div
          v-if="slide.heading === activeTextBlock"
          class="slide"
          :key="slide.id"
        >
          <p>{{ slide.title }}</p>
        </div>
      </template>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "OverviewCarousel",
  data() {
    return {
      slides: [
         {
          title:
            "Catalyze the development of next-generation bioelectronic medicines by providing access to high-value datasets, maps, and predictive simuatations",
          id: 1,
          heading: 'Goal'
        },
        {
          title:
            "Launched in July 2019, the SPARC Portal is an open-source web application that provides access to a growing collection of interactive autonomic neuroscience resources",
          id: 2,
          heading: 'Current'
        },
        {
          title: "The SPARC Portal will enable users to run advanced analytics and computational studies to predict the effects of neuromodulation on organ function.",
          id: 3,
          heading: 'Future'
        },
      ],
      activeTextBlock: 'Goal',
      timer: 0,
      autoplayTimeout: () => {}
    };
  },

  created() {
    this.startAutoplay()
  },


  methods: {
    /**
     * Start autoplay for slides
     */
    startAutoplay: function () {
      this.timer = setInterval(this.next, 10000);
    },

    /**
     * Function to iterate to the next slide and change the
     * navigation ticker
     */
    next: function () {
      if (this.activeTextBlock === 'Goal'){
        this.activeTextBlock = 'Current'
      } else if (this.activeTextBlock === 'Current') {
        this.activeTextBlock = 'Future'
      } else {
        this.activeTextBlock = 'Goal'
      }
    },

    /**
     * Toggle slide based on heading selection
     * @param {Object} slide
     */
    toggleSlide: function(slide) {
      clearInterval(this.timer)
      this.activeTextBlock = slide

      clearTimeout(this.autoplayTimeout);
      this.autoplayTimeout = setTimeout(() => {
        this.startAutoplay()
      }, 5000);
    }
  }
};
</script>

<style lang="scss" scoped>
.carousel-view {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.carousel {
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
.slide {
  margin: 1em;
  font-weight: normal;
}

.dot {
  margin-left: 18px;
}

.option {
  padding: 0 0.5em;

  a {
    text-decoration: none;
    color: #f9f2fc;

    &.active {
      color: #c200fd;
    }
  }
}
</style>