<template>
    <div class="header">
        <div class="logo">
            <sparc-logo/>
            <span class="data-portal-title">Data Portal</span>
        </div>
        <div class="navigation">
            <ul>
                <li><a class="active" href="/">Overview</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/data-core">Data Core</a></li>
                <li><a href="/map-core">Map Core</a></li>
                <li><a href="/simulation-core">Simulation Core</a></li>
            </ul>
        </div>
    </div>
</template>

<script>
    import SparcLogo from "../logo/SparcLogo.vue";

    export default {
        name: 'sparc-header',
        components: {
            SparcLogo
        }
    }
</script>

<style scoped lang="scss">
    .header {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;

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