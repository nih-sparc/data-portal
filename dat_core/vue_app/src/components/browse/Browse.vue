<template>
  <div id="sparc-dat-core-browse">
    <div class="header">
      <div class="gradient">
        <el-row type="flex" justify="center">
          <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
            <div class="breadcrumb">
              <el-row>
                <el-col :xs="24" :lg="12">
                  <h1>Data Core</h1>
                  <p>DAT-CORE provides a sustainable scientific data management platform for scientific data management and publishing of SPARC data.</p>
                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="top section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <div class="header">
            <h2>Browse the Meta Data</h2>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="search section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="12" :lg="8">
          <search-controls @query="fetchResults" />
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

          <div class="files-table">
            <el-table
              v-if="searchType === 'files'"
              :data="results"
            >
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
                width="112"
              >
                <template slot-scope="scope">
                  <bf-button @click="downloadFile(scope)" >
                    Download
                  </bf-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <pagination
            :selected="page"
            :pageSize="limit"
            :total="totalCount"
            @selectPage="selectPage"
          />
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
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
      page: 0,
      results: [],
      searchType: ''
    };
  },

  mounted: function() {
    this.fetchResults(['datasets', ''])
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

    selectPage(index) {
      this.page = index;
      this.fetchResults();
    },
    async fetchResults([type, terms]) {
      this.results = [];
      this.loading = true;
      this.searchType = type

      const requestUrl = `https://api.blackfynn.io/discover/search/${type}?query=${terms || ""}&limit=${this.limit}&offset=${this.page * this.offset}`;

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
     * @param {Object} file
     */
    downloadFile: function(file) {

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
