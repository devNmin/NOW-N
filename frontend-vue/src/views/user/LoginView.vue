<template>
  <LoginForm/>
</template>

<script>
import LoginForm from '@/components/user/LoginForm'
export default {
  components: { LoginForm }
}
</script>
<style>

.login-padding-box {
  min-height: calc(100vh - var(--footer-height));
  justify-content: center;
  background: #198d4d;
}
div.background {
  background-size: cover;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin-top: var(--header-height);
  padding: 64px;
  box-sizing: border-box;
}

.container-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

v-application{
  font-family: 'MaruBuri';
}

.account-form {
  position: sticky;
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 48px;
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(4px);
  margin: auto;
}

.form-actions {
  display: flex;
  justify-content: space-between;
}

.login-info-box {
  border: 1px solid #6DCEF5;
  border-radius: 15px;
  color: aliceblue;
  width: 360px;
  height: 64px;
  font-size: 32px;
  text-align: center;
  box-shadow: 5px 5px;
}
.input-div {
  justify-content: space-around;
  display: flex;
}
.click-div {
  margin: auto;
  color: #ffffff;
  background: #6DCEF5;
}
</style>
