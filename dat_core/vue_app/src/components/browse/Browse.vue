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
import DataTable from "../data-table/DataTable.vue";
import Grid from "../grid/Grid.vue";
import SearchControls from "../search-controls/SearchControls.vue";
import Pagination from "../Pagination/Pagination.vue";

export default {
  name: "browse",
  components: {
    DataTable,
    Grid,
    SearchControls,
    Pagination
  },
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
            case "file":
              this.results = response.data.files.map(response => ({
                key: response.uri,
                title: response.name,
                description: "",
                href: "/",
                cta: "Download file"
              }));
              break;
          }

          this.loading = false;
        }.bind(this)
      );
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

.card {
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
