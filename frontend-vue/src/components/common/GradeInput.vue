<template>
  <h1 class="label-box">등급</h1>
  <!-- <label for="input-box" class="label-box">{{label}}</label> -->
  <select v-model="gradeData.userCase" @change="gradechange" class="input-box select-box-border">
    <option v-for="userCase_ex in gradeData.userCaseData"
        :key="userCase_ex"
        :value="userCase_ex">{{userCase_ex}}</option>
  </select>
  <div class="error-box" v-if="authError">{{authError["user.password"]}}
  </div>

</template>

<script>

export default {
  setup (props, { emit }) {
    const gradeData = {
      userCase: '일반유저',
      userCaseData: ['일반유저', '트레이너']
    }
    function gradechange (event) {
      emit('update:modelValue', event.target.value)
    }
    return {
      gradeData,
      gradechange
    }
  }
}
</script>

<style>
</style>
