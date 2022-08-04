<template>
  <div @change="onChange">
  <h1 class="label-box">Email</h1>
  <div style="height: 10px;"></div>
    <div class="split-page">
      <div>
          <span class="box">
              <input type="text" v-model="emailData.first" class="input-split-box2" placeholder="email">
          </span>
      </div>
      <div class="split-margin-box2"></div>
      <div>
        <span>
          <select v-model="emailData.second" class="input-split-box2 select-box-border">
            <option v-for="second_ex in emailData.second_email"
              :key="second_ex"
             :value="second_ex">{{second_ex}}</option>
          </select>
        </span>
      </div>
    </div>
    <span class="error_next_box"></span>
  </div>
</template>

<script>
import { reactive, computed } from 'vue'
export default {
  setup (props, { emit }) {
    const emailData = reactive({
      first: '',
      second: '',
      email: computed(() => emailChange()),
      second_email: ['naver.com', 'hanmail.com', 'daum.com', 'nate.com', 'gmail.com', 'google.com']
    })
    function emailChange () {
      return emailData.first + '@' + emailData.second
    }
    function onChange (event) {
      emit('update:modelValue', emailData.email)
    }

    return {
      emailData,
      onChange
    }
  }
}
</script>
<style>
.split-margin-box2 {
  width: 40px;
}
.input-split-box2 {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
  background-color: none;
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 130px;
  height: 45px;
  margin: auto;
  font-size: 20px;
  padding-left: 20px;
  padding: 0px;
}
</style>
