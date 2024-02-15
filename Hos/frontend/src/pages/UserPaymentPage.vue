<template>
  <div>
      <h1 class="topic">
      How would you like to pay?
      </h1>
      <div>
        <p class="text-center">
          Please choose your payment method to pay $ {{ amount }} 
        </p>
      </div>
      <div class="link-container">
      <router-link to="UserCardPay" class="link" @click="to_bye_card(this.order)">Card</router-link>
      <button class="link" @click="to_bye_cash(this.order)">Cash</button>
      <router-link to="userHelp" class="link">Help</router-link>
      <button class="link" @click="show_order(order)">Details</button>
      <!-- Add a section to display order details -->
      <div v-if="bill.length > 0"> 
        <h2>Order Details</h2>
        <ul class="text-center">
          <li v-for="item in bill" :key="item.dish_name">
            {{ item.dish_name }} - Qty: {{ item.dish_qty }} - Price: {{ item.dish_price }}
          </li>
        </ul>
      </div>

    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data(){
    return{
      order: this.$route.params.order,
      amount:0,
      bill:[],
    };
  },
  created() {
    this.get_order_amount();
  },
  methods: {
    get_order_amount(){
      const endpoint = `http://localhost:8000/api/function/get_order_amount/?order_code=${this.order}`;
      axios.get(endpoint)
      .then((response) => {
          this.amount = response.data.order_total_amount;
        })
        .catch((error) => {
          console.error('Error fetching amount:', error);
        });
    },
    //choose to pay by cash
    to_bye_cash(order){
      this.$router.push('/userBye');
      // create payment and set payment method as card
      const endpoint = `http://localhost:8000/api/function/pay_cash/?order_code=${order}`;
      axios.get(endpoint)
      .then(() => {
          alert("pay in: Cash")
        })
        .catch((error) => {
          console.error('Error fetching amount:', error);
        });

    },
    //choose to pay by card
    to_bye_card(order){
      // create payment and set payment method as card
      const endpoint = `http://localhost:8000/api/function/pay_card/?order_code=${order}`;
      axios.get(endpoint)
      .then(() => {
          alert("pay in: Card")
        })
        .catch((error) => {
          console.error('Error fetching amount:', error);
        });
    },
    // start the checkout process
    pay_bill(order){
      const endpoint = `http://localhost:8000/api/function/pay_bill/?order_code=${order}`;
      axios.get(endpoint)
      .then((response) => {
          this.amount = response.data.order_amount;
        })
        .catch((error) => {
          console.error('Error fetching amount:', error);
        });
    },
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
  mounted() {
    this.pay_bill(this.order);
  }
}
</script>
