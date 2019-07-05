import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    simcoreSearch: {
      simcoreSearchForm: {
        isFetching: false
      }
    },
    entities: {
      datasets: []
    }
  },
  mutations: {
    SET_IS_FETCHING(state, isFetching) {
      state.simcoreSearch.simcoreSearchForm.isFetching = isFetching;
    },
    SET_DATASETS(state, datasets) {
      state.entities.datasets = datasets;
    }
  },
  actions: {
    fetchDatasets(context) {
      context.commit('SET_IS_FETCHING', true);
      fetch('/api/sim/datasets')
        .then(response => {
          context.commit('SET_IS_FETCHING', false);
          if (response.ok) {
            return response.json();
          } else {
            console.error("Couldn't fetch the data");
          }
        })
        .then(json => {
          context.commit('SET_DATASETS', json.datasets);
        })
        .catch(error => {
          context.commit('SET_IS_FETCHING', false);
          console.error(
            'The request failed due to a network error: ' + error.message
          );
        });
    }
  }
});
