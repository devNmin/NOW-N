<template>
  <div class='logo-div'>logo</div>
  <div class="page-name">비밀번호찾기</div>
  <div class="input-div">
    <div></div>
    <input class='login-info-box' type="text" placeholder="아이디">
    <div></div>
  </div>
  <br>
  <br>
  <br>
    <div class="input-div">
    <div></div>
    <input class='login-info-box' type="text" placeholder="이름">
    <div></div>
  </div>
  <br>
  <br>
  <br>
  <div class="input-div">
    <div></div>
    <input class='login-info-box' type="text" placeholder="생년월일">
    <div></div>
  </div>
  <br>
  <br>
  <br>
  <div class="input-div">
    <div></div>
    <input class='login-info-box' type="text" placeholder="이메일">
    <div></div>
  </div>
  <br>
  <br>
</template>

<script>
export default {

}
</script>

<style>
.logo-div {
  margin: auto;
  width: 160px;
  height: 80px;
  left: 50vw;
  font-size: 50px;
  text-align: center;
}
.page-name {
    margin: auto;
  width: 400px;
  height: 100px;
  left: 50vw;
  font-size: 50px;
  text-align: center;
}
.login-info-box {
  border: 1px solid #6DCEF5;
  border-radius: 15px;
  color: aliceblue;
  width: 360px;
  height: 64px;
  font-size: 32px;
  text-align: center;
}
.input-div {
  justify-content: space-around;
  display: flex;

}
.click-div {

  margin: auto;
  color: #ffffff;
  background: #6DCEF5;

}
</style>
