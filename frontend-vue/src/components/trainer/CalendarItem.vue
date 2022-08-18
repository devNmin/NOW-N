<template>
<div @click="changeMark" class="hover-pointer">
  <img v-show="data.mark == 2" class="calender-img" src="@\assets\x.png" alt="x">
  <img v-show="data.mark == 1" class="calender-img" src="@\assets\v.png" alt="v">
</div>
</template>

<script>
import { reactive } from '@vue/reactivity'

export default {
  setup () {
    const data = reactive({
      mark: 0
    })
    function changeMark () {
      console.log(data.mark)
      data.mark = data.mark + 1
      if (data.mark === 3) {
        data.mark = 0
      }
    }
    return {
      data,
      changeMark
    }
  }
}

</script>

<style scope>

.hover-pointer {
    width: 45px;
  height: 48px;
}
.hover-pointer:hover {
  cursor: pointer;
}
</style>
