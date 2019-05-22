<template>
  <div class="sparc-filter-list">
        <el-tag
            v-for="filter in filters"
            :key="filter.m"
            closable
            :type="info"
            @close="handleClose(filter)">
            {{filter.m}} {{filter.o}} {{filter.v}}
        </el-tag>
  </div>
</template>

<script>

export default {
    name: 'sparc-filter-list',

    props: {
        filters: {
            type: Array
        }
    },
    data() {
        return {
        
        };
    },
    methods: {
        handleClose(filter) {
            this.$emit('filterRemoved', filter)
    },
    }
    

}
</script>

<style lang="scss" scoped>
    .el-tag + .el-tag {
        margin-left: 10px;
    }

</style>
