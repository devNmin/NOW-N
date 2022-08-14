<template>
  <div>
    <div style="display:flex; justify-content:flex-end; margin-left: 150px;"><i>아이콘넣기</i><div>{{genere}}</div></div>
  <router-link :to="`/gx/conferences/${room.id}`" class="room-item" v-if="room" :room="room">
    <img :src="state.imgUrl" alt="testImg" width="300" style="margin-left: 50px; margin-right: 50px;" >
  </router-link>
  <div>
    <div style="display:flex; justify-content:space-between;">
    <div>{{room.title}}</div>
    <div>참가자수{{room.participate_count}}/ {{room.max_user}}</div>
    </div>
    <!-- <div>{{room.thumnail}}</div> -->
  </div>
  </div>
</template>

<script>
import { getStorage, ref, getDownloadURL } from 'firebase/storage'
import { onMounted } from 'vue'
import { reactive } from '@vue/runtime-core'
export default {
  props: {
    room: Object
  },
  setup (props) {
    const storage = getStorage()
    const state = reactive({ imgUrl: ' ' })
    let genere = ''
    // 'rooms/' + roomInfo.owner_id + '_' + roomInfo.title)
    getDownloadURL(ref(storage, props.room.thumnail))
      .then((url) => {
        state.imgUrl = url
      })
    onMounted(() => {
      console.log('onMounted', state.imgUrl) // 2
    }
    )
    console.log('듸뒤뒤뒤', state.imgUrl) // 1

    switch (props.room.category) {
      case 0: // if (x === 'value1')
        genere = '필라테스'
        break
      case 1: // if (x === 'value1')
        genere = '맨몸운동'
        break
      case 2: // if (x === 'value1')
        genere = '요가'
        break
      case 3: // if (x === 'value1')
        genere = '스트레칭'
        break
      case 4: // if (x === 'value1')
        genere = '기구운동'
        break
      case 5: // if (x === 'value1')
        genere = 'Etc'
        break
    }
    return { genere, state }
  }
}
</script>

<style>
.thumbnail1{
  margin:auto;
  /* grid-area: thumbnail; */
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
</style>
