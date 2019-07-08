import Vue from 'vue';
import Router from 'vue-router';
import DatasetSearchPage from './views/DatasetSearchPage.vue';
import DatasetDetailPage from './views/DatasetDetailPage.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      component: DatasetSearchPage
    },
    {
      name: 'dataset-detail',
      path: '/dataset/:id',
      component: DatasetDetailPage,
      props: true
    }
  ]
});
