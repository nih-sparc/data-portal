<template>
    <div id="sparc-browse">
        <div id="left-content-column">
            <router-link to="bar">Go to Bar</router-link>
            <router-link to="foo">Go to Foo</router-link>
        </div>
        <div id="right-content-column">
            <div class="sparc-browse">
                <div class="browse-search-bar">
                    <sparc-browse-search 
                        v-bind:models="models"
                        v-bind:activeModel="activeModel"
                        @labelChanged="onLabelChanged"/>
                    <sparc-browse-filter 
                        @addFilter="onAddFilter"/>
                </div>
                <div class="browse-table">
                    <el-table                   
                        :data="tableData"
                        @sort-change="sortChange"
                        style="width: 100%"
                        height="calc(100vh - 130px)">
                        <el-table-column v-for="tableColumn in tableColumns" :key="tableColumn.name"
                            v-bind:prop="tableColumn.prop"
                            v-bind:label="tableColumn.name"
                            sortable=custom
                            width="200" />        
                        <infinite-loading
                            slot="append"
                            @infinite="infiniteHandler"
                            force-use-infinite-wrapper=".el-table__body-wrapper">
                        </infinite-loading>  
                    </el-table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading';
import SparcBrowseSearch from '../sparc-browse-search/SparcBrowseSearch.vue'
import SparcBrowseFilter from '../sparc-browse-filter/SparcBrowseFilter.vue'

export default {
    components: {
        InfiniteLoading,
        SparcBrowseSearch,
        SparcBrowseFilter
    },
    name: 'sparc-browse',
    

    data() {
      return {
        tableColumns: [],
        tableData: [],
        event:[],
        filterOptions: {prop: '', order: 'ascending'},
        scrollState: '',
        models:[],
        activeModel: '',
        filters: []
      }
    },
    computed: {
        visibleRecords() {
            return this.tableData.slice((this.currentPage-1)*this.pageSize, this.currentPage*this.pageSize )
        }
    },

    props: {
       
    },
    methods: {
        onLabelChanged(ev) {
            console.log("on lable changed")
            this.activeModel = ev.value
            
            if (this.scrollState) {
                this.scrollState.reset()
            }

            this.updateColumnHeaders()
            this.updateURI()
            this.requestData(0, 50)
        },
        updateURI() {
            const m = encodeURI(this.activeModel)
            const q = window.btoa(this.filters) 

            this.$router.push({ path: 'models', query: { model: m, filters: q } })
        },
        sortChange(ev) {
            this.event = ev
            if (this.scrollState) {
                this.scrollState.reset()
            }
            this.filterOptions = {prop: ev.prop, order: ev.order}
            this.requestData(0, 50)
            
        },
        updateColumnHeaders() {
            var req_str = '../api/db/model/' + this.activeModel + '/props'

            this.axios
            .get(req_str)
            .then(response => {
                var columnHeaders = []
                for(var k in response.data) {
                    columnHeaders.push({
                       name: response.data[k],
                       prop: response.data[k] 
                    })
                }
                this.tableColumns = columnHeaders
            })
            .catch(e => {
                console.log(e)
            })
        },
        onAddFilter(ev) {
            console.log('adding filter')

            this.filters.push({
                m: ev.model,
                o: ev.operand,
                v: ev.value
            })
            this.updateURI()
            
            if (this.scrollState) {
                this.scrollState.reset()
            }

            this.requestData(0, 50)

        },
        onRemoveFilter(ev) {
            console.log('remove filter')
        },
        requestData(offset, limit, append) {
            const orderby = encodeURI(this.filterOptions['prop'])
            const descend = encodeURI(this.filterOptions['order'])
            const activeModel = encodeURI(this.activeModel)
            
            var req_str = '../api/db/model/' + activeModel + '?offset=' + offset + '&limit=' + limit
            if (orderby) {
                req_str += '&orderby=' + orderby + '&desc=' + descend
            }
            if (this.filters) {
                const filters = encodeURI(JSON.stringify(this.filters))
                req_str += '&filters=' + filters
            }

            console.log(req_str)
            this.axios
            .get(req_str)
            .then(response => {
                console.log('get results')
                if (append) {
                    this.tableData = this.tableData.concat(response.data)
                    if (this.scrollState) {
                        if (response.data.length > 0) {
                            this.scrollState.loaded()
                        } else {
                            this.scrollState.complete()
                        }
                    }
                }
                else {
                   this.tableData = response.data 
                   if (this.scrollState) {
                        if (response.data.length > 0) {
                            this.scrollState.loaded()
                        } else {
                            this.scrollState.complete()
                        }
                    } 
                }
            })
            .catch(e => {
                console.log(e)
            })
        },
        infiniteHandler(state) {
            this.scrollState = state
            if (this.activeModel){
                this.requestData(this.tableData.length, 50, true)
            } else {
                state.complete()
            }
        },
    },
    mounted () {
        this.axios
            .get('../api/db/labels ')
            .then(response => {
                this.models = response.data
            })
            .catch(e => {
                console.log(e)
            })

        
    },

}
</script>

<style lang="scss" scoped>

    #sparc-browse {
        display: flex;
        flex-direction: row;
        width: 100%;
    }

    .sparc-browse {
        margin-right: 8px;
        margin-bottom: 8px;
        display: flex;
        flex-direction: column
    }

    .browse-table {
        border: 1px solid lightgray;
    }

    .browse-search-bar {
        display: flex;
        margin-bottom: 8px;
        justify-content: space-between;
    }

    #left-content-column {
        flex: 0;
        flex-basis: 250px;
    }

    #right-content-column {
        flex: 1;
        overflow:scroll;
    }
</style>
