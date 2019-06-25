import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.use(VueRouter)

import SparcHeader from "./components/header/Header.vue";
import SparcFooter from "./components/footer/Footer.vue";

new Vue({
  render: h => h(SparcHeader)
}).$mount('#sparc-header');

new Vue({
  render: h => h(SparcFooter)
}).$mount('#sparc-footer');
