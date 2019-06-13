<template>
    <div class="contain">
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "contain"
    }
</script>

<style scoped lang="scss">
    .contain {
        padding: 0 3rem;
        height: 100%;
        margin: 0 auto;
    }
</style>

