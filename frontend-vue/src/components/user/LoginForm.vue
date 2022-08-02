<template>
  <form @submit.prevent="login(credentials)">
    <h1>로그인</h1>
    <BaseInput placeholder="아이디" v-model="credentials.user_id"></BaseInput>
    <BaseInput placeholder="비밀번호" type="password" v-model="credentials.password"></BaseInput>
    <div class="login-nav">
      <router-link to="/users/findid">아이디 찾기</router-link>|
      <router-link to="/users/findpw">비밀번호 찾기</router-link>|
      <router-link to="/users/regist">회원가입</router-link>
    </div>
    <kakaoLogin></kakaoLogin>

    <GoogleLogin class="google-login"></GoogleLogin>
    <BaseButton @click="submit">로그인</BaseButton>
  </form>
</template>

<script>
import BaseButton from '../common/BaseButton.vue'
import BaseInput from '../common/BaseInput.vue'
import kakaoLogin from '@/components/user/KakaoLogin.vue'
import GoogleLogin from '@/components/user/GoogleLogin.vue'
import { reactive } from 'vue'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  components: { BaseButton, BaseInput, kakaoLogin, GoogleLogin },

  setup () {
    const credentials = reactive({
      user_id: '',
      password: ''
    })

    const submit = () => {
      axios.post({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      }).then((res) => {
        console.log(res)
        window.alert('로그인')
      })
    }
    return {
      credentials, submit
    }
  }
}
</script>

<style>

form {
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 48px;
  background-color: grey;
  /* background-color: rgba(255, 255, 255, 0.8); */
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
