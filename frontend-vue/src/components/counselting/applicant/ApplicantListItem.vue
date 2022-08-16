<template>
    <div class="deco-bar2" v-show="hide"></div>
    <div class="trainer-list-box2" v-show="hide">
      <div class="trainer-list-deco-box"></div>
      <div class="div1-noPadding"><img class="trainer-list-img" :src="imgData" alt=""></div>
      <div class="div2 item-padding">{{applycantItemData.name}}</div>
      <div class="div3 item-padding">{{applycantItemData.gender}}</div>
      <div class="div3 item-padding">{{applycantItemData.height}} / {{applycantItemData.user_weight}}</div>
      <div class="div4 item-padding2">
<router-link to="/counselting/apply" class="trainer-apply-style2" @click="accept" type="button">수락</router-link>
<button class="trainer-apply-style2 reject" type="button" @click="reject">거절</button>
      </div>
      <div class="trainer-list-deco-box"></div>
    </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
export default {
  props: {
    applycantData: {
      type: Object
    },
    hide: {
      type: Boolean
    }
  },
  setup (props) {
    const store = useStore()
    const applycantItemData = ref(computed(() => props.applycantData))
    function accept () {
      localStorage.setItem('applicantUserPk', applycantItemData.value.id)
    }
    function reject () {
      store.dispatch('rejectCounselting', applycantItemData.value.id)
    }
    return {
      applycantItemData,
      accept,
      reject
    }
  }
}
</script>

<style>
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
.trainer-apply-style2 {
  box-sizing: border-box;

  height: 30px;
  font-size: 16px;
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
.reject {
  border: 2px solid red;
  color: red;
}
.trainer-apply-style2:hover {
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

.item-padding2 {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  justify-content: center;
  padding: 40px 15px;
}
</style>
