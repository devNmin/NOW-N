<template>
    <div id="main-container" class="container">
        <div id="join" v-if="!session">
            <div id="join-dialog" class="jumbotron vertical-center">
                <h1>Join a video session</h1>
                <div class="form-group">
                    <p>
                        <label>Participant</label>
                        <input v-model="myUserName" class="form-control" type="text" required>
                    </p>
                    <p>
                        <label>Session</label>
                        <input v-model="mySessionId" class="form-control" type="text" required>
                    </p>
                    <p class="text-center">
                        <button class="btn btn-lg btn-success" @click="joinSession">Join!</button>
                    </p>
                </div>
            </div>
        </div>

        <div id="session" v-if="session">
            <div id="session-header">
                <h1 id="session-title">{{ mySessionId }}</h1>
                <input class="btn btn-large btn-danger" type="button" id="buttonLeaveSession" @click="leaveSession"
                    value="Leave session">
            </div>
            <div id="main-video" class="col-md-6">
                <user-video :stream-manager="mainStreamManager" />
            </div>
            <div id="video-container" class="col-md-6">
                <user-video :stream-manager="publisher" @click="updateMainVideoStreamManager(publisher)" />
                <user-video v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub"
                    @click="updateMainVideoStreamManager(sub)" />
            </div>
            <div style="width:100px; height:100px">
                <UserChat id="user-chat" :chatLog="chatLog" @sendMessage="sendMessage" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { OpenVidu } from 'openvidu-browser'
import UserVideo from '@/components/UserVideo'
import { reactive, toRefs } from 'vue'
import { UserChat } from '@/components/UserChat.vue'
import { useRouter } from 'vue-router'

axios.defaults.headers.post['Content-Type'] = 'application/json'

const OPENVIDU_SERVER_URL = 'https://' + location.hostname + ':4443'
const OPENVIDU_SERVER_SECRET = 'MY_SECRET'

export default {
  name: 'App',

  components: {
    UserVideo, UserChat
  },

  setup () {
    const state = reactive({
      OV: undefined,
      session: undefined,
      mainStreamManager: undefined,
      publisher: undefined,
      subscribers: [],
      mySessionId: 'SessionA',
      myUserName: 'Participant2'
    })

    console.log(state)
    function joinSession () {
      // --- Get an OpenVidu object ---
      state.OV = new OpenVidu()

      // --- Init a session ---
      state.session = state.OV.initSession()

      // --- Specify the actions when events take place in the session ---

      // On every new Stream received...
      state.session.on('streamCreated', ({ stream }) => {
        const subscriber = state.session.subscribe(stream)
        state.subscribers.push(subscriber)
      })

      // On every Stream destroyed...
      state.session.on('streamDestroyed', ({ stream }) => {
        const index = state.subscribers.indexOf(stream.streamManager, 0)
        if (index >= 0) {
          state.subscribers.splice(index, 1)
        }
      })

      // On every asynchronous exception...
      state.session.on('exception', ({ exception }) => {
        console.warn(exception)
      })

      // --- Connect to the session with a valid user token ---

      // 'getToken' method is simulating what your server-side should do.
      // 'token' parameter should be retrieved and returned by your own backend
      getToken(state.mySessionId).then(token => {
        state.session.connect(token, { clientData: state.myUserName })
          .then(() => {
            // --- Get your own camera stream with the desired properties ---

            const publisher = state.OV.initPublisher(undefined, {
              audioSource: undefined, // The source of audio. If undefined default microphone
              videoSource: undefined, // The source of video. If undefined default webcam
              publishAudio: true, // Whether you want to start publishing with your audio unmuted or not
              publishVideo: true, // Whether you want to start publishing with your video enabled or not
              resolution: '640x480', // The resolution of your video
              frameRate: 30,			// The frame rate of your video
              insertMode: 'APPEND',	// How the video is inserted in the target element 'video-container'
              mirror: false // Whether to mirror your local video or not
            })

            state.mainStreamManager = publisher
            state.publisher = publisher

            // --- Publish your stream ---

            state.session.publish(state.publisher)
          })
          .catch(error => {
            console.log('There was an error connecting to the session:', error.code, error.message)
          })
      })

      window.addEventListener('beforeunload', leaveSession)
    }

    function leaveSession () {
      // --- Leave the session by calling 'disconnect' method over the Session object ---
      if (state.session) state.session.disconnect()

      state.session = undefined
      state.mainStreamManager = undefined
      state.publisher = undefined
      state.subscribers = []
      state.OV = undefined

      window.removeEventListener('beforeunload', state.leaveSession)

      const router = useRouter()
      router.push({ name: 'Home' })
    }

    function updateMainVideoStreamManager (stream) {
      if (state.mainStreamManager === stream) return
      state.mainStreamManager = stream
    }

    /**
         * --------------------------
         * SERVER-SIDE RESPONSIBILITY
         * --------------------------
         * These methods retrieve the mandatory user token from OpenVidu Server.
         * This behavior MUST BE IN YOUR SERVER-SIDE IN PRODUCTION (by using
         * the API REST, openvidu-java-client or openvidu-node-client):
         *   1) Initialize a Session in OpenVidu Server	(POST /openvidu/api/sessions)
         *   2) Create a Connection in OpenVidu Server (POST /openvidu/api/sessions/<SESSION_ID>/connection)
         *   3) The Connection.token must be consumed in Session.connect() method
         */

    function getToken (mySessionId) {
      return createSession(mySessionId).then(sessionId => createToken(sessionId))
    }

    // See https://docs.openvidu.io/en/stable/reference-docs/REST-API/#post-session
    function createSession (sessionId) {
      return new Promise((resolve, reject) => {
        axios
          .post(`${OPENVIDU_SERVER_URL}/openvidu/api/sessions`, JSON.stringify({
            customSessionId: sessionId
          }), {
            auth: {
              username: 'OPENVIDUAPP',
              password: OPENVIDU_SERVER_SECRET
            }
          })
          .then(response => response.data)
          .then(data => resolve(data.id))
          .catch(error => {
            if (error.response.status === 409) {
              resolve(sessionId)
            } else {
              console.warn(`No connection to OpenVidu Server. This may be a certificate error at ${OPENVIDU_SERVER_URL}`)
              if (window.confirm(`No connection to OpenVidu Server. This may be a certificate error at ${OPENVIDU_SERVER_URL}\n\nClick OK to navigate and accept it. If no certificate warning is shown, then check that your OpenVidu Server is up and running at "${OPENVIDU_SERVER_URL}"`)) {
                location.assign(`${OPENVIDU_SERVER_URL}/accept-certificate`)
              }
              reject(error.response)
            }
          })
      })
    }

    // See https://docs.openvidu.io/en/stable/reference-docs/REST-API/#post-connection
    function createToken (sessionId) {
      return new Promise((resolve, reject) => {
        axios
          .post(`${OPENVIDU_SERVER_URL}/openvidu/api/sessions/${sessionId}/connection`, {}, {
            auth: {
              username: 'OPENVIDUAPP',
              password: OPENVIDU_SERVER_SECRET
            }
          })
          .then(response => response.data)
          .then(data => resolve(data.token))
          .catch(error => reject(error.response))
      })
    }

    return { ...toRefs(state), joinSession, leaveSession, updateMainVideoStreamManager, getToken, createSession, createToken }
  }
}
</script>
