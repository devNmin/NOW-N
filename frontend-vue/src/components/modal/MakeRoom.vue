<template>
  <div class="grid-container">
    <div class="title">
      1
    </div>
    <div class="private">2</div>
    <div class="password">3</div>
    <div class="image">4</div>
    <div></div>
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
  grid-template-rows: 10% 10% 20% 20% 40%;
  grid-template-columns: 40% 20% 40%;
  grid-template-areas:
    "title private image"
    "password password image"
    "sports sports image"
    "endtime maxpeople maxpeople"
    "roominfo roominfo roominfo";
  /* column-gap: 10px;
  row-gap: 30px; */
  height: 90vh;
}
.title{
  margin: 0;
  grid-area: title;
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
