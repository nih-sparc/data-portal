import Vue from 'vue'
import VueRouter from 'vue-router'
import BrowseApp from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import SparcWelcome from './components/sparc-welcome/SparcWelcome.vue'
import SparcBrowse from './components/sparc-browse/SparcBrowse.vue'
import SparcRecordDetail from './components/sparc-record-detail/SparcRecordDetail.vue'
import locale from 'element-ui/lib/locale/lang/en'

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI, { locale });
Vue.use(VueAxios, axios)
Vue.use(VueRouter)

const router = new VueRouter({
  base: '/browse',
  routes: [
    { path: '/', redirect: '/models' },
    { path: '/record', redirect: '/models' },
    {
      path: '/record/:id',
      name: 'Record',
      component: SparcRecordDetail,
    },
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
    
  ],
})

new Vue({
  router,
  render: h => h(BrowseApp)
}).$mount('#browse')
