<template>
    <div>
        <div class="header-and-hero">
            <div class="texture">
                <contain>
                    <img alt="blob1" :src="irregularBlob1"/>
                    <img alt="blob2" :src="irregularBlob2"/>
                </contain>
            </div>
            <div class="content">
                <div class="nav section">
                    <contain>
                        <sparc-header/>
                    </contain>
                </div>
                <div class="section">
                    <contain>
                        <el-row>
                            <el-col :span="10">
                                <h1>Advancing the neuromodulation field toward treatments that change lives.</h1>
                                <el-button type="primary" class="explore-the-data">Explore the data</el-button>
                            </el-col>
                        </el-row>
                    </contain>
                </div>
            </div>

        </div>

        <div class="section about">
            <contain>
                <ul>
                    <li>Goal</li>
                    <li>Current</li>
                    <li>Future</li>
                </ul>
                <h3>SPARC is a consortium of researchers, data experts, coders, and scientists seeking to map the nervous system. The project is data focused and split into 3 core groups.</h3>
            </contain>
        </div>
        <div class="section cores">
            <contain>
                <el-row type="flex" justify="space-around" :gutter="20">
                    <el-col>
                        <el-card shadow="never" :body-style="{ padding: '0px' }">
                            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                 class="image">
                            <div style="padding: 14px;">
                                <span>Data core</span>
                                <div class="bottom clearfix">
                                    <el-button type="text" class="button">Browse the data</el-button>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col>
                        <el-card shadow="never" :body-style="{ padding: '0px' }">
                            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                 class="image">
                            <div style="padding: 14px;">
                                <span>Map core</span>
                                <div class="bottom clearfix">
                                    <el-button type="text" class="button">Check out the visualizations</el-button>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col>
                        <el-card shadow="never" :body-style="{ padding: '0px' }">
                            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                 class="image">
                            <div style="padding: 14px;">
                                <span>Simulation core</span>
                                <div class="bottom clearfix">
                                    <el-button type="text" class="button">Launch o2S2PARC Platform</el-button>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </contain>

        </div>
        <div class="section">
            <contain>
                <h2>Search the portal</h2>

            </contain>
        </div>
        <div class="section">
            <contain>
                <h2>Featured datasets</h2>

            </contain>
        </div>
        <div class="section footer">
            <sparc-footer/>
        </div>
    </div>
</template>

<script>
    import Contain from "../contain/Contain.vue";
    import SparcFooter from "../footer/Footer.vue";
    import SparcHeader from "../header/Header.vue";
    import irregularBlob1 from "../../assets/images/irregular-blob-1.svg";
    import irregularBlob2 from "../../assets/images/irregular-blob-2.svg";

    export default {
        name: "landing-page",
        components: {
            Contain,
            SparcFooter,
            SparcHeader
        },
        data: () => ({
            irregularBlob1,
            irregularBlob2
        })
    }
</script>

<style lang="scss" scoped>
    .header-and-hero {
        min-height: 560px;
        height: 560px;
        font-family: SFProText-Regular;

        .texture {
            z-index: 0;
            position: absolute;
            height: 100%;
            min-height: 100%;
        }

        .content {
            z-index: 1;
            position: absolute;

            h1 {
                font-size: 48pt;
            }

            .nav {
                height: 50px;
            }

            .hero {

            }
        }
    }

    .about {
        background: #24245B;
        color: white;
        min-height: 150px;
    }

    .section {
        padding: 20px 0px;
    }

    .explore-the-data {
        background: #8300BF;
        text-transform: uppercase;
        border: 0px;
    }

    .cores {
        background: #EDF1FC;
    }

    .footer {
        padding: 60px 0px;
        background: #EDF1FC;
    }
</style>