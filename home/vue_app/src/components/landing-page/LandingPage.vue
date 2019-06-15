<template>
    <el-col>
        <div class="header-and-hero">
            <div class="texture">
                <div class="blobs">
                    <div class="blob blob1">
                        <img alt="Irregular blob" :src="irregularBlob1"/>
                    </div>
                    <div class="blob blob2">
                        <img alt="Irregular blob" :src="irregularBlob2"/>
                    </div>
                </div>
            </div>
            <div class="content">
                <div class="nav section">
                    <el-row type="flex" justify="center">
                        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                            <sparc-header/>
                        </el-col>
                    </el-row>
                </div>
                <div class="hero section">
                    <el-row type="flex" justify="center">
                        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                            <el-row>
                                <el-col :xs="22" :sm="22" :md="16" :lg="14">
                                    <h1>Advancing the neuromodulation field toward treatments that change lives.</h1>
                                    <el-button type="primary" class="explore-the-data">Explore the data</el-button>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </div>
            </div>
        </div>
        <div class="section about">
            <div class="texture">
                <div class="blobs">
                    <div class="blob1">
                        <img alt="blob" :src="transparentBlob3"/>
                    </div>
                    <div class="blob2">
                        <img alt="blob" :src="transparentBlob3"/>
                    </div>
                </div>
            </div>
            <div class="content">
                <el-row type="flex" justify="center">
                    <el-col :xs="22" :sm="22" :md="14" :lg="14">
                        <div class="options">
                            <span class="option"><a class="active">Goal</a></span>
                            <span>•</span>
                            <span class="option"><a>Current</a></span>
                            <span>•</span>
                            <span class="option"><a>Future</a></span>
                        </div>
                        <p>SPARC is a consortium of researchers, data experts, coders, and scientists seeking to map
                            the nervous system. The project is data focused and split into 3 core groups.</p>
                    </el-col>
                </el-row>
            </div>
        </div>
        <div class="section cores">
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                    <div class="cards">
                        <el-row type="flex" :gutter="20">
                            <el-col :md="8" v-for="core in cores" v-bind:key="core.name">
                                <el-card class="core-card" shadow="never" :body-style="{ padding: '0px' }">
                                    <img v-bind:src="core.image" class="image">
                                    <div class="content">
                                        <p>{{core.name}}</p>
                                        <p>{{core.description}}</p>
                                        <div class="bottom clearfix">
                                            <el-button type="text" class="button">{{core.linkText}}</el-button>
                                        </div>
                                    </div>
                                </el-card>
                            </el-col>
                        </el-row>
                    </div>
                </el-col>
            </el-row>

        </div>
        <div class="section search">
            <el-row>
                <el-col>
                    <h1>Search the portal</h1>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="12" :lg="8">
                    <div class="controls">
                        <el-row justify="center" type="flex">
                            <el-col :xs="8" :sm="6">
                                <div class="control">
                                    <el-select
                                            v-model="value2"
                                            multiple
                                            collapse-tags
                                            size="large"
                                            style="width: 100%; height: 100%; margin: 0; padding: 0; border-radius: 0"
                                            placeholder="Select">
                                        <el-option
                                                key="1" label="Datasets" value="datasets">
                                        </el-option>
                                    </el-select>
                                </div>
                            </el-col>
                            <el-col :xs="16" :sm="18">
                                <div class="control">
                                    <el-autocomplete
                                            popper-class="my-autocomplete"
                                            v-model="state"
                                            size="large"
                                            :fetch-suggestions="querySearch"
                                            placeholder="Start typing..."
                                            style="width: 100%; height: 100%; border-radius: 0; padding: 0; margin: 0;"
                                            @select="handleSelect">
                                        <i
                                                class="el-icon-edit el-input__icon"
                                                slot="suffix"
                                                @click="handleIconClick">
                                        </i>
                                        <template slot-scope="{ item }">
                                            <div class="value">{{ item.value }}</div>
                                            <span class="link">{{ item.link }}</span>
                                        </template>
                                    </el-autocomplete>
                                </div>
                            </el-col>
                        </el-row>
                        <el-row>
                            <div class="search-button">
                                <el-button
                                        type="primary"
                                        class="view-search-results"
                                >
                                    View Results
                                </el-button>
                            </div>
                        </el-row>
                    </div>
                </el-col>
            </el-row>
        </div>
        <div class="section">
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                    <div>
                        <el-row>
                            <el-col>
                                <h2 class="section-header">Featured datasets</h2>
                            </el-col>
                        </el-row>
                        <el-row type="flex" justify="flex-start">
                            <el-col :span="12" class="flush-column">
                                <div class="featured-dataset-image"
                                     :style="{ backgroundImage: `url('${datasetAbstractImage}')` }"/>
                            </el-col>
                            <el-col :span="12" class="flush-column">
                                <div class="featured-dataset-description">
                                    <div class="content">
                                        <h2>Powley 2018 VNS-Gastric MRI Study</h2>
                                        <p>Lu, K. H., et al. (2018). Vagus nerve stimulation promotes gastric emptying
                                            by increasing pyloric opening measured with magnetic resonance imaging.</p>
                                        <div class="actions">
                                            <el-button type="primary" class="view-dataset">View dataset</el-button>
                                        </div>
                                    </div>
                                </div>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col>
                                <div class="featured-dataset-carousel-navigation">
                                    <ul>
                                        <li class=""></li>
                                        <li class="active"></li>
                                        <li class=""></li>
                                        <li class=""></li>
                                        <li class=""></li>
                                    </ul>
                                </div>

                            </el-col>
                        </el-row>
                    </div>
                </el-col>
            </el-row>
        </div>
        <el-col class="section footer">
            <el-row type="flex" justify="center">
                <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                    <el-col class="footer-content">
                        <el-row>
                            <el-col :md="8">
                                <sparc-logo class="logo"></sparc-logo>
                                <div class="contact">
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
                            <el-col :md="16">
                                <el-row type="flex" class="link-sections">
                                    <el-col :sm="12" :lg="8" class="link-section">
                                        <p class="link-header">About</p>
                                        <ul>
                                            <li><a href="/">About SPARC</a></li>
                                            <li><a href="/">About SPARC</a></li>
                                        </ul>
                                    </el-col>
                                    <el-col :md="12" :lg="8" class="link-section">
                                        <p class="link-header">About</p>
                                        <ul>
                                            <li><a href="/">About SPARC</a></li>
                                            <li><a href="/">About SPARC</a></li>
                                        </ul>
                                    </el-col>
                                    <el-col :md="12" :lg="8" class="link-section">
                                        <p class="link-header">About</p>
                                        <ul>
                                            <li><a href="/">About SPARC</a></li>
                                            <li><a href="/">About SPARC</a></li>
                                        </ul>
                                    </el-col>
                                    <el-col :md="12" :lg="8" class="link-section">
                                        <p class="link-header">About</p>
                                        <ul>
                                            <li><a href="/">About SPARC</a></li>
                                            <li><a href="/">About SPARC</a></li>
                                        </ul>
                                    </el-col>
                                    <el-col :md="12" :lg="8" class="link-section">
                                        <p class="link-header">About</p>
                                        <ul>
                                            <li><a href="/">About SPARC</a></li>
                                            <li><a href="/">About SPARC</a></li>
                                        </ul>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
                </el-col>
            </el-row>
            <el-row>
                <el-col>
                    <p>NIH Stimulating Peripheral Activity to Relieve Conditions</p>
                    <p>&copy; 2019 All Rights Reserved. <a href="https://blackfynn.com/privacy">Privacy Policy</a></p>
                </el-col>
            </el-row>
        </el-col>
    </el-col>
