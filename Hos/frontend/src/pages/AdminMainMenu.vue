<template>
    <div class="container mt-5  text-center">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <h2>ADMIN MODE</h2>
          <div class="mb-4">
            <h4>Total Revenue</h4>
            <p>{{ totalRevenue }}</p>
          </div>
          <div class="mb-4 link-container">
            <div class="mb-3">
              <RouterLink to= "containerMenu" class="btn link">Manage all Menus</RouterLink>
            </div>
            <div class="mb-3">
              <RouterLink to= "adminTable" class="btn link">Manage all Tables</RouterLink>
            </div>
            <div class="mb-3">
              <button @click="orderDetails" class="btn link">View historical Orders</button>
            </div>
          </div>
          <div v-if="order.length > 0"> 
            <h2>Order Details</h2>
            <ul class="text-center">
            <li v-for="item in order" :key="item.dish_name" style="list-style: none;">
                {{ item.dish_name }} - Quantity Sold: {{ item.dish_qty }}
            </li>
            </ul>
        </div>
          <div class="mb-3 link-container">
            <button @click="goBack" class="btn link">Log Out</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios';
  export default {
    data() {
      return {
        totalRevenue: 0,
        order: [],
        admin: this.$route.params.admin,
      };
    },
    methods: {
      orderDetails() {
        // 导航到订单详情页面，可以使用 Vue Router
        const endpoint = `http://localhost:8000/api/function/get_all_orders/`;
        axios.get(endpoint)
        .then((response) => {
            this.order = response.data;
            //alert(this.order);
          })
          .catch((error) => {
            console.error('Error fetching amount:', error);
          });
      },
      goBack() {
        // 返回上一级菜单，可以使用 Vue Router
        const endpoint = `http://localhost:8000/api/function/logout/`;
        axios.get(endpoint, {params: {admin: this.admin}})
        .then((response) => {
            console.log(response);
            if(response.data.success === true){
              this.$router.push({name: 'hosWelcome'});
              alert('admin '+this.admin+' logout successfully!');
            }
            else{
                alert('logout failed, please try again');
            }
        })
        .catch((error) => {
            console.log(error);
        });
      }
    },
    mounted() {
      const endpoint = `http://localhost:8000/api/function/get_total_revenue/`;
      axios.get(endpoint)
        .then((response) => {
          this.totalRevenue = response.data.totalRevenue;
            //alert(this.order);
        }).catch((error) => {
          console.error('Error fetching amount:', error);
      });
    },
  };
  </script>
  