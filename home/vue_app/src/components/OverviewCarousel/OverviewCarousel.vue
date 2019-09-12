<template>
  <div class="carousel-view">
    <div class="carousel-controls">
      <div class="options">
        <span class="option">
          <a :class="{ active: activeTextBlock === 'Goal' }" href="#" @click.prevent="next">Goal</a>
        </span>
        <span>•</span>
        <span class="option">
          <a
            :class="{ active: activeTextBlock === 'Current' }"
            href="#"
            @click.prevent="next"
          >Current</a>
        </span>
        <span>•</span>
        <span class="option">
          <a :class="{ active: activeTextBlock === 'Future' }" href="#" @click.prevent="next">Future</a>
        </span>
      </div>
    </div>
  <el-row type="flex" justify="center">
    <transition-group tag="div">
      <div v-for="slide in slides" class="slide" :key="slide.id">
        <h4>{{ slide.title }}</h4>
      </div>
    </transition-group>
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
          title: "The SPARC Portal will enable users to run advanced analytics and computational studies to predict the effects of neuromodulation on organ function.",
          id: 3,
          heading: 'Future'
        },
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
        }
      ],
      activeTextBlock: 'Goal'
    };
  },

  created() {
    setInterval(this.next, 10000);
  },


  methods: {
    /**
     * Function to iterate to the next slide and change the
     * navigation ticker
     */
    next: function () {
      const first = this.slides.shift();
      if (this.activeTextBlock === 'Goal'){
        this.activeTextBlock = 'Current'
      } else if (this.activeTextBlock === 'Current') {
        this.activeTextBlock = 'Future'
      } else {
        this.activeTextBlock = 'Goal'
      }
      this.slides = this.slides.concat(first);
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
  flex: 0 0 50em;
  margin: 1em;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: visibility 0s, opacity 0s linear;
  font-weight: normal;
}
.slide:first-of-type {
  opacity: 0;
}
.slide:last-of-type {
  opacity: 0;
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