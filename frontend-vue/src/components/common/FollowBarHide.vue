<template>
  <div
  class="followbar-hide">
    <div
    class="hide-icon-position"
    @click="changeView">
      <i class="fa-solid fa-angle-right"></i>
    </div>
  </div>
</template>

<script>

import { useStore } from 'vuex'
export default {
  setup (props, { emit }) {
    const store = useStore()
    function changeView () {
      emit('hideFollow')
      store.dispatch('hide')
    }
    return {
      changeView
    }
  }
}
</script>

<style>
.followbar-hide {
  background-color: #FFFFFF;
  width: 20px ;
  height: 980px;
  position: fixed;
  margin-top: 5rem;
}
.followbar-hide:hover {
  cursor: pointer;
}
.hide-icon-position {
  top: 500px;
}
</style>
