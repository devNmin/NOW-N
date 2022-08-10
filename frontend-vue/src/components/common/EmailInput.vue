<template>
<<<<<<< HEAD
  <div @change="onChange">
  <h1 class="label-box">Email</h1>
=======
  <div>
  <h1 class="label-box">이메일</h1>
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  <div style="height: 10px;"></div>
    <div class="split-page">
      <div>
          <span class="box">
<<<<<<< HEAD
              <input type="text" v-model="emailData.first" class="input-split-box2" placeholder="email">
          </span>
      </div>
      <div class="split-margin-box2"></div>
      <div>
        <span>
          <select v-model="emailData.second" class="input-split-box2 select-box-border">
=======
              <input type="text" @change="onChange" v-model="emailData.first" class="input-split-box2" placeholder="email">
          </span>
      </div>
      <div class="split-margin-box2"> @</div>
      <div>
        <span>
          <select v-model="emailData.second" @change="onChange" class="input-split-box2 select-box-border">
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
<<<<<<< HEAD
      second: '',
=======
      second: 'naver.com',
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
      email: computed(() => emailChange()),
      second_email: ['naver.com', 'hanmail.com', 'daum.com', 'nate.com', 'gmail.com', 'google.com']
    })
    function emailChange () {
      return emailData.first + '@' + emailData.second
    }
    function onChange (event) {
<<<<<<< HEAD
=======
      console.log(emailData.email)
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
<<<<<<< HEAD
  width: 40px;
=======
  display: flex;
  width: 40px;
  justify-content: center;
  align-items : center;
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
}
.input-split-box2 {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
<<<<<<< HEAD
  background-color: none;
=======
  background-color: #EEEEEE;
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
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
