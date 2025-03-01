<script setup>
    import { ref } from 'vue'

    const emit = defineEmits(['onSubmitClick', 'onCancelClick'])
    
    const filters = ref({ regions: [] })

    function clearFilters(){
        filters.value = { regions: [] }
    }

    function onSubmitClick(){
        filters.value.type = 'table'
        emit('onSubmitClick', filters.value)
    }
</script>

<template>

    <div class="border p-4 my-2">
        filters: {{ filters }}

        <div class="mt-2">
            Название таблицы<br>
            <input type="text" v-model="filters.title">
        </div>

        <div class="mt-2">
            Код КПГЗ<br>
            <input type="text" v-model="filters.kpgz_code">
        </div>

        <div class="mt-2">
            Дата<br>
            Начало: <input type="date" v-model="filters.dateStart"><br>
            Конец: <input type="date" v-model="filters.dateEnd">
        </div>

        <div class="mt-2">
            Регион<br>
            <label><input type="checkbox" value="city1" v-model="filters.regions"> Город 1</label><br>
            <label><input type="checkbox" value="city2" v-model="filters.regions"> Город 2</label><br>
            <label><input type="checkbox" value="city3" v-model="filters.regions"> Город 3</label><br>
        </div>

        <div class="mt-2">
            <label><input type="checkbox" v-model="filters.yearMoney"> Годовой денежный оборот</label>
        </div>

        <div class="mt-2">
            <div>
                <button @click="onSubmitClick">Принять</button>
            </div>
            <div>
                <button @click="clearFilters">Очистить</button>
            </div>
            <div>
                <button @click="emit('onCancelClick')">Отменить</button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>