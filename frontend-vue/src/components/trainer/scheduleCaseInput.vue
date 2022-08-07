<template>
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
      userCase: 'G.X',
      userCaseData: ['G.X', 'T.X']
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
