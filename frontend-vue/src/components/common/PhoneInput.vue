<template>
  <div>
  <h1 class="label-box">전화번호</h1>
  <div style="height: 10px;"></div>
    <div class="split-page">
      <div>
        <span>
          <select v-model="phoneData.first" @change="onChange" class="input-split-box select-box-border">
            <option v-for="first_ex in phoneData.first_num"
              :key="first_ex"
             :value="first_ex">{{first_ex}}</option>
          </select>
        </span>
      </div>
      <div class="split-margin-box">ㅡ</div>
      <div>
        <span class="box">
            <input type="text" @change="onChange" v-model="phoneData.second" class="input-split-box" maxlength="4">
        </span>
      </div>

      <div class="split-margin-box">ㅡ</div>
      <div>
        <span class="box">
            <input type="text" @change="onChange" v-model="phoneData.third" class="input-split-box" maxlength="4">
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
    const phoneData = reactive({
      first: '010',
      second: '',
      third: '',
      phone_number: computed(() => phoneChange()),
      first_num: ['010', '011', '0130', '016', '017', '018', '019']
    })
    function phoneChange () {
      return phoneData.first + phoneData.second + phoneData.third
    }
    function onChange (event) {
      emit('update:modelValue', phoneData.phone_number)
    }
    return {
      phoneData,
      phoneChange,
      onChange
    }
  }
}

</script>

<style>
.split-page {
  display: flex;
  justify-content: center;
  margin: auto;
}

.split-margin-box {
  display: flex;
  width: 30px;
  justify-content: center;
  align-items : center;
}
.input-split-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
  background-color: none;
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 80px;
  height: 45px;
  margin: auto;
  font-size: 20px;
  padding-left: 20px;
  padding: 0px;
}
.select-box-border {
 height: 47px;
}
</style>
