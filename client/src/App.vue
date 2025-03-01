<script setup>
    import { ref } from 'vue'

    import MetricItem from "./components/MetricItem.vue"
    import MyTable from "./components/MyTable.vue"

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
</script>

<template>
    <div class="container mt-2">
        <div class="row">
            <div class="col-2 border">Тут фильтры</div>
            <div class="col-8">

                <div class="border">
                    <my-table :head_values="table_data.head" :body_values="table_data.body" />
                </div>

                <div class="border mt-2">
                    Тут графики
                </div>
                
            </div>
            <div class="col-2 border">
                <metric-item v-for="metric in metrics" :metric="metric.metric" :value="metric.value"/>
            </div>
        </div>
    </div>
</template>

<style scoped>
    body{
        color: #1A1A1A;
    }
</style>
