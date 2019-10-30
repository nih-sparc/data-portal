<template>
  <div id="sparc-dat-core-browse">
    <div class="header">
      <div class="gradient">
        <el-row type="flex" justify="center">
          <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
            <div class="breadcrumb">
              <el-row>
                <el-col :xs="24" :lg="12">
                  <h3>Data</h3>
                  <p>A growing collection of SPARC data provides insight into neural control of organ function. Datasets are annotated with common standards, allowing users to perform cross-dataset comparisons and analyses.</p>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="search section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="12" :lg="8">
          <search-controls
            :search-on-load="true"
            :is-clear-search-visible="isClearSearchVisible"
            submit-text="Go"
            @query="onSearchQuery"
          />
        </el-col>
      </el-row>
    </div>
    <div class="section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <div class="tableMetadata">
            <div class="number-of-records">Showing {{ totalCount }} datasets</div>
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

          <grid-embargo
            v-if="searchType === 'embargo'"
            v-loading="loading"
            :cards="results"
          />

          <div
            v-if="searchType === 'files'"
            class="files-table">
            <el-table :data="results">
              <el-table-column
                fixed
                label="Name"
                min-width="300"
              >
                <template slot-scope="scope">
                  <div v-if="isMicrosoftFileType(scope)">
                    <a href="#" @click.prevent="openFile(scope)">  {{ scope.row.name }} </a>
                  </div>
                  <div v-else>
                    {{ scope.row.name }}
                  </div>
                </template>
              </el-table-column>
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
                align="right"
                fixed="right"
                label="Operation"
                min-width="100"
                width="100"
              >
                <template slot-scope="scope">
                  <el-dropdown
                    trigger="click"
                    @command="onCommandClick"
                  >
                    <el-button
                      icon="el-icon-more"
                      size="small"
                    />
                    <el-dropdown-menu slot="dropdown">
                      <el-dropdown-item
                        :command="{
                          type: 'requestDownloadFile',
                          scope
                        }"
                      >
                        Download
                      </el-dropdown-item>
                      <el-dropdown-item
                        v-if="isMicrosoftFileType(scope)"
                        :command="{
                          type: 'openFile',
                          scope
                        }"
                      >
                        Open
                      </el-dropdown-item>
                    </el-dropdown-menu>
                  </el-dropdown>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-col>
      </el-row>
      <el-row
        v-if="totalCount > 0"
        type="flex"
        justify="center"
      >
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
  pathOr,
  propOr
} from 'ramda'
import Grid from "../grid/Grid.vue";
import GridEmbargo from "../gridEmbargo/GridEmbargo.vue";

import SearchControls from "../search-controls/SearchControls.vue";
import Pagination from "../Pagination/Pagination.vue";
import BfButton from '../shared/BfButton/BfButton.vue'

import FormatStorage from '../../mixins/bf-storage-metrics/index'

import "regenerator-runtime/runtime";

export default {
  name: "browse",

  components: {
    BfButton,
    Grid,
    SearchControls,
    Pagination,
    GridEmbargo
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

  computed: {
    /**
     * Compute if the clear search
     * button is visible
     * @returns {Boolean}
     */
    isClearSearchVisible: function() {
      return this.searchTerms !== ''
    },
  },

  created: function () {
    if (window.gtag) {
      const routerBase = pathOr('', ['options', 'base'], this.$router)
      window.gtag('config', 'UA-143804703-1', {
        'page_title' : this.$route.name,
        'page_path': `${routerBase}/#${this.$route.fullPath}`
      })
    }
  },

  methods: {

    /**
       * Checks if file is MS Word, MS Excel, or MS Powerpoint
       * @param {Object} scope
       */
      isMicrosoftFileType: function(scope) {
        return scope.row.fileType === 'MSWord' || scope.row.fileType === 'MSExcel' || scope.row.fileType === 'PowerPoint'
      },
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

    onCommandClick: function(evt) {
      const scope = propOr({}, 'scope', evt)
      const type = propOr({}, 'type', evt)
      const handler = this[type]

      if (typeof handler === 'function') {
        handler(scope)
      }
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
      let requestUrl = ''

      switch (type) {
        case "datasets":
        case "files":
          requestUrl = `https://api.blackfynn.io/discover/search/${type}?limit=${this.limit}&offset=${offset}&organization=SPARC%20Consortium`;

          if (terms) {
            requestUrl += `&query=${terms}`
          }
          break;
        case "embargo":
          requestUrl = `/api/datasets/embargo`;
          break;
      }

      // Update URL to reflect the search
      this.$router.push({
        query: {
          searchType: type,
          searchTerms: terms
        }
      })

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
            case "embargo":
              this.results = response.data
              this.limit = response.data.length;
              this.offset = 0;
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
     * Opens a file in a new tab
     * This is currently for MS Word, MS Excel, and Powerpoint files only
     * @param {Object} scope
     */
    openFile: function(scope) {
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
          const url = response.data
          const encodedUrl = encodeURIComponent(url)
          const finalURL = `https://view.officeapps.live.com/op/view.aspx?src=${encodedUrl}`
          window.open(finalURL, '_blank')
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
