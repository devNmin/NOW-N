<template>
  <div class="container">
    <div class="gx-make-modal">
      <div class="gx-title">
        <label>
          제목
          <input type="text">
        </label>
      </div>
      <div class="gx-private">
        <label>
          비공개
          <input type="checkbox">
        </label>
      </div>
      <div class="gx-password">
        <label>
          비밀번호
          <input type="password">
        </label>
      </div>
      <div class="gx-image">
        <p>섬네일 사진</p>
      </div>
      <div class="gx-category">
        <label>
          필라테스
          <input type="checkbox">
        </label>

        <label>
          맨몸운동
          <input type="checkbox">
        </label>

        <label>
          요가
          <input type="checkbox">
        </label>

        <label>
          스트레칭
          <input type="checkbox">
        </label>

        <label>
          기구운동
          <input type="checkbox">
        </label>

        <label>
          기타
          <input type="checkbox">
        </label>
      </div>
      <div class="gx-time">
        <label>
          종료 시간
          <input type="text">
        </label>
      </div>
      <div class="gx-personal">
        <label>
          최대 인원
          <input type="text">
        </label>
      </div>
      <div class="gx-explain">
        <input type="text">
        <button type="button" @click="createRoom">방 생성</button>
        <button type="button" @click="moveToGxRoom">취소</button>
      </div>
    </div>
  </div>
</template>

<script>

import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

export default {
  setup () {
    const store = useStore()
    const router = useRouter()

    const roomInfo = {
      conference_id: 0,
      owner_id: 0,
      title: '',
      password: '',
      category: 0,
      start_time: '',
      end_time: '',
      max_user: 0,
      description: ''
    }

    function createRoom () {
      // 유효성 검사 필요

      store.dispatch('createRoomInfo', roomInfo)
      router.push({ name: 'GxRoom' })
    }

    function moveToGxRoom () {
      router.push({ name: 'GX-main' })
    }

    return { roomInfo, createRoom, moveToGxRoom }
  }
}
</script>

<style scoped>
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
