<template>
  <div>
    <div class="link-container">
    <router-link to="adminMainMenu" class="link">Back to Admin Main Page</router-link>
    <router-link to="adminTable" class="link">Change to Table Admin</router-link>
    </div>
    <!-- seperate the screen into two parts -->
    <!-- left part for editing-->
    <div class="col-md-4 edit-menu-form">
      <div>
        <div class="form-group">
          <input type="hidden" v-model="dish_id">
        </div>
        <div class="form-group">
          <label for="dish_name">Name:</label>
          <textarea class="form-control narrow-input" v-model="dish_name" @input="validateDishname" placeholder="dish_Name"></textarea>
        </div>
        <div class="form-group">
          <label for="dish_name">Type:</label>
          <select class="form-control narrow-input" v-model="dish_type">
            <option value="" disabled selected>-Choose-</option>
            <option value="MainCourse">Main Course</option>
            <option value="Seafood">Seafood</option>
            <option value="Vegetarian">Vegetarian</option>
            <option value="Noodles">Noodles</option>
            <option value="Meat">Meat</option>
          </select>
        </div>
        <div class="form-group">
          <label for="dish_name">Price:</label>
          <textarea class="form-control narrow-input" v-model="dish_price" @input="validateDishprice" placeholder="dish_Price"></textarea>
        </div>
        <div class="form-group">
          <label for="dish_name">Sold:</label>
          <textarea class="form-control narrow-input" v-model="dish_qty" placeholder="dish_Qty"></textarea>
        </div>
        <div class="form-group">
          <button class="btn btn-block narrow-input" @click="saveMenu(menu)">Save</button>
        </div>
      </div>
    </div>
    <!-- right part for menu -->
    <div class="col-md-8 offset-md-4 table-container" >
      <table class="table table-bordered table-hover table-header">
        <thead>
          <th class="text-center sticky-header">Name</th>
          <th class="text-center sticky-header">Type</th>
          <th class="text-center sticky-header">Pic</th>
          <th class="text-center sticky-header">Price</th>
          <th class="text-center sticky-header">Sold</th>
          <th class="text-center sticky-header">Edit</th>
          <th class="text-center sticky-header">Delete</th>
        </thead>
        <tbody>
          <tr v-for='menu in menus' :key='menu.dish_id'>
            <td class="text-center dish_name">{{menu.dish_name}}</td>
            <td class="text-center">{{menu.dish_type}}</td>
            <td class="text_center">
              <img :src="`http://localhost:8000/api/static/images/${menu.dish_name}.jpg`" alt="Dish Image"> <!--import the image from backend-->
            </td>
            <td class="text-center">{{menu.dish_price}}</td>
            <td class="text-center">{{menu.dish_qty}}</td>
            <td class="text-center">
              <button class="btn" @click="editMenu(menu)">
                <i class="fa fa-edit"></i>
              </button>
            </td>
            <td class="text-center">
              <button class="btn" @click="delateMenu(menu)">
                <i class="fa fa-trash"></i>
              </button>
            </td>
          </tr>
        </tbody>
        </table>
      </div>
    <div>
      <br>
      <br>
      <br>
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
      admin: this.$route.params.admin,
    }
  },
  methods: {
    getAll(){
      axios.get(this.base_url)
      .then(response => {
        this.menus = response.data
        this.url = '',
        this.dish_id = '';
        this.dish_name = '';
        this.dish_type = '';
        this.dish_pic = '';
        this.dish_price = '';
        this.dish_qty = ''
      })
    },
    validateDishprice(event){
      let input = event.target.value;
      let isNumeric = /^\d+(\.\d+)?$/.test(input); // 使用正则表达式检查是否为数字

      if (!isNumeric) {
        // 如果输入不是数字，显示错误信息或进行其他操作
        console.log('Price must be a number.');
        // 可以设置一个错误状态以在页面上显示错误信息
        this.PriceValid = false;
      } else {
        // 如果是数字，进行其他操作或重置错误状态
        this.PriceValid = true;
      }
    }, 
    validateDishname(event){
      let input = event.target.value;
      let isAlphabetic = /^[a-zA-Z]+$/.test(input); // 使用正则表达式检查是否为数字

      if (!isAlphabetic) {
        // 如果输入不是数字，显示错误信息或进行其他操作
        console.log('Name must be Alphabetic.');
        // 可以设置一个错误状态以在页面上显示错误信息
        this.NameValid = false;
      } else {
        // 如果是数字，进行其他操作或重置错误状态
        this.NameValid = true;
      }
    },       
    saveMenu(){
        // Check if any of the input fields are empty
    if (
      !this.dish_name ||
      !this.dish_type ||
      !this.dish_price
    ) {
      // Show an error message or alert indicating that all fields must be filled
      alert('Please fill all the FIELDS except dish picture\nYou can leave the picture field empty for now');
      return; // Stop the function execution
    }
      // two situations: one for add and one for update
      if(this.url == ''){
        // add new menu
        if (this.dish_qty != 0){
          alert('Please set the sold number to 0');
          return;
        }
        if (this.PriceValid === false){
          alert('Price must be a number.');
          return;
        }
        if (this.NameValid === false){
          alert('Name must be Alphabetic.');
          return;
        }
        axios.post(this.base_url,{
          dish_id:this.dish_id,
          dish_name:this.dish_name,
          dish_type:this.dish_type,
          dish_price:this.dish_price
        })
          .then(()=>{
            this.getAll();
          })
        alert('Add dish:"'+ this.dish_name +'" successfully!');
      }else{
        // update existed menu
        axios.put(this.url,{
          dish_id:this.dish_id,
          dish_name:this.dish_name,
          dish_type:this.dish_type,
          dish_price:this.dish_price,
          dish_qty:this.dish_qty
        })
          .then(()=>{
            this.getAll();
          })
        alert('Update dish:"'+ this.dish_name +'" successfully!');
      }
    },
    editMenu(menu){
      // edit menu when click the save button
      this.url = menu.url;
      this.dish_id = menu.dish_id;
      this.dish_name = menu.dish_name;
      this.dish_type = menu.dish_type;
      this.dish_pic = menu.dish_pic;
      this.dish_price = menu.dish_price;
      this.dish_qty = menu.dish_qty
    },
    delateMenu(menu){
      // delete menu when click the delete button
      const deleted=menu.dish_name;
      axios.delete(menu.url)
        .then(()=>{
          this.getAll();
        })
      alert('Delete dish:"'+ deleted +'" successfully！！!');
    },
    tableAdminMode(){
      this.$router.push('/adminTable')
    }
  },
  mounted() {
    this.getAll();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* used to narrow the textarea width and the button */
.edit-menu-form {
  width: 150px;
  margin-left: 100px;
  margin-top: 20px;
}
.narrow-input {
  width: 150px; 
}
.table-container {
  width: 100%;
  margin-top: -450px;
  height: 620px; /* height */
  overflow-y: scroll; /* scroll */
  border: 1px solid #ccc; /* style */
  margin-right: 150px;  /* Reduce the left margin */

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
    width: 20px; /* let the height adapt automatically */
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
  display: flex;  /* 使用 Flex 布局 */
  justify-content: flex-start;  /* 水平向左靠齐 */
  gap: 10px;  /* 间距设置为 10px，根据需要进行调整 */
}
.link{
  font-size: 10px;
  background-color: wheat;
  margin: 0 0px;
  border-radius: 5px; /* set rounder */
  padding: 5px 10px; /* set inside padding */
}

</style>
