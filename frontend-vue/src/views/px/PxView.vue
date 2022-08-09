<template>
  <div class="container">
    <div class="PX-grid">
      <div class="PX-menu">
      </div>
      <div class="PX-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
.PX-grid{
  display: grid;
  grid-template-rows: 1fr 7fr;
  grid-template-areas:
  "px-menu"
  "px-content";
}

.PX-menu{
  grid-area: px-menu;
}

.PX-content{
  grid-area: px-content;
}
</style>>
