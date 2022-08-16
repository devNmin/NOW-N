<template>
  <FollowBar></FollowBar>
  <div class="create-conference">
    <div class="gx-make-modal">
      <div class="gx-title">
        <label>
          제목
          <input type="text" v-model="roomInfo.title">
        </label>
      </div>
      <div class="gx-private">
        <label>
          비공개
          <input type="checkbox" v-model="roomInfo.private">
        </label>
      </div>
      <div class="gx-password" >
        <label>
          비밀번호
          <input type="password" v-model="roomInfo.password" v-if="roomInfo.private">
          <input type="password" v-model="roomInfo.password" v-else disabled>
        </label>
      </div>
      <div class="gx-image" >
        썸네일 이미지
        <input type="file" style="" id="img" multiple="multiple" @change="uploadFile">
      </div>
      <div class="gx-category">
        <label>필라테스<input type="radio" value=0 v-model="roomInfo.category"></label>
        <label>맨몸운동<input type="radio" value=1 v-model="roomInfo.category"></label>
        <label>요가<input type="radio" value=2 v-model="roomInfo.category"></label>
        <label>스트레칭<input type="radio" value=3 v-model="roomInfo.category"></label>
        <label>기구운동<input type="radio" value=4 v-model="roomInfo.category"></label>
        <label>기타<input type="radio" value=5 v-model="roomInfo.category"></label>
      </div>
      <div class="gx-time">
        <label>
          종료 시간
          <select v-model="roomInfo.end_time">
            <option v-for="option in optionsTimes"
              :value="option.value" :key="option" >
              {{option.text}}
            </option>
          </select>
        </label>
      </div>
      <div class="gx-personal">
        <label>
          최대 인원
          <select v-model="roomInfo.max_user">
            <option value="none" selected>=== 선택 ===</option>
            <option v-for="option in optionsMembers" :value="option.value" :key="option">
              {{option.text}}
            </option>
          </select>
        </label>
      </div>
      <div class="gx-explain">
        <input type="text" v-model="roomInfo.description">
      </div>
    </div>
    <div class="conference-button">
      <button type="button" @click="createRoom">방 생성</button>
      <button type="button" @click="moveToGxRoom">취소</button>
    </div>
  </div>
</template>

<script>
import { reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { getStorage, uploadBytes, ref } from 'firebase/storage'
import FollowBar from '@/components/common/FollowBar.vue'
export default {
  components: {
    FollowBar
  },
  setup () {
    const store = useStore()
    const router = useRouter()
    const NowDate = new Date()
    const optionsMembers = [
      { text: '1명', value: 1 },
      { text: '2명', value: 2 },
      { text: '3명', value: 3 },
      { text: '4명', value: 4 },
      { text: '5명', value: 5 },
      { text: '6명', value: 6 }
    ]
    const optionsTimes = [
      { text: '1시간후', value: 1 },
      { text: '2시간후', value: 2 },
      { text: '3시간후', value: 3 }
    ]

    const roomInfo = reactive({
      owner_id: computed(() => store.state.accounts.currentUserPk),
      password: null,
      category: 0,
      start_time: '',
      end_time: 1,
      title: null,
      description: '',
      max_user: 1,
      thumnail: '',
      is_active: false
    })
    const uploadFile = (e) => {
      const storage = getStorage()
      const file = e.target.files[0]
      console.log(roomInfo.owner_id)
      const storageRef = ref(storage, 'rooms/' + roomInfo.owner_id + '_' + roomInfo.title)
      uploadBytes(storageRef, file).then(() => {
        console.log('Uploaded a blob or file!')
      })
    }
    async function createRoom () {
      // 유효성 검사 필요
      roomInfo.thumnail = 'rooms/' + roomInfo.owner_id + '_' + roomInfo.title
      console.log('roomInfo.thumnail', roomInfo.thumnail)
      NowDate.setHours(NowDate.getHours() + roomInfo.end_time)
      roomInfo.end_time = NowDate.toISOString()
      console.log(roomInfo)
      await store.dispatch('createRoomInfo', roomInfo)

      const conference = store.state.room.roomInfo
      console.log(conference)
      router.push({ path: `/gx/conferences/${conference.id}`, params: { conference_id: conference.id, title: conference.title } })
    }

    function moveToGxRoom () {
      router.push({ name: 'GX-main' })
    }

    return { uploadFile, NowDate, optionsMembers, optionsTimes, roomInfo, createRoom, moveToGxRoom }
  }
}
</script>

<style scoped>
.create-conference{
  margin-left: 500px;
  margin-top: 100px;
}

.gx-make-modal{
  display:grid;
  width: 700px;
  height: 500px;
  grid-template-columns: 5fr 2fr 3fr;
  grid-template-rows: 1fr 1fr 2fr 1fr 3fr;
  grid-template-areas:
  "gx-title gx-private gx-image"
  "gx-password . gx-image"
  "gx-category gx-category gx-image"
  "gx-time gx-personal gx-personal"
  "gx-explain gx-explain gx-explain";
  padding: 50px;
  border: 1px solid #6dcef5;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

.gx-title{
  grid-area: gx-title;
}

.gx-private{
  grid-area: gx-private;
}

.gx-image{
  grid-area: gx-image;
}

.gx-password{
  grid-area: gx-password;
}

.gx-category{
  grid-area: gx-category;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr 1fr;
}

.gx-time{
  grid-area: gx-time;
}

.gx-personal{
  grid-area: gx-personal;
}

.gx-explain{
  display:flex;
  grid-area: gx-explain;
}
</style>
