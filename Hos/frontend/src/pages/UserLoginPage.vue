<template>
  <div>
    <div>
      <form id="user-login">
        <!-- phone number inputer -->
        <div class="form-group">
          <label for="InputPhoneNumber" class="center-label">Phone Number</label>
          <input type="tel" 
            class="form-control small-input center-input" 
            id="exampleInputPhoneNumber" 
            aria-describedby="phoneHelp" 
            v-model="phoneNumber" 
            @input="validatePhoneNumber">
          <small id="emailHelp" class="form-text text-muted center-label">We will never share your phone number with anyone else</small>
        </div>
        <!-- table number inputer -->
        <div class="form-group small-input center-input">
          <label for="exampleFormControlSelect1">Table number</label>
          <select class="form-control" id="exampleFormControlSelect1" v-model="table_id" @change="reserveTable">
            <option disabled value="">--Select a Table--</option>
            <option
            v-for="table of tables"
            :key="table.table_id"
            :value="table.table_name"
            :disabled="table.table_status === false"
            >{{ table.table_name }}
            </option>
          </select>
        </div>
        <!-- choose number of guest by check box -->
        <div class="form-group small-input center-input">
          <label for="exampleFormControlSelect1">Number of Guest</label>
          <select class="form-control" id="exampleFormControlSelect1" v-model="peopleNumber">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
          </select>
        </div>
      </form>
    </div>
    <div class="link-container">
      <button @click="saveAndNavigate" class="link">Start Order</button>
      <router-link to="hosWelcome" class="link">Back</router-link>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data(){
    return {
      phoneNumber: '',
      table_id: null,
      order_code: '',
      peopleNumber:'1',
      tables:[],
      reserveTable:null,
      phoneNumberValid: false,
    }
  },
  created() {
    // 获取桌子列表和状态信息，假设API返回一个包含桌子信息的数组
    axios.get("http://localhost:8000/api/table")
      .then(response => {
        this.tables = response.data;
        // for(const table of this.tables)
        // alert(`Table ${table.table_name} status: ${table.table_status}`);
      })
      .catch(error => {
        console.error("获取桌子信息时出错", error);
      });
  },
  methods: {
    validatePhoneNumber(event) {
      let phoneNumber = event.target.value.replace(/\D/g, '');
      this.phoneNumber = phoneNumber;
      // 此方法用于验证电话号码字段
      if (this.phoneNumber === '') {
        // 如果电话号码为空，可以显示错误信息或进行其他操作
        console.log('Phone number is required.');
      } else {
        // 如果电话号码有效，可以进行其他操作或重置错误状态
        this.phoneNumberValid = true;
      }
    },  
    saveAndNavigate() {
      if (this.table_id === null) {
        // 如果用户没有选择桌子，可以显示错误信息或进行其他操作
        alert('Please select a table before proceeding.');
      } 
      else if(this.phoneNumberValid === false){
        alert('Please input Phone Number before proceeding.');
      } 
      else {
        const endpoint = `http://localhost:8000/api/function/reserve_table/?table_name=${this.table_id}`;
        axios.get(endpoint)
          .then((response) => {
            this.table_status = response.data;
          })
          .catch((error) => {
            console.error('Error fetching dishes:', error);
          });
        const timestamp = new Date().getTime();
        this.order_code = this.table_id+'_'+timestamp.toString();
        axios.post('http://localhost:8000/api/order/', {
          order_code: this.order_code,
          order_table: this.table_id, 
          order_numberOfPeople: this.peopleNumber,
        })
        .catch((error) => {
            console.log(error);
        });
        this.$router.push({name: 'userMenu', params: { number: this.peopleNumber, table: this.table_id, order: this.order_code }})
        // 这里可以检查 this.phoneNumberValid 状态，如果有效才执行保存和导航操作
        if (this.phoneNumber.trim() !== '' && /^\d+$/.test(this.phoneNumber)) {
          // 执行保存操作
          axios.post('http://localhost:8000/api/user/', {
            customer_phone: this.phoneNumber,
          }).catch((error) => {
            console.log(error);
          });
          //alert('Customer "' + this.phoneNumber + '"\ncreate order: "' + this.order_code + '"\nat Table_' + this.table_id + ' successfully!');
        } else {
          // 如果电话号码无效，可以显示错误信息或进行其他操作
          console.log('Phone number is invalid.');
          // 你可以在这里设置错误提示信息或样式
        }
      }
    }
  }
}
</script>


<style>
.center-label {
  display: flex;
  justify-content: center;
  align-items: center;
}
.small-input {
  width: 150px;
}

.center-input {
  margin: 0 auto;
  display: block;
}
.centered-checkbox-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>