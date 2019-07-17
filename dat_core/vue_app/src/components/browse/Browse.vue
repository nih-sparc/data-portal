<template>
  <div id="sparc-dat-core-browse">
    <div class="header">
      <div class="gradient">
        <el-row type="flex" justify="center">
          <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
            <div class="breadcrumb">
              <el-row>
                <el-col :xs="24" :lg="12">
                  <h3>Find SPARC data</h3>
                  <p>A growing list of SPARC datasets provides insight into neural control of organ function and datasets are annotated with a common standard.</p>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <!-- <div class="top section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <div class="header">
            <h2>Browse the Meta Data</h2>
          </div>
        </el-col>
      </el-row>
    </div> -->
    <div class="search section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="12" :lg="8">
          <search-controls @query="onSearchQuery" />
        </el-col>
      </el-row>
    </div>
    <div class="section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <div class="tableMetadata">
            <div class="number-of-records">Showing {{ totalCount }} records</div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <grid
            v-if="searchType === 'datasets'"
            v-loading="loading"
            :cards="results"
          />

          <div
            v-if="searchType === 'files'"
            class="files-table"
          >
            <el-table :data="results">
              <el-table-column
                fixed
                prop="name"
                label="Name"
              />
              <el-table-column
                prop="fileType"
                label="File type"
                width="120"
              />
              <el-table-column
                prop="size"
                label="Size"
                width="120"
                :formatter="formatStorage"
              />
              <el-table-column
                fixed="right"
                label="Operations"
                min-width="132"
                width="132"
              >
                <template slot-scope="scope">
                  <bf-button @click="requestDownloadFile(scope)" >
                    Download
                  </bf-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="12" :lg="8">
          <pagination
            :selected="page"
            :page-size="limit"
            :total-count="totalCount"
            @select-page="selectPage"
          />
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
import {
  compose,
  last,
  defaultTo,
  split,
  pathOr
} from 'ramda'
import Grid from "../grid/Grid.vue";
import SearchControls from "../search-controls/SearchControls.vue";
import Pagination from "../Pagination/Pagination.vue";
import BfButton from '../shared/BfButton/BfButton.vue'

import FormatStorage from '../../mixins/bf-storage-metrics/index'

export default {
  name: "browse",

  components: {
    BfButton,
    Grid,
    SearchControls,
    Pagination
  },

  mixins: [
    FormatStorage
  ],

  data() {
    return {
      loading: false,
      totalCount: 0,
      limit: 16,
      offset: 0,
      page: 1,
      results: [],
      searchType: '',
      searchTerms: ''
    };
  },

  mounted: function() {
    this.fetchResults('datasets', '')
  },

  methods: {
    /**
     * Format storage column
     * @param {Object} row
     * @param {Object} column
     * @param {Number} cellValue
     * @returns {String}
     */
    formatStorage: function (row, column, cellValue) {
      return this.formatMetric(cellValue)
    },

    /**
     * On search query event from search controls
     * @param {String} selectedType
     * @param {String} terms
     */
    onSearchQuery: function(selectedType, terms) {
      this.page = 1
      this.fetchResults(selectedType, terms)
    },

    selectPage(index) {
      this.page = index;
      this.fetchResults(this.searchType, this.searchTerms);
    },
    async fetchResults(type, terms) {
      this.results = [];
      this.loading = true;
      this.searchType = type;
      this.searchTerms = terms;

      const offset = (this.page - 1) * this.limit
      const requestUrl = `https://api.blackfynn.io/discover/search/${type}?query=${terms || ""}&limit=${this.limit}&offset=${offset}&organization=SPARC%20Consortium`;

      this.$http.get(requestUrl).then(
        function(response) {
          this.totalCount = response.data.totalCount;
          this.limit = response.data.limit;
          this.offset = response.data.offset;

          switch (type) {
            case "datasets":
              this.results = response.data.datasets
              break;
            case "files":
              this.results = response.data.files.map(response => ({
                uri: response.uri,
                name: response.name,
                size: response.size,
                fileType: response.fileType
              }));
              break;
          }

          this.loading = false;
        }.bind(this)
      );
    },

    /**
     * Download file
     * @param {Object} scope
     */
    requestDownloadFile: function(scope) {
      const filePath = compose(
        last,
        defaultTo([]),
        split('s3://blackfynn-discover-use1/'),
        pathOr('', ['row', 'uri']),
      )(scope)

      const fileName = pathOr('', ['row', 'name'], scope)

      const requestUrl = `/api/download?key=${filePath}`
      this.$http.get(requestUrl).then(
        response => {
          this.downloadFile(fileName, response.data)
        }
      )
    },

    /**
     * Create an `a` tag to trigger downloading file
     * @param {String} filename
     * @param {String} url
     */
    downloadFile: function(filename, url) {
      const el = document.createElement('a')
      el.setAttribute('href', url)
      el.setAttribute('download', filename)

      el.style.display = 'none'
      document.body.appendChild(el)

      el.click()

      document.body.removeChild(el)
    }
  }
};
</script>

<style lang="scss">
.browse-table {
  border: 1px solid #e4e7ed;
}
</style>

<style lang="scss" scoped>
button.clear-all {
  color: #8300bf;
  background: none;
}

.table-metadata {
  display: flex;
}

.number-of-records {
  text-align: right;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  text-align: left;

  .tag {
    text-align: center;
    margin-right: 2em;
    background: #f9f2fc;
    border: 1px solid #8300bf;
    border-radius: 4px;
    display: flex;
    color: #8300bf;
    padding: 0.3em;
    text-transform: uppercase;

    .content {
      text-align: left;
    }

    .delete {
      text-align: right;
      padding-left: 1em;
    }
  }
}

.files-table {
  background: #fff;
  border: 1px solid rgb(228, 231, 237);
  padding: 16px;
}

.section {
  padding: 1em 0;
}

.header {
  .gradient {
    padding: 1.5em 0;
    color: #f0f2f5;
    background-image: linear-gradient(90deg, #0026ff 0%, #00ffb9 100%);

    .breadcrumb {
      width: 50%;
    }
  }
}

.top {
  padding-top: 2em;
  .header {
    h2 {
      text-align: center;
    }
  }
}
</style>
