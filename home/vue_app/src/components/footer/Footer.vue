<template>
    <div class="footer-content">
        <contain>
            <el-row>
                <el-col :span="8">
                    <sparc-logo class="logo"/>
                    <div class="contact uppercase">
                        <p>
                            National Institutes of Health<br/>
                            900 Rockville Pike, Bethesda, Maryland
                        </p>
                        <p>
                            gene.civillico@nih.gov
                        </p>
                        <p>
                            301-451-3180
                        </p>

                    </div>
                    <div class="social">
                        <p>Twitter</p>
                        <p>Facebook</p>
                    </div>
                    <div class="external-link uppercase">
                        <a href="https://nih.gov">Visit the NIH site ></a>
                    </div>
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