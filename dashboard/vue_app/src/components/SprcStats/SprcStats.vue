<template>
  <div class="pt-histograms">
    <div class="pt-histograms__box first-box">
      <div class="pt-histograms__box-content">
        <div class="pt-histograms__box-heading">Contributors</div>
        <div
          class="pt-histograms__box-value large-text"
          v-loading="isLoading">
          <span v-if="!isLoading">14</span>
        </div>
      </div>
    </div>
    <div class="pt-histograms__box first-box">
      <div class="pt-histograms__box-content">
        <div class="pt-histograms__box-heading">Data</div>
        <div
          class="pt-histograms__box-value large-text"
          v-loading="isLoading">
          <span v-if="!isLoading">14</span>
        </div>
      </div>
    </div>
    <div class="pt-histograms__box first-box">
      <div class="pt-histograms__box-content">
        <div class="pt-histograms__box-heading">File types</div>
        <div
          class="pt-histograms__box-value large-text"
          v-loading="isLoading">
          <span v-if="!isLoading">14</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  countBy,
  filter,
  pluck,
  propEq,
  prop,
  uniq,
  defaultTo,
  innerJoin
} from 'ramda'

import BfVega from '../bf-vega/BfVega.vue'

export default {
  name: 'sprc-stats',
  props: {
    baseline_values: Array,
    subjects: Array,
    status: String
  },

  components: {
    BfVega
  },

  data() {
    return {
      open: false,
      ageSpec: {},
      ageData: {
        height: 45,
        mark: {
          type: 'bar',
          color: '#1C46BD'
        },
        encoding: {
          x: {
            field: 'age',
            bin: true,
            type: 'quantitative',
            axis: {
              title: ''
            }
          },
          y: {
            field: 'patient_id',
            aggregate: 'count',
            type: 'quantitative',
            axis: null,
            cell: {
              stroke: 'transparent'
            }
          }
        },
        config: {
          style: {
            cell: {
              stroke: 'transparent'
            }
          }
        }
      },
      genderSpec: {},
      genderData: {
        height: 50,
        mark: {
          type: 'bar',
          color: '#1C46BD'
        },
        encoding: {
          x: {
            field: 'patient_id',
            aggregate: 'count',
            type: 'quantitative',
            axis: null,
            cell: {
              stroke: 'transparent'
            }
          },
          y: {
            field: 'sex',
            type: 'ordinal',
            axis: {
              labels: true,
              title: ' '
            },
            cell: {
              stroke: 'transparent'
            }
          }
        },
        config: {
          axis: {
            labels: false
          },
          style: {
            cell: {
              stroke: 'transparent'
            }
          }
        }
      }
    }
  },

  computed: {
    /**
     * Returns number of subjects
     * @returns {Number}
     */
    subject_count: function () {
      return this.subjects.length
    },
    /**
     * Returns is loading status
     * @returns {Boolean}
     */
    isLoading: function() {
      return this.status !== 'done'
    }
  },

  watch: {
  },

  methods: {
    /**
     * Predicate function used to intersect filtered subjects with baseline data
     * @param {Object}
     * @param {Number}
     * @returns {Boolean}
     */
    chartDataPredicate: (baselineListObj, subjectId) => baselineListObj.patient_id === subjectId,
    /**
     * Builds vega lite spec object
     * @param {Object} obj
     * @param {Array} values
     * @returns {Object}
     */
    buildSpec: function(obj, values) {
      return {
        data: {
          values
        },
        height: obj.height,
        mark: 'bar',
        encoding: obj.encoding,
        config: obj.config
      }
    },
  },
}
</script>

<style lang="scss">
@import '../../../../../static/css/_variables.scss';

.pt-histograms {
  display: flex;
  padding: 0 50px;
  justify-content: space-between;

  .pt-histograms__box {
    align-items: center;
    background: #fff;
    border: solid 1px $pudendal;
    display: flex;
    flex: 1;
    height: 110px;
    margin: 20px 8px;
    max-width: 30%;
    padding: 8px 16px 0;

    &.first-box {
      margin-left: 0;
    }

    &.last-box {
      margin-right: 0;
    }

    &.extra-flex {
      flex: 1.16;
    }

    .pt-histograms__box-content {
      align-items: flex-start;
      display: flex;
      flex: 1;
      flex-direction: column;
      height: 100%;

      .pt-histograms__box-heading {
        color: $text-color;
        font-size: 14px;
        font-weight: 600;
        line-height: 20px;
        margin-bottom: 8px;

        &.is-link {
          color: $median;
          cursor: pointer;
        }
      }

      .pt-histograms__box-value {
        font-size: 12px;
        line-height: 15px;
        min-height: 80px;
        overflow: hidden;
        width: 100%;

        &.large-text {
          font-size: 36px;
          line-height: 43px;
        }
      }
    }
  }
  .histogramChart {
    svg.marks {
      width: 100%;
    }
  }
}
</style>


