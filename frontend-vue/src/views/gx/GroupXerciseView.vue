<template>
  <FollowBar></FollowBar>
  <div class="GX-container">
      <div class="GX-content">
        <router-view></router-view>
      </div>
  </div>
</template>
<script>

import FollowBar from '@/components/common/FollowBar.vue'
export default {
  components: {
    FollowBar
  },

  setup () {
    return { }
  }
}
</script>
<style scoped>

.GX-container{
  height: 100%;
  width: calc(100%-290px);
  margin-left: 290px;
}

.GX-content{
  height: 100%;
  width: 100%;
}

</style>
