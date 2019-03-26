import Vue from 'vue'
import VueRouter from 'vue-router'
import BrowseApp from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import SparcWelcome from './components/sparc-welcome/SparcWelcome.vue'
import SparcBrowse from './components/sparc-browse/SparcBrowse.vue'


Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.use(VueRouter)

const router = new VueRouter({
  base: '/browse',
  routes: [
    { path: '/', redirect: '/models' },
    {
      path: '/models',
      name: 'Browse',
      component: SparcBrowse,
    },
    {
      path: '/:model',
      name: 'help',
      component: SparcWelcome,
    },
    {
      path: '/detail',
      name: 'Details',
      component: SparcBrowse,
    },
  ],
})

new Vue({
  router,
  render: h => h(BrowseApp)
}).$mount('#browse')
