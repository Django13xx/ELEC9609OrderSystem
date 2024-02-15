<template>
  <div>
    <div class="welcome-background"></div>
    <h1 class="titleWelcome">WELCOME TO THE WORLD OF HOT POT</h1>
    <div class="link-container link-position">
        <router-link to="userLogin" class="link">Welcome</router-link>
        <router-link to="admin" class="link">Admin Mode</router-link>
        <router-link to="home" class="link">Home Page</router-link>
    </div>
  </div>
</template>

<style>
.titleWelcome {
  background-color: rgba(255, 194, 195, 0.5);
  margin-top: 10%;
  font-size: 60px;
  color: wheat;
  text-align: center;
  line-height: 1.5;
  font-weight: bold;
  font-style: italic;
  position: relative; /* 将标题设为相对定位，以便调整 z-index */
  z-index: 1; /* 设置标题在前侧 */
}
.link-position{
  z-index: 0;
}

.welcome-background {
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
  filter: blur(5px); 
}

</style>
