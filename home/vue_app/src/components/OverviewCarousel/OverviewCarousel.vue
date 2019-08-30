<template>
     <div class='carousel-view'>
    <transition-group
      class='carousel'
      tag="div">
      <div
        v-for="slide in slides"
        class='slide'
        :key="slide.id">
        <h4> {{ slide.title }} </h4>
      </div>
    </transition-group>
    <div class='carousel-controls'>
      <button class='carousel-controls__button' @click="previous">prev</button>
      <button class='carousel-controls__button' @click="next">next</button>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'OverviewCarousel',
        data() {
            return {
                slides: [
                {
                    title: 'Catalyze the development of next-generation bioelectronic medicines by providing access to high-value datasets, maps, and predictive simuatations',
                    id: 1
                },
                {
                    title: 'Launched in July 2019, the SPARC Portal is an open-source web application that provides access to a growing collection of interactive autonomic neuroscience resources',
                    id: 2
                },
                {
                    title: 'The SPARC Portal will enable users to run advanced analytics and computational studies to predict the effects of neuromodulation on organ function.',
                    id: 3
                }
            ]
            }
        },

        methods: {
             next () {
      const first = this.slides.shift()
      this.slides = this.slides.concat(first)
    },
    previous () {
      const last = this.slides.pop()
      this.slides = [last].concat(this.slides)
    }
        },
    }
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
  width: 24em;
}
.slide {
  flex: 0 0 20em;
  margin: 1em;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: transform 0.3s ease-in-out;
}
.slide:first-of-type {
  opacity: 0;
}
.slide:last-of-type {
  opacity: 0;
}
</style>