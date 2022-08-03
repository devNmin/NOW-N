<template>
  <BaseHeader></BaseHeader>
  <FollowBar></FollowBar>
  <div class="home">
    <router-view/>
  </div>
</template>

<script>
import BaseHeader from '@/components/common/BaseHeader.vue'
import FollowBar from '@/components/common/FollowBar.vue'
export default {
  name: 'HomeView',
  components: {
    BaseHeader, FollowBar
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
