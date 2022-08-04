<template>
  <div class="video" v-if="streamManager">
    <ov-video class="user-video" :stream-manager="streamManager" />
    <div>
      <p style="color:white;">{{ clientData }}</p>
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

<style>
.user-video{
  height:290px;
  width:290px;
}
</style>
