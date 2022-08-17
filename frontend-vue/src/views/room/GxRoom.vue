<template>
  <div class="gxroom-container" style="width:100%; height:100%">
    <div class="session" v-if="session">
      <div class="session-header">
        <h1 id="session-title">{{ mySessiontitle }}</h1>
      </div>

      <div class="session-video">
        <user-video :stream-manager="publisher" />
        <user-video
          v-for="sub in subscribers"
          :key="sub.stream.connection.connectionId"
          :stream-manager="sub"
        />
      </div>

      <div class="session-chat">
        <div>
          <span>채팅창</span>
        </div>
        <div class="messages" v-html="messages" id="messages">
        </div>
        <form class="chatFooter" onsubmit="return false">
          <input class="chat_input" id="msg" type="text" autocomplete="off" placeholder="메세지를 입력하세요."/>
          <button id="submitBtn" type="submit" @click="sendMessage">Enter</button>
        </form>
      </div>

      <div class="session-footer">
        <div class="button">
          <button v-bind:class="{'green': audio, 'red': !audio}" @click="muteAudio">
            <i v-show="audio" class="fas fa-microphone fa-2x" style="font-size:2rem; margin-right:15px; margin-left:5px;"></i>
            <i v-show="!audio" class="fas fa-microphone-slash fa-2x" style="font-size:2rem;"></i>
            <span>{{audioMsg}}</span>
          </button>
        </div>
        <div class="button">
          <button :class="{'green': video, 'red': !video}" @click="muteVideo">
            <i v-show="video" class="fas fa-video" style="font-size:2rem; margin-right:15px; margin-left:5px;"></i>
            <i v-show="!video" class="fas fa-video-slash fa-2x" style="font-size:2rem;"></i>
            <span>{{videoMsg}}</span>
          </button>
        </div>
      </div>

      <div class="session-exit">
        <input
          class="gxroom-button"
          type="button"
          id="buttonLeaveSession"
          @click="leaveSession"
          value="O U T"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { OpenVidu } from 'openvidu-browser'
import UserVideo from '@/components/room/UserVideo'
import { ref, toRefs, reactive, computed, watch, nextTick } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { onMounted } from '@vue/runtime-core'

axios.defaults.headers.post['Content-Type'] = 'application/json'
const OPENVIDU_SERVER_URL = 'https://' + 'i7b108.p.ssafy.io:8443'
const OPENVIDU_SERVER_SECRET = 'ssafy'
export default {
  components: {
    UserVideo
  },

  props: {
    conference_id: {
      type: Number
    },
    title: {
      type: String
    }
  },

  setup (props) {
    const store = useStore()
    const router = useRouter()

    const roomInfo = ref(computed(() => store.state.room.roomInfo))

    const messages = ref('')

    const userInfo = ref(computed(() => store.state.profile.myinfo))

    const state = reactive({
      OV: undefined,
      session: undefined,
      publisher: undefined,
      subscribers: [],
      mySessionId: props.conference_id,
      mySessiontitle: roomInfo.value.title,
      myUserName: userInfo.value.name,
      audio: true,
      video: true,
      audioMsg: '마이크 ON',
      videoMsg: '비디오 ON'
    })

    onMounted(() => {
      joinSession()
    })

    async function joinSession () {
      console.log('joinSession')
      // 현재 방 정보 가져오기
      await store.dispatch('getRoomInfo', state.mySessionId)
      state.mySessiontitle = roomInfo.value.title
      console.log('title ' + state.mySessiontitle)

      // 현재 유저 정보 가져오기
      await store.dispatch('profile', localStorage.getItem('userPk')) // load user profile
      state.myUserName = userInfo.value.name
      console.log(userInfo.value.name)

      // --- Get an OpenVidu object ---
      state.OV = new OpenVidu()
      // --- Init a session ---
      state.session = state.OV.initSession()

      // 같은 session 내에서 텍스트 채팅을 위한 signal
      state.session.on('signal:my-chat', (event) => {
        const message = event.data.split('&$')
        console.log('>>>>>>>>>>>>>> message : ', message)
        if (message === '') {
          messages.value += ''
        } else {
          console.log('저장된 : ', '현재 : ', message[0])
          if (message[0] === state.myUserName) {
            console.log(messages.value)
            console.log('내가 쓴 메시지')
            messages.value += '<div align="right">' + '<div style="padding: 10px; margin-bottom: 10px; width: 60%; background-color: #fff; border-radius: 10px;  word-wrap: break-word;"">' + '<div style="font-weight: 900;">' + message[0] + ' 님의 메시지: </div>' + '<div>' + message[1] + ' </div>' + '</div>' + '</div>'
          } else {
            console.log('니가 쓴 메시지')
            messages.value += '<div align="left">' + '<div style="padding: 10px; margin-bottom: 10px; width: 60%; background-color: #6363bf; color: #fff; border-radius: 10px;  word-wrap: break-word;"">' + '<div style="font-weight: 900;">' + message[0] + ' 님의 메시지: </div>' + '<div class="mb-3">' + message[1] + ' </div>' + '</div>'
          }
        }
      })

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
              publishAudio: state.audio, // Whether you want to start publishing with your audio unmuted or not
              publishVideo: state.video, // Whether you want to start publishing with your video enabled or not
              resolution: '640x480', // The resolution of your video
              frameRate: 30, // The frame rate of your video
              insertMode: 'APPEND', // How the video is inserted in the target element 'video-container'
              mirror: false // Whether to mirror your local video or not
            })
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
      console.log('몇명인지')
      console.log(state.subscribers.length)
      if (state.subscribers.length === 0) {
        store.dispatch('deleteRoomInfo', props.conference_id)
      }
      // --- Leave the session by calling 'disconnect' method over the Session object ---
      if (state.session) state.session.disconnect()
      state.session = undefined
      state.publisher = undefined
      state.subscribers = []
      state.OV = undefined

      window.removeEventListener('beforeunload', leaveSession)
      router.push({ name: 'gxConferences' })
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

    function muteAudio () {
      state.audio = !state.audio
      if (state.audio === true) state.audioMsg = '마이크 ON'
      else state.audioMsg = '마이크 OFF'
      state.publisher.publishAudio(state.audio)
    }

    function muteVideo () {
      state.video = !state.video
      if (state.video === true) state.videoMsg = '비디오 ON'
      else state.videoMsg = '비디오 OFF'
      state.publisher.publishVideo(state.video)
    }

    function sendMessage () {
      const message = document.getElementById('msg').value
      if (message !== '') {
        console.log('message ', message)

        state.session.signal({
          data: state.myUserName + '&$' + message,
          to: [],
          type: 'my-chat'
        })
          .then(() => {
            console.log('message sent successfully!!')
            document.getElementById('msg').value = ''
          })
          .catch(error => {
            console.error(error)
          })
      }
    }

    watch(() => messages.value, (newM, pre) => {
      console.log('와치')
      console.log(newM)
      nextTick(() => {
        const msg = document.getElementById('messages')
        console.log('메시지')
        console.log(msg)
        msg.scrollTo({ top: msg.scrollHeight, behavior: 'smooth' })
      })
    })

    return {
      ...toRefs(state),
      joinSession,
      leaveSession,
      getToken,
      createSession,
      createToken,
      muteAudio,
      muteVideo,
      roomInfo,
      sendMessage,
      messages
    }
  }
}
</script>

