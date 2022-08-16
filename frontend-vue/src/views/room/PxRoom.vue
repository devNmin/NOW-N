<template>
<div class="pxroom-container"  style="width:100%; height:100%">
    <div v-if="!session">
      <div class="px-dialog">
        <h1>담당코치의 Code를 입력하세요</h1>
        <div class="form-group">
          <p style="font-size:30px;">
            <label>참가자 : </label>
            <input style="font-size:25px;" v-model="myUserName" class="form-control" type="text" required />
          </p>
          <p style="font-size:30px;">
            <label>입장 Code : </label>
            <input style="font-size:25px;" v-model="mySessionId" class="form-control" type="text" required />
          </p>
          <p style="margin-left:220px;">
            <button style="font-size: 20px;" @click="joinSession">
              입장하기
            </button>
          </p>
        </div>
      </div>
    </div>

    <div class="session" v-if="session">
      <div class="session-video"  id="capture">
        <UserVideoPx :stream-manager="publisher" style="width:25%; height:33%; position:absolute; top:60.5%; right:13%; z-index:2;"/>
        <UserVideoPx
            v-for="sub in subscribers"
            :key="sub.stream.connection.connectionId"
            :stream-manager="sub"
            style="width:100%;height:90%; position:absolute; z-index:1;"
            />
      </div>

      <div class="session-schedule">
        <div><span>Schedule</span></div>
        <div class="schedule" v-html="schedules" id="schedules"></div>
        <form class="scheduleFooter" onsubmit="return false">
          <input class="chat_input" id="sch" type="text" autocomplete="off" placeholder="일정을 입력하세요."/>
          <button id="submitBtn" type="submit" @click="sendSchedule">Enter</button>
        </form>
      </div>

      <div class="session-chat">
        <div>
          <span>채팅창</span>
        </div>
        <div class="messages" v-html="messages" id="messages"></div>
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
        <div class="button">
            <button @click="onSave">screenshot</button>
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
import html2canvas from 'html2canvas'
import axios from 'axios'
import { OpenVidu } from 'openvidu-browser'
import UserVideoPx from '@/components/room/UserVideoPx'
import { reactive, toRefs, ref, watch, nextTick } from 'vue'
axios.defaults.headers.post['Content-Type'] = 'application/json'
const OPENVIDU_SERVER_URL = 'https://' + 'i7b108.p.ssafy.io:8443'
const OPENVIDU_SERVER_SECRET = 'ssafy'
export default {
  components: {
    UserVideoPx
  },
  setup () {
    const messages = ref('')

    const schedules = ref('')

    const state = reactive({
      OV: undefined,
      session: undefined,
      publisher: undefined,
      subscribers: [],
      mySessionId: '',
      myUserName: '',
      audio: true,
      video: true,
      audioMsg: '마이크 ON',
      videoMsg: '비디오 ON',
      index: 0
    })

    async function joinSession () {
      // --- 1) Get an OpenVidu object ---
      state.OV = new OpenVidu()
      // --- 2) Init a session ---
      state.session = state.OV.initSession()
      // --- 3) Specify the actions when events take place in the session ---
      // On every new Stream received...
      state.session.on('streamCreated', ({ stream }) => {
        const subscriber = state.session.subscribe(stream)
        state.subscribers.push(subscriber)
      })

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

      // 같은 session 내에서 텍스트 스케줄을 위한 signal
      state.session.on('signal:my-schedule', (event) => {
        const schedule = event.data.split('&$')
        console.log('>>>>>>>>>>>>>> schedule : ', schedule)
        if (schedule === '') {
          schedules.value += ''
        } else {
          schedules.value += '<div align="left">' + '<div style="padding: 10px; margin-bottom: 10px; width: 60%; background-color: #6363bf; color: #fff; border-radius: 10px;  word-wrap: break-word;"">' + '<div class="mb-3">' + schedule[1] + ' </div>' + '</div>'
        }
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
      // --- 4) Connect to the session with a valid user token ---
      // Get a token from the OpenVidu deployment
      getToken(state.mySessionId).then((token) => {
        // First param is the token. Second param can be retrieved by every user on event
        // 'streamCreated' (property Stream.connection.data), and will be appended to DOM as the user's nickname
        state.session.connect(token, { clientData: state.myUserName })
          .then(() => {
            // --- 5) Get your own camera stream with the desired properties ---
            // Init a publisher passing undefined as targetElement (we don't want OpenVidu to insert a video
            // element: we will manage it on our own) and with the desired properties
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
            // --- 6) Publish your stream ---
            state.session.publish(state.publisher)
          })
          .catch((error) => {
            console.log('There was an error connecting to the session:', error.code, error.message)
          })
      })
      window.addEventListener('beforeunload', leaveSession)
    }

    function leaveSession () {
      // --- 7) Leave the session by calling 'disconnect' method over the Session object ---
      if (state.session) state.session.disconnect()
      // Empty all properties...
      state.session = undefined
      state.publisher = undefined
      state.subscribers = []
      state.OV = undefined
      // Remove beforeunload listener
      window.removeEventListener('beforeunload', leaveSession)
    }

    async function getToken (mySessionId) {
      return createSession(mySessionId).then((sessionId) =>
        createToken(sessionId)
      )
    }

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

    function onSave () {
      state.index += 1
      const capture = document.querySelector('#capture')
      html2canvas(capture).then(
        canvas => {
          saveAs(canvas.toDataURL(), state.index + '이미지.jpg')
          // const textToImg = canvas.toDataURL()
          console.log(canvas)
        }
      )
    }

    const saveAs = (uri, filename) => {
      const link = document.createElement('a')
      if (typeof link.download === 'string') {
        link.href = uri
        link.download = filename
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
      } else {
        window.open(uri)
      }
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

    function sendSchedule () {
      const schedule = document.getElementById('sch').value
      if (schedule !== '') {
        state.session.signal({
          data: state.myUserName + '&$' + schedule,
          to: [],
          type: 'my-schedule'
        })
          .then(() => {
            console.log('message sent successfully!!')
            document.getElementById('sch').value = ''
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

    watch(() => schedules.value, (newS, pre) => {
      console.log('와치')
      console.log(newS)
      nextTick(() => {
        const sch = document.getElementById('schedules')
        console.log('스케줄')
        console.log(sch)
        sch.scrollTo({ top: sch.scrollHeight, behavior: 'smooth' })
      })
    })

    return { ...toRefs(state), joinSession, leaveSession, getToken, createSession, createToken, muteAudio, muteVideo, onSave, saveAs, messages, schedules, sendMessage, sendSchedule }
  }
}
</script>

<style scoped>
.px-dialog{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.session {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-rows: 4fr 4fr 1fr;
  grid-template-columns: 2fr 1fr;
  grid-template-areas:
  "session-video session-schedule"
  "session-video session-chat"
  "session-footer session-exit";
  grid-gap: 1rem;
}

.session-video{
  grid-area: session-video;
  position:relative;
  padding: 20px;
  background-color: #D9D9D9;
  border-radius: 20px;
  margin-left:30px;
  margin-top: 50px;
}

.session-schedule{
    margin-top: 50px;
    grid-area: session-schedule;
    width:100%;
    height:80%;
}
.session-chat{
    margin-top: 20px;
    grid-area: session-chat;
    width:100%;
    height: 100%;
}
.session-footer{
    grid-area: session-footer;
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
  grid-area: session-exit;
  width:100%;
  height:100%;
  grid-column:2/3;
  grid-row:3/4;
  display:flex;
  justify-content: center;
}

.gxroom-button {
  margin-top:20px;
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
  height: 250px;
  /* background-color: #ccc; */
  background-color: #8cd5f2;
  /* /* border: 5px #ccc solid; */
  border-radius: 5px;
  /* box-shadow: 5px 5px 5px rgb(235, 235, 235); */
  font-size: 18px;
  word-break: break-all;
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

.scheduleFooter{
    height: 10%;
    width: 100%;
  line-height: 30px;
  border-top: 1px solid rgba(156, 172, 172, 0.2);
  display: flex;
  flex-shrink: 0;
  display: inline-block;
}

.chatFooter {
  height: 10%;
  width: 100%;
  line-height: 30px;
  border-top: 1px solid rgba(156, 172, 172, 0.2);
  display: flex;
  flex-shrink: 0;
  display: inline-block;
}

#submitBtn {
  width: 55px;
  height:55px;
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
  height:5.5%;
  width:500px;
  flex-grow: 1;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: transparent;
  padding: 0 30px;
  font-size: 16px;
  position: absolute;
}

.schedule {
  flex-grow: 1;
  padding: 10px 20px;
  overflow: auto;
  height: 250px;
  background-color: #c8c1e4;
  border-radius: 5px;
  font-size: 18px;
  word-break: break-all;
  position: relative;
}
</style>
