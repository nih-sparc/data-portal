<template>
  <div class="sparc-browse-search">
    <el-select v-model="activeModel" filterable placeholder="Select" @change="handleSelect">
        <el-option
        v-for="item in modelOptions"
        :key="item.value"
        :label="item.label"
        :value="item.value">
        </el-option>
    </el-select>
  </div>
</template>

<script>
    export default {
        name: 'sparc-browse-search',

        props: {
            models: {
                type: Array
            }
        },
        watch: {
            // Set initial value after retrieving models from parent
            models (newVal, oldVal) {
                this.activeModel = newVal[0]
                this.$emit('labelChanged', { value: this.activeModel})
            }
        },

        data() {
            return {
                activeModel: '',  
            }
        },
        computed: {
            modelOptions() {
                var modelOpts = []
                for (var item in this.models) {
                    modelOpts.push({
                        value: this.models[item],
                        label: this.models[item]
                    })
                }
                return modelOpts
            }
        },
        methods: {
            handleSelect(ev) {
                console.log('Handle Select')
                this.$emit('labelChanged', { value: this.activeModel})
            }
        }
    }   
</script>

<style lang="scss" scoped>
    @import '../../../../../static/css/_variables.scss';

    .el-select {
        min-width: 200px;
    }

    .sparc-dataset-filter {
    margin-bottom: 8px;
    }

    .el-autocomplete {
    display: flex;
    }

    .el-autocomplete .el-input {
    width: 110px;
    }
    .input-with-select .el-input-group__prepend {
    background-color: #fff;
    }
</style>
