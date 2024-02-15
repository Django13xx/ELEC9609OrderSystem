<template>
  <div>
    <div>
      <h5 class="custom-menu-intro">
        LEFT: Menu View
        <br>
        RIGHT: Sopping Cart
        <br>
        <br>
        "+" to add Dish
        <br>
         "-" to delete dish
        <br>
        Place order when ready
        <br>
        <br>
        Try AI generating menu
        <br>
        Have fun with HOS!
      </h5>
    </div>
    <!-- <div><p class="people-number-style">Number of People: {{ number }}</p></div>
    <div><p class="table-number-style">Number of Table: {{ table }}</p></div>
    <div><p class="order-number-style">Number of order: {{ order }}</p></div> -->
    <div>
        <!-- 显示总价格 -->
      <p class="custom-price text-center">Total Price: <br>${{ totalCartPrice }}</p>
      <!-- seperate the screen into two parts -->
      <!-- left part for editing-->
      <div class="col-md-4 table-container-cart">
        <h2 class="table-name">Shopping Cart</h2>
        <table class="table table-bordered table-hover table-header">
          <thead>
            <th class="text-center sticky-header">Name</th>
            <th class="text-center sticky-header">Price</th>
            <th class="text-center sticky-header">Qty</th>
            <th class="text-center sticky-header">Add</th>
            <th class="text-center sticky-header">Delete</th>
          </thead>
          <tbody>
            <tr v-for='item in cart' :key='item.id'>
              <td class="text-center dish_name">{{item.name}}</td>
              <td class="text-center">{{item.price}}</td>
              <td class="text-center">{{item.qty}}</td>
              <td class="text-center">
                <button class="btn" @click="increaseQuantity(item)">
                  <i class="fa fa-plus"></i>
                </button>
              </td>
              <td class="text-center">
                <button class="btn" @click="decreaseQuantity(item)">
                  <i class="fa fa-minus"></i>
                </button>
              </td>
            </tr>
          </tbody>
          </table>
      </div>
      <!-- right part for menu -->
      <div class="col-md-6 offset-md-4 table-container-menu">
        <h2 class="table-name">Main Menu</h2>
        <table class="table table-bordered table-hover table-header">
          <thead>
            <th class="text-center sticky-header">Name</th>
            <th class="text-center sticky-header">Type</th>
            <th class="text-center sticky-header">Pic</th>
            <th class="text-center sticky-header">Price</th>
            <th class="text-center sticky-header">Edit</th>
          </thead>
          <tbody>
            <tr v-for='menu in menus' :key='menu.dish_id'>
              <td class="text-center dish_name">{{menu.dish_name}}</td>
              <td class="text-center">{{menu.dish_type}}</td>
              <td class="text_center">
                <img :src="`http://localhost:8000/api/static/images/${menu.dish_name}.jpg`" alt="Dish Image"> <!--import the image from backend-->
              </td>
              <td class="text-center">{{menu.dish_price}}</td>
              <td class="text-center">
                <button class="btn" @click="addToCart(menu)">
                  <i class="fa fa-plus"></i>
                </button>
              </td>
            </tr>
          </tbody>
          </table>
      </div>
      <div class="chat-interface">
    <div class="input-container">
      <input v-model="inputMessage" @keyup.enter="sendMessage" placeholder="Get help from AI services..." />
      <button @click="sendMessage">Send</button>
    </div>
    <div class="chat-display">
      <h7>
        HOS Chatbot (Chatgpt):
      </h7>
      <div class="message">
        {{ message }}
      </div>
    </div>
  </div>
    </div>
      <div class="link-container">
      <button class="custom_remove_all menulink link" @click="remove_all">Clear Cart</button>
      <router-link :to="{name:'orderSuccess'}" class="menuLink customRouterOrder" @click="saveAndNavigate">Place Order</router-link>
      <button v-if="showButton" @click="autoDish" class="menuLink customButton blinking-button">AI MENU</button>
      </div>
  </div>
</template>

