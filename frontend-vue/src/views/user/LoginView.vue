<template>
    <div class="container">
        <div class="container-center">
            <LoginForm></LoginForm>
            <RegistUser></RegistUser>
        </div>
    </div>
</template>

<script>
import LoginForm from '@/components/user/LoginForm.vue'
import RegistUser from '@/components/user/RegistUser.vue'

export default {
  components: {
    LoginForm, RegistUser
  }
}
</script>
