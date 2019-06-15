<template>
    <div class="footer-content">
        <contain>
            <el-row>
                <el-col :span="8">

                </el-col>
                <el-col :span="16">
                    <el-row>

                    </el-row>
                </el-col>
            </el-row>
        </contain>
    </div>
</template>

<script>
    import SparcLogo from "../logo/SparcLogo.vue"
    import Contain from "../contain/Contain.vue"

    export default {
        name: "sparc-footer",
        components: {
            SparcLogo,
            Contain
        }
    }
</script>

<style scoped lang="scss">
    .footer-content {
        font-size: 10pt;
        size: 10pt;
    }

    .uppercase {
        text-transform: uppercase;
    }
</style>