</template>

<script>
    import SparcHeader from "../header/Header.vue";
    import irregularBlob1 from "../../assets/images/irregular-blob-1.svg";
    import irregularBlob2 from "../../assets/images/irregular-blob-2.svg";
    import transparentBlob3 from "../../assets/images/transparent-blob-3.svg";
    import mapCore from "../../assets/images/map-core.png";
    import simulationCore from "../../assets/images/simulation-core.png";
    import dataCore from "../../assets/images/data-core.png";
    import SparcLogo from "../logo/SparcLogo.vue";
    import datasetAbstractImage from "../../assets/images/dataset-abstract-image.png"

    export default {
        name: "landing-page",
        components: {
            SparcHeader,
            SparcLogo
        },
        data: () => ({
            irregularBlob1,
            irregularBlob2,
            mapCore,
            simulationCore,
            dataCore,
            transparentBlob3,
            datasetAbstractImage,
            cores: [
                {
                    name: "Data Core",
                    description: "Powered by Blackfynn, the data portal houses and synthesizes the metadata from an array of datasets.",
                    link: "/data-core",
                    linkText: "Visit data core",
                    image: dataCore
                },
                {
                    name: "Map Core",
                    description: "Powered by Blackfynn, the data portal houses and synthesizes the metadata from an array of datasets.",
                    link: "/map-core",
                    linkText: "Visit data core",
                    image: mapCore
                },
                {
                    name: "Simulation Core",
                    description: "Powered by Blackfynn, the data portal houses and synthesizes the metadata from an array of datasets.",
                    link: "/simulation-core",
                    linkText: "Visit data core",
                    image: simulationCore
                }
            ]
        })
    }
</script>

