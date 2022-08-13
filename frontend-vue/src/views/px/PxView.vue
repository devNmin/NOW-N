<template>
  <FollowBar></FollowBar>
  <div class="PX-container">
    <div class="PX-grid">
      <div class="PX-menu"></div>
      <div class="PX-content">
        <router-view></router-view>
      </div>
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
.PX-menu{
  display: flex;
  align-items: center;
  margin: 20px 20px 20px 0px;
  gap: 50px;
}
.PX-grid{
  display: grid;
  width:100vw;
  height:100%;
  grid-template-rows: 1fr 7fr;
  position: relative;
  left: 150px;
  top: 15px;
}
.PX-content{
  height: 100%;
  width: 70%;
}

.PX-container{
  height: 85%;
  position: relative;
  width: 85%;
  left: 15%;
}

</style>>
