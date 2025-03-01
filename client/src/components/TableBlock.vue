<script setup>
    import { ref } from 'vue'

    const props = defineProps(['params', 'id'])
    const emit = defineEmits(['onDeleteClick'])

    const table_example = {
        head: ["Код КПГЗ", "Наименование КПГЗ", "ИНН Победителя", "Начало КС", "Окончание КС"],
        body: [
            ["01.13.13.01.01", "РАСХОДНЫЕ МАТЕРИАЛЫ И КОМПЛЕКТУЮЩИЕ ДЛЯ ЛАЗЕРНЫХ ПРИНТЕРОВ И МФУ", "7721663977", "2022-12-02 09:18:07.577", "2022-12-02 15:17:08.287" ],
            ["01.13.13.01.01", "РАСХОДНЫЕ МАТЕРИАЛЫ И КОМПЛЕКТУЮЩИЕ ДЛЯ ЛАЗЕРНЫХ ПРИНТЕРОВ И МФУ", "7721663977", "2022-12-02 09:18:07.577", "2022-12-02 15:17:08.287" ]
        ]
    }

    const head_values = ref(table_example.head)
    const body_values = ref(table_example.body)
</script>

<template>
    <div class="border p-2 table-responsive position-relative">
        {{ props.params }}
        <h5 class="my-3 text-center">{{ props.params.title }}</h5>

        <button class="position-absolute top-0 end-0 m-2" @click="emit('onDeleteClick', props.id)">del</button>

        <table class="table-borderless m-3">
            <thead>
                <tr>
                    <th class="p-2 text-center">№</th>
                    <th v-for="value in head_values" class="p-2 text-center">{{ value }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(body, index) in body_values">
                    <td class="p-3 text-center"><strong>{{ index+1 }}</strong></td>
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