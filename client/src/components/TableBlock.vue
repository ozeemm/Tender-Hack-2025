<script setup>
    import { ref, onBeforeMount, defineExpose } from 'vue'

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
    
    const showingColumns = ref([])
    
    function toggleAllColumns(){
        showingColumns.value = head_values.value
    }

    onBeforeMount(() => {
        toggleAllColumns()
    })

</script>

<template>
    <div class="border p-2 table-responsive position-relative">
        params: {{ props.params }}<br>

        <div class="d-flex justify-content-center">
            <h5 class="col-10 my-3 text-center">{{ props.params.title }}</h5>

            <!--Фильтры-->
            <div v-if="!isBlockCreating" class="col-auto mt-auto mb-auto">
                    <div class="btn-group">
                        <button type="button" class="btn btn-default dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            <i class="bi bi-funnel"></i>
                        </button>

                        <ul class="dropdown-menu">
                            <li v-for="value in head_values">
                                <label class="dropdown-item">
                                    <input type="checkbox" class="form-check-input" :value="value" v-model="showingColumns"> {{ value }}
                                </label>
                            </li>
                        </ul>
                    </div>
                </div>

            <button class="col-auto btn btn-default" @click="emit('onDeleteClick', props.id)">
                <i class="bi bi-trash3"></i>
            </button>
        </div>

        <table class="table-borderless m-3">
            <thead>
                <tr>
                    <th class="p-2 text-center">№</th>
                    <template v-for="value in head_values">
                        <th v-if="showingColumns.includes(value)" class="p-2 text-center">{{ value }}</th>
                    </template>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(body, index) in body_values">
                    <td class="p-3 text-center"><strong>{{ index+1 }}</strong></td>
                    <template v-for="(value, j) in body">
                        <td v-if="showingColumns.includes(head_values[j])" class="p-3 text-center">{{ value }}</td>
                    </template>
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