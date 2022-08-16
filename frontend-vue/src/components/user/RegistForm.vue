<template>
  <div :class="{ background }"
    class="login-padding-box">
    <form @submit.prevent="signup(credentials)" class="regist-form">
      <BaseInput v-model="credentials.name" label="이름"></BaseInput>
      <BaseInput v-model="credentials.user_id" label="아이디" er="user_id"></BaseInput>
      <BaseInput type="password" v-model="credentials.password" label="비밀번호"></BaseInput>
      <BaseInput type="password" v-model="credentials.password_check" label="비밀번호 확인"></BaseInput>
      <BirthInput v-model="credentials.birth" @birth="birth" type="number"></BirthInput>
      <PhoneInput v-model="credentials.phone_number" @phone="phone" type="number"></PhoneInput>
      <EmailInput v-model="credentials.email" @email="email"></EmailInput>
      <GradeInput v-model="credentials.grade"></GradeInput>
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
import GradeInput from '../common/GradeInput.vue'
import { useStore } from 'vuex'
export default {
  name: 'RegistUser',
  components: { BaseInput, BaseButton, BirthInput, PhoneInput, EmailInput, GradeInput },
  setup (props) {
    const store = useStore()
    const credentials = reactive({
      user_id: '',
      password: '',
      password_check: '',
      name: '',
      email: '@naver.com',
      birth: '0101',
      phone_number: '010',
      grade: '일반유저',
      nickname: 'asd'
    })
    function signup () {
      store.dispatch('signup', credentials)
    }
    return {
      credentials,
      signup
    }
  }
}
</script>

<style>
.regist-form {
  position: sticky;
  width: 400px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 48px;
  margin: auto;
  background-color: rgba(255, 255, 255, 0.8);
}

.form-actions {
  display: flex;
  justify-content: space-between;
}
.new-div {
  margin: 200px;
}
</style>
