<template>
  <div class="trainer-first">
    <div class=""></div>
    <div class="around-box">

   </div>
  <div class="deco-bar"></div>
  <div class="calender-box">
  <div></div>
  <TrainerCalendar/>
  <div> 채팅룸</div>
  <div></div>
  </div>
    <form @submit.prevent="apply(credentials)" class="login-form">
      <PurposeInput @purposechange="purposechange"/>
      <ScheduleDateInput v-model="applyData.start_date"/>
      <ScheduleDateInput v-model="applyData.end_date"/>
      <input type="number" v-model="applyData.times">
      <textarea v-model="applyData.comment" cols="30" rows="10"></textarea>
      <button type="button" @click="apply">제출</button>
      <div class="deco-bar"></div>
    </form>
  </div>
</template>

<script>
import ScheduleDateInput from '@/components/trainer/scheduleDateInput.vue'
import TrainerCalendar from '@/components/trainer/TrainerCalendar.vue'
import PurposeInput from '@/components/trainer/purposeInput.vue'
import { reactive } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
export default {
  components: { ScheduleDateInput, TrainerCalendar, PurposeInput },
  setup () {
    const store = useStore()
    const userPk = store.getters.currentUser.id
    const applyData = reactive({
      coaching_id: computed(() => store.getters.currentTrainerPk),
      is_exercise: true,
      is_diet: false,
      times: 1,
      start_date: '01.01',
      end_date: '01.01',
      comment: ''
    })
    function purposechange (purposeData) {
      applyData.is_exercise = purposeData.is_exercise
      applyData.is_diet = purposeData.is_diet
    }
    function apply () {
      const coachPk = applyData.coaching_id
      console.log('asdf')
      console.log(applyData)
      store.dispatch('requestAdvice', { userPk, coachPk, applyData })
    }
    return {
      applyData,
      purposechange,
      apply
    }
  }
}
</script>

<style>
.trainer-appl {
  position: absolute;
  top: 10%;
  left: 20%;
  width: 60%;
  height: 60%;
}
.chat {
  display: flex;
  width: 30%;
}
.calender-box {
  display: flex;
  justify-content: space-around;
  width: 100%;
  height: 30%;
  margin: 0px;
}
.around-box {
  padding: 10px;
  display: flex;
  justify-content: space-between;
}
.deco-bar {
  width: 100%;
  border-bottom: 4px solid var(--trainer-decoBar-color);
}
</style>
