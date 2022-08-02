<template>
  <div>
  <h1 class="label-box">birth
  </h1>
      <div class="Birth-page">

        <div id="bir_yy">
            <span class="box">
                <input type="text" id="yy" class="input-Birth-box" maxlength="4" placeholder="년(4자)">
            </span>
        </div>
        <div class="birth-margin-box"></div>
        <div id="bir_mm">
          <span>
            <select id="mm" class="input-Birth-box select-box-border">
              <option>월</option>
              <option value="01">1</option>
              <option value="02">2</option>
              <option value="03">3</option>
              <option value="04">4</option>
              <option value="05">5</option>
              <option value="06">6</option>
              <option value="07">7</option>
              <option value="08">8</option>
              <option value="09">9</option>
              <option value="10">10</option>
              <option value="11">11</option>
              <option value="12">12</option>
            </select>
          </span>
        </div>

        <div class="birth-margin-box"></div>
        <div id="bir_dd">
          <span class="box">
            <input type="text" id="dd" class="input-Birth-box" maxlength="2" placeholder="일">
          </span>
        </div>
      </div>
    <span class="error_next_box"></span>
  </div>
</template>

<script>
export default {
}
</script>

<style>
.Birth-page {
  display: flex;
  justify-content: center;
  margin: auto;
}

.birth-margin-box {
  width: 20px;
}
.input-Birth-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
  background-color: none;
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 90px;
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
