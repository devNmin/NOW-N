<template>
  <div class="thumbnail-container" @click="moveToConference">
    <div class="roomImg">
        <img :src="state.imgUrl" alt="testImg" class="cover">
    </div>

    <div class="roomInfo">
      <div class="info-category">
        {{genere}}
      </div>
      <div style="display:flex; flex-direction: column;">
        <div><h2>{{room.title}}</h2></div>
        <div>{{room.description}}</div>
        <div style="display:flex; justify-content:flex-end; align-items: center; ">
          <img src="@/assets/people.png" alt=" 아이콘넣기" width="20">&nbsp;{{room.participate_count}} / {{room.max_user}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getStorage, ref, getDownloadURL } from 'firebase/storage'
import { onMounted } from 'vue'
import { reactive } from '@vue/runtime-core'
import { useRouter } from 'vue-router'

export default {
  props: {
    room: Object
  },
  setup (props) {
    const router = useRouter()
    const storage = getStorage()
    const state = reactive({ imgUrl: ' ' })
    let genere = ''
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
        genere = '요  가'
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

    function moveToConference () {
      router.push({ path: `/gx/conferences/${props.room.id}` })
    }
    return { genere, state, moveToConference }
  }
}
</script>

<style scoped>

.thumbnail-container{
  cursor: pointer;
  width:100%;
  height:100%;
  border: solid 0.5px;
  border-color: rgb(204, 204, 204);
  display: grid;
  grid-template-rows: 1fr 1fr;
}

.thumbnail-container:hover{
  box-shadow: 10px 5px 5px gray;
}
.roomImg{
  width:100%;
  height:160px;
  background-size:cover;
  border-bottom: solid;
  border-bottom-width: thin;
  border-bottom-color: gray;
}

.roomImg .cover{
  width:100%;
  height:100%;
  object-fit:fill;
}

.roomInfo{
  padding: 10px;
  display:flex;
  flex-direction: column;
}

.info-category{
  border: solid;
  border-radius: 5px;
  width:80px;
  text-align: center;
  text-shadow: -1px 0 black, 0 1px black;
}
</style>
