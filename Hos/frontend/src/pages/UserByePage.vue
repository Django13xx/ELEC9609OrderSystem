<template>
  <div>
      <h1 class="topic">
      Thank you for using our service!!
      </h1>
      <div class="link-container">
        <button @click="navigateToHosWelcome" class="link">Welcome Page</button>
      </div>
      <div class="countdown text-center">
      Redirect to Welcome Page in : {{ countdown }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      countdown: 5,
    };
  },
  methods: {
    navigateToHosWelcome() {
      this.$router.push({ path: '/' }); // route to the root path
    }
  },
  mounted() {
    const timer = setInterval(() => {
      if (this.countdown === 1) {
        clearInterval(timer);
        this.$router.push({ path: '/' });
      } else {
        this.countdown -= 1;
      }
    }, 1000);
  },
};
</script>






