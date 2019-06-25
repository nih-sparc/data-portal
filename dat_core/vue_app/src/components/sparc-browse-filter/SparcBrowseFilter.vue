<template>
  <div class="sparc-browse-filter">
    <el-select class="propSelect" v-model="propValue" filterable placeholder="Filter on..." @change="handleSelectProp">
        <el-option
        v-for="item in propOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value">
        </el-option>
    </el-select>
    <el-select v-if="isPropNumeric" class="operandSelect" 
        v-model="matchValue" 
        filterable 
        placeholder="Select..." 
        @change="handleSelectMatch">
        <el-option
            v-for="item in operantOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
    </el-select>
    <el-input-number v-if="isPropNumeric" 
        v-model="propValueNumeric" 
        controls-position="right"
        v-bind:min="propRange.min"
        v-bind:max="propRange.max"
        ></el-input-number>
    <el-select v-else-if="isPropBoolean" 
        v-model="input" placeholder="Select">
        <el-option 
            v-for="item in boolOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
    </el-select>
    <el-autocomplete v-else
        class="stringInput"
        placeholder="Property value..." 
        v-model="input" 
        :fetch-suggestions="querySearchAsync"
        @select="handleSelect"></el-autocomplete>
    <el-button class="add-button" type="primary" icon="el-icon-plus" circle @click="addFilter"></el-button>

  </div>
</template>

