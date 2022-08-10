<template>
  <div>
    <div id="google-signin-btn"></div>
<<<<<<< HEAD
    <button type="button" @click="signOut">로그아웃</button>
=======
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  </div>
</template>

<script>
import { onMounted } from 'vue'
export default {
  setup () {
    onMounted(() => {
      window.gapi.signin2.render('google-signin-btn', { onsuccess: onSignIn })
    })
    const onSignIn = (googleUser) => {
      const profile = googleUser.getBasicProfile()
      console.log('ID: ' + profile.getId())
      console.log('Full Name: ' + profile.getName())
      console.log('Given Name: ' + profile.getGivenName())
      console.log('Family Name: ' + profile.getFamilyName())
      console.log('Image URL: ' + profile.getImageUrl())
      console.log('Email: ' + profile.getEmail())
      const idToken = googleUser.getAuthResponse().id_token
      console.log('ID Token: ' + idToken)
    }
    const signOut = () => {
      window.gapi.auth2.getAuthInstance().disconnect()
    }
    return {
      onSignIn,
      signOut
    }
  }
}
</script>

<style>
<<<<<<< HEAD

=======
.abcRioButton {
  width: 300px !important;
  height: 45px !important;
  margin: auto;
}
.abcRioButtonContentWrapper {
  display: flex;
  height: 100%;
  width: 100%;
  align-items: center;
}
.abcRioButtonIcon {
  margin: 0px 90px 0px 7px;
}
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
</style>
