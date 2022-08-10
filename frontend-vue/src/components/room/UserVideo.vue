<template>
<<<<<<< HEAD
  <div v-if="streamManager">
    <ov-video :stream-manager="streamManager" />
    <div>
      <p>{{ clientData }}</p>
=======
  <div class="video" v-if="streamManager">
    <ov-video class="user-video" :stream-manager="streamManager" />
    <div>
      <p style="color:white;">{{ clientData }}</p>
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
    </div>
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
<<<<<<< HEAD
=======

<style>
.user-video{
  height:290px;
  width:290px;
}
</style>
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
