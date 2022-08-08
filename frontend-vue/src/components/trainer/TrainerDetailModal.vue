<template>
  <div class="modal">
    <div class="img-box"><img  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ6yI5v-1UCyMx8CdTpABg9QzItPHcPLZh7_1ZnzOpTg&s" alt=""></div>
    <button type="button" @click="toggleModal" class="modal-x-button"><i class="fa-solid fa-xmark"></i></button>
      <div>name</div>
    <div class="detail-deco-bar"></div>
    <div>나이:</div> <div>경력:</div>
    <router-link to="/trainer/schedule">스케쥴</router-link>
    <router-link to="/trainer/apply">신청하기</router-link>
  </div>
</template>

<script>
export default {
  setup () {
    function toggleModal () {
      document.querySelector('.modal').classList.toggle('open')
    }
    return {
      toggleModal
    }
  }
}
</script>

<style>
.modal {
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
.img-box {
  width: 100%;
  height: 40%;;
}
.open {
  display: block !important;
}
.modal-action--negative:hover,
.modal-action--negative:active {
  background: #ff5454;
  border-color: #ff5454;
}
.modal-x-button {
  position: absolute;
  top: 3%;
  left: 95%;
}
.detail-deco-bar {
  position: relative;
  left: 15%;
  width: calc(70% - 3px) !important;
  border: 3px solid #000000;
}
</style>
