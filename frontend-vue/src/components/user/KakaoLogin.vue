<template>
  <div><img @click="kakaoLogin" src="@\assets\kakao_login_icon2.png" alt="카카오 로그인">
  </div>
</template>

<script>
export default {
  name: 'kakao-login',
  setup () {
    const kakaoLogin = () => {
      window.Kakao.Auth.login(
        {
          scope: 'profile_nickname, profile_image, account_email, gender',
          success: getProfile
        })
    }

    const getProfile = (authObj) => {
      window.Kakao.API.request({
        url: '/v2/user/me',
        success: res => {
          const kakaoAccount = res.kakao_account
          console.log(kakaoAccount)
          alert('로그인성공')
        }

      })
    }
    return {
      kakaoLogin,
      getProfile
    }
  }
}
</script>
<style>
.social-button {
  border: 0px;
  padding: 0px;
}
</style>
