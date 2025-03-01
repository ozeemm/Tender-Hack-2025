<script setup>
import { ref, useTemplateRef } from 'vue'

import Chart from 'chart.js/auto';

import MetricItem from "./components/MetricItem.vue"
import TableBlock from "./components/TableBlock.vue"
import TableCreator from "./components/TableCreator.vue"

const testChart = useTemplateRef('testChart')
const innInput = useTemplateRef('innInput')
const metricsParamsCollapseButton = useTemplateRef('metricsParamsCollapseButton')

const metrics = ref([
    { metric: "Метрика", value: "10000000 млн." },
    { metric: "Метрика", value: "32.4%" },
    { metric: "Метрика", value: "250" }
])

const INN = ref("Меня забыли")
const metricsParams = ref({ "param": "param1" })

function onInnSubmit() {
    INN.value = innInput.value
}

function showChart() {
    const data = [
        { year: 2010, count: 10 },
        { year: 2011, count: 20 },
        { year: 2012, count: 15 },
        { year: 2013, count: 25 },
        { year: 2014, count: 22 },
        { year: 2015, count: 30 },
        { year: 2016, count: 28 },
    ];

    testChart.value.hidden = false

    new Chart(testChart.value, {
        type: 'bar',
        data: {
            labels: data.map(row => row.year),
            datasets: [
                {
                    label: 'Acquisitions by year',
                    data: data.map(row => row.count)
                }
            ]
        }
    })
}

const blocks = ref([])
const isBlockCreating = ref(false)
const creatingBlock = ref()

function onAddTableClick() {
    isBlockCreating.value = true
    creatingBlock.value = TableCreator
}

function onSubmitBlockCreating(params) {
    if (params.type == 'table') {
        blocks.value.push({ component: TableBlock, params: params })
    }

    onCancelBlockCreating()
}

function onBlockDeleteClick(index) {
    blocks.value.splice(index, 1)
}

function onCancelBlockCreating() {
    isBlockCreating.value = false
    creatingBlock.value = null
}

</script>

<template>
    <div class="container mt-2 mb-2" v-if="INN != null">
        <div>
            ИНН: {{ INN }}<br>
            metricsParams: {{ metricsParams }}<br>
            isBlockCreating: {{ isBlockCreating }}
        </div>

        <div class="row">
            <!-- Блоки -->
            <div class="col-10">
                <!-- Отображение блоков -->
                <div v-for="(block, index) in blocks" class="mb-2 mt-2">
                    <component :is="block.component" :params="block.params" :id="index"
                        @onDeleteClick="onBlockDeleteClick"/>
                </div>

                <!-- Отображение блока создания -->
                <div v-if="isBlockCreating">
                    <component :is="creatingBlock" 
                        @onSubmitClick="onSubmitBlockCreating"
                        @onCancelClick="onCancelBlockCreating"/>
                </div>

                <div class="border mt-2">
                    <canvas class="m-2 p-4 border" ref="testChart" hidden="true" />
                </div>

                <!--Кнопка "Добавить"-->
                <div v-if="!isBlockCreating" class="d-flex justify-content-center">
                    <div class="btn-group">
                        <button type="button" class="btn btn-success dropdown-toggle" data-bs-toggle="dropdown"aria-expanded="false">
                            Добавить
                        </button>

                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#" @click="onAddTableClick">Таблица</a></li>
                            <li><a class="dropdown-item" href="#" @click="console.log('Создай что-то ещё')">Что-то ещё</a></li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Метрики -->
            <div class="col-2 border">
                <div class="text-end" data-bs-toggle="collapse" href="#collapseMetricsParams">O</div>
                <div class="collapse border p-2" id="collapseMetricsParams" ref="metricsParamsCollapseButton">
                    <label><input type="radio" name="metricsRadioButton" value="param1" v-model="metricsParams.param">
                        Параметр 1</label>
                    <label><input type="radio" name="metricsRadioButton" value="param2" v-model="metricsParams.param">
                        Параметр 2</label>
                    <label><input type="radio" name="metricsRadioButton" value="param3" v-model="metricsParams.param">
                        Параметр 3</label>
                </div>
                <metric-item v-for="metric in metrics" :metric="metric.metric" :value="metric.value" />
            </div>
        </div>
    </div>
    <div v-else>
        <form @submit.prevent="onInnSubmit">
            ИНН: <input type="text" ref="innInput">
            <button type="submit">ОК</button>
        </form>
    </div>
</template>

<style scoped>
body {
    color: #1A1A1A;
}
</style>
