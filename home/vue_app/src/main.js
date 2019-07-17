import Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import VueRouter from 'vue-router'
import SparcLandingPage from "./components/landing-page/LandingPage.vue"
import SparcAboutPage from "./components/about-page/AboutPage.vue"
import MarketingApp from './App.vue'
import DatasetPage from "./components/dataset-landing-page/DatasetPage.vue";

Vue.config.productionTip = false
Vue.config.devtools = true

Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.use(VueRouter)

const router = new VueRouter({
  base: '/',
  routes: [
    { path: '/', redirect: '/home' },
    {
      path: '/home',
      name: 'Home',
      component: SparcLandingPage,
    },
    {
      path: '/about',
      name: 'About',
      component: SparcAboutPage
    },
    {
      path: '/dataset/:datasetId',
      name: 'Dataset',
      component: DatasetPage
    }
  ],
})


new Vue({
  router,
  render: h => h(MarketingApp)
}).$mount('#home')

