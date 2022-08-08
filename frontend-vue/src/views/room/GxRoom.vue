<template>
  <div class="gxroom-container">
    <div id="join" v-if="!session">
      <div id="join-dialog" class="jumbotron vertical-center">
        <h1>Join a video session</h1>
        <div class="form-group">
          <p>
            <label>Participant</label>
            <input
              v-model="myUserName"
              class="form-control"
              type="text"
              required
            />
          </p>
          <p>
            <label>Session</label>
            <input
              v-model="mySessionId"
              class="form-control"
              type="text"
              required
            />
          </p>
          <p class="text-center">
            <button class="btn btn-lg btn-success" @click="joinSession()">
              Join!
            </button>
          </p>
        </div>
      </div>
    </div>

    <div class="session" v-if="session">
      <div class="session-header">
        <h1 id="session-title">{{ mySessionId }}</h1>
      </div>
      <!-- 방장 화면
            <div id="main-video" class="col-md-6">
                <user-video :stream-manager="mainStreamManager" />
            </div> -->

      <!-- 입장 인원 화면 -->
      <div class="session-video" style="background-color: black">
        <user-video :stream-manager="publisher" />
        <user-video
          v-for="sub in subscribers"
          :key="sub.stream.connection.connectionId"
          :stream-manager="sub"
        />
      </div>

      <div class="session-chat">
        <UserChat
          ref="chat"
          @message="sendMessage"
          :subscribers="subscribers"
        ></UserChat>
      </div>

      <div class="session-footer">
        <input type="button" value="cam"/>
        <input type="button" value="mic"/>
        <input type="button" value="캡쳐"/>
        <input
          class="gxroom-button"
          type="button"
          id="buttonLeaveSession"
          @click="leaveSession"
          value="Leave session"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { OpenVidu } from 'openvidu-browser'
import UserVideo from '@/components/room/UserVideo'
import { reactive, toRefs } from 'vue'
import { UserChat } from '@/components/room/UserChat.vue'
// import { useRouter } from 'vue-router'
// import { useStore } from 'vuex'

