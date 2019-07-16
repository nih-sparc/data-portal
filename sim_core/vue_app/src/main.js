import Vue from 'vue'
import VueRouter from 'vue-router'
import BrowseApp from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en'
import SparcSim from "./components/SparcSim/sparc-sim.vue";

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI, { locale });
Vue.use(VueAxios, axios)
Vue.use(VueRouter)

const router = new VueRouter({
  base: '/sim',
  routes: [
    {
      path: '/',
      name: 'Sim',
      component: SparcSim,
    }
  ],
})

new Vue({
  router,
  render: h => h(BrowseApp)
}).$mount('#sim')
