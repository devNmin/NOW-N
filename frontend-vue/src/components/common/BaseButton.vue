<template>
  <div class="button-container">
    <button :disabled="disabled">
      <slot></slot>
    </button>
  </div>
</template>

<script>

export default {
  props: {
    disabled: {
      type: Boolean,
      default: false
    }
  }
}
</script>
<style scoped>

.button-container{
<<<<<<< HEAD
  display:inline-block;
=======
  display:block;
  margin:auto;
  /* display:inline-block; */
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
}
button{
  /* background-color: var(--color-grey-900); */
  color: #6dcef5;

  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  width: 300px;
  height: 50px;
  font-size: 32px;
  text-align: center;
<<<<<<< HEAD
=======
  font-weight: bold;
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
}

button:hover {
  background-color: #6dcef5;
  color: white;
  font-weight: bold;
}

button.disabled{
  cursor: default;
  background-color: var(--color-grey-100);
  border: 2px solid var(--color-grey-500);
  color: var(--color-grey-500);
}
</style>
