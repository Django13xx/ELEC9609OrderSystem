<template>
    <div>
        <!-- Your Vue component template here -->
        <button @click="autoDish">Auto Dish</button>
        <ul>
            <li v-for="dish in selectedDishes" :key="dish.id">{{ dish.name }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            selectedDishes: [],
        };
    },
    methods: {
        async autoDish() {
            const jsonData = {
                //create a json object to send to backend
                //The rules are in the HOS\README.md
                // e.g. number_of_people: 4, preferences: ['NoPork', 'NoVegetables'], style: 'Random Pairings'
            };

            try {
                const response = await axios.post('http://localhost:8000/api/auto_dish/', jsonData);
                this.selectedDishes = response.data.selected_dishes;
                // 处理后端返回的点菜结果
                // 更新Vue组件的数据以显示所选菜品
            } catch (error) {
                // 处理错误
                console.error(error);
            }
        },
    },
};
</script>

