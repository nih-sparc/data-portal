import Vue from 'vue'
import Browse from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI);
Vue.use(VueAxios, axios)

new Vue({
  render: h => h(Browse),
}).$mount('#browse')