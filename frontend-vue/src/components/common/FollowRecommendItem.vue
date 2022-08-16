<template>
  <router-link to="/trainer">
    <div class="follow-item-box">
      <div>
        <img class="follow-img" alt="이미지">
      </div>
        <div class="follow-item-info-box2">{{recommendData.nickname}}</div>
    </div>
  </router-link>
</template>

<script>
import { computed, ref } from '@vue/runtime-core'
export default {
  props: {
    recommendData: {
      type: Object
    }
  },
  setup (props) {
    const recommendItemData = ref(computed(() => props.recommendData)

    )
    return {
      recommendItemData
    }
  }
}
</script>

<style>
.follow-item-box {
  display: flex;
  width: 270px;
}
.follow-img {
  display: flex;
  background-size: cover;
  margin: 5px 10px 5px 10px;
  width: 50px;
  height: 50px;
  border-radius: 50%;

}
.follow-item-info-box2 {
  padding: 5px;
  margin: auto;
  height: 50px;
}
</style>
