<template>
<<<<<<< HEAD
  <label for="input-box" class="label-box">{{label}}
  </label>
=======
  <h5 for="input-box" class="label-box">{{label}}</h5>
  <!-- <label for="input-box" class="label-box">{{label}}
  </label> -->
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  <input
  class="input-box"
  :label="label"
  :type="type"
  :value="modelValue"
  @input="updateInput"
  />
  <div class="error-box" v-if="authError">{{authError["user.password"]}}
  </div>

</template>

<script>

export default {
  props: {
    modelValue: {
      type: [String, Number],
      default: ''
    },
    value: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'text'
    },
    label: {
      type: String,
      default: ''
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
.input-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
<<<<<<< HEAD
  background-color: none;
=======
  background-color: #EEEEEE;
>>>>>>> 6e30b2d743e6e8a45fc6337f56e11abda909bc48
  border-bottom: solid 2px #6dcef5;
  border-radius: 2px;
  width: 300px;
  height: 45px;
  margin: auto;
  font-size: 20px;
  padding-left: 20px;
  padding: 0px;
}
.input-box:hover {
  border-bottom: 2px solid var(--color-primary);
}
.input-box:focus {
  outline: none;
  border-bottom: 2px solid var(--color-primary);
}
.label-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 20px;
  text-align: left;
  width: 300px;
  height: 20px;
  margin: auto;
}
.error-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 10px;
  color: red;
  text-align: left;
  width: 300px;
  height: 20px;
  margin: auto;
}
</style>
