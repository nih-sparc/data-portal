import Vue from 'vue'
import VueRouter from 'vue-router'
import BrowseApp from './App.vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import SparcWelcome from './components/sparc-welcome/SparcWelcome.vue'
import SparcBrowse from './components/browse/Browse.vue'
import SparcRecordDetail from './components/sparc-record-detail/SparcRecordDetail.vue'
import SparcRecord from "./components/record/Record.vue"
import DatasetDetails from "./components/DatasetDetails/DatasetDetails.vue"
import locale from 'element-ui/lib/locale/lang/en'
import * as svgicon from 'vue-svgicon'
import './assets/icons'

import striptags from 'striptags';
Vue.prototype.$sanitize = (html, allowedTags=['br']) => striptags(html, allowedTags)

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI, { locale });
Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(svgicon, {
  tagName: 'svg-icon'
})

const router = new VueRouter({
  base: '/browse',
  routes: [
    {
      path: '/',
      name: 'Browse',
      component: SparcBrowse
    },
    {
      path: '/datasets/:datasetId',
      name: 'Dataset',
      component: DatasetDetails,
      props: true
    },
    {
      path: '/record/:id',
      name: 'Record',
      component: SparcRecord
    }
  ],
})

new Vue({
  router,
  render: h => h(BrowseApp)
}).$mount('#browse')
