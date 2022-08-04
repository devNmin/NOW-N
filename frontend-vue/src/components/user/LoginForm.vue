<template>
  <router-view>
    <div :class="{ background }"
      class="login-padding-box">
      <form @submit.prevent="login(credentials)"
      class="account-form">
        <h1>로그인</h1>
        <BaseInput v-model="credentials.user_id" label="Id" err="user_id"></BaseInput>
        <BaseInput type="password" v-model="credentials.password" label="Password" err="password"></BaseInput>
        <div class="login-nav">
          <router-link class="view-button" to="findId/">아이디 찾기</router-link>
          <router-link class="view-button" to="findId/">아이디 찾기</router-link>
          <router-link class="view-button" to="signUp/">회원가입</router-link>
        </div>
        <kakaoLogin></kakaoLogin>

        <GoogleLogin class="google-login"></GoogleLogin>
        <BaseButton @click="submit">로그인</BaseButton>
      </form>
    </div>
  </router-view>
</template>

<script>
import BaseButton from '../common/BaseButton.vue'
import BaseInput from '../common/BaseInput.vue'
import kakaoLogin from '@/components/user/KakaoLogin.vue'
import GoogleLogin from '@/components/user/GoogleLogin.vue'
import { useStore } from 'vuex'

export default {
  components: { BaseButton, BaseInput, kakaoLogin, GoogleLogin },
  setup () {
    const store = useStore()
    const credentials = {
      user_id: '',
      password: ''
    }
    function login () {
      store.dispatch('login', credentials)
    }
    function changeView (ChangeView) {
      store.commit('SET_LOGIN_VIEW_CASE', ChangeView)
    }
    return {
      credentials,
      login,
      changeView
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
    margin: 2px;
    padding: 2px;
    color: #6dcef5;
}
.view-button {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  background: none;
  color: #6dcef5;
  border: 0px;
  width: 80px;
  height: 20px;
  font-size: 7px;
  padding-left: 20px;
  padding: 0px;
  border-bottom: inset 2px ;
}
.view-button:hover {
  border: 0px;
  border-style: inset;
  border-bottom: solid 2px #6dcef5;

  border-radius: 2px;
  cursor: pointer;
}

</style>
