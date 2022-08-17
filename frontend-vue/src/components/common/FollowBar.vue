<template>
  <div>
    <div class="followbar">
      <div class="follow-list"  v-if="hide">
        <div>
          <div class="followbar-title">
            <div>팔로우 중인 채널</div>
          </div>
          <FollowBarItem
          class="followLink"
          v-for="(followItem, i) in followData.followlist"
          :key="i"
          :followData="followItem"
          @click="onClick (followItem.pk)" />
        </div>
        <div v-if="followData.followings < 8">
          <div class="followbar-title">
            <div>추천 채널</div>
          </div>
          <FollowRecommendItem
          class="followLink"
          v-for="(recommendItem, i) in recommendData"
          :key="i"
          :recommendData="recommendItem"
          @click="onClick (recommendItem.id)"
          />
        </div>
      </div>
      <div @click="hideBar" class="follow-hide-bar">
        <div class="hide-icon" >
          <i class="fa-solid fa-angle-left" v-show="hide"></i>
          <div
          class="hide-icon-position">
          <i class="fa-solid fa-angle-right" v-show="!hide"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import FollowBarItem from '@/components/common/FollowBarItem.vue'
import FollowRecommendItem from '@/components/common/FollowRecommendItem.vue'
import { useStore } from 'vuex'
import { ref } from '@vue/reactivity'
import { computed } from '@vue/runtime-core'
export default {
  name: 'FollowBar',
  components: {
    FollowBarItem,
    FollowRecommendItem
  },
  setup (props, { emit }) {
    const store = useStore()
    const getFollowList = store.dispatch('followList', localStorage.getItem('userPk'))
    const getRecommendList = store.dispatch('recommendList')
    const followData = ref(computed(() => store.getters.followList))
    const recommendData = ref(computed(() => store.getters.recommendList))
    const hide = ref(computed(() => store.getters.hideFollow))
    function hideBar () {
      store.dispatch('hide')
    }
    function onClick (data) {
      store.commit('SET_MODAL_DATA', data)
    }
    return {
      getFollowList,
      getRecommendList,
      followData,
      recommendData,
      hide,
      hideBar,
      onClick
    }
  }
}
</script>
<style>
.followbar{
  /* background-color: #EFEFF1; */
  top: 88px;
  background: linear-gradient(to right,rgba(202, 217, 218, 0.5),rgba(255,255,255, 0.5));
  height: 978px;
  position: fixed;
  display: flex;
}
.follow-hide-bar {
  top: 88px;
  display: flex;
  width: 20px;
  height: 975px;
  margin: 0px;
}
.follow-list {
  width: 270px ;
  height: 900px;
}

.followbar-title{
  display: flex;
  justify-content: center;
  font-size:20px;
  font-weight: bold;
  text-align: center;
  padding:5px;
}
.followbar-close-button {
  width: 20px;
  height: 20px;
}
.followbar-close-button:hover {
  cursor: pointer;
}
.hide-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
  border: 2px solid none;
}
.hide-icon:hover {
  cursor: pointer;
}
.followbar-container{
  display:grid;
  height: 50px;
  grid-template-columns: 50px 300px;
}

/*

 */

.followbar-hide {
  background-color: #FFFFFF;
  width: 20px ;
  height: 980px;
  position: fixed;
  margin-top: 5rem;
}
.followbar-hide:hover {
  cursor: pointer;
}
.hide-icon-position {
  top: 500px;
}

.followLink {
  color: #6dcef5 !important;
  cursor: pointer;
  text-decoration: none  !important;;
}
</style>
