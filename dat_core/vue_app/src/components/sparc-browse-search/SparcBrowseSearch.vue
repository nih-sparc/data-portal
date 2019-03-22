<template>
  <div class="sparc-browse-search">
    <el-select v-model="value8" filterable placeholder="Select" @change="handleSelect">
        <el-option
        v-for="item in options"
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
        },

        data() {
            return {
                options: [],
                value8: '',  
                input: '',
                select: 'content',
                ev:[]
            }
        },
        computed: {
            placeHolder() {
                if (this.select == 'content') {
                return 'Find dataset...'  
                } else if (this.select == 'authors') {
                return 'Find dataset by author...' 
                }
            }
        },
        mounted () {
            this.axios
                .get('../api/db/labels ')
                .then(response => {
                    const resp = response.data
                    this.value8 = response.data[0]
                    for (var item in resp) {
                        this.options.push({
                            value: resp[item],
                            label: resp[item]
                        })
                    }
                })
                .catch(e => {
                    console.log(e)
                })
        },
        methods: {
            handleSelect(ev) {
                this.$emit('labelChanged', { value: ev})
                this.ev = ev
                console.log(ev)
            }
        }
    }   
</script>

<style lang="scss" scoped>
    @import '../../../../../static/css/_variables.scss';

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
