<template>
  <div class="trainer-first">
    <div class=""></div>
    <div class="around-box">

   </div>
  <div class="apply-box">
    <div class="apply-info-box">
      <img class="apply-img" src="@/assets/paper.png" alt="">
    <form @submit.prevent="apply(credentials)">
      <div class="apply-form">
      <PurposeInput @purposechange="purposechange"/>
      <div class="apply-info-box">
        <label for="exercise_value" style="font-size: 24px; padding-top: 10px;">트레이닝 횟수: &nbsp;</label>
        <input id="exercise_value" min="0" max="100" class="apply-input" type="number" v-model="applyData.times">
      </div>
      <div class=" apply-info-box">
        <div style="font-size: 24px; padding-top: 10px;">식단관리 기간</div>
      </div>
      <div class="apply-date-split apply-info-box">
        <ScheduleDateInput v-model="applyData.start_date"/>
      <div style="font-size: 24px; padding-top: 6px;">&nbsp;~&nbsp;</div>
        <ScheduleDateInput v-model="applyData.end_date"/>
      </div>

      <div class="apply-info-box">
      <textarea class="comment-box" placeholder="comment" v-model="applyData.comment" cols="30" rows="10"></textarea>
      </div>
      <div class="apply-button" type="button" @click="apply">제출</div>
      </div>
      <div class="stamp" v-show="data.toggle_submit"><img src="@/assets/stamp.png" alt=""></div>
    </form>
  </div>
  <div> 채팅룸</div>
  </div>

  </div>
</template>

<script>
import ScheduleDateInput from '@/components/trainer/scheduleDateInput.vue'
import PurposeInput from '@/components/trainer/purposeInput.vue'
import { reactive } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
export default {
  components: { ScheduleDateInput, PurposeInput },
  setup () {
    const store = useStore()
    const data = reactive({
      toggle_submit: computed(() => store.getters.applyStamp)
    })
    const applyData = reactive({
      coaching_id: computed(() => store.getters.currentTrainerPk),
      is_exercise: true,
      is_diet: false,
      times: '1',
      start_date: '01.02',
      end_date: '01.01',
      comment: ''
    })
    function purposechange (purposeData) {
      applyData.is_exercise = purposeData.is_exercise
      applyData.is_diet = purposeData.is_diet
    }
    function apply () {
      store.dispatch('requestAdvice', { applyData })
    }

    return {
      applyData,
      data,
      purposechange,
      apply
    }
  }
}
</script>

<style>
.trainer-first {
  position: absolute;
  top: 10%;
  left: 20%;
  width: 60%;
  height: 60%;
  min-width: 760px;
}
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
.apply-box {
  display: flex;
  justify-content: space-around;
  width: 100%;
  height: 30%;
  margin: 0px;
  z-index: 1;
}
.around-box {
  padding: 20px;
  display: flex;
  justify-content: space-between;
}
.apply-info-box {
  display: flex;
  margin-top: 24px;
}
.deco-bar {
  width: 100%;
  border-bottom: 4px solid var(--trainer-decoBar-color);
}
.apply-date-split {
  font-size: 16px;
  text-align: center;
  height: 47px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  position: relative;
  display: flex;
  justify-content: center;
}
.apply-img {
  position: absolute;
  z-index: -1;
}
.apply-form {
  left: 100px;
  position: relative;
  top: 20%;
}
.apply-input {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  text-align: center;
  color: black;
  border: 0px;
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 80px;
  height: 45px;
  margin: none;
  font-size: 20px;
  outline: none;
}
.comment-box {
  width: 100%;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border: solid 2px #6dcef5;
  resize: none;
}
.apply-button {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: #6dcef5;
}
.stamp {
  position: absolute;
   left: 35%;
  z-index: 1;
}
</style>
