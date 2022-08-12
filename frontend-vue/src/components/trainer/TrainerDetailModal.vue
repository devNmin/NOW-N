<template>
  <div class="modal-background" @click="toggleModal">
    <div class="modal open">
      <div class="modal-box">
        <div class="modal-name-box">name: {{data.name}}</div>
        <div class="modal-img-box"><img style="object-fit: cover;" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ6yI5v-1UCyMx8CdTpABg9QzItPHcPLZh7_1ZnzOpTg&s" alt=""></div>
        <div @click="toggleModal" class="modal-x-button"><i class="fa-solid fa-xmark"></i></div>
        <div class="modal-follow-box">
          <div></div>
          <div>follower:{{data.followers}}</div>
          <div></div>
        </div>
        <div class="detail-deco-bar"></div>
        <div class="trainer-detail-info-box">
          <div class="split-box-info1">
            <div class="modal-info">나이: {{data.age}}</div>
            <div class="modal-info">트레이닝 비용: {{data.exercise_price}}</div>
            <div class="modal-info">코멘트: {{data.comment}}</div>
          </div>
          <div class="split-box-info2">
            <div class="modal-info">경력: {{data.career}}</div>
            <div class="modal-info">식단관리 비용: {{data.diet_price}}</div>
          </div>
        </div>
        <div class="modal-view-button">
          <div></div>
          <router-link to="/trainer/apply" class="trainer-apply-style">신청하기</router-link>
          <div></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
export default {
  setup (props, { emit }) {
    const store = useStore()
    const backgroundData = reactive({
      back: false
    })
    const data = ref(computed(() => store.getters.currentTrainer))
    function toggleModal () {
      emit('toggleModal', false)
    }
    return {
      backgroundData,
      data,
      toggleModal
    }
  }
}
</script>

<style>
.modal-background {
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0;
  background: rgba(0, 0, 0, 0.8);
}
.modal {
  min-height: 315px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  position: fixed;
  display: none;
  z-index: 200;
  top: 20%;
  left: 30%;
  width: 40%;
  height: 60%;
  background: white;
  border: 1px solid #6dcef5;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}
.modal-box {

  margin: 5%;
  width: 90%;
  height: 90%;
}
.modal-name-box {
  text-align: center;
}
.modal-img-box {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 40%;
}
.modal-follow-box {
  display: flex;
  justify-content: space-around;
}
.open {
  display: block !important;
}
.modal-x-button {
  position: absolute;
  top: 3%;
  left: 95%;
}
.detail-deco-bar {
  position: relative;
  margin: 0px 15% 0px 15%;
  width: calc(70% - 6px);
  height: 0px;
  border: 1px solid #000000;
}
.trainer-detail-info-box {
  display: flex;
  margin: 0px 15% 0px 15%;
  width: 70%;
  height: 35%;
}
.split-box-info1 {
  display: inline;
  width: 50%;
}
.split-box-info2 {
  display: inline;
  width: 50%;
}
.modal-view-button {
  display: flex;
  justify-content: space-around;
  margin: auto;
}
.modal-info {
  padding: 4%;
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
</style>
