<template>
    <form @submit.prevent="signup(credentials)"
    class="account-form">
      <h1>회원가입</h1>
      <BaseInput v-model="credentials.user_id" label="Id" err="user_id"></BaseInput>
      <BaseInput v-model="credentials.name" label="Name" err="name"></BaseInput>
      <BaseInput v-model="credentials.password" label="Password" err="password"></BaseInput>
      <BaseInput v-model="credentials.birth" label="Birth" type="number" err="birth"></BaseInput>
      <BaseInput v-model="credentials.password_check" label="Password Check" err="password_check"></BaseInput>
      <BaseInput v-model="credentials.phone_number" label="Phone Number" type="number"></BaseInput>
      <BaseInput v-model="credentials.email" label="Email"></BaseInput>
      <BaseInput v-model="credentials.grade" label="Grade"></BaseInput>
      <BaseButton>회원가입</BaseButton>
    </form>
</template>

<script>
import { reactive } from 'vue'
import BaseInput from '../common/BaseInput.vue'
import BaseButton from '../common/BaseButton.vue'
import { useStore } from 'vuex'
export default {
  name: 'RegistUser',
  components: { BaseInput, BaseButton },
  setup () {
    const store = useStore()
    const credentials = reactive({
      user_id: '',
      password: '',
      password_check: '',
      name: '',
      email: '',
      birth: 0,
      phone_number: 0,
      grade: 0
    })

    function signup () {
      store.dispatch('signup', credentials)
      console.log(store.getters('authError'))
    }
    return {
      credentials,
      signup
    }
  }
}
</script>

<style>
.margin-box {
  width: 10vw;
}
.new-div {
  margin: 200px;
}
</style>
