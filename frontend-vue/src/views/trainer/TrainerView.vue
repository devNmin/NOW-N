<template>

<div class="trainer-first">
  <div class="around-box">
    <div>ALL ({{data.ALL_num}})</div>
    <div><SearchBar/></div>
  </div>
  <div class="deco-bar"></div>
  <CalendarEx/>
  <TrainerListEx/>
  <TrainerListItem v-for="t_num in data.ALL_num"
  :key="t_num"
  :imgData="data.img[t_num - 1]"
  :nameData="data.name[t_num - 1]"
  :exerciseData="data.exercise[t_num - 1]"
  :priceData="data.price[t_num - 1]"/>
  <div class="deco-bar"></div>
  <div> <PageNation/></div>
  <TrainerDetailModal/>
</div>

</template>

<script>
import TrainerDetailModal from '@/components/trainer/TrainerDetailModal.vue'
import SearchBar from '@/components/common/SearchBar.vue'
import TrainerListEx from '@/components/trainer/TrainerListEx.vue'
import TrainerListItem from '@/components/trainer/TrainerListItem.vue'
import PageNation from '@/components/common/PageNation.vue'
import { onMounted } from 'vue'
import { useStore } from 'vuex'
export default {
  name: 'TrainerView',
  components: { SearchBar, TrainerListEx, TrainerListItem, PageNation, TrainerDetailModal },
  setup () {
    const store = useStore()
    const data = {
      ALL_num: 4,
      img: ['1img', '2img', '3img', '4img'],
      name: ['a', 'b', 'c', 'd'],
      exercise: ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ'],
      price: ['1', '2', '3', '4']
    }
    onMounted(() => {
      store.dispatch('trainerList')
    })
    return {
      data
    }
  }
}
</script>

<style>
.trainer-first {
  position: absolute;
  border: 5px solid #000000;
  top: 200px;
  left: 400px;
  width: 1000px;
  height: 500px;
}
.around-box {
  display: flex;
  justify-content: space-between;
}
.deco-bar {
  width: 1000px;
  border: 2px solid #EEE;
}
</style>
