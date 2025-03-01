<script setup>
    const props = defineProps(['head_values', 'body_values'])
</script>

<template>
    <div class="table-responsive">
        <table class="table-borderless m-3">
            <thead>
                <tr>
                    <th v-for="value in props.head_values" class="p-2 text-center">{{ value }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="body in props.body_values">
                    <td v-for="value in body" class="p-3 text-center">{{ value }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
    th{
        background-color: #D4DBE6;
    }

    td{
        background-color: #E7EEF7;
        color: #8C8C8C;
        font-size: 14px;
        border-bottom: 1px solid #D4DBE6 !important;
    }
</style>