<script setup>
import { ref, useTemplateRef } from 'vue'

import MetricItem from "./components/MetricItem.vue"
import TableBlock from "./components/TableBlock.vue"
import TableCreator from "./components/TableCreator.vue"
import BarChartBlock from "./components/BarChartBlock.vue"
import BarChartCreator from "./components/BarChartCreator.vue"

const innInput = useTemplateRef('innInput')
const metricsParamsCollapseButton = useTemplateRef('metricsParamsCollapseButton')

const metrics = ref([
    { metric: "Метрика", value: "10000000 млн." },
    { metric: "Метрика", value: "32.4%" },
    { metric: "Метрика", value: "250" }
])

const INN = ref()
const metricsParams = ref({ "period": "whole" })

function onInnSubmit() {
    INN.value = innInput.value.value
}

const blocks = ref([])
const isBlockCreating = ref(false)
const creatingBlock = ref()

function onAddTableClick() {
    isBlockCreating.value = true
    creatingBlock.value = TableCreator
}

function onAddBarChartClick(){
    isBlockCreating.value = true
    creatingBlock.value = BarChartCreator
}

function onSubmitBlockCreating(params) {
    if (params.type == 'table') {
        blocks.value.push({ component: TableBlock, params: params })
    } else if(params.type == 'barchart'){
        blocks.value.push({ component: BarChartBlock, params: params })
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
            isBlockCreating: {{ isBlockCreating }}<br>
            blocks: {{ blocks.length }}<br>
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

                <!--Кнопка "Добавить"-->
                <div v-else class="d-flex justify-content-center mt-2">
                    <div class="btn-group">
                        <button type="button" class="btn btn-success dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            Добавить
                        </button>

                        <ul class="dropdown-menu">
                            <li>
                                <a class="dropdown-item" href="#" @click="onAddTableClick">
                                    <i class="bi bi-table"></i> Таблица
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item" href="#" @click="onAddBarChartClick">
                                    <i class="bi bi-bar-chart"></i> Столбчатая диаграмма
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Метрики -->
            <div class="col-2 border">
                <div class="text-end" data-bs-toggle="collapse" href="#collapseMetricsParams">
                    <i class="bi bi-list"></i>
                </div>

                <div class="collapse border p-2" id="collapseMetricsParams" ref="metricsParamsCollapseButton">
                    <label><input type="radio" name="metricsRadioButton" value="lastMonth" v-model="metricsParams.period">
                        Последний месяц</label>
                    <label><input type="radio" name="metricsRadioButton" value="lastYear" v-model="metricsParams.period">
                        Последний год</label>
                    <label><input type="radio" name="metricsRadioButton" value="whole" v-model="metricsParams.period">
                        Весь период</label>
                </div>
                <metric-item v-for="metric in metrics" :metric="metric.metric" :value="metric.value" />
            </div>
        </div>
    </div>
    <div v-else>
        <div class="container">
            <form @submit.prevent="onInnSubmit" class="d-flex justify-content-center" style="margin-top: 25%;">
                <label>
                    <input type="text" class="form-control form-control-lg" placeholder="Введите ИНН" ref="innInput">
                </label>
                <button class="btn btn-default ms-1" type="submit">
                    <i class="bi bi-box-arrow-in-right h3"></i>
                </button>
            </form>
        </div>
    </div>
</template>

<style scoped>
body {
    color: #1A1A1A;
}

</style>
