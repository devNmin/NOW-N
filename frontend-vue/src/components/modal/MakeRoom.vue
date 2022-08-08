<template>
  <div class="grid-container">
    <div class="title">
      <div class="titletext">제목</div>
    </div>
    <div class="private">비공개</div>
    <div class="image">사진</div>
    <div class="password">비밀번호</div>
    <div class="sports">운동종류</div>
    <div class="endtime">종료시간</div>
    <div class="maxpeople">최대인원</div>
    <div class="roominfo">방정보</div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.grid-container{
  font-family: 'MaruBuriOTF';
  font-style: normal;
  display: grid;
  grid-template-rows: 15% 15% 20% 20% 30%;
  grid-template-columns: 40% 20% 40%;
  grid-template-areas:
    "title private image"
    "password password image"
    "sports sports image"
    "endtime maxpeople maxpeople"
    "roominfo roominfo roominfo";
  /* column-gap: 10px;
  row-gap: 30px; */
  height: 100vh;
  background: white;
}
.title{
  margin: 0;
  grid-area: title;
}
.titletext{
  float: left;
  font-size: 2vh;

}
.private{
  margin: 0;
  grid-area: private;
}
.password{
  margin: 0;
  grid-area: password;
}
.image{
  margin: 0;
  grid-area: image;
}
.sports{
  margin: 0;
  grid-area: sports;
}
.endtime{
  margin: 0;
  grid-area: endtime;
}
.maxpeople{
  margin: 0;
  grid-area: maxpeople;
}
.roominfo{
  margin: 0;
  grid-area: roominfo;
}
</style>
