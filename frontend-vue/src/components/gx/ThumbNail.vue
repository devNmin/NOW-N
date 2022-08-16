<template>
  <div style="margin:0 50px;">
    <div >
      <div style="display:flex; justify-content: space-between; margin-bottom:5px; ">
        <div>{{room.title}}</div>
        <div>{{genere}}</div>
      </div>
    </div>
  <router-link :to="`/gx/conferences/${room.id}`" class="room-item" v-if="room" :room="room">
    <img :src="state.imgUrl" alt="testImg" width="300" class='roomImg' >
  </router-link>
  <div>
    <div style="display:flex; justify-content:flex-end; align-items: center; ">
      <img src="@/assets/people.png" alt=" 아이콘넣기" width="20"> {{room.participate_count}}/ {{room.max_user}}
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
} // people.png
</script>

<style>
.roomImg{
  box-sizing: border-box;
  border: 1px solid #000000;
  border-radius: 20px;
}
</style>
