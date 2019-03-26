<template>
  <div class="sparc-browse-filter">
    <el-select v-model="propValue" filterable placeholder="Select" @change="handleSelectProp">
        <el-option
        v-for="item in propOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value">
        </el-option>
    </el-select>
    <el-select v-model="matchValue" filterable placeholder="Select" @change="handleSelectMatch">
        <el-option
        v-for="item in matchOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value">
        </el-option>
    </el-select>
    <el-input placeholder="Please input" v-model="input"></el-input>
    <el-button class="add-button" type="primary" icon="el-icon-plus" circle @click="addFilter"></el-button>

  </div>
</template>

<script>
    export default {
        name: 'sparc-browse-filter',

        props: {
        },

        data() {
            return {
                propOptions: [{
                    value: 'patient:age_at_baseline',
                    label: 'patient:age_at_baseline'
                    }, {
                    value: 'something',
                    label: 'something'
                    }, {
                    value: 'else',
                    label: 'else'
                    }],
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
                filters: {}
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
                this.$emit('addFilter', { model: this.propValue, operand: this.matchValue, value: this.input})

            }
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
</style>
