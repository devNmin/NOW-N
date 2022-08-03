<template>
  <div class="box">
    <BaseHeader></BaseHeader>
    <GroupXercise></GroupXercise>
  </div>
</template>
<script>
import GroupXercise from '@/components/GroupXercise/GroupXercise.vue'
import BaseHeader from '@/components/common/BaseHeader.vue'
export default {
    components: {
      BaseHeader,
      GroupXercise
    }
}
</script>
<style scoped>
.box{
  height: 1500px;
}
</style>
