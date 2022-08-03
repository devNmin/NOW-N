<template>
  <div v-if="streamManager">
    <ov-video :stream-manager="streamManager" />
    <div>
      <p>{{ clientData }}</p>
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
