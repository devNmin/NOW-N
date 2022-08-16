<template>
  <div class="purpose-box">
    <h1 style="margin: 0px;">목표: &nbsp;</h1>
    <select v-model="purposeData.select_case" @change="purposechange" class="purpose-select">
      <option value="1">운동</option>
      <option value="2">다이어트</option>
      <option value="3">운동 + 다이어트</option>
    </select>
  </div>
    <div class="error-box" v-if="authError">{{authError["user.password"]}}</div>
</template>

<script>
import { reactive } from '@vue/reactivity'

export default {
  setup (props, { emit }) {
    const purposeData = reactive({
      is_excise: true,
      is_diet: false,
      select_case: 1
    })
    function purposechange () {
      purposeData.is_excise = false
      purposeData.is_diet = false
      if (purposeData.select_case === '1') {
        purposeData.is_excise = true
        purposeData.is_diet = false
      } else if (purposeData.select_case === '2') {
        purposeData.is_excise = false
        purposeData.is_diet = true
      } else if (purposeData.select_case === '3') {
        purposeData.is_excise = true
        purposeData.is_diet = true
      }
      emit('purposechange', purposeData)
    }
    return {
      purposeData,
      purposechange
    }
  }
}
</script>

<style>
.purpose-box {
  display: flex;
  justify-content: center;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
}
.purpose-select {border: 0px;
  background-color: none;
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 200px;
  height: 45px;
  margin: 0px;
  font-size: 20px;
  padding-left: 20px;
  padding: 0px;
  min-width: 20px;
  text-align: center;
  outline: none;
  }
</style>
