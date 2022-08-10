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
  display:block;
  margin:auto;
  /* display:inline-block; */
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
  font-weight: bold;
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
