<template>
  <div class="carousel-view">
    <div class="carousel-controls">
      <div class="options">
        <span class="option">
          <a :class="{ active: activeTextBlock === 'goal' }" href="#" @click.prevent="next">Goal</a>
        </span>
        <span>•</span>
        <span class="option">
          <a
            :class="{ active: activeTextBlock === 'current' }"
            href="#"
            @click.prevent="next"
          >Current</a>
        </span>
        <span>•</span>
        <span class="option">
          <a :class="{ active: activeTextBlock === 'future' }" href="#" @click.prevent="next">Future</a>
        </span>
      </div>
    </div>
    <transition-group class="carousel" tag="div">
      <div v-for="slide in slides" class="slide" :key="slide.id">
        <h4>{{ slide.title }}</h4>
      </div>
    </transition-group>
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
          id: 1
        },
        {
          title:
            "Launched in July 2019, the SPARC Portal is an open-source web application that provides access to a growing collection of interactive autonomic neuroscience resources",
          id: 2
        },
        {
          title:
            "The SPARC Portal will enable users to run advanced analytics and computational studies to predict the effects of neuromodulation on organ function.",
          id: 3
        }
      ],
      activeTextBlock: "goal"
    };
  },

  mounted() {
    setInterval(this.next, 5000);
  },

  methods: {
    next: function () {
      const first = this.slides.shift();
      console.log ("first one ", first)
      // if (first.id === 1) {
      //   this.activeTextBlock = "goal"
      // } else if (first.id === 2) {
      //   this.activeTextBlock = "current";
      // } else {
      //   this.activeTextBlock = "future";
      // }
      this.slides = this.slides.concat(first);
    },
    previous: function () {
      const last = this.slides.pop();
      this.slides = [last].concat(this.slides);
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
  transition: transform 0.3s ease-in-out;
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