<template>
  <div class="input-container">
    <input
    :type="type"
    :value="modelValue"
    :placeholder="placeholder"
    @input="updateInput"
    />
  </div>
</template>

<script>

export default {
  props: {
    modelValue: {
      type: [String, Number],
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'text'
    }
  },
  methods: {
    updateInput (event) {
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style>

.input-container{
  display: inline-block;
  flex-direction: column;
  gap: 8px;
}
input {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  background-color: white;
  color: black;
  border-color: #6dcef5;
  border: solid 2px #6dcef5;
  border-radius: 8px;
  width: 340px;
  height: 50px;
  font-size: 25px;
  padding-left: 20px;
}
input:hover{
  border-bottom: 2px solid var(--color-primary);
}
input:focus{
  outline: none;
  border-bottom: 2px solid var(--color-primary);
}
.input::placeholder {
    color: #6dcef5;
}
</style>
