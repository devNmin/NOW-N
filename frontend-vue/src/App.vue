<template>
  <div id="app">
    <BaseHeader></BaseHeader>
    <!-- <FollowBarHide/> -->
    <FollowBar @hideFollow="hideFollow" v-show="data.hideFollow == true"></FollowBar>
    <main class="main">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
// import FollowBarHide from '@/components/common/FollowBarHide.vue'
import FollowBar from '@/components/common/FollowBar.vue'
import BaseHeader from '@/components/common/BaseHeader.vue'
import { useStore } from 'vuex'
import { reactive, computed } from '@vue/runtime-core'

export default {
  components: {
    BaseHeader,
    FollowBar
    // FollowBarHide
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
<style>

html {
  overflow-x: hidden;
  overflow-y: scroll;
}

#app {
  height: 100vh;
  font-family: 'MaruBuriOTF';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
}

.main{
  height: calc(100vh - 86px);
}
.container {
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin-top: var(--header-height);
  padding: 64px;
  box-sizing: border-box;
}

.container-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

v-application{
  font-family: 'MaruBuri';
}
</style>
