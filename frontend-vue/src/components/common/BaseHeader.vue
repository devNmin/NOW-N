<template>
  <header class="header-base">
    <!-- <img src="@/assets/logo.png" style="width:50px;height:50px"> -->
    <HeaderMenu></HeaderMenu>
  </header>
</template>

<script>
import HeaderMenu from './HeaderMenu.vue'
export default {
  components: { HeaderMenu }
}
</script>

<style>

header.header-base{
  padding: 1rem;
  height: 1rem;
  width: 100vw;
  background-color: #6DCEF5;
  justify-content: space-between;
  align-items: center;
  padding: 32px 64px;
}
</style>
