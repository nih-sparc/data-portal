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
    <el-select class="operandSelect" v-model="matchValue" filterable placeholder="Select..." @change="handleSelectMatch">
        <el-option
        v-for="item in matchOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value">
        </el-option>
    </el-select>
    <el-input placeholder="Property value..." v-model="input"></el-input>
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
                matchOptions: [{
                    value: 'STARTS WITH',
                    label: 'Starts With'
                    }, {
                    value: 'ENDS WITH',
                    label: 'Ends With'
                    }, {
                    value: 'CONTAINS',
                    label: 'Contains'
                    }, {
                    value: '<',
                    label: '<'
                    }, {
                    value: '>',
                    label: '>'
                    }, {
                    value: '=',
                    label: '='
                    }],
                propValue: '',  
                matchValue:'',
                input: '',
                select: 'content',
                filters: {},
                propObjects: [],
                activeNeighbors: []
            }
        },
        computed: {
            propOptions () {
                var propObjs = []

                for (var i in this.propObjects) {
                    if (this.activeNeighbors.includes(this.propObjects[i]['model'])) {
                        const str = this.propObjects[i]['model'] + ':' + this.propObjects[i]['prop']
                        propObjs.push( {'value': str, 'label':str.substring(0, 50)} )
                    }
                }
                // let matchedProps = this.propObjects.find(obj => obj.name in this.activeNeighbors);


                // for (var item in matchedProps) {
                //     console.log(item)
                //     const str = this.matchedProps[item]['model'] + ':' + this.matchedProps[item]['prop']
                //     propObjs.push( {'value': str, 'label':str.substring(0, 50)})
                // }
                return propObjs
            }
        },
        methods: {
            handleSelectProp(ev) {
                // this.$emit('propChanged', { value: ev})
                // this.ev = ev
                console.log(ev)
            },
            handleSelectMatch(ev) {
                // this.$emit('matchChanged', { value: ev})
                // this.ev = ev
                console.log(ev)
            },
            addFilter(ev) {
                console.log('Added filter')
                // Update query in URL which will trigger reload of data
                var valueStr = this.input
                if (['CONTAINS','STARTS WITH','ENDS WITH'].includes(this.matchValue)) {
                    valueStr = '"' + valueStr + '"'
                }

                this.$emit('addFilter', { model: this.propValue, operand: this.matchValue, value: valueStr})

            }
        },
        
        mounted () {
            this.axios
                .get('../api/db/graph/properties ')
                .then(response => {
                    this.propObjects = response.data
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
        min-width: 150px;
    }
</style>
