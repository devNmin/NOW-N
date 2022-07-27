<template>
  <form @submit.prevent>
    <h1>로그인</h1>
    <BaseInput placeholder="아이디"></BaseInput>
    <BaseInput placeholder="비밀번호" type="password"></BaseInput>
    <div class="login-nav">
      <router-link to="/users/findid">아이디 찾기</router-link>|
      <router-link to="/users/findpw">비밀번호 찾기</router-link>|
      <router-link to="/users/regist">회원가입</router-link>
    </div>
    <BaseButton @click="onSubmit">로그인</BaseButton>
  </form>
</template>

<script>
import BaseButton from '../common/BaseButton.vue'
import BaseInput from '../common/BaseInput.vue'

export default {
  components: { BaseButton, BaseInput }

}
</script>

<style>

form {
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 48px;
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(4px);
}

.form-actions {
  display: flex;
  justify-content: space-between;
}

.login-nav {
    text-align: center;
      font-size: 15px;
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
