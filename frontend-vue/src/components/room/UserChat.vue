<template>
    <div class="absolute flex top-0 h-screen z-20 right-0 flex-row border-l border-main-100">
        <!-- chat-bar -->
        <div ref="content"
            class="transition-all pt-16 pb-12 px-8 w-80 duration-700 bg-main-300 overflow-hidden flex flex-col items-center justify-between"
            :class="[state.isSidebarOpen ? 'max-w-lg' : 'max-w-0']">
            <!-- 채팅 내용 -->
            <ul class="border-2 h-full w-full border-main-100 bg-tc-500 p-4 overflow-y-auto m-0" id="chat-bar">
                <li class="flex flex-col mb-2" v-for="(chat, idx) in state.chats" :key="idx">
                    <!-- 내가 보낸 채팅인 경우 -->
                    <div v-if="chat.isMyMessage" class="border-r-2 border-sub-200 pr-2">
                        <div class="flex flex-row-reverse items-center">
                            <span class="text-sub-200 text-md ml-2 font-bold">Me</span>
                            <span class="text-tc-400 text-xs">{{ chat.time }}</span>
                        </div>
                        <div>
                            <p class="text-tc-300 text-sm break-all text-right">
                                {{ chat.content }}
                            </p>
                        </div>
                    </div>
                    <!-- 다른 사람이 보낸 채팅인 경우 -->
                    <div v-else class="border-l-2 border-main-100 pl-2">
                        <div class="flex flex-row items-center">
                            <span class="text-main-100 text-md mr-2 font-bold">{{
                                    chat.userId
                            }}</span>
                            <span class="text-tc-400 text-xs">{{ chat.time }}</span>
                        </div>
                        <div>
                            <p class="text-tc-300 text-sm break-all text-left">
                                {{ chat.content }}
                            </p>
                        </div>
                    </div>
                </li>
            </ul>

            <div class="flex flex-col items-start w-full mt-8">
                <!-- 메시지 보낼 유저 선택창 -->
                <div class="relative inline-flex border-3 rounded-lg border-main-100 w-1/2 mb-4 h-7 p-0">
                    <select v-model="state.selectedUser"
                        class="cursor-pointer font-bold px-4 py-0 text-sm form-select border-0 rounded-md text-gray-600 w-full h-5-5 border-transparent focus:border-transparent focus:ring-0 appearance-none">
                        <option selected="selected" value="all">all</option>
                        <option v-for="(sub, idx) in state.subscribers" :value="sub.stream.connection" :key="idx">
                            {{ JSON.parse(sub.stream.connection.data).clientData }}
                        </option>
                    </select>
                </div>

                <!-- 메시지 작성 -->
                <div class="w-full p-0 flex flex-row justify-between items-center">
                    <textarea v-model="state.message" @keydown.enter="sendMessage"
                        class="w-5/6 border-2 border-main-100 text-xs focus:border-main-100 focus:border-2 resize-none"
                        cols="" rows="2"></textarea>
                    <svg @click="sendMessage()" class="h-6 w-6 send-icon cursor-pointer" version="1.1"
                        xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                        viewBox="0 0 491.022 491.022" style="enable-background: new 0 0 491.022 491.022"
                        xml:space="preserve">

                    </svg>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.border-3 {
    border-width: 3px;
}

.h-5-5 {
    height: 1.375rem;
}

.send-icon {
    fill: #6667ab;
}
</style>

<script>
import { reactive } from 'vue'

export default {
  props: {
    subscribers: Object
  },

  setup (props, { emit }) {
    const state = reactive({
      // right: true,
      isSidebarOpen: true,
      selectedUser: 'all',
      message: '',
      subscribers: props.subscribers,
      chats: []
    })

    const toggle = () => {
      state.isSidebarOpen = !state.isSidebarOpen
    }

    const sendMessage = () => {
      const strippeddMessage = state.message.trim()

      if (strippeddMessage === '') return

      console.log('보낼 메시지 : ' + strippeddMessage)

      emit('message', {
        content: strippeddMessage,
        to: state.selectedUser
      })

      event.preventDefault() // enter키 누를 때 줄바꿈 방지
      state.message = '' // 메시지 창 초기화

      console.log(state.subscribers)
    }

    const addMessage = async (messageData, isMyMessage, isPrivate) => {
      const message = JSON.parse(messageData)

      // 내가 보낸 메시지인 경우
      if (isMyMessage) {
        message.sender += ' (You)'
      }

      // 개인 메시지인 경우
      if (isPrivate) {
        message.content += ' (private)'
      }

      const chatBar = document.querySelector('#chat-bar')
      const isScrollBottom =
                chatBar.scrollHeight - chatBar.scrollTop <= chatBar.clientHeight + 2

      // await 키워드 => 새로운 채팅 메시지 추가 완료 후 스크롤바가 아래로 이동되도록 함.
      await state.chats.push({
        userId: message.sender,
        time: message.time,
        content: message.content,
        isMyMessage: isMyMessage
      })

      // 채팅 스크롤이 끝까지 내려가 있는 경우 => 스크롤바 맨 아래로 이동시키기
      if (isScrollBottom) {
        chatBar.scrollTo({ top: chatBar.scrollHeight, behavior: 'smooth' })
      }

      console.log('메시지 수신 완료')
    }

    return { state, toggle, sendMessage, addMessage }
  }
}
</script>
