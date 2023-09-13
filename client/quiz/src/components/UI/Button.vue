<script>
    export default {
        props: {
            text: String,
            path: String,
            type: String,
        }
    }
</script>

<template>
    <router-link v-if=path :to=path>
        <button :type=type>{{ text }}</button>
    </router-link>
    <button v-else :type=type>{{ text }}</button>
</template>

<style scoped>
    button {
        border: 0;
        background-color: var(--color-header);
        color: var(--color-blue-active);
        border-radius: 8px;
        padding: calc(var(--index) * 0.5) calc(var(--index) * 0.7);
        transition: var(--transition);
        font-weight: bold;
        font-size: calc(var(--index) * 0.7);
    }

    button:hover {
        background-color: var(--color-blue);
        color: var(--color-header);
        cursor: pointer;
    }

    button:active {
        background-color: var(--color-blue-active);
        color: var(--color-header);
    }
</style>