axios.defaults.headers.post['Content-Type'] = 'application/json'
const OPENVIDU_SERVER_URL = 'https://' + 'i7b108.p.ssafy.io'
const OPENVIDU_SERVER_SECRET = 'ssafy'
export default {
  name: 'App',
  components: {
    UserVideo,
    UserChat
  },

  setup () {
    // const store = useStore()

    const state = reactive({
      OV: undefined,
      session: undefined,
      mainStreamManager: undefined,
      publisher: undefined,
      subscribers: [],
      mySessionId: '',
      myUserName: ''
      // router: useRouter(),
      // store: useStore()
    })

    function joinSession () {
      // --- Get an OpenVidu object ---
      state.OV = new OpenVidu()
      // --- Init a session ---
      state.session = state.OV.initSession()

      // --- Specify the actions when events take place in the session ---
      // On every new Stream received...
      state.session.on('streamCreated', ({ stream }) => {
        const subscriber = state.session.subscribe(stream)
        subscriber.userId = state.myUserName // subscriber에 user추가
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

      // // 채팅 signal 받기
      // state.session.on('signal:public-chat', event => {
      //   this.$refs.chat.addMessage(event.data, JSON.parse(event.data).sender === this.myUserName, false)
      // })

      // --- Connect to the session with a valid user token ---
      // 'getToken' method is simulating what your server-side should do.
      // 'token' parameter should be retrieved and returned by your own backend
      getToken(state.mySessionId).then((token) => {
        state.session
          .connect(token, { clientData: state.myUserName })
          .then(() => {
            // --- Get your own camera stream with the desired properties ---
            const publisher = state.OV.initPublisher(undefined, {
              audioSource: undefined, // The source of audio. If undefined default microphone
              videoSource: undefined, // The source of video. If undefined default webcam
              publishAudio: true, // Whether you want to start publishing with your audio unmuted or not
              publishVideo: true, // Whether you want to start publishing with your video enabled or not
              resolution: '640x480', // The resolution of your video
              frameRate: 30, // The frame rate of your video
              insertMode: 'APPEND', // How the video is inserted in the target element 'video-container'
              mirror: false // Whether to mirror your local video or not
            })
            state.mainStreamManager = publisher
            state.publisher = publisher
            // --- Publish your stream ---
            state.session.publish(state.publisher)
          })
          .catch((error) => {
            console.log(
              'There was an error connecting to the session:',
              error.code,
              error.message
            )
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

      // this.$store.commit('', state.publisher)

      // this.$store.dispatch('', state.mySessionId)

      window.removeEventListener('beforeunload', leaveSession)
    }

    /**
     * --------------------------
     * SERVER-SIDE RESPONSIBILITY
     * --------------------------
     * These methods retrieve the mandatory user token from OpenVidu Server.
     * This behavior MUST BE IN YOUR SERVER-SIDE IN PRODUCTION (by using
     * the API REST, openvidu-java-client or openvidu-node-client):
     *   1) Initialize a Session in OpenVidu Server(POST /openvidu/api/sessions)
     *   2) Create a Connection in OpenVidu Server (POST /openvidu/api/sessions/<SESSION_ID>/connection)
     *   3) The Connection.token must be consumed in Session.connect() method
     */
    function getToken (mySessionId) {
      return createSession(mySessionId).then((sessionId) =>
        createToken(sessionId)
      )
    }

    // See https://docs.openvidu.io/en/stable/reference-docs/REST-API/#post-session
    function createSession (sessionId) {
      return new Promise((resolve, reject) => {
        axios
          .post(
            `${OPENVIDU_SERVER_URL}/openvidu/api/sessions`,
            JSON.stringify({
              customSessionId: sessionId
            }),
            {
              auth: {
                username: 'OPENVIDUAPP',
                password: OPENVIDU_SERVER_SECRET
              }
            }
          )
          .then((response) => response.data)
          .then((data) => resolve(data.id))
          .catch((error) => {
            if (error.response.status === 409) {
              resolve(sessionId)
            } else {
              console.warn(
                `No connection to OpenVidu Server. This may be a certificate error at ${OPENVIDU_SERVER_URL}`
              )
              if (
                window.confirm(
                  `No connection to OpenVidu Server. This may be a certificate error at ${OPENVIDU_SERVER_URL}\n\nClick OK to navigate and accept it. If no certificate warning is shown, then check that your OpenVidu Server is up and running at "${OPENVIDU_SERVER_URL}"`
                )
              ) {
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
          .post(
            `${OPENVIDU_SERVER_URL}/openvidu/api/sessions/${sessionId}/connection`,
            {},
            {
              auth: {
                username: 'OPENVIDUAPP',
                password: OPENVIDU_SERVER_SECRET
              }
            }
          )
          .then((response) => response.data)
          .then((data) => resolve(data.token))
          .catch((error) => reject(error.response))
      })
    }

    return {
      ...toRefs(state),
      joinSession,
      leaveSession,
      getToken,
      createSession,
      createToken
    }
  }
}
</script>

<style>
.session {
  width: 100%;
  height: 750px;
  display: grid;
  margin: 20px;
  grid-template-rows: 15% 75% 10%;
  grid-template-columns: 66% 34%;
  grid-gap: 1rem;
}

.session-header {
  grid-column: 1/3;
  grid-row: 1/2;
}

.session-video{
  display:grid;
  grid-template-rows: repeat(2, 1fr);
  grid-template-columns: repeat(3, 1fr);
}

.session-footer{
  grid-column: 1/3;
  grid-row: 3/4;
  display: flex;
}

.session-footer
.gxroom-button {
  background-color: red;
  color: white;
  border: none;
}

.gxroom-button:hover {
  background-color: firebrick;
}
</style>
