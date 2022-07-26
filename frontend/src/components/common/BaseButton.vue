<template>
    <button :class="{disabled, toggled}" :disabled="disabled" @click.stop="onClick">
      <slot></slot>
    </button>
</template>

<script>

export default {
  props: {
    disabled: {
      type: Boolean,
      default: false
    },
    toggled: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    onClick () {
      this.$emit('click', !this.toggled)
    }
  }
}
</script>
<style scoped>

button{
  background-color: #6dcef5;
  color: white;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
}

button:hover {
  background-color: var(--color-grey-900);
  color: white;
}

button.disabled{
  cursor: default;
  background-color: var(--color-grey-100);
  border: 2px solid var(--color-grey-500);
  color: var(--color-grey-500);
}

button.toggled{
  background-color: var(--color-grey-900);
  color: white;
}

button.toggled:hover{
  background-color: var(--color-primary);
  border: 2px solid var(--color-primary);
}
</style>
