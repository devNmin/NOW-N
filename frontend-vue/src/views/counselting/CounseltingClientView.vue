<template>
<FollowBar></FollowBar>
<div class="trainer-first">
  <div></div>
  <div class="around-box">
    <div>ALL ({{clientList.length}})</div>
    <SearchBar @search="search" v-model="data.searchValue"/>
  </div>
  <div class="deco-bar"></div>
  <ClientListEx/>
  <div v-show="clientList.length === 0" class="empty-img"><img src="@/assets/x.png" alt=""><h1> 검색 결과가 없습니다</h1></div>
  <ClientListItem v-for="(a_item, i) in clientList"
  :hide="changeList(i)"
  :key="i"
  :clientListData="clientList[i]"
  @toggleModal="toggleModal"/>
  <div class="deco-bar"></div>
  <div class="trainer-page-nation"><PageNation :maxCount="trainerListCount" :countGap="4" @changePage="changePage"/></div>
  <TrainerDetailModal v-show="data.is_modal" :trainer="data.trainerId" @toggleModal="toggleModal"/>
</div>

</template>

<script>
import TrainerDetailModal from '@/components/trainer/TrainerDetailModal.vue'
import SearchBar from '@/components/common/SearchBar.vue'
import ClientListEx from '@/components/counselting/client/clientListEx.vue'
import ClientListItem from '@/components/counselting/client/clientListItem.vue'
import PageNation from '@/components/common/PageNation.vue'
import FollowBar from '@/components/common/FollowBar.vue'
import { computed, reactive, ref } from 'vue'
import { useStore } from 'vuex'
export default {
  name: 'CounseltongApplicantView',
  components: { SearchBar, ClientListEx, ClientListItem, PageNation, TrainerDetailModal, FollowBar },
  setup () {
    const store = useStore()
    const clientList = ref(computed(() => store.getters.clientList))
    const data = reactive({
      img: [],
      pageStart: 0,
      pageEnd: 4,
      is_modal: false
    })
    const getClientList = store.dispatch('getClientList', localStorage.getItem('userPk'))
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
    return {
      clientList,
      getClientList,
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
