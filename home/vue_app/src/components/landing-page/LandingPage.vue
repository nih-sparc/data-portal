<template>
  <div>
    <div class="head">
      <div class="texture">
        <el-row class="blob-row" type="flex" justify="center">
          <el-col class="blob-column" :sm="24" :md="12" :lg="12" :xl="12">
            <img class="blob1" alt="Irregular blob" :src="irregularBlob1" />
          </el-col>
          <el-col class="blob-column" :sm="24" :md="12" :lg="12" :xl="12">
            <img class="blob2" alt="Irregular blob" :src="irregularBlob2" />
          </el-col>
        </el-row>
      </div>
      <div class="content">
        <div class="hero section">
          <el-row type="flex" justify="center">
            <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
              <el-row>
                <el-col :xs="22" :sm="22" :md="12" :lg="12">
                  <h1 class="hero-header">A modern view into the autonomic nervous system.</h1>
                  <el-button type="primary" class="explore-the-data">Explore the data</el-button>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
    <div class="about">
      <div class="texture">
        <el-row class="blob-row" type="flex" justify="space-between">
          <el-col class="blob-column" :sm="24" :md="12" :lg="12" :xl="12">
            <img class="blob3" alt="Irregular blob" :src="transparentBlob3" />
          </el-col>
          <el-col class="blob-column" :sm="24" :md="12" :lg="12" :xl="12">
            <img class="blob4" alt="Irregular blob" :src="transparentBlob3" />
          </el-col>
        </el-row>
      </div>
      <div class="section content">
        <el-row type="flex" justify="center">
          <el-col :xs="22" :sm="22" :md="14" :lg="14">
            <div class="options">
              <span class="option">
                <a :class="{ active: activeTextBlock === 'goal' }" href="#" @click.prevent="toggleText('goal')">Goal</a>
              </span>
              <span>•</span>
              <span class="option">
                <a :class="{ active: activeTextBlock === 'current' }" href="#" @click.prevent="toggleText('current')">Current</a>
              </span>
              <span>•</span>
              <span class="option">
                <a :class="{ active: activeTextBlock === 'future' }" href="#" @click.prevent="toggleText('future')">Future</a>
              </span>
            </div>
            <p>
              {{ activeText }}
            </p>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="section cores">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <el-row class="cards" type="flex" justify="center" :gutter="20">
            <el-col :xs="20" :sm="8" v-for="core in cores" v-bind:key="core.name">
              <el-card class="core-card" shadow="never" :body-style="{ padding: '0px' }">
                <img v-bind:src="core.image" class="image" />
                <div class="content">
                  <p>{{core.name}}</p>
                  <p>{{core.description}}</p>
                  <div class="bottom clearfix">
                    <el-button type="text" class="button">{{core.linkText}}</el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>
    <div class="section search">
      <el-row>
        <el-col>
          <h1>Search the portal</h1>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="12" :lg="8">
          <div class="controls">
            <el-row justify="center" type="flex" gutter="5">
              <el-col :xs="8" :sm="6">
                <div class="control">
                  <el-select
                    v-model="value2"
                    multiple
                    collapse-tags
                    size="large"
                    style="width: 100%; height: 100%; margin: 0; padding: 0; border-radius: 0"
                    placeholder="Select"
                  >
                    <el-option key="datasets" label="Datasets" value="datasets"></el-option>
                    <el-option key="files" label="Files" value="files"></el-option>
                  </el-select>
                </div>
              </el-col>
              <el-col :xs="16" :sm="18">
                <div class="control">
                  <el-autocomplete
                    v-model="state"
                    size="large"
                    :fetch-suggestions="querySearch"
                    placeholder="Start typing..."
                    style="width: 100%; height: 100%; border-radius: 0; padding: 0; margin: 0;"
                    @select="handleSelect"
                  >
                    <i class="el-icon-search el-input__icon" slot="suffix" @click="handleIconClick"></i>
                    <template slot-scope="{ item }">
                      <div class="value">{{ item.value }}</div>
                      <span class="link">{{ item.link }}</span>
                    </template>
                  </el-autocomplete>
                </div>
              </el-col>
            </el-row>
            <el-row>
              <div class="search-button">
                <el-button type="primary" class="view-search-results">View Results</el-button>
              </div>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <featured-datasets />
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import irregularBlob1 from "../../assets/images/irregular-blob-1.svg";
import irregularBlob2 from "../../assets/images/irregular-blob-2.svg";
import transparentBlob3 from "../../assets/images/transparent-blob-3.svg";
import mapCore from "../../assets/images/map-core.png";
import simulationCore from "../../assets/images/simulation-core.png";
import dataCore from "../../assets/images/data-core.png";
import datasetAbstractImage from "../../assets/images/dataset-abstract-image.png";
import SparcFooter from "../../../../../shared/vue_app/src/components/footer/Footer.vue";
import FeaturedDatasets from "../featured-datasets-carousel/FeaturedDatasetsCarousel.vue";

