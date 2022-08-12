<template>
  <div v-show="data.listMode" class="trainer-list-box1">
    <div class="trainer-list-deco-box"></div>
    <div class="div1">이미지</div>
    <div class="div2">닉네임</div>
    <div class="div3">운동 종류</div>
    <div class="div3">가격</div>
    <div class="div4">신청</div>
    <div class="trainer-list-deco-box"></div>
  </div>
  <div></div>
</template>

<script>
import { reactive } from '@vue/reactivity'
import { computed } from '@vue/runtime-core'
export default {
  props: {
    listMode: {
      type: Boolean
    }
  },
  setup (props) {
    const data = reactive({
      listMode: computed(() => props.listMode)
    })
    return {
      data
    }
  }
}
</script>

<style>
.trainer-list-box1 {
  display: flex;
  justify-content: center;
  height: 10%;
  width: 100%;
  margin: 10px;
  text-align: center;
}
.trainer-list-deco-box {
  width: 5%;
}
.div1 {
  box-sizing: border-box;
  width: 30%;
  padding: 15px;
  margin: 0px 15px 0px 15px;
}
.div2 {
  box-sizing: border-box;
  width: 15%;
  padding: 15px;
}
.div3 {
  box-sizing: border-box;
  width: 15%;
  padding: 15px;
}
.div4 {
  box-sizing: border-box;
  width: 15%;
  padding: 15px;
}

</style>
