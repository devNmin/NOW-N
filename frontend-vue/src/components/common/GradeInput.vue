<template>
<<<<<<< HEAD
  <label for="input-box" class="label-box">{{label}}
  </label>
    <select v-model="gradeData.userCase" @change="gradechange" class="input-split-box select-box-border">
      <option v-for="userCase_ex in gradeData.userCaseData"
        :key="userCase_ex"
        :value="userCase_ex">{{userCase_ex}}</option>
    </select>
=======
  <h1 class="label-box">등급</h1>
  <!-- <label for="input-box" class="label-box">{{label}}</label> -->
  <select v-model="gradeData.userCase" @change="gradechange" class="input-box select-box-border">
    <option v-for="userCase_ex in gradeData.userCaseData"
        :key="userCase_ex"
        :value="userCase_ex">{{userCase_ex}}</option>
  </select>
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  <div class="error-box" v-if="authError">{{authError["user.password"]}}
  </div>

</template>

<script>

export default {
  setup (props, { emit }) {
    const gradeData = {
<<<<<<< HEAD
      userCase: '',
      userCaseData: ['일반유저', '트레이너']
    }
    function gradechange (event) {
      console.log(event.target.value)
=======
      userCase: '일반유저',
      userCaseData: ['일반유저', '트레이너']
    }
    function gradechange (event) {
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
