<template>
  <div class="video" v-if="streamManager">
    <p class="userName">{{ clientData }}</p>
    <ov-video class="user-video" :stream-manager="streamManager" />
  </div>
</template>

<script>
import OvVideo from './OvVideo'
import { computed } from 'vue'

export default {
  name: 'UserVideo',

  components: {
    OvVideo
  },

  props: {
    streamManager: Object
  },

  setup (props) {
    const clientData = computed(() => {
      const Data = getConnectionData()
      return Data.clientData
    })

    function getConnectionData () {
      const { connection } = props.streamManager.stream
      return JSON.parse(connection.data)
    }

    return { clientData, getConnectionData }
  }
}
</script>

<style>
.user-video{
  height:100%;
  width:100%;
  display:flex;
  align-items: center;
  justify-content: center;
}

.userName{
  padding:5px;
  background-color:white;
  position:absolute;
}

/* .video{
  display:flex;
  justify-content: center;
} */
</style>
