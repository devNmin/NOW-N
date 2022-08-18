<template>
  <div :class="{ background }"
    class="login-padding-box">
    <form @submit.prevent="signup(credentials)"
    class="account-form">
      <h1>회원가입</h1>
      <BaseInput v-model="credentials.user_id" label="Id" er="user_id"></BaseInput>
      <BaseInput v-model="credentials.name" label="Name"></BaseInput>
      <BaseInput v-model="credentials.password" label="Password"></BaseInput>
      <BaseInput v-model="credentials.password_check" label="Password Check"></BaseInput>
      <BirthInput v-model="credentials.birth" @birth="birth" type="number"></BirthInput>
      <PhoneInput v-model="credentials.phone_number" @phone="phone" type="number"></PhoneInput>
      <EmailInput v-model="credentials.email" @email="email"></EmailInput>
      <BaseInput v-model="credentials.grade" label="Grade"></BaseInput>
      <BaseButton>회원가입</BaseButton>
    </form>
  </div>
</template>

<script>
import { reactive } from 'vue'
import BaseInput from '../common/BaseInput.vue'
import BaseButton from '../common/BaseButton.vue'
import BirthInput from '../common/BirthInput.vue'
import PhoneInput from '../common/PhoneInput.vue'
import EmailInput from '../common/EmailInput.vue'

import { useStore } from 'vuex'
export default {
  name: 'RegistUser',
  components: { BaseInput, BaseButton, BirthInput, PhoneInput, EmailInput },
  setup (props) {
    const store = useStore()
    const credentials = reactive({
      user_id: '',
      password: '',
      password_check: '',
      name: '',
      email: '',
      birth: '',
      phone_number: '',
      grade: 0
    })
    function birth (data) {
      credentials.birth = data
    }
    function phone (data) {
      credentials.phone_number = data
    }
    function email (data) {
      credentials.email = data
    }
    function signup () {
      store.dispatch('signup', credentials)
    }
    return {
      credentials,
      birth,
      phone,
      email,
      signup
    }
  }
}
</script>

<style scope>

form {
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
.new-div {
  margin: 200px;
}
</style>
