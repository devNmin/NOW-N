<template>
    <form @submit.prevent="signup(credentials)"
    class="account-form">
      <h1>회원가입</h1>
      <BaseInput v-model="credentials.user_id" label="Id" er="user_id"></BaseInput>
      <BaseInput v-model="credentials.name" label="Name"></BaseInput>
      <BaseInput v-model="credentials.password" label="Password"></BaseInput>
      <BirthInput v-model="credentials.birth" @birth="birth" type="number"></BirthInput>
      <BaseInput v-model="credentials.password_check" label="Password Check"></BaseInput>
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
import BirthInput from '../common/BirthInput.vue'
import { useStore } from 'vuex'
export default {
  name: 'RegistUser',
  components: { BaseInput, BaseButton, BirthInput },
  setup (props) {
    const store = useStore()
    const credentials = reactive({
      user_id: '',
      password: '',
      password_check: '',
      name: '',
      email: '',
      birth: '',
      phone_number: 0,
      grade: 0
    })
    function birth (data) {
      credentials.birth = data
      console.log('확인' + credentials.birth)
    }

    function signup () {
      store.dispatch('signup', credentials)
    }
    return {
      credentials,
      birth,
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