<style lang="scss" scoped>
    * {
        font-family: 'San Francisco UI', sans-serif;
    }

    .section-header {
        margin-bottom: 1em;
    }

    .cards {

    }

    .flush-column {
        overflow: hidden;
    }

    .featured-dataset-image {
        min-height: 25em;
        background-size: cover;
        background-repeat: no-repeat;
        border-radius: .3em 0 0 .3em;
    }

    .featured-dataset-carousel-navigation {
        width: 100%;
        text-align: center;
        user-select: none;
        margin: .2em 0;

        ul {
            padding: 0;
            margin: 0;
            height: 100%;

            li {
                padding: 0;
                display: inline-block;
                margin: 0 .3em;
                min-width: 2em;
                border-bottom: 5px solid #909399;
                cursor: pointer;

                &.active {
                    border-bottom: 5px solid #24245B;
                }
            }
        }
    }

    .featured-dataset-description {
        height: 100%;
        background: #24245B;
        display: flex;
        justify-content: center;
        flex-direction: column;
        border-radius: 0 .3em .3em 0;

        .content {
            padding: 3em 1.5em;
            color: white;

            h2 {
                font-size: 1.5em;
            }

            p {

            }

            .actions {
                margin-top: 2em;

                .view-dataset {
                    background: #8300BF;
                    text-transform: uppercase;
                    border: 0;
                }
            }
        }
    }

    .core-card {
        width: 100%;

        img {
            width: 100%;
        }

        .content {
            padding: .5em;
            background: #F5F7FA;
        }
    }

    .search {
        background: #8300BF;
        color: white;
        text-align: center;

        .search-button {
            padding-top: 1em;

            .view-search-results {
                background: #24245B;
                text: #fff;
                border: 0;
            }
        }

        .controls {
            padding-top: 1em;
            min-height: 4em;

            .control {
                display: inline-block;
                height: 100%;
                width: 100%;
                font-size: 2em;

                .search-type-selector {
                    padding: .5em;
                    border: 0;
                    color: #8300BF;
                    border-radius: 0;
                    background: none;
                    -webkit-appearance: none;
                    width: 100%;
                    height: 100%;
                }

                .search-input {
                    background: none;
                    border: 0;
                    padding: .5em;
                    color: #8300BF;
                    border-radius: 0;
                    -webkit-appearance: none;
                    width: 100%;
                    height: 100%;

                    ::placeholder {
                        color: #8300BF;
                        opacity: 1;
                    }
                }
            }
        }
    }

    .texture {
        z-index: 0;
        height: 100%;
        min-height: 100%;
        position: absolute;
        width: 100%;
        user-select: none;
        overflow: hidden;

        .blobs {
            height: 100%;
            width: 100%;
            margin: 0 auto;
            display: flex;
            flex-direction: row;
            flex-wrap: nowrap;
            justify-content: space-around;
            align-items: flex-start;

            .blob {
                height: 100%;

                img {
                    height: 100%;
                }

                .blob1 {

                }

                .blob2 {
                    transform: scale(0.3);
                }
            }
        }
    }

    h1 {
        font-size: 3em;
        font-weight: normal;
        padding: 0;
        margin: 0;
    }

    h2 {
        font-size: 2em;
        font-weight: normal;
        padding: 0;
        margin: 0;
    }

    h3 {
        font-size: 1.5em;
        font-weight: normal;
        padding: 0;
        margin: 0;
    }

    .content {
        z-index: 1;
        position: relative;
    }

    .header-and-hero {
        font-family: 'Asap', sans-serif;
        position: relative;

        .content {

            .nav {
                height: 35px;
                padding: 0;
                padding-top: 2rem;
            }

            .hero {
                padding: 6em 0px;
            }
        }

    }

    .about {
        background: #24245B;
        color: #F9F2FC;
        text-align: center;
        font-family: 'Asap', sans-serif;
        font-size: 22px;
        padding: 40px 0px;
        position: relative;

        .option {
            padding: 0 .5em;

            a {
                text-decoration: none;
                color: #F9F2FC;

                &.active {
                    color: #C200FD;
                }
            }
        }

        .texture {
            position: absolute;
            z-index: 0;

            .blob1 {
                transform: scale(0.3);
            }

            .blob2 {
                transform: scale(0.5);
            }
        }
    }

    .section {
        padding: 3rem 0;
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

        color: #5D6478;
        text-transform: uppercase;

        .link-header {
            color: #000;
        }

        .footer-content {
            font-size: 10pt;
            size: 10pt;
            font-weight: bold;

            .contact {

            }

            .logo {
                height: 30px;
                margin-bottom: 4em;
            }
        }

    }

    .link-sections {
        display: flex;
        flex-wrap: wrap;
    }

    .link-section {
        padding-bottom: 5em;

        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;

            li {
                padding: .5em 0;
                margin: 0;

                a {
                    color: #606266;
                    text-decoration: none;

                    &:hover {
                        color: #909399;
                    }
                }
            }
        }
    }
</style>