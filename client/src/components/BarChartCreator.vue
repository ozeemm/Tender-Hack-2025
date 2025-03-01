<script setup>
import { ref } from 'vue'

const emit = defineEmits(['onSubmitClick', 'onCancelClick'])

const data = ref({})

function clearData() {
    data.value = {}
}

function onSubmitClick() {
    data.value.type = 'barchart'
    emit('onSubmitClick', data.value)
}
</script>

<template>

    <div class="border p-4 my-2">
        data: {{ data }}

        
        <div class="d-flex row justify-content-evenly">
            <div class="col-auto border m-1">
                <b>Название диаграммы</b><br>
                <input type="text" v-model="data.title">
            </div>
        </div>
        <hr>
        <div class="d-flex row justify-content-center mt-3">
            <div class="col-auto">
                <button @click="emit('onCancelClick')">Отменить</button>
            </div>
            <div class="col-auto">
                <button @click="clearData">Очистить</button>
            </div>
            <div class="col-auto">
                <button @click="onSubmitClick">Создать</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>