<template>
  <router-link :to="`/gx/${room.id}`" class="room-item" v-if="room">
    <div>{{room.title}}</div>
  </router-link>
</template>

<script>
export default {
  props: {
    room: Object
  }
}
</script>

<style>
.thumbnail1{
  margin:auto;
  /* grid-area: thumbnail; */
  box-sizing: border-box;
  width: 300px;
  height: 240px;
  background: url(http://cdn.kormedi.com/wp-content/uploads/2021/09/08_014.jpg);
  border: 1px solid #000000;
  border-radius: 20px;
}
</style>
