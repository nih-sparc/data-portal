import Vue from 'vue'
import Browse from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';

Vue.config.productionTip = false
Vue.config.devtools = 


Vue.use(ElementUI);
Vue.use(VueAxios, axios)

new Vue({
  render: h => h(Browse),
  mounted () {
    // Axios.get('/api/datasets')
    //   .then(function (response) {
    //     console.log(response)
    //   })
  }
}).$mount('#dashboard')