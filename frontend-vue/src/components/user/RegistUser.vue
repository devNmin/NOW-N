<template>

    <form @submit.prevent="signup(credentials)">
      <div class='logo-div'>logo</div>
      <div class="page-name">회원가입</div>
      <div class="input-div">
        <BaseInput v-model="credentials.id" label="아이디" :placeholder="ㅁㄴㅇㄻㄴㅇㄹ아이디"></BaseInput>
        <div class="magin-box"></div>
        <BaseInput v-model="credentials.username" label="이름"></BaseInput>
      </div>
      <div class="input-div">
        <BaseInput v-model="credentials.password" label="비밀번호" password></BaseInput>
        <BaseInput v-model="credentials.birth" label="생년월일"></BaseInput>
      </div>
      <div class="input-div">
        <BaseInput v-model="credentials.password_check" label="비밀번호 확인" password></BaseInput>
        <BaseInput v-model="credentials.phone_number" label="전화번호"></BaseInput>
      </div>
      <div class="input-div">
        <BaseInput v-model="credentials.email" label="이메일"></BaseInput>
        <BaseInput v-model="credentials.is_staff" label="클래스"></BaseInput>
      </div>
      <BaseButton>회원가입</BaseButton>
    </form>

</template>

<script>
import { mapActions } from 'vuex'
import { reactive } from 'vue'
import BaseInput from '../common/BaseInput.vue'
import BaseButton from '../common/BaseButton.vue'
export default {
  name: 'RegistUser',
  components: { BaseInput, BaseButton },
  setup () {
    const credentials = reactive({
      id: '',
      password: '',
      password_check: '',
      username: '',
      email: '',
      birth: 0,
      phone_number: 0,
      is_staff: true
    })
    const signup = () => mapActions(['signup'])
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
</style>
