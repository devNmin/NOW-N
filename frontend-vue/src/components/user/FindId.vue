<template>
  <div class='logo-div'>logo</div>
  <div class="page-name">아이디찾기</div>
  <div class="input-div">
    <div class="input-div1">
      <BaseInput placeholder="이름"></BaseInput>
    </div>
    <!-- <input class='login-info-box' type="text" placeholder="이름"> -->
    <div></div>
  </div>
  <div class="input-div2">
    <div></div>
    <BaseInput placeholder="생년월일"></BaseInput>
    <!-- <input class='login-info-box' type="text" placeholder="생년월일"> -->
    <div></div>
  </div>
  <div class="input-div3">
    <div></div>
    <BaseInput placeholder="이메일"></BaseInput>
    <!-- <input class='login-info-box' type="text" placeholder="이메일"> -->
    <div></div>
  </div>
  <div class="searchid">
    <BaseButton>아이디찾기</BaseButton>
  </div>
  <!-- <div class="login-info-box click-div">
    아이디찾기
  </div> -->
</template>

<script>
import BaseButton from '../common/BaseButton.vue'
import BaseInput from '../common/BaseInput.vue'
export default {
  components: {
    BaseButton,
    BaseInput
  }
}
</script>

<style>
.logo-div {
  position: absolute;
  top: 100px;
  width: 160px;
  height: 80px;
  left: 45vw;
  font-size: 50px;
  text-align: center;
}
.page-name {
  position: absolute;
  top: 180px;
  width: 400px;
  height: 100px;
  left: 37vw;
  font-size: 30px;
  text-align: center;
  color: #6DCEF5;
}
.login-info-box {
  top: 100px;
  border: 1px solid #6DCEF5;
  border-radius: 15px;
  color: aliceblue;
  width: 360px;
  height: 64px;
  font-size: 32px;
  text-align: center;
}
.input-div1 {
  position: absolute;
  top : 250px;
  left: 38vw;
  justify-content: space-around;
  display: flex;
}
.input-div2 {
  position: absolute;
  top : 400px;
  left: 38vw;
  justify-content: space-around;
  display: flex;
}
.input-div3 {
  position: absolute;
  top : 550px;
  left: 38vw;
  justify-content: space-around;
  display: flex;
}
.searchid {
  position: absolute;
  top : 700px;
  left: 38vw;
  justify-content: space-around;
  display: flex;
}
.click-div {
  top: 100px;
  margin: auto;
  color: #ffffff;
  background: #6DCEF5;

}
</style>
