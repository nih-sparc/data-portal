<template>
    <div class="metadata-table">
        <div class="metadata-table-dropdown">
             <el-select v-model="value" placeholder="Select Model" @change="getMetadataRecords">
    <el-option
      v-for="(model, index) in models"
      :key="`${model}-${index}`"
      :label="model.modelName"
      :value="model.modelName">
    </el-option>
  </el-select>
        </div>
         <div class="metadata-table-content">
      <div
        v-if="hasError"
        class="error-wrap"
      >
        <p>Sorry, an error has occurred</p>
        <el-button
          type="primary"
          @click="getMetadataRecords"
        >
          Try again
        </el-button>
      </div>
      <el-table
        v-else
        :data="properties"
        :default-sort = "{prop: 'name', order: 'ascending'}"
        v-loading="isLoading"
      >
        <el-table-column
          v-for="prop in properties"
          :key="prop.label"
          :prop="prop.value"
          :label="prop.label"
          :formatter="formatColumn"
        >
        </el-table-column>
          <!-- <template
            v-if="scope.row.type === 'File'"
            slot-scope="scope"
          >
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
              </el-dropdown-menu>
            </el-dropdown>
          </template> -->
      </el-table>
    </div>
    </div>
</template>

<script>
import { propOr, head, find, propEq } from 'ramda'
    export default {
        name: 'MetadataTable',
        data() {
            return {
                isLoading: false,
                models: [],
                records: [],
                properties: []
            }
        },

        props: {
            datasetDetails: {
                type: Object,
                default: () => {}
            },
        },

        computed: {
            getRecordsUrl: function() {
                const model = propOr('', 'modelName', head(this.models))
                const datasetId = propOr('', 'id', this.datasetDetails)
                return `https://api.blackfynn.io/discover/search/records?datasetId=${datasetId}&model=${model}`
            }
        },

        watch: {
            getRecordsUrl:{
                handler: function(val) {
                    if (val) {
                        this.getMetadataRecords()
                    }
                },
                immediate: true
            },
            datasetDetails: {
                handler: function(val){
                    if (val) {
                      this.models = propOr([], 'modelCount', this.datasetDetails)
                    }
                },
                immediate: true
            }
        },

        methods: {
            getMetadataRecords: function() {
                this.axios.get(this.getRecordsUrl)
        .then(response => {
           this.records = propOr([], 'records', response.data)
           this.records.forEach(record => {
              const properties = propOr({}, 'properties', record)


              for (let key in properties) {
                  const keyExists = find(propEq('label', key), this.properties)
                  if (keyExists) {
                      // find the object with that key and push to the array
                  }
                this.properties.push({
                    label: key,
                    value: properties[key]
                })
              }
           })

        })
        .catch(error => {
          // handle error
          this.errorLoading = true
        })
            },

        formatColumn: function(row) {
            return row.value
        }
        },
    }
</script>

<style lang="scss" scoped>

</style>