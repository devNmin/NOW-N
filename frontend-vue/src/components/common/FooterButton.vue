<template>
  <div class="footer">
    <img src="@/assets/chatbot_normal.png"  @click="showAlert" alt="test" width="100">
  </div>
</template>

<script>
import { inject } from 'vue'

export default {
  components: {
  },
  setup () {
    const swal = inject('$swal')

    function showAlert () {
      swal({
        title: '알림',
        text: '수신된 메시지가 없습니다.',
        type: 'warning',
        timer: 1500,
        customClass: 'sweet-size',
        confirmButtonClass: 'btn-danger',
        showConfirmButton: false
      })
    }
    return { showAlert }
  }
}
</script>

<style>

</style>
