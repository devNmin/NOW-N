<template>
    <div class="deco-bar2" v-show="hide"></div>
    <div class="trainer-list-box2" v-show="hide">
      <div class="trainer-list-deco-box"></div>
      <div class="div1-noPadding"><img class="trainer-list-img" :src="imgData" alt=""></div>
      <div class="div2 item-padding">{{clientItemData.name}}</div>
      <div class="div3 item-padding">{{clientItemData.gender}}</div>
      <div class="div3 item-padding">{{clientItemData.height}} / {{clientItemData.user_weight}}</div>
      <div class="div4 item-padding"><button class="trainer-apply-style3" type="button" @click="toggleModal">상담 내역</button></div>
      <div class="trainer-list-deco-box"></div>
    </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
export default {
  props: {
    clientListData: {
      type: Object
    },
    hide: {
      type: Boolean
    }
  },
  setup (props, { emit }) {
    const store = useStore()
    const clientItemData = ref(computed(() => props.clientListData))
    function toggleModal () {
      store.dispatch('getCounselList', clientItemData.value.id)
      store.dispatch('requestTrainerDetail', clientItemData.value.id)
      emit('toggleModal', true)
    }
    return {
      clientItemData,
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
.trainer-apply-style3 {
  box-sizing: border-box;
  width: 100px;
  height: 30px;
  font-size: 12px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  padding: 5px 15px;
  border: 2px solid #6dcef5;
  gap: 10px;
  border-radius: 25px;
  background-color: #FFF;
  color: #6dcef5;
  text-decoration-line: none;
  text-align: center;
}
.trainer-apply-style3:hover {
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
