<template>
  <div class="px-coaching-content">
    <div class="px-coachinfo px-info-box">
      <div class="img-title">
        <img class="info-img" src="@/assets/card.png" alt="">
        <div class="info-title">coach</div>
      </div>
      {{infoData.coach}}
    </div>

    <div class="px-community px-info-box">
      <div class="img-title">
        <img class="info-img" src="@/assets/communityIcon.png" alt="">
        <div class="info-title">history</div>
      </div>
      {{infoData.trainhistory}}
    </div>
    <div class="px-schedule px-info-box">
      <div class="img-title">
      <img class="info-img" src="@/assets/calenderIcon.png" alt="">
        <div class="info-title">schedule</div>
      </div>
      {{infoData.schedule}}
    </div>
    <div class="px-consulting px-info-box">
      <div class="img-title">
<img style="  width: 120px; height: 100px;" src="@/assets/paperIcon.png" alt="">
        <div class="info-title">counselting</div>
      </div>
      {{infoData.counselhistory}}
    </div>
  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
export default {
  setup () {
    const store = useStore()
    const getInfomations = store.dispatch('getCoachInfo', 1)
    const infoData = ref(computed(() => store.getters.infomations))
    return {
      store,
      getInfomations,
      infoData
    }
  }
}
</script>

<style scoped>
.px-coaching-content{
  display: grid;
  width: calc(100vw - 600px);
  height: 100%;
  margin-top: 60px;
  grid-template-columns: 1fr 2fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-template-areas:
  "px-coachinfo px-schedule"
  "px-community px-schedule"
  "px-consulting px-consulting";
  gap: 10px 20px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  background-color: none;
  font-size: 20px;
}
.px-coachinfo{
  border: 8px ridge #6dcef5;

}
.px-schedule{
    border: 8px ridge #6dcef5;
  grid-area: px-schedule;
}

.px-community{
    border: 8px ridge #6dcef5;
  grid-area: px-community;
}

.px-consulting{
    border: 8px ridge #6dcef5;
  grid-area: px-consulting;
}
.img-title {
  position: relative;
  display: flex;

}
.info-img {
  width: 100px;
  height: 60px;
}
.info-title {
  margin: auto;
  font-size: 30px;
}
.px-info-box {
  position: relative;
  border-radius: 15px;
  padding: 5px;
}
</style>
