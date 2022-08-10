<template>
  <div class="deco-bar2"></div>
  <div class="trainer-list-box2">
    <div class="trainer-list-deco-box"></div>
    <div class="div1-noPadding"><img class="trainer-list-img" :src="imgData" alt=""></div>
    <div class="div2 item-padding">{{nameData}}</div>
    <div class="div3 item-padding">{{exerciseData}}</div>
    <div class="div3 item-padding">{{priceData}}</div>
    <div class="div4 item-padding"><button class="trainer-apply-style" type="button" @click="toggleModal">신청하기</button></div>
    <div class="trainer-list-deco-box"></div>
  </div>
</template>

<script>
export default {
  props: {
    imgData: {
      type: String
    },
    nameData: {
      type: String
    },
    exerciseData: {
      type: String
    },
    priceData: {
      type: String
    }
  },
  setup (props) {
    const trainerItemData = {
      imgdata: props.imgData,
      namedata: props.nameData,
      exerciseData: props.exerciseData,
      priceData: props.priceData
    }
    function toggleModal () {
      document.querySelector('.modal').classList.toggle('open')
    }
    return {
      trainerItemData,
      toggleModal
    }
  }
}
</script>

<style>
.trainer-list-box2 {
  display: flex;
  height: 20%;
  margin: 10px;
  width: 100%;
  font-size: 16px;
}
.div1-noPadding {
    width: 30%;
    margin: 0px 15px 0px 15px;
}
.trainer-list-img {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  border-radius: 30% 20%;
  object-fit: cover;
}
.trainer-apply-style {
  width: 100px;
  height: 30px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  padding: 5px 15px;
  border: none;
  gap: 10px;
  background: #35A740;
  border-radius: 25px;
}
.deco-bar2 {
  position: relative;
  left: 5%;
  width: 90%;
  border: 1px solid #EEE;
}
.item-padding {
  display: flex;
  justify-content: center;
  padding: 40px 15px;
}
</style>
