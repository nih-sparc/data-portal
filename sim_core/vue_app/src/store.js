import Vue from 'vue';
import Vuex from 'vuex';
import { normalize } from 'normalizr';
import { dataset as datasetSchema } from './schemas';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    simcoreSearch: {
      simcoreSearchForm: {
        isFetching: false
      }
    },
    simcoreDetail: {
      isFetching: false
    },
    entities: {
      datasets: {}
    }
  },
  mutations: {
    SET_SIMCORESEARCH_IS_FETCHING(state, isFetching) {
      state.simcoreSearch.simcoreSearchForm.isFetching = isFetching;
    },
    SET_SIMCOREDETAIL_IS_FETCHING(state, isFetching) {
      state.simcoreDetail.isFetching = isFetching;
    },
    SET_DATASETS(state, datasets) {
      state.entities.datasets = normalize(datasets, [
        datasetSchema
      ]).entities.datasets;
    },
    SET_DATASET(state, dataset) {
      state.entities.datasets[dataset.id] = dataset;
    }
  },
  actions: {
    fetchDatasets(context) {
      context.commit('SET_SIMCORESEARCH_IS_FETCHING', true);
      fetch('/api/sim/dataset')
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            context.commit('SET_SIMCORESEARCH_IS_FETCHING', false);
            console.error(
              "Couldn't fetch the data: The server returned an error status."
            );
          }
        })
        .then(json => {
          context.commit('SET_DATASETS', json.datasets);
          context.commit('SET_SIMCORESEARCH_IS_FETCHING', false);
        })
        .catch(error => {
          context.commit('SET_SIMCORESEARCH_IS_FETCHING', false);
          console.error('The request failed: ' + error.message);
        });
    },

    fetchDataset(context, id) {
      const { datasets } = context.state.entities;
      if (datasets && datasets[id]) {
        return;
      }
      context.commit('SET_SIMCOREDETAIL_IS_FETCHING', true);
      fetch('/api/sim/dataset/' + id)
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            context.commit('SET_SIMCOREDETAIL_IS_FETCHING', false);
            console.error(
              "Couldn't fetch the data: The server returned an error status."
            );
          }
        })
        .then(json => {
          context.commit('SET_DATASET', json);
          context.commit('SET_SIMCOREDETAIL_IS_FETCHING', false);
        })
        .catch(error => {
          context.commit('SET_SIMCOREDETAIL_IS_FETCHING', false);
          console.error('The request failed: ' + error.message);
        });
    }
  }
});
