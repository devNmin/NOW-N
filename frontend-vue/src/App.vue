<template>
  <div id="app">
    <BaseHeader></BaseHeader>
    <main class="main">
      <router-view></router-view>
    </main>
    <FooterButton></FooterButton>
  </div>
</template>

<script>
import FooterButton from '@/components/common/FooterButton.vue'
import BaseHeader from '@/components/common/BaseHeader.vue'
import { reactive } from '@vue/runtime-core'

export default {
  components: {
    BaseHeader,
    FooterButton
  },
  setup () {
    const data = reactive({
      a: 1
    })

    return {
      data
    }
  }
}
</script>
<style>
.footer {
  position: fixed;
  right: 15px;
  bottom: 25px;
}
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
