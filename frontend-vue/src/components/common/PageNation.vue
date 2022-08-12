<template>
  <div class="pn-icon-box">
    <div class="page-nation-icon" @click="pageDown"><i class="fa-solid fa-angle-left"></i></div>
    <div class="page-nation-icon">{{pageData.page}}</div>
    <div class="page-nation-icon" @click="pageUp"><i class="fa-solid fa-angle-right"></i></div>
  </div>
</template>

<script>
import { reactive } from '@vue/reactivity'
export default {
  setup (props, { emit }) {
    const pageData = reactive({
      page: 1
    })
    function pageDown () {
      if (pageData.page > 1) {
        pageData.page = pageData.page - 1
      }
      emit('changePage', pageData.page)
    }
    function pageUp () {
      pageData.page = pageData.page + 1
      emit('changePage', pageData.page)
    }
    return {
      pageDown,
      pageUp,
      pageData

    }
  }

}
</script>

<style>
.pn-icon-box {
  display: flex;

}
.page-nation-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  width: 20px;
  height: 20px;
  border: 2px solid #6dcef5;
  border-radius: 15%;
  background-color: none;
  margin: 5px;
}
</style>
