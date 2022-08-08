<template>
  <div class="trainer-list-box">
    <div class="div1"><img :src="imgData" alt=""></div>
    <div class="div2">{{nameData}}</div>
    <div class="div3">{{exerciseData}}</div>
    <div class="div3">{{priceData}}</div>
    <div class="div3"><button type="button" @click="toggleModal">버튼</button></div>
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
.trainer-list-box {
  display: flex;
  height: 50px;
  margin: 10px;
  border-bottom: 2px solid #EEE;
}
.div1 {
  width: 70px;
}
.div2 {
  width: 150px;
}
.div3 {
  width: 300px;
}

</style>
