<template>
    <div class="sparc-browse">
        <div class="browse-search-bar">
            <sparc-browse-search @labelChanged="onLabelChanged"/>
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
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading';
import SparcBrowseSearch from '../sparc-browse-search/SparcBrowseSearch.vue'

export default {
    components: {
        InfiniteLoading,
        SparcBrowseSearch
    },
    name: 'sparc-browse',

    data() {
      return {
        tableColumns: [],
        tableData: [],
        event:[],
        filterOptions: {prop: '', order: 'ascending'},
        scrollState: {},
        model: ''
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
            console.log('Label Changed' + ev.value)
            this.model = ev.value
            this.updateColumnHeaders()
            this.requestData(0,50)
        },
        sortChange(ev) {
            console.log('Sort change ' + ev)
            this.event = ev
            this.filterOptions = {prop: ev.prop, order: ev.order}
            this.requestData(0, 50, ev.prop, ev.order)
            
        },
        updateColumnHeaders() {
            var req_str = '../api/db/model/' + this.model + '/props'

            this.axios
            .get(req_str)
            .then(response => {
                console.log("Updating headers")
                var columnHeaders = []
                for(var k in response.data) {
                    columnHeaders.push({
                       name: response.data[k],
                       prop: response.data[k] 
                    })
                }
                console.log(columnHeaders)
                this.tableColumns = columnHeaders
            })
            .catch(e => {
                console.log(e)
            })
        },
        requestData(offset, limit, orderby, descend, append) {
            
            var req_str = '../api/db/model/' + this.model + '?offset=' + offset + '&limit=' + limit 
            if (orderby != '') {
                req_str += '&orderby=' + orderby + '&desc=' + descend
            }

            this.axios
            .get(req_str)
            .then(response => {
                if (append) {
                    this.tableData = this.tableData.concat(response.data)
                    if (this.scrollState) {
                        this.scrollState.loaded()
                    } else {
                        console.log('no state')
                    }
                }
                else {
                   this.tableData = response.data 
                }
            })
            .catch(e => {
                console.log(e)
            })
        },
        infiniteHandler(state) {
            this.scrollState = state
            this.requestData(this.tableData.length, 50, this.filterOptions.prop, this.filterOptions.order, true)
        },
        getRecords(model, offset, limit) {
            console.log('../api/db/model/' + model +'?offset='+ offset + '&limit=' + limit)
            
        }
    },
    mounted () {
        this.model = location.pathname.split('/')[2]

        this.axios
            .get('../api/db/labels')
            .then(response => {

                this.model = response.data[0]
                this.updateColumnHeaders()
                this.requestData(0,50)
            })
            .catch(e => {
                console.log(e)
            })
    },

}
</script>

<style lang="scss" scoped>

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
        margin-bottom: 8px
    }
</style>
