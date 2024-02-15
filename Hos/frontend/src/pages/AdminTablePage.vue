<template>
    <div>
        <div class="link-container">
            <router-link to="adminMainMenu" class="link">Back to Admin Main Page</router-link>
            <router-link to="containerMenu" class="link">Change to Menu Admin</router-link>
        </div>
        <div class="col-md-8 offset-md-2 table-container">
        <table class="table table-bordered table-hover table-header">
            <thead>
            <th class="text-center sticky-header">Table</th>
            <th class="text-center sticky-header">Capacity</th>
            <th class="text-center sticky-header">Status</th>
            <th class="text-center sticky-header">Change Status</th>
            </thead>
            <tbody>
            <tr v-for='table in tables' :key='table.dish_id'>
                <td class="text-center table_name">{{table.table_name}}</td>
                <td class="text-center">{{table.table_capacity}}</td>
                <td :class="{'red-text': !table.table_status, 'green-text': table.table_status}">
                  {{ table.table_status ? 'Free' : 'Occupied' }}
                </td>
                <td class="text-center">
                <button class="btn" @click="editTable(table)">
                    <i class="fa fa-edit"></i>
                </button>
                </td>
            </tr>
            </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AdminTablePage',
  props: {
  },
  data(){
    return {
      base_url:'http://127.0.0.1:8000//api/table/',
      tables:null,
      url:'',
      table_id:'',
      table_capacity:'',
      table_status:'',
      table_name:'',
      admin: this.$route.params.admin,
    }
  },
  methods: {
    getAll(){
      axios.get(this.base_url)
      .then(response => {
        this.tables = response.data
        this.url = '',
        this.table_id = '';
        this.table_capacity = '';
        this.table_status = '';
        this.table_name = '';
      })
    },
    editTable(table){
      // edit menu when click the change status button
      //change between true and false
      axios.put(table.url,{
          table_id:table.table_id,
          table_name:table.table_name,
          table_status:!table.table_status,
          table_capacity:table.table_capacity
        })
          .then(()=>{
            this.getAll();
          })
        // window.alert('Update status of:"'+ table.table_name +'" successfully!');
    }
  },
  mounted() {
        this.getAll();
        setInterval(() => {
          this.getAll();
        }, 10000);
  }
}
</script>

<style scoped>
.table-container {
  width: 100%;
  height: 620px; /* height */
  overflow-y: scroll; /* scroll */
  border: 1px solid #ccc; /* style */
  display: flex; /* 使用 Flex 布局 */
  justify-content: center; /* 水平居中 */
  margin-top: 5px;
}

.sticky-header {
  position: -webkit-sticky;
  position: sticky;
  top: 0; /* stick the tablehead in the top */
  background-color:#E81E25; /* set colour for table head */
  color: white;
}

.table_name{
  background-color: wheat;
}

.btn {
  background-color: wheat;
  border: none;
  color: black;
  padding: 5px 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 2px 2px;
  cursor: pointer;
}
/* for the link to go back */
.link-container {
  display: flex;  /* 使用 Flex 布局 */
  justify-content: flex-start;  /* 水平向左靠齐 */
  gap: 10px;  /* 间距设置为 10px，根据需要进行调整 */
}
.link{
  font-size: 10px;
  background-color: wheat;
  margin: 0 20px;
  border-radius: 5px; /* set rounder */
  padding: 5px 10px; /* set inside padding */
}
.red-text {
  color: red;
}

.green-text {
  color: green;
}

</style>