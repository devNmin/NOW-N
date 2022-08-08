<template>
  <div class="back">
    <div class="body">
      <div class="grid-container-meetingroom">
        <div class="title">
          <h1 class="titlebox">
          </h1>
        </div>
        <div class="screen">
          <h2 class="screenbox"></h2>
        </div>
        <div class="routine">
          <h3 class="routinebox"></h3>
        </div>
        <div class="chatting">
          <h4 class="chattingbox"></h4>
        </div>
        <div class="meetingbutton">
          <button class="mike-button">마이크</button>
          <button class="video-button">비디오</button>
          <button class="capture-button">캡쳐</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.back{
  height: 94vh;
}
.body{
  margin: 5vh;
  width: 94vw;
  height: 87vh;
  background: #FFFFFF;
}
.grid-container-meetingroom {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 5% 43% 32% 10%;
  grid-template-columns: 70% 30%;
  grid-template-areas:
    "title title"
    "screen routine"
    "screen chatting"
    "meeting-button chatting";
  column-gap: 3vw;
  height: 93vh;
}
.title{
  margin: 0;
  grid-area: title;
}
.titlebox{
  margin-left: 3vw;
  width: 50vw;
  height: 5vh;
  background: grey;
}
.screen{
  margin-left: 3vw;
  margin-top: 3vh;
  grid-area: screen;
}
.screenbox{
  border: 1px solid #000000;
  border-radius: 20px;
  width: 64vw;
  height: 60vh;
}
.routine{
  margin: 0;
  grid-area: routine;
}
.routinebox{
  width: 23vw;
  height: 35vh;
  background: grey;
}
.chatting{
  margin: 0;
  grid-area: chatting;
}
.chattingbox{
  width: 23vw;
  height: 35vh;
  background: grey;
}
.meeting-button{
  margin: 0;
  grid-area: meeting-button;
}
.mike-button{
  margin-left: 20vw;
  width: 7vw;
  height: 5vh;
  float: left;
}
.video-button{
  margin-left: 4vw;
  width: 7vw;
  height: 5vh;
  float: left;
}
.capture-button{
  margin-left: 4vw;
  width: 7vw;
  height: 5vh;
  float: left;
}
</style>
