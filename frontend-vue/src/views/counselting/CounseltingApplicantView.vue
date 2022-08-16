<template>
<FollowBar></FollowBar>
<div class="trainer-first">
  <div></div>
  <div class="around-box">
    <div>ALL ({{applycantList.length}})</div>
    <SearchBar @search="search" v-model="data.searchValue"/>
  </div>
  <div class="deco-bar"></div>
  <ApplicantListEx/>
  <div v-show="applycantList.length === 0" class="empty-img"><img src="@/assets/x.png" alt=""><h1> 검색 결과가 없습니다</h1></div>
  <ApplicantListItem v-for="(a_item, i) in applycantList"
  :hide="changeList(i)"
  :key="i"
  :applycantData="applycantList[i]"
  @toggleModal="toggleModal"/>
  <div class="deco-bar"></div>
  <div class="trainer-page-nation"><PageNation :maxCount="trainerListCount" :countGap="4" @changePage="changePage"/></div>
  <TrainerDetailModal v-show="data.is_modal" :trainer="data.trainerId" @toggleModal="toggleModal"/>
</div>

</template>

<script>
import TrainerDetailModal from '@/components/trainer/TrainerDetailModal.vue'
import SearchBar from '@/components/common/SearchBar.vue'
import ApplicantListEx from '@/components/counselting/applicant/ApplicantListEx.vue'
import ApplicantListItem from '@/components/counselting/applicant/ApplicantListItem.vue'
import PageNation from '@/components/common/PageNation.vue'
import FollowBar from '@/components/common/FollowBar.vue'
import { computed, reactive, ref } from 'vue'
import { useStore } from 'vuex'
export default {
  name: 'CounseltongApplicantView',
  components: { SearchBar, ApplicantListEx, ApplicantListItem, PageNation, TrainerDetailModal, FollowBar },
  setup () {
    const store = useStore()
    const applycantList = ref(computed(() => store.getters.applicantList))
    const data = reactive({
      img: [],
      pageStart: 0,
      pageEnd: 4,
      is_modal: false
    })
    const getApplyList = store.dispatch('getApplycantList')
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
      applycantList,
      getApplyList,
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
