import Vue from 'vue'
import Browse from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(Browse),
}).$mount('#dashboard')