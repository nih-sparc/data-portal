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
                    <el-option v-for="type in types" v-bind:key="type.key">{{ type.label }}</el-option>
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
          <div class="tableMetadata">
            <div class="tags">
              <div v-for="tag in appliedTags" v-bind:key="tag.key" class="tag">
                <div class="content">{{ tag.key }} = {{ tag.value }}</div>
                <div class="delete">X</div>
              </div>
            </div>
            <div class="number-of-records">Showing {{ totalCount }} records</div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <grid v-bind:cards="responseCards" />
        </el-col>
      </el-row>
    </div>
    <div class="data section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <data-table table-class="browse-table" :totalCount="totalCount" />
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
import DataTable from "../data-table/DataTable.vue";
import Grid from "../grid/Grid.vue";

const example = {
  key: "dataset1",
  title: "Powley 2018 VNS-Gastric MRI Study",
  description:
    "Lu, K. H., et al. (2018). Vagus nerve stimulation promotes gastric emptying by increasing pyloric opening measured with magnetic resonance imaging. Neurogastroenterology & Motility",
  href: "/dataset1",
  cta: "Explore dataset"
};

export default {
  name: "browse",
  components: {
    DataTable,
    Grid
  },
  data: () => ({
    types: [
      {
        label: "Datasets",
        key: "dataset"
      },
      {
        label: "Models",
        key: "model"
      },
      {
        label: "Files",
        key: "file"
      }
    ],
    totalCount: 1,
    properties: {
      dataset: [
        {
          label: "Sample size",
          key: "sampleSize"
        }
      ],
      model: [
        {
          label: "Protein target",
          key: "proteinTarget"
        }
      ],
      file: [
        {
          label: "File type",
          key: "fileType"
        },
        {
          label: "Compression",
          key: "compression"
        }
      ]
    },
    appliedTags: [
      {
        key: "model",
        value: "mouse"
      },
      {
        key: "model",
        value: "mouse"
      },
      {
        key: "model",
        value: "mouse"
      }
    ],
    responseCards: [example, example, example, example, example],
    tableData: [
      {
        date: "2016-05-03",
        name: "Tom",
        state: "California",
        city: "Los Angeles",
        address: "No. 189, Grove St, Los Angeles",
        zip: "CA 90036",
        tag: "Home"
      },
      {
        date: "2016-05-02",
        name: "Tom",
        state: "California",
        city: "Los Angeles",
        address: "No. 189, Grove St, Los Angeles",
        zip: "CA 90036",
        tag: "Office"
      },
      {
        date: "2016-05-04",
        name: "Tom",
        state: "California",
        city: "Los Angeles",
        address: "No. 189, Grove St, Los Angeles",
        zip: "CA 90036",
        tag: "Home"
      },
      {
        date: "2016-05-01",
        name: "Tom",
        state: "California",
        city: "Los Angeles",
        address: "No. 189, Grove St, Los Angeles",
        zip: "CA 90036",
        tag: "Office"
      }
    ]
  })
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

.search {
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
</style>
