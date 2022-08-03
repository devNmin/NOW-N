<template>
  <div>
    <div id="google-signin-btn"></div>
    <button type="button" @click="signOut">로그아웃</button>
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

</style>
