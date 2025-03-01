<script setup>
import { ref } from 'vue'

const emit = defineEmits(['onSubmitClick', 'onCancelClick'])

const filters = ref({ regions: [] })

function clearFilters() {
    filters.value = { regions: [] }
}

function onSubmitClick() {
    filters.value.type = 'table'
    emit('onSubmitClick', filters.value)
}
</script>

<template>

    <div class="border p-4 my-2">
        filters: {{ filters }}

        <div class="d-flex row justify-content-evenly">
            <div class="col-auto border m-1">
                <b>Название таблицы</b><br>
                <input type="text" v-model="filters.title">
            </div>

            <div class="col-auto border m-1">
                <b>Код КПГЗ</b><br>
                <input type="text" v-model="filters.kpgz_code">
            </div>

            <div class="col-auto border m-1">
                <b>Дата</b><br>
                <label style="display: inline-block; width: 60px;">Начало:</label> <input type="date" v-model="filters.dateStart"><br>
                <label style="display: inline-block; width: 60px; margin-top: 6px;">Конец:</label> <input type="date" v-model="filters.dateEnd">
            </div>

            <div class="col-auto border m-1">
                <b>Регион</b><br>
                <label><input type="checkbox" value="city1" v-model="filters.regions"> Город 1</label><br>
                <label><input type="checkbox" value="city2" v-model="filters.regions"> Город 2</label><br>
                <label><input type="checkbox" value="city3" v-model="filters.regions"> Город 3</label><br>
            </div>
        </div>
        <hr>
        <div class="d-flex row justify-content-center mt-3">
            <div class="col-auto">
                <button @click="emit('onCancelClick')">Отменить</button>
            </div>
            <div class="col-auto">
                <button @click="clearFilters">Очистить</button>
            </div>
            <div class="col-auto">
                <button @click="onSubmitClick">Создать</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>