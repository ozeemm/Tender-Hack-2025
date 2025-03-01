<script setup>
    import { ref, useTemplateRef, onMounted } from 'vue'

    import Chart from 'chart.js/auto';

    import MetricItem from "./components/MetricItem.vue"
    import MyTable from "./components/MyTable.vue"

    const testChart = useTemplateRef('testChart')
    const innInput = useTemplateRef('innInput')
    const metricsParamsCollapseButton = useTemplateRef('metricsParamsCollapseButton')

    const metrics = ref([
        { metric: "Метрика", value: "10000000 млн." },
        { metric: "Метрика", value: "32.4%" },
        { metric: "Метрика", value: "250" }
    ])

    const table_data = ref({
        head: ["Код КПГЗ", "Наименование КПГЗ", "ИНН Победителя", "Начало КС", "Окончание КС"],
        body: [
            ["01.13.13.01.01", "РАСХОДНЫЕ МАТЕРИАЛЫ И КОМПЛЕКТУЮЩИЕ ДЛЯ ЛАЗЕРНЫХ ПРИНТЕРОВ И МФУ", "7721663977", "2022-12-02 09:18:07.577", "2022-12-02 15:17:08.287" ],
            ["01.13.13.01.01", "РАСХОДНЫЕ МАТЕРИАЛЫ И КОМПЛЕКТУЮЩИЕ ДЛЯ ЛАЗЕРНЫХ ПРИНТЕРОВ И МФУ", "7721663977", "2022-12-02 09:18:07.577", "2022-12-02 15:17:08.287" ]
        ]
    })
    
    const INN = ref()
    const filters = ref({})
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

    function clearFilters(){
        filters.value = {}
    }
</script>

<template>
    <div class="container mt-2 mb-2" v-if="INN != null">
        <div>
            filters: {{ filters }}<br>
            metricsParams: {{ metricsParams }}
        </div>

        <div class="row">
            <!-- Фильтры -->
            <div class="col-2 border">
                <div class="text-center mt-2">
                    <h5>Фильтры</h5>
                </div>
                <div class="mt-2">
                    Код КПГЗ<br>
                    <input type="text" v-model="filters.kpgz_code">
                </div>
                
                <div class="mt-2">
                    Дата<br>
                    Начало: <input type="date" v-model="filters.dateStart">
                    Конец: <input type="date" v-model="filters.dateEnd">
                </div>
                
                <div class="mt-2">
                    Регион<br>
                    <label><input type="checkbox"> Город 1</label><br>
                    <label><input type="checkbox"> Город 2</label><br>
                    <label><input type="checkbox"> Город 3</label><br>
                </div>

                <div class="mt-2">
                    <div>
                        <button @click="showChart">Принять</button>
                    </div>
                    <div>
                        <button @click="clearFilters">Очистить</button>
                    </div>
                </div>
            </div>

            <!-- Таблица, графики -->
            <div class="col-8">

                <div class="border">
                    <my-table :head_values="table_data.head" :body_values="table_data.body" />
                </div>

                <div class="border mt-2">
                    <canvas class="m-2 p-4 border" ref="testChart" hidden="true"/>
                </div>

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
