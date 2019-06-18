<template>
    <div class="dataset-landing-page">
        <div class="dataset-breadcrumb-gradient">
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                    <div class="breadcrumb">
                        Data Core / Powley 2018 VNS-Gastric MRI Study
                    </div>
                </el-col>
            </el-row>
        </div>
        <div class="dataset-info-section">
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                    <el-row :gutter="20">
                        <el-col :span="16">
                            <div class="dataset-info">
                                <h2>Powley 2018 VNS-Gastric MRI Study</h2>
                                <p>Lu, K. H., et al. (2018). Vagus nerve stimulation promotes gastric emptying by increasing pyloric
                                    opening measured with magnetic resonance imaging. Neurogastroenterology & Motility, e1338</p>
                                <div class="updated-on">
                                    <p>Updated on January 9, 2019 </p>
                                </div>
                                <div class="authors">
                                    <p>Bartek Rajwa</p><span></span><span><strong>Kevin M. Jackson</strong></span>
                                </div>
                                <div class="actions">
                                    <el-button
                                            type="primary"
                                            class="get-dataset"
                                    >
                                        Get Dataset
                                    </el-button>
                                    <el-button
                                            type="secondary"
                                            class="view-simulations"
                                    >
                                        View Simulations
                                    </el-button>
                                </div>
                                <div class="attributes">
                                    <div class="file-count">

                                    </div>
                                    <div class="file-size">

                                    </div>
                                    <div class="license">

                                    </div>
                                </div>
                            </div>

                        </el-col>
                        <el-col :span="8">
                            <div class="dataset-image">
                                <img :src="datasetAbstractImage"/>
                            </div>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
        </div>
        <div class="about-this-dataset-section">
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                    <h3>About this dataset</h3>
                    <div class="updated-on">
                        <p>January 9, 2019</p>
                        <p class="label">Last Updated</p>
                    </div>
                    <div class="cite-dataset">
                        <p>Cite this dataset</p>
                        <textarea
                                value="Bartek Rajwa and Kevin Jackson. “Powley 2018 VNS-Gastric MRI Study.” https://doi.org/10.7939/r3m8ac11"/>
                        <ul>
                            <li>Formatted as:</li>
                            <li><a class="active" href="">APA</a></li>
                            <li><a href="">Chicago</a></li>
                            <li><a href="">IEEE</a></li>
                            <li><a href="https://datacite.org">More on Datacite.org</a></li>
                        </ul>
                    </div>
                    <div class="tags">
                        <ul>
                            <li>Nervous System</li>
                            <li>Stimulation</li>
                            <li>Animals</li>
                            <li>Research</li>
                        </ul>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import datasetAbstractImage from "../../assets/images/dataset-abstract-image.png"

    export default {
        name: "dataset-page",
        components: {},
        data: () => ({
            datasetAbstractImage
        })
    }
</script>

<style lang="scss" scoped>
    .dataset-breadcrumb-gradient {
        padding: 1.5em 0;
        color: #F0F2F5;
        background-image: linear-gradient(90deg, #0026FF 0%, #00FFB9 100%);
    }
    .dataset-landing-page {
        padding-top: 6em;
        background: #fff;
    }

    .dataset-info-section {
        padding: 2em 0em;

        .updated-on {
            font-size: 10pt;

            p {
                color: #303133;
                padding: 0;
                margin: 0;
            }
        }

        .authors {
            font-size: 10pt;

            p {
                color: #303133;
                padding: 0;
                margin: 0;
            }
        }
    }

    .dataset-info {
        overflow: hidden;

        h1 {
            margin-bottom: 1em;
        }
    }

    .dataset-image {
        overflow: hidden;
    }



    .actions {
        padding: 2em 0em;
    }

    .about-this-dataset-section {
        padding: 3em 0em;
        overflow: hidden;
        background: #24245B;
        color: white;
    }
</style>