const cores = [
  {
    name: "Data Core",
    description:
      "A collection of curated data provides new insights into the autonomic nervous system. ",
    link: "/data-core",
    linkText: "Explore SPARC Datasets",
    image: dataCore
  },
  {
    name: "Map Core",
    description:
      "Interactive visualizations facilitate exploration of nerve-organ anatomy and function.",
    link: "/map-core",
    linkText: "View Interactive Maps",
    image: mapCore
  },
  {
    name: "Simulation Core",
    description:
      "An online simulation platform enables predictive modeling of neuromodulation effects.",
    link: "/simulation-core",
    linkText: "Explore Simulation Models",
    image: simulationCore
  }
];

export default {
  name: "landing-page",
  components: {
    FeaturedDatasets
  },

  data: () => ({
    textBlocks: {
      goal: 'The SPARC Portal is a free, open-source platform that aims to catalyze development of next-generation bioelectronic medicines.',
      current: 'The SPARC Portal provides a growing collection of autonomic neuroscience datasets, maps, and computational models ⁠— as well as the ability to interact with those resources all within your web browser.',
      future: 'Launched in July 2019, the SPARC Portal will enable users to run advanced analytics and multiscale simulations for predicting the effects of neuromodulation on organ function.'
    },
    activeTextBlock: 'goal',
    irregularBlob1,
    irregularBlob2,
    mapCore,
    simulationCore,
    dataCore,
    transparentBlob3,
    datasetAbstractImage,
    cores,
    value2: '',
    state: ''
  }),

  computed: {
    /**
     * Compute active text to show
     * @returns {String}
     */
    activeText: function () {
      return this.textBlocks[this.activeTextBlock]
    }
  },

  methods: {
    /**
     * Sets the activeTextBlock
     * @param {String}
     */
    toggleText: function(key) {
      this.activeTextBlock = key
    },

    /**
     * @TODO temp function
     */
    handleIconClick: function() {

    }
  }
};
</script>

<style lang="scss" scoped>
.page-container {
  margin-top: -5em;
}

.section-header {
  margin-bottom: 1em;
}

.cards {
  flex-wrap: wrap;
  margin-top: -2em;
}

.flush-column {
  overflow: hidden;
}

.core-card {
  width: 100%;
  margin-top: 2em;

  img {
    width: 100%;
  }

  .content {
    padding: 1em;
    background: #f5f7fa;
  }
}

.search {
  background: #8300bf;
  color: white;
  text-align: center;

  .search-button {
    padding-top: 1em;

    .view-search-results {
      background: #24245b;
      text: #fff;
      border: 0;
    }
  }

  .controls {
    padding-top: 1em;
    min-height: 4em;

    .control {
      display: inline-block;
      height: 100%;
      width: 100%;
      font-size: 2em;

      .search-type-selector {
        padding: 0.5em;
        border: 0;
        color: #8300bf;
        border-radius: 0;
        background: none;
        -webkit-appearance: none;
        width: 100%;
        height: 100%;

        > input {
          border-radius: 0 !important;
          border: 0 !important;
          background: none;
        }
      }

      .search-input {
        background: none;
        border: 0;
        padding: 0.5em;
        color: #8300bf;
        -webkit-appearance: none;
        width: 100%;
        height: 100%;

        > input {
          border-radius: 0 !important;
          border: 0 !important;
          background: none;
        }

        ::placeholder {
          color: #8300bf;
          opacity: 1;
        }
      }
    }
  }
}

.texture {
  z-index: 0;
  height: 100%;
  min-height: 100%;
  position: absolute;
  width: 100%;
  user-select: none;
  overflow: hidden;

  .blob-row {
    height: 100%;
    background: none;
    flex-wrap: wrap;

    .blob-column {
      height: 100%;
      text-align: center;
      padding-left: 5em;
      padding-right: 5em;
      padding-bottom: 3em;
      background: none;

      img {
        height: 100%;
      }

      img.blob1 {
        padding-left: 5em;
      }

      img.blob2 {
        transform: scale(0.7);
      }

      img.blob3 {
        margin-top: 1em;
        margin-left: -3em;
        transform: scale(1.8);
      }

      img.blob4 {
        margin-top: 5em;
        margin-right: -1em;
        transform: scale(1.8);
      }
    }
  }
}

.content {
  z-index: 1;
  position: relative;
}

.hero-header {
  margin-bottom: 0.5em;
}

.head {
  position: relative;
  z-index: -1;

  .content {
    .hero {
      padding-top: 13em;
      padding-bottom: 10em;
    }
  }
}

.about {
  background: #24245b;
  color: #f9f2fc;
  text-align: center;
  font-family: "Asap", sans-serif;
  font-size: 22px;
  position: relative;

  .content {
    .option {
      padding: 0 0.5em;

      a {
        text-decoration: none;
        color: #f9f2fc;

        &.active {
          color: #c200fd;
        }
      }
    }
  }
}

.section {
  padding: 5rem 0;
}

.explore-the-data {
  background: #8300bf;
  text-transform: uppercase;
  border: 0px;
}

.cores {
  background: #edf1fc;
}
</style>
