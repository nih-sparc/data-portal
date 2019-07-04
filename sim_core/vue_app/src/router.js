import Vue from "vue";
import Router from "vue-router";
import SimcoreSearch from "./views/SimcoreSearch.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "sim",
      component: SimcoreSearch
    }
  ]
});
