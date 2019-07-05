<template>
   <div class="contain">
       <el-row class="row" type="flex" justify="center">
           <el-col class="col" :xs="22" :lg="18">
               <slot></slot>
           </el-col>
       </el-row>
   </div>
</template>

<script>
    export default {
        name: "contain",
    }
</script>

<style scoped lang="scss">
    .contain {
        .row {
            .col {
            }
        }
    }
</style>

