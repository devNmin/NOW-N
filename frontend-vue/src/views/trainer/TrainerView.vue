<template>
  <FollowBar></FollowBar>
  <div class="trainer-first">
    <div></div>
    <div class="around-box">
      <div>ALL ({{trainerListCount}})</div>
      <SearchBar @search="search" v-model="data.searchValue"/>
    </div>
    <div class="deco-bar"></div>
    <TrainerListEx/>
    <div class="empty-img" v-show="trainerListCount === 0"><img src="@/assets/x.png" alt=""><h1> 검색 결과가 없습니다</h1></div>
    <TrainerListItem v-for="( t_item, i ) in trainerList"
    :hide="changeList(i)"
    :key="i"
    :trainerData="trainerList[i]"
    @toggleModal="toggleModal"/>
    <div class="deco-bar"></div>
    <div class="trainer-page-nation"> <PageNation :maxCount="trainerListCount" :countGap="4" @changePage="changePage"/></div>
    <TrainerDetailModal v-show="data.is_modal" :trainer="data.trainerId" @toggleModal="toggleModal"/>
  </div>

</template>

<script>
import TrainerDetailModal from '@/components/trainer/TrainerDetailModal.vue'
import SearchBar from '@/components/common/SearchBar.vue'
import TrainerListEx from '@/components/trainer/TrainerListEx.vue'
import TrainerListItem from '@/components/trainer/TrainerListItem.vue'
import PageNation from '@/components/common/PageNation.vue'
import FollowBar from '@/components/common/FollowBar.vue'
import { computed, reactive, ref, watch } from 'vue'
import { useStore } from 'vuex'
export default {
  name: 'TrainerView',
  components: { SearchBar, TrainerListEx, TrainerListItem, PageNation, TrainerDetailModal, FollowBar },
  setup () {
    const store = useStore()
    const trainerList = ref(computed(() => store.getters.trainerList))
    const trainerListCount = ref(computed(() => store.getters.trainerListCount))
    const data = reactive({
      img: [],
      trainerId: '0',
      pageStart: 0,
      pageEnd: 4,
      is_modal: false,
      wah: null
    })
    const getTrainerList = store.dispatch('trainerList')
    function search (searchValue) {
      store.dispatch('trainerSearch', searchValue)
    }
    function changePage (pageValue) {
      data.pageStart = 4 * (pageValue - 1)
      data.pageEnd = 4 * pageValue
    }
    function changeList (i) {
      if (data.pageStart <= i && i < data.pageEnd) {
        return true
      } else {
        return false
      }
    }
    function toggleModal (isModal) {
      data.is_modal = isModal
    }
    watch(() => store.getters.modalData, () => {
      data.trainerId = store.getters.modalData
      store.dispatch('requestTrainerDetail', data.trainerId)
      store.dispatch('isFollow', data.trainerId)
      data.is_modal = true
    })
    return {
      trainerList,
      trainerListCount,
      getTrainerList,
      changePage,
      changeList,
      search,
      data,
      toggleModal
    }
  }
}
</script>

<style>
:root {
  --trainer-decoBar-color: #6DCEF5;
}
.trainer-first {
  position: absolute;
  top: 10%;
  left: 20%;
  width: 60%;
  height: 60%;
  min-width: 760px;
}
.around-box {
  padding: 10px;
  display: flex;
  justify-content: space-between;

}
.deco-bar {
  width: 100%;
  border-bottom: 4px ridge var(--trainer-decoBar-color);
}
.trainer-page-nation {
  margin-left: 90%;
}
.empty-img {
  display: flex;
  align-items: center;
}
</style>
