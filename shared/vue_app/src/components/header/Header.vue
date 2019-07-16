<template>
    <div class="nav">
        <el-row type="flex" justify="center">
            <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
                <div class="header">
                    <div class="logo">
                        <sparc-logo/>
                        <!-- <span class="data-portal-title">Data Portal</span> -->
                    </div>
                    <div class="navigation">
                        <ul>
                            <li :key="link.href" v-for="link in links">
                                <a v-bind:class="{active: link.active}" :href="link.href">{{ link.title }}</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import SparcLogo from "../logo/SparcLogo.vue";

    const path = () => window.location.pathname || "";
    const hash = () => window.location.hash || "";

    const pathOrHashContainsString = (query) => (path().indexOf(query) > -1) || (hash().indexOf(query) > -1);

    const links = [
        {
            title: "Overview",
            href: "/",
            active: pathOrHashContainsString("/") && !pathOrHashContainsString("/about") && !pathOrHashContainsString("/browse") && !pathOrHashContainsString("/map")
        },
        {
            title: "About",
            href: "/#/about",
            active: pathOrHashContainsString("/about")
        },
        {
            title: "Browse Data",
            href: "/browse/#",
            active: pathOrHashContainsString("/browse")
        },
        {
            title: "Visualize Maps",
            href: "/map",
            active: pathOrHashContainsString("/map")
        },
        {
            title: "Run Simulations",
            href: "/sim/#"
        }
    ];

    export default {
        name: 'sparc-header',
        components: {
            SparcLogo
        },
        data: () => ({
            links
        })
    }
</script>

<style scoped lang="scss">
    @import '../../../../../static/css/_variables.scss';

    .nav {
        height: 3em;
        padding: 0;
        padding-top: 1rem;
    }

    .header {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-end;

        .logo {
            height: 40px;
            white-space: nowrap;
        }

        .navigation {
            padding: 0px;
            height: 100%;

            ul {
                li {
                    display: inline;
                    margin: 0px 10px;

                    a {
                        text-decoration: none;
                        color: black;
                        padding-bottom: 10px;

                        &.active {
                            border-bottom: 2px solid #8300BF;
                            color: #8300BF;
                        }

                        &:hover {
                            color: #8300BF;
                        }
                    }


                }
            }
        }
    }

    .data-portal-title {
        font-family: "SF Pro Text";
        font-size: 14px;
        color: #303133;
        line-height: 14px;
        position: relative;
        bottom: 5px;
        margin-left: 5px;
        user-select: none;
    }
</style>