<style>
.session {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-rows: 2fr 7fr 1fr;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1rem;
}

.session-header {
  grid-column: 1/3;
  grid-row: 1/2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.session-video{
  padding: 20px;
  display:grid;
  grid-template-rows: repeat(2, 1fr);
  grid-template-columns: repeat(3, 1fr);
  background-color: #D9D9D9;
  border-radius: 20px;
  margin-left:30px;
}

.session-chat{
  grid-column: 2/3;
  grid-row: 2/3;
  display:flex;
  flex-direction: column;
}

.session-footer{
  grid-column: 1/2;
  grid-row: 3/4;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 50px;
  /* border-radius: 10px;
  background-color: #6dcef5; */
}

.session-footer .button{
  width: 15%;
}

.session-exit{
  width:100%;
  height:100%;
  grid-column:2/3;
  grid-row:3/4;
  display:flex;
  justify-content: center;
}
.gxroom-button {
  font-size:20px;
  width:15%;
  height:40%;
  background-color: red;
  border-radius: 5px;
  color: white;
  border: none;
}

.gxroom-button:hover {
  background-color: firebrick;
}

.green{
  cursor: pointer;
  border-radius: 5px;
  font-size: 20px;
  border-color: rgb(20, 220, 47);
  background-color:rgb(20, 220, 47);
}

.red{
  cursor: pointer;
  border-radius: 5px;
  font-size: 20px;
  border-color: rgb(245, 88, 71);
  background-color:rgb(245, 88, 71);
}

.messages {
  flex-grow: 1;
  padding: 10px 20px;
  overflow: auto;
  height: 90%;
  /* background-color: #ccc; */
  background-color: #8cd5f2;
  /* /* border: 5px #ccc solid; */
  border-radius: 5px;
  /* box-shadow: 5px 5px 5px rgb(235, 235, 235); */
  font-size: 18px;
  word-break: break-all;
  font-family: "BMJua";
  position: relative;
}

.messages::-webkit-scrollbar {
  width: 5px;
  height: 1px;
}

.messages::-webkit-scrollbar-track {
  background-color: rgb(255, 255, 255);
}

.messages::-webkit-scrollbar-thumb {
  background-color: rgb(126, 125, 125);
}

.messages::-webkit-scrollbar-button {
  display: none;
}

.chatFooter {
  height:10%;
  display: flex;
}

#msg {
  height: 5.5%;
}
#submitBtn {
  width: 55px;
  height: 5.5%;
  border: none;
  background: transparent;
  font-size: 16px;
  cursor: pointer;
  position: absolute;
  right: 0%;
  background-color: #6363bf;
  border-radius: 5px;
  color: #fff;
}

#submitBtn:hover {
  background-color: #fff;
  color: #6363bf;
}

.chat_input{
  width:500px;
  flex-grow: 1;
  border: 1px solid #ccc;
  padding-left: 15px;
  border-radius: 5px;
  background: transparent;
  font-size: 16px;
  position: absolute;
}
</style>
