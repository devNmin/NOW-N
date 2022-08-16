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
  height: 85%;
  position: relative;
  width: 85%;
  left: 15%;
}

.GX-content{
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
  width: 85%;
  margin-top: 50px
}

</style>
