<template>
  <BaseHeader></BaseHeader>
  <FollowBarHide/>
  <FollowBar @hideFollow="hideFollow" v-show="data.hideFollow == true"></FollowBar>
  <div class="home">
    <router-view ></router-view>
  </div>
</template>

<script>
import FollowBarHide from '@/components/common/FollowBarHide.vue'
import BaseHeader from '@/components/common/BaseHeader.vue'
import { useStore } from 'vuex'
import FollowBar from '@/components/common/FollowBar.vue'
import { reactive, computed } from '@vue/runtime-core'
export default {
  name: 'HomeView',
  components: {
    BaseHeader, FollowBar, FollowBarHide
  },
  setup () {
    const store = useStore()
    const data = reactive({
      a: 1,
      hideFollow: computed(() => store.getters.hideFollow)
    })
    function hideFollow () {
      console.log('메렁' + data.hideFollow)
    }
    return {
      hideFollow,
      data
    }
  }
}
</script>

<style  scoped>
.home {
  position: relative;
  left: 300px;
  top: 80px;
  width:100%;
  height:1500px;
  align-items: center;
}
</style>
