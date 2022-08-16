<template>
  <router-link to="/trainer">
    <div class="follow-item-box">
      <div>
        <img class="follow-img" alt="이미지">
      </div>
        <div class="follow-item-info-box">{{followData.name}}</div>
        <div class="follow-item-info-box">팔로워 수 : {{followData.follow_count}}</div>
    </div>
  </router-link>
</template>

<script>
import { computed, ref } from '@vue/runtime-core'

export default {
  props: {
    followData: {
      type: Object
    }
  },
  setup (props) {
    const followItemData = ref(computed(() => props.followData))

    return {
      followItemData
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
.follow-item-info-box {
  padding: 5px;
  margin: 5px 5px 5px 5px;
  width: 85px;
  height: 50px;
}
</style>
