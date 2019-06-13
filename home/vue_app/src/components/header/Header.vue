<template>
    <div class="header">
        <sparc-logo/>
        Data portal
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
    }
</style>