<script>
    export default {
        name: 'sparc-browse-filter',

        props: {
            activeModel: {
                type: String
            },
            hops: {
                type: Number
            }
        },
        watch: {
            // Set initial value after retrieving models from parent
            activeModel (newVal, oldVal) {
                this.axios
                .get('../api/db/graph/model/' + this.activeModel + '/hops/' + this.hops)
                .then(response => {
                    this.activeNeighbors = response.data
                })
                .catch(e => {
                    console.log(e)
            })    
            }
        },
        data() {
            return {
                links: [],
                boolOptions: [{
                    value: 'true',
                    label: 'true'
                    }, {
                    value: 'false',
                    label: 'false'
                    }
                ],
                matchOptions: [{
                    value: 'STARTS WITH',
                    label: 'Starts With',
                    type: ['String','','Date']
                    }, {
                    value: 'ENDS WITH',
                    label: 'Ends With',
                    type: ['String','','Date']
                    }, {
                    value: 'CONTAINS',
                    label: 'Contains',
                    type: ['String','','Date']
                    }, {
                    value: '<',
                    label: '<',
                    type: ['Number', 'Float', 'Integer', 'Long','Double']
                    }, {
                    value: '>',
                    label: '>',
                    type: ['Number', 'Float', 'Integer','Long','Double']
                    }, {
                    value: '=',
                    label: '=',
                    type: ['Number', 'Float', 'Integer','Long','Double']
                    }, {
                    value: 'IS',
                    label: 'IS',
                    type: ['Boolean']
                    }
                    ],
                propValue: {'value': {'name':'', 'type':'String'}, 'label':''},  
                propRange: {},
                matchValue:'',
                input: '',
                propValueNumeric: NaN,
                select: 'content',
                filters: {},
                propObjects: [],
                activeNeighbors: [],
                hideProps: ['id','label','updatedAt','createdAt','updatedBy','createdBy', 'deleted','organizationId','datasetId'],
                ev:[],
            }
        },
        computed: {
            propOptions () {
                var propObjs = []

                for (var i in this.propObjects) {
                    if (this.activeNeighbors.includes(this.propObjects[i]['model']) && !this.hideProps.includes(this.propObjects[i]['prop'])) {
                        const str = this.propObjects[i]['model'] + ':' + this.propObjects[i]['prop']
                        propObjs.push( {'value': i, 'type':this.propObjects[i]['type'], 'label':str.substring(0, 50)} )
                    }
                }
                return propObjs
            },
            isPropNumeric () {
                if (this.propObjects[this.propValue]) {
                    return ['Number', 'Float', 'Integer', 'Long','Double'].includes(this.propObjects[this.propValue]['type'])
                } 
                return false
            },
            isPropBoolean () {
                if (this.propObjects[this.propValue]) {
                    return this.propObjects[this.propValue]['type'] == 'Boolean'
                } 
                return false
            },
            operantOptions () {
                let curType
                if (this.propObjects[this.propValue]) {
                    curType = this.propObjects[this.propValue]['type']
                } else {
                    return []
                }
                console.log('Curtype: ' + curType)
                var opObjs = []
                for (var option in this.matchOptions) {
                    const curOption = this.matchOptions[option]
                    if (curOption['type'].includes(curType)) {
                        opObjs.push( {
                            value: curOption['value'],
                            label: curOption['label']

                        })
                    }
                }
                return opObjs
            }
        },
        methods: {
            handleSelectProp(ev) {
                this.input = ''
                this.matchValue = 'CONTAINS'
                this.propValueNumeric = NaN

                if (this.isPropBoolean) {
                    this.matchValue = 'IS'
                } else if (this.isPropNumeric) {
                    this.matchValue = '>'
                    const model = this.propObjects[this.propValue]['model']
                    const prop = this.propObjects[this.propValue]['prop']
                    this.axios
                        .get('../api/db/graph/' + model +'/' + prop + '/range')
                        .then(response => {
                            this.propRange = response.data
                            this.propValueNumeric = this.propRange['min']
                        })
                        .catch(e => {
                            console.log(e)
                    })
                }
            },
            handleSelectMatch(ev) {
            },
            addFilter(ev) {
                // Update query in URL which will trigger reload of data
                var valueStr = ''
                if (this.isPropNumeric) {
                    valueStr = this.propValueNumeric.toString();
                } else {
                    valueStr = this.input
                }

                const curProp = this.propObjects[this.propValue]['model'] + ':' + this.propObjects[this.propValue]['prop']
                this.$emit('addFilter', { model: this.propObjects[this.propValue]['model'], prop: curProp, operand: this.matchValue, value: valueStr})
                
                this.input = ''
                this.matchValue = ''
                this.propValue = ''
                this.propValueNumeric = NaN
            },
            querySearchAsync(queryString, cb) {
                
                var links = this.links;
                const curProp = this.propObjects[this.propValue]['model'] + ':' + this.propObjects[this.propValue]['prop']

                const activeModel = this.propObjects[this.propValue]['model']
                
                // Filter
                var valueStr = this.input
                const filters = encodeURIComponent(JSON.stringify([{m: curProp, o: this.matchValue, v:valueStr}]))
                const responseProps = JSON.stringify([this.propObjects[this.propValue]['prop']])

                console.log('Setting filter: ' + filters)
                var req_str = '../api/db/model/' + activeModel + '?offset=' + 0 + '&limit=' + 30 + '&filters=' + filters + '&responseProps=' + responseProps

                var results
                var res = []
                this.axios
                    .get(req_str)
                    .then(response => {
                        results = response.data
                        this.ev = results
                        for (var item in results) {
                            for (var i in results[item]) {
                                res.push({value:results[item][i]})
                            }

                            
                        }
                    })
                    .catch(e => {
                        console.log(e)
                })
                clearTimeout(this.timeout);
                this.timeout = setTimeout(() => {
                    cb(res);
                }, 500 * Math.random());
            },
            createFilter(queryString) {
                return (link) => {
                return (link.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
                };
            },
            handleSelect(item) {
                console.log(item);
            }
        },
        mounted () {
            this.axios
                .get('../api/db/graph/properties ')
                .then(response => {
                    this.propObjects = response.data
                    console.log(this.propObjects)
                })
                .catch(e => {
                    console.log(e)
            })

        }
    }   
</script>

<style lang="scss" scoped>
    @import '../../../../../static/css/_variables.scss';

    .sparc-browse-filter {
        display: flex;
        flex-direction: row
    }

    .add-button {
        margin-left: 20px;
    }

    .propSelect {
        min-width: 300px;
    }

    .operandSelect {
        width: 100px;
    }

    .stringInput {
        min-width: 300px;
    }
</style>
