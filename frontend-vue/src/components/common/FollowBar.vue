<template>
  <div>
    <div class="followbar">
      <div class="follow-list">
        <div class="followbar-title">
          <div>팔로우 중인 채널</div>
        </div>
        <FollowBarItem
        v-for="likeI in followData.likeNum"
        :key="likeI"
        :imgdata="followData.img[likeI - 1]"
        :namedata="followData.name[likeI - 1]"
        :followNumdata="followData.followNum[likeI - 1]"
        />
      </div>
      <div @click="changeView" class="follow-hide-bar">
        <div class="hide-icon">
          <i class="fa-solid fa-angle-left"></i>
        <div
    class="hide-icon-position"
    @click="changeView">
      <i class="fa-solid fa-angle-right"></i>
    </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import FollowBarItem from '@/components/common/FollowBarItem.vue'
import { useStore } from 'vuex'
export default {
  name: 'FollowBar',
  components: {
    FollowBarItem
  },
  setup (props, { emit }) {
    const store = useStore()
    const followData = {
      img: [1, 2],
      name: ['승', '주'],
      followNum: ['1', '2'],
      likeNum: 2
    }
    function changeView () {
      emit('hideFollow')
      store.dispatch('hide')
    }
    return {
      followData,
      changeView
    }
  }
}
</script>
<style>
.followbar{
  /* background-color: #EFEFF1; */
  background: linear-gradient(to right,rgba(202, 217, 218, 0.5),rgba(255,255,255, 0.5));
  width: 15% ;
  height: 980px;
  position: fixed;
  display: flex;
}
.follow-hide-bar {
  display: flex;
  width: 20px;
  height: 980px;
  margin: 0px;
}
.follow-list {
  width: 270px ;
  height: 900px;
}

.followbar-title{
  display: flex;
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
</style>
