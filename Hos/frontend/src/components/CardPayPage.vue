<template>
  <div class="user-payment">
    <h1 class="text-center">Pay by card</h1>
    <h4 class="text-center">
          Total amount:{{ amount }}
    </h4>
    <form @submit.prevent="processPayment">
      <!-- 支付信息表单（添加监听） -->
      <div class="form-group">
        <label for="cardHolder">Holder Name:</label>
        <input type="text" id="Holder Name" v-model="holderName" @input="validateHolderName"  placeholder="holder name" required>
      </div>
      <div class="form-group">
        <label for="cardNumber">Card Number:</label>
        <input type="text" id="cardNumber" v-model="cardNumber" @input="validateCardNumber" placeholder="Card Number" required>
      </div>
      <div class="form-group">
        <label for="expiryDate">Expire Date:</label>
        <input type="text" id="expiryDate" v-model="expiryDate" @input="validateExpiryDate" placeholder="Expire Date (MM/YY)" required>
      </div>
      <div class="form-group">
        <label for="cvv">CVV:</label>
        <input type="text" id="cvv" v-model="cvv" @input="validateCVV" placeholder="CVV" required>
      </div>
      <div class="link-container">
        <router-link to="UserCardPay" class="link" @click="processPayment">Pay</router-link>
        </div>
    </form>

    <!-- 支付结果提示 -->
    <div v-if="paymentStatus" class="payment-status">
      {{ paymentStatus }}
    </div>
  </div>
</template>

//for the payment processing

<script>
import axios from 'axios';
export default {
  data() {
    return {
      // available data
      order: this.$route.params.order,
      amount: 0,
      holderName: '',
      cardNumber: '',
      expiryDate: '',
      cvv: '',
      paymentStatus: '', // use this to show the payment result
    };
  },
  created() {
    this.get_order_amount();
  },
  watch: {
    paymentStatus(newStatus) {
      if (newStatus === 'Payment Successful!') {
        setTimeout(() => {
          this.$router.push('/userBye');
        }, 1500);
      }
    },
  },
  methods: {
    get_order_amount() {
      const endpoint = `http://localhost:8000/api/function/get_order_amount/?order_code=${this.order}`;
      axios.get(endpoint)
        .then((response) => {
          this.amount = response.data.order_amount;
        })
        .catch((error) => {
          console.error('Error fetching amount:', error);
        });
    },
    validateHolderName() {
      const regex = /^[a-zA-Z]*$/; // 正则表达式，匹配字母
      if (!regex.test(this.holderName)) {
        this.holderName = this.holderName.substring(0, this.holderName.length - 1); // 删除最后一个字符
      }
    },
    validateCardNumber() {
      const regex = /^[0-9]*$/; // 正则表达式，匹配数字
      if (!regex.test(this.cardNumber)) {
        this.cardNumber = this.cardNumber.substring(0, this.cardNumber.length - 1); // 删除最后一个字符
      }
    },
    validateCVV() {
      const regex = /^[0-9]*$/; // 正则表达式，匹配数字
      if (!regex.test(this.cvv)) {
        this.cvv = this.cvv.substring(0, this.cvv.length - 1); // 删除最后一个字符
      }
    },
    validateExpiryDate() {
      const regex = /^[0-9/]*$/; // 正则表达式，匹配数字和斜杠
      if (!regex.test(this.expiryDate)) {
        this.expiryDate = this.expiryDate.substring(0, this.expiryDate.length - 1); // 删除最后一个字符
      }
    },
    processPayment() {
      // 在这里可以添加具有处理支付的逻辑，通过调用另一个方法或直接编写逻辑。
      this.submitCardPay();  // 现在这里调用了submitCardPay
    },
    submitCardPay() {
      // 使用查询参数构建完整的URL
      const urlWithParams = `http://localhost:8000/api/function/card_check/?name=${this.holderName}&number=${this.cardNumber}&date=${this.expiryDate}&cvv=${this.cvv}`;
      // 发送GET请求到构建的URL
      axios.get(urlWithParams)
        .then(response => {
          // 处理响应，例如更新支付状态
          if (response.data) {
            this.paymentStatus = 'Payment Successful!';
          } else {
            this.paymentStatus = 'Payment Failed! Please try again.';
          }
        })
        .catch(error => {
          console.error('Error during payment submission:', error);
          this.paymentStatus = 'Payment Failed due to an unexpected error.';
        });
    },
  },
};
</script>



<style scoped>
/* 样式可以根据你的需求进行自定义 */
.user-payment {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 8px;
}

button {
  background-color: #007BFF;
  color: #fff;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
}

.payment-status {
  margin-top: 20px;
  padding: 10px;
  background-color: #dff0d8;
  border: 1px solid #c3e6cb;
  color: #155724;
  text-align: center;
}
</style>
