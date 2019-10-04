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
          v-for="heading in headings"
          :key="heading"
          :prop="heading"
          :label="heading"
        />
      </el-table>
    </div>
    </div>
</template>

<script>
import { propOr, head } from 'ramda'
    export default {
        name: 'MetadataTable',
        data() {
            return {
                isLoading: false,
                models: [],
                records: [],
                properties: [],
                headings: [],
                defaultModel: '',
                dropdownSelection: false
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
                if (!this.dropdownSelection) {
                   this.defaultModel = propOr('', 'modelName', head(this.models))
                }
                const datasetId = propOr('', 'id', this.datasetDetails)
                return `https://api.blackfynn.io/discover/search/records?datasetId=${datasetId}&model=${this.defaultModel}`
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
            getMetadataRecords: function(model = '') {
                if (model !== '') {
                    this.dropdownSelection = true
                    this.defaultModel = model
                }
                this.axios.get(this.getRecordsUrl)
        .then(response => {
           this.headings = []
           this.properties = []
           this.records = propOr([], 'records', response.data)
           const properties = propOr({}, 'properties', head(this.records))
           // just to get the property names for the table since they're all
           // the same across records
           for (let key in properties) {
             this.headings.push(key)
           }

           // now to get the properties
           this.records.forEach(record => {
               const properties = propOr({}, 'properties', record)
               this.properties.push(properties)
           })

        })
        .catch(error => {
          // handle error
          this.errorLoading = true
        })
            },
        },
    }
</script>

<style lang="scss" scoped>
    .metadata-table-content {
      background: #fff;
      border: 1px solid rgb(228, 231, 237);
      padding: 16px;
      margin-top: 20px;
      margin-bottom: 30px;
    }
</style>