<template>
    <div class="page">
        <el-row type="flex" justify="center">
            <el-col :xs="22" :sm="22" :md="16" :lg="12" :xl="12">
                <div class="about">
                    <h1>About the Data Portal</h1>
                    <p>The SPARC Portal provides interactive access to a growing collection of data, maps, and computational models that focus on the role of the autonomic nervous system in controlling organ function. These resources are made freely available to the community with the intent of advancing the neuromodulation field towards more precise treatment of diseases and conditions.</p>
                    <div class="rule-container">
                        <div class="rule"></div>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: 'about-page',
        components: {

        }
    }
</script>

<style scoped lang="scss">
    .page {
        padding-top: 8em;

        p {
            color: #606266;
        }
    }

    .about {
        text-align: center;
        min-height: 50vh;
    }

    .rule-container {
        padding-top: 3em;
        display: flex;
        justify-content: center;
        padding-bottom: 5em;
    }

    .rule {
        width: 5em;
        border-bottom: 5px solid #24245B;
    }
</style>