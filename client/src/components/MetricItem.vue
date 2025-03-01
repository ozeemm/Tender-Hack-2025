<script setup>
    const props = defineProps(['metric', 'value'])
</script>

<template>
    <div class="border p-2 m-2">
        <div>{{ props.metric }}</div>
        <div>{{ props.value }}</div>
    </div>
</template>