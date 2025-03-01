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
    
    const INN = ref("123")
    const metricsParams = ref({ "param": "param1" })

    function onInnSubmit(){
        INN.value = innInput.value
    }

    function showChart(){
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

    function onAddtableClick(){
        isBlockCreating.value = true
        creatingBlock.value = TableCreator
    }

    function onSubmitBlockCreating(params){
        if(params.type == 'table'){
            blocks.value.push({ component: TableBlock, params: params })
        }

        onCancelBlockCreating()
    }

    function onBlockDeleteClick(index){
        blocks.value.splice(index, 1)
    }

    function onCancelBlockCreating(){
        isBlockCreating.value = false
        creatingBlock.value = null
    }
</script>

<template>
    <div class="container mt-2 mb-2" v-if="INN != null">
        <div>
            <h5>Не забудь стартовую страничку с ИНН</h5>
            metricsParams: {{ metricsParams }}<br>
            isBlockCreating: {{ isBlockCreating }}
        </div>

        <div class="row">
            <!-- Блоки -->
            <div class="col-10">
                <!--Отображение блоков-->
                <div v-for="(block, index) in blocks">
                    <component :is="block.component" :params="block.params" :id="index" @onDeleteClick="onBlockDeleteClick"/>
                </div>
                
                <!--Отображение -->
                <div v-if="isBlockCreating">
                    <component :is="creatingBlock" @onSubmitClick="onSubmitBlockCreating" @onCancelClick="onCancelBlockCreating"/>
                </div>

                <div class="border mt-2">
                    <canvas class="m-2 p-4 border" ref="testChart" hidden="true"/>
                </div>

                <button v-if="!isBlockCreating" @click="onAddtableClick">Добавить таблицу</button>


            </div>

            <!-- Метрики -->
            <div class="col-2 border">
                <div class="text-end" data-bs-toggle="collapse" href="#collapseMetricsParams">O</div>
                <div class="collapse border p-2" id="collapseMetricsParams" ref="metricsParamsCollapseButton">
                        <label><input type="radio" name="metricsRadioButton" value="param1" v-model="metricsParams.param"> Параметр 1</label>
                        <label><input type="radio" name="metricsRadioButton" value="param2" v-model="metricsParams.param"> Параметр 2</label>
                        <label><input type="radio" name="metricsRadioButton" value="param3" v-model="metricsParams.param"> Параметр 3</label>
                </div>
                <metric-item v-for="metric in metrics" :metric="metric.metric" :value="metric.value"/>
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
    body{
        color: #1A1A1A;
    }
</style>
