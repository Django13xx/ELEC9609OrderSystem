<template>
  <div>
      <h1 class="topic">
      Order Success !!
      </h1>
      <div><p class="text-center">Order {{ order }} created!</p></div>
      <div></div>
      <div class="link-container">
        <div>
          <table class="table table-bordered table-hover table-header">
        <thead>
          <th class="text-center sticky-header">Dish Name</th>
          <th class="text-center sticky-header">Dish Quantity</th>
          <th class="text-center sticky-header">Total Price</th>

        </thead>
        <tbody>
          <tr v-for='item in bill' :key='item.dish_name'>
            <td class="text-center dish_name">{{item.dish_name}}</td>
            <td class="text-center">{{item.dish_qty}}</td>
            <td class="text-center">{{item.dish_price}}</td>
          </tr>
        </tbody>
        </table>
        </div>
      <router-link to="userPayment" class="link">Check Out</router-link>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      order: this.$route.params.order,
      bill: [],
    }
  },
  methods:{
    show_order(order){
      const endpoint = `http://localhost:8000/api/function/show_bill/?order_code=${order}`;
      axios.get(endpoint)
      .then((response) => {
          this.bill = response.data;
          //alert(this.bill);
        })
        .catch((error) => {
          console.error('Error fetching amount:', error);
        });
    }
  },
  computed: {
    amount() {
      return this.$route.params.amount;
    }
  },
  mounted(){
    setTimeout(() => {
      this.show_order(this.order);
    }, 1000);
      //alert("Bill: dish_name"+this.bill.dish_name+"dish_qty"+this.bill.dish_qty+"dish_price"+this.bill.dish_price);
  }
}
</script>
