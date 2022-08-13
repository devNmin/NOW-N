<template>
  <router-view>
    <div :class="{ background }" class="loginbox">
      <form @submit.prevent="login(credentials)" class="login-form">
        <a href="/">
          <img src="@\assets\Logo2.png" alt="Logo.png" style="display:block; margin:auto;" width="230" height="100">
        </a>
        <BaseInput v-model="credentials.user_id" label="아이디" err="user_id"></BaseInput>
        <BaseInput type="password" v-model="credentials.password" label="비밀번호" err="password"></BaseInput>
        <BaseButton style="display:block; margin:auto;" @click="submit">로그인</BaseButton>
        <div class="login-nav">
          <router-link class="view-button" to="findId/">아이디 찾기</router-link>|
          <router-link class="view-button" to="findId/">아이디 찾기</router-link>|
          <router-link class="view-button" to="signUp/">회원가입</router-link>
        </div>
        <kakaoLogin style="display:block; margin:auto;" ></kakaoLogin>

        <GoogleLogin class="google-login"></GoogleLogin>
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
  setup (props, { emit }) {
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
.login-form {
  position: sticky;
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 48px;
  margin-top: 5px;
}
.loginbox{
  margin-top: 110px;
}
form {
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding: 48px;
  margin: auto;
  /* background-color: grey; */
  /* background-color: rgba(255, 255, 255, 0.8); */
  /* backdrop-filter: blur(4px); */
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
  border-bottom: 2px solid #EEEEEE;
  text-decoration: none;
  margin: 20px;
}
.view-button:hover {
  border: 0px;
  border-style: inset;
  border-bottom: solid 2px #6dcef5;

  border-radius: 2px;
  cursor: pointer;
}

</style>
