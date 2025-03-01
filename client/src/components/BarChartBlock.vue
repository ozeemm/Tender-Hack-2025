<script setup>
    import { ref, useTemplateRef, onMounted } from 'vue'
    import Chart from 'chart.js/auto';

    const props = defineProps(['params', 'id'])
    const emit = defineEmits(['onDeleteClick'])

    const chart = useTemplateRef('chart')

    const data = ref([
        { year: 2010, count: 10 },
        { year: 2011, count: 20 },
        { year: 2012, count: 15 },
        { year: 2013, count: 25 },
        { year: 2014, count: 22 },
        { year: 2015, count: 30 },
        { year: 2016, count: 28 },
    ]);

    onMounted(() => {
        new Chart(chart.value, {
            type: 'bar',
            data: {
                labels: data.value.map(row => row.year),
                datasets: [
                    {
                        label: 'Какие-то данные',
                        data: data.value.map(row => row.count)
                    }
                ]
            }
        })
    })
    
</script>

<template>
    <div class="border p-3">
        params: {{ props.params }}

        <div class="d-flex justify-content-center">
            <h5 class="col-11 text-center mb-3">{{ props.params.title }}</h5>

            <button class="col-auto btn btn-default" @click="emit('onDeleteClick', props.id)">
                <i class="bi bi-trash3"></i>
            </button>
        </div>

        <canvas class="m-2 p-4 border" ref="chart" />
    </div>
</template>

<style scoped>

</style>