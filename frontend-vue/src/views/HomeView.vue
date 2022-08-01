<template>
  <BaseHeader></BaseHeader>
  <div class="home">
    <h1>메인 페이지</h1>
  </div>
</template>

<script>
import BaseHeader from '@/components/common/BaseHeader.vue'

export default {
  name: 'HomeView',
  components: {
    BaseHeader
  }
}
</script>

<style  scoped>
.home {
  width:100%;
  height:700px;
  align-items: center;
}
</style>
