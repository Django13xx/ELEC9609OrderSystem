<template>
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
                <img :src="`/static/images/${menu.dish_name}.jpg`" alt="Dish Image"> <!--import the image from backend-->
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
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'ContainerMenu',
    props: {
    },
    data(){
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
        cart:[]
      }
    },
    computed: {
      totalCartPrice() {
        // compute the total price in the shopping cart
        const totalPrice = this.cart.reduce((total, item) => total + item.qty * item.price, 0);
        return totalPrice.toFixed(2);
      }
    },
    methods: {
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
      addToCart(menu) {
      const cartItem = this.cart.find(item => item.name === menu.dish_name);
      if (cartItem) {
        cartItem.qty++;
      } else {
        const UniqueId = this.cart.length + 1;
        this.cart.push({ id: UniqueId, name: menu.dish_name, price: menu.dish_price, qty: 1 });
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
      }
    },
    mounted() {
      this.getAll();
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .custom-price {
    position: fixed;
    top: 460px;
    right: 520px;
    font-size: 18px;
    font-weight: bold;
    color: #E81E25; /* 文本颜色 */
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
  
  </style>