<script>
// import router from '@/router/router';
import axios from 'axios';
export default {
  name: 'UserMenuPage',

  data() {
    return {
      base_url:'http://localhost:8000/api/menu/',
      menus:null,
      url:'',
      dish_id:'',
      dish_name:'',
      dish_type:'',
      dish_pic:'',
      dish_price:'',
      dish_qty:'',
      cart:[],
      showButton: false,
      number: this.$route.params.number,
      table: this.$route.params.table,
      order: this.$route.params.order,
      amount: 0,
      dishes: [],
      inputMessage: '',
      messages: [],
      message: ''
    };
  },
  created() {
    // 1秒后将showButton设置为true，显示按钮
    setTimeout(() => {
      this.showButton = true;
    }, 1000); // 1000毫秒 = 1秒
  },
  computed:{
    totalCartPrice() {
        // compute the total price in the shopping cart
        const totalPrice = this.cart.reduce((total, item) => total + item.qty * item.price, 0);
        return totalPrice.toFixed(2);
      },
  },
  methods: {
    saveAndNavigate(){
      for (const dish of this.cart){
        axios.post('http://localhost:8000/api/orderContent/', {
          order:this.order,
          dish_name:dish.name,
          dish_qty:dish.qty,
        })
        .then(response => {
          console.log('order content create successfully', response.data);
          //alert('order content '+ dish.name +' create successfully')
        })
        .catch(error => {
          //alert('order content '+ dish.name +' create failed')
          console.error('order content create failed', error);
          
        });
      }
      this.amount = this.totalCartPrice;
      //alert('the amount is'+this.amount)
      const endpoint = `http://localhost:8000/api/function/order_unpaid/?order_code=${this.order}&total_amount=${this.amount}`;
      axios.get(endpoint)
      .then(() =>{
        console.log('Axios Success:', endpoint);
        //alert('order create success')
      })
      .catch(error => {
        console.error('Axios Error:', error);
      });
    },
    autoDish() {
      const endpoint = `http://localhost:8000/api/function/auto_dish/?people_number=${this.number}`;
      axios.get(endpoint)
        .then((response) => {
          this.dishes = response.data;
          // delete all the dishes in the cart
          this.cart = [];
          //add the AI Menu instead
          for (const dish of this.dishes) {
            const menuInstance = this.findMenuInstance(dish);
            if (menuInstance) {
              for (let i = 0; i < dish.dish_qty; i++) {
                this.addToCart(menuInstance);
              }
            }
          }
        })
        .catch((error) => {
          console.error('Error fetching dishes:', error);
        });
    },
    findMenuInstance(dish) {
      for (const menuInstance of this.menus) {
        if (menuInstance.dish_name === dish.dish_name) {
          return menuInstance;
        }
      }
      return null; // Handle cases where the menu instance is not found
    },
    getAll(){
        axios.get(this.base_url)
        .then(response => {
          this.menus = response.data
          this.url = '';
          this.dish_id = '';
          this.dish_name = '';
          this.dish_type = '';
          this.dish_pic = '';
          this.dish_price = '';
          this.dish_qty = ''
        })
      },
      //method for adding to cart
      addToCart(menu){
      const cartItem = this.cart.find(item => item.name === menu.dish_name);
      if (cartItem) {
        cartItem.qty++;
      } else {
        const UniqueId = this.cart.length + 1;
        this.cart.push({id: UniqueId, name: menu.dish_name, price: menu.dish_price, qty: 1});
      }
      },
      //increase and decrease the quantity of the dish
      increaseQuantity(item) {
      item.qty++;
      },
      decreaseQuantity(item) {
      if (item.qty > 1) {
        item.qty--;
        } else {
            // delete from the cart
            const index = this.cart.findIndex(cartItem => cartItem.id === item.id);
            if (index !== -1) {
            this.cart.splice(index, 1);
            }
        }
      },
      remove_all(){
        this.cart = [];
      },
      sendMessage() {
      if (this.inputMessage.trim() === '') return;
      const endpoint = `http://localhost:8000/api/function/ai_services/?statement=${this.inputMessage}`;
      axios.get(endpoint)
        .then((response) => {
          if (response.data && response.data.message) {
            this.message = response.data.message;
          } else {
            alert('Invalid response data');
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      this.inputMessage = ''; // Clear the input box
    },
  },
  mounted() {
      this.getAll();
  }
}

</script>

<style scoped>
.custom-price {
    position: fixed;
    top: 255px;
    right: 525px;
    font-size: 18px;
    font-weight: bold;
    color: #E81E25;
  }
  .table-name{
    text-align: center;
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    vertical-align: middle;
    background-color: #E81E25;
    color: white;
  }
  .text-center{
    vertical-align: middle;
  }
  .narrow-input {
    width: 150px;
  }
  .table-container-cart {
    width: 100%;
    margin-top: 20px;
    height: 620px; /* height */
    overflow-y: scroll; /* scroll */
    border: 1px solid #ccc; /* style */
    margin-left: 900px;  /* Reduce the right margin */

  }
  .table-container-menu {
    width: 100%;
    margin-top: -620px;
    height: 620px; /* height */
    overflow-y: scroll; /* scroll */
    border: 1px solid #ccc; /* style */
    margin-left: 20px;
  }

  .sticky-header {
    position: -webkit-sticky;
    position: sticky;
    top: 0; /* stick the tablehead in the top */
    background-color:#E81E25; /* set colour for table head */
    color: white;
  }

  .dish_name{
    background-color: wheat;
  }

  img {
      width: 100px; /* let the height adapt automatically */
      height: auto;
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
  .custom_remove_all{
    position: fixed;
    top: 230px;
    right: 570px;
  }

  /* for the link to go back */
  .link-container {
      display: flex;
      justify-content: center;
  }
  .link{
    font-size: 10px;
    background-color: wheat;
    margin: 0 20px;
    border-radius: 5px; /* set rounder */
    padding: 5px 10px; /* set inside padding */
  }
/* custom the intruduction of the menu page */
.custom-menu-intro{
  position: fixed;
  top: 80px;
  right: 500px;
  font-size: smaller;
}
/* create the blinking */
@keyframes blink {
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
}

.blinking-button {
  animation: blink 1s 3; /* 1s for one blink and 3 times in total */
}
/* set the basic font of all the links */
.menuLink{
  font-size: 10px;
  color: black;
  font-weight: bolder;
  border: 0.5px solid black;
  background-color: wheat;
  margin: 10px 0;
  border-radius: 5px; /* set rounder */
  padding: 5px 10px; /* set inside padding */
}
/* set the format of button AI Menu */
.customButton{
  position: fixed;
  top: 220px;
  right: 490px;
}
/* set the format of the button order */
.customRouterOrder{
  position: fixed;
  top: 300px;
  right: 535px;
}
/* set the format of the button back */
.customRouterBack{
  position: fixed;
  top: 650px;
  right: 560px;
}

.chat-interface {
  position: fixed;
  bottom: 90px;
  right: 465px;
  max-width: 188px;
  font-size: small
}

.chat-display {
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
  overflow-y: auto;
  max-height: 200px;
}

.message {
  background-color: #f0f0f0;
  padding: 5px;
  margin: 5px 0;
  border-radius: 5px;
}

.input-container {
  border-radius: 5px;
}

</style>