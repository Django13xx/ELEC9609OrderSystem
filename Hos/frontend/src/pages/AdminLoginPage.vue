<template>
    <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <form @submit.prevent="login">
          <h2 class="mb-4 center-label">ADMIN LOGIN</h2>
          <div class="mb-3">
            <label for="username" class="form-label center-label">Admin Staff Id:</label>
            <input type="text" class="form-control  small-input center-input" id="input-username" @input="validateUsername" v-model="inputUsername" required>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label center-label">Password:</label>
            <input type="password" class="form-control  small-input center-input" id="input-password" @input="validatePassword" v-model="inputPassword" required>
          </div>
          <div class="text-center link-container">
            <button type="submit" class="btn link">Login</button>
            <button @click="goToWelcome" class="btn link">Back</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      inputUsername: '',
      inputPassword: '',
    };
  },
  methods: {
    goToMainMenu() {
        this.$router.push({name: 'adminMainMenu', params: { admin: this.inputUsername }})
    },
    goToWelcome() {
        this.$router.push({name: 'hosWelcome'})
    },
    validateUsername(event){
      let input = event.target.value;
      let isNumeric = /^\d+$/.test(input); // 使用正则表达式检查是否为数字

      if (!isNumeric) {
        // 如果输入不是数字，显示错误信息或进行其他操作
        console.log('Username must be a number.');
        // 可以设置一个错误状态以在页面上显示错误信息
        this.UsernameValid = false;
      } else {
        // 如果是数字，进行其他操作或重置错误状态
        this.UsernameValid = true;
      }
    },
    validatePassword(event){
      let input = event.target.value;
      let isNumeric = /^\d+$/.test(input); // 使用正则表达式检查是否为数字

      if (!isNumeric) {
        // 如果输入不是数字，显示错误信息或进行其他操作
        console.log('Password must be a number.');
        // 可以设置一个错误状态以在页面上显示错误信息
        this.PasswordValid = false;
      } else {
        // 如果是数字，进行其他操作或重置错误状态
        this.PasswordValid = true;
      }
    },
    login(){
      if (this.UsernameValid === false) {
        // 如果用户没有选择桌子，可以显示错误信息或进行其他操作
        alert('Username must be a number.');
      } 
      else if(this.PasswordValid === false){
        alert('Password must be a number.');
      } 
      else {
        const endpoint = `http://localhost:8000/api/function/login_check/?name=${this.inputUsername}&password=${this.inputPassword}`;
        axios.get(endpoint)
        .then((response) => {
            console.log(response);
            //alert('responds data: ' + response.data)
            if(response.data === true){
                this.goToMainMenu();
            }
            else{
                this.loginStatus = 'failed';
                alert('login failed, please try again');
            }
        })
        .catch((error) => {
            console.log(error);
        });
    }
  }
}
};
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
</style>