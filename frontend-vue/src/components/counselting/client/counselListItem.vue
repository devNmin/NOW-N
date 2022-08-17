<template>
  <div>
      <div class="trainer-list-box2">
      <i class="fa-solid fa-utensils" v-show="!counselData.is_diet">&nbsp;{{counselData.start_date}} ~ {{counselData.end_date}}</i>
      &nbsp;&nbsp;&nbsp;&nbsp;
      <i class="fa-solid fa-dumbbell" v-show="!counselData.is_excise">&nbsp;{{counselData.times}}</i>
    </div>
  </div>
</template>

<script>
import { computed, reactive } from '@vue/runtime-core'
export default {
  props: {
    counselItem: {
      type: Object
    }
  },
  setup (props, { emit }) {
    const counselData = computed(() => props.counselItem)
    const dateLen = reactive({
      endDate: computed(() => counselData.value.end_date.lenth)
    })
    return {
      counselData,
      dateLen

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
.item-padding {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  padding: 40px 15px;
}
</style>
