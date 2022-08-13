<template>
  <div class="px-coaching-content">
    <div class="px-coachinfo">
      코치 정보
    </div>
    <div class="px-schedule">
      스케줄
    </div>
    <div class="px-community">
      커뮤니티
    </div>
    <div class="px-consulting">
      컨설팅
    </div>
  </div>
</template>

<script>
// import { reactive, computed } from 'vue'
// import { useStore } from 'vuex'
export default {
  setup () {
    // const store = useStore()

    const trainerInfo = ''

    return { trainerInfo }
  },
  async created () {
    this.$store.dispatch('getTrainerId')
  }
}
</script>

<style scoped>
.px-coaching-content{
  display: grid;
  width:100%;
  height: 100%;
  grid-template-columns: 3fr 2fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-template-areas:
  "px-coachinfo px-schedule"
  "px-community px-schedule"
  "px-consulting px-consulting";
  gap: 10px 20px;
}

.px-coachinfo{
  background-color: blue;
  grid-area: px-coachinfo;
}

.px-schedule{
  background-color: blue;
  grid-area: px-schedule;
}

.px-community{
  background-color: blue;
  grid-area: px-community;
}

.px-consulting{
  background-color: blue;
  grid-area: px-consulting;
}
</style>
