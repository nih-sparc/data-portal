import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en';

import striptags from 'striptags';
Vue.prototype.$sanitize = (html, allowedTags=['br']) => striptags(html, allowedTags);

Vue.config.productionTip = false;
Vue.config.devtools = true;
Vue.use(ElementUI, { locale });

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#sim');
