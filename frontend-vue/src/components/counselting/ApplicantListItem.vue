<template>
    <div class="deco-bar2" v-show="hide"></div>
    <div class="trainer-list-box2" v-show="hide">
      <div class="trainer-list-deco-box"></div>
      <div class="div1-noPadding"><img class="trainer-list-img" :src="imgData" alt=""></div>
      <div class="div2 item-padding">{{nameData}}</div>
      <div class="div3 item-padding">{{exerciseData}}</div>
      <div class="div3 item-padding">{{priceData}}</div>
      <div class="div4 item-padding"><button class="trainer-apply-style" type="button" @click="toggleModal">신청</button></div>
      <div class="trainer-list-deco-box"></div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
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
    },
    trainer: {
      type: Number
    },
    hide: {
      type: Boolean
    }
  },
  setup (props, { emit }) {
    const store = useStore()
    const trainerItemData = {
      imgdata: props.imgData,
      namedata: props.nameData,
      exerciseData: props.exerciseData,
      priceData: props.priceData,
      hide: props.hide
    }
    function toggleModal () {
      store.dispatch('requestTrainerDetail', props.trainer)
      emit('toggleModal', true)
    }
    return {
      trainerItemData,
      toggleModal
    }
  }
}
</script>

<style scope>
.trainer-list-box2 {
  display: flex;
  justify-content: center;
  height: 20%;
  margin: 10px;
  width: 100%;
  font-size: 16px;
}
.div1-noPadding {
  box-sizing: border-box;
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
  box-sizing: border-box;
  width: 100px;
  height: 30px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  padding: 5px 15px;
  border: 1px solid #6dcef5;
  gap: 10px;
  border-radius: 25px;
  background-color: #FFF;
  color: #6dcef5;
  text-decoration-line: none;
  text-align: center;
}
.trainer-apply-style:hover {
  cursor: pointer;
}
.deco-bar2 {
  position: relative;
  left: 5%;
  width: 90%;
  border-bottom: 3px solid var(--trainer-decoBar-color);
}
.item-padding {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  padding: 40px 15px;
}
</style>
