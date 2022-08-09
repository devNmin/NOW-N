<template>
  <BaseHeader></BaseHeader>
  <FollowBarHide/>
  <FollowBar @hideFollow="hideFollow" v-show="data.hideFollow == true"></FollowBar>
  <div class="home home-hide">
    <router-view ></router-view>
  </div>
</template>

<script>
import FollowBarHide from '@/components/common/FollowBarHide.vue'
import BaseHeader from '@/components/common/BaseHeader.vue'
import { useStore } from 'vuex'
import FollowBar from '@/components/common/FollowBar.vue'
import { reactive, computed, watch, onMounted } from '@vue/runtime-core'
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
    watch(data, () => {
      document.querySelector('.home').classList.toggle('home-hide')
      console.log('asdf')
    })
    onMounted(() => {
      store.dispatch('trainerList', 123)
    })
    return {
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
  width: calc(100% - 300px);
  height: 870px;
  align-items: center;
}
.home-hide {
  left: 20px;
  width: calc(100% - 20px);
}
</style>
