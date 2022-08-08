<template>
  <div>

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
  grid-template-rows: 30% 20% 20% 30%;
  grid-template-columns: 40% 20% 40%;
  grid-template-areas:
    "title"
    "thumbnail";
  column-gap: 10px;
row-gap: 30px;
}

</style>
