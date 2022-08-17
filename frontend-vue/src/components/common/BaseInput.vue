<template>
  <h5 for="input-box" class="label-box">{{label}}</h5>
  <!-- <label for="input-box" class="label-box">{{label}}
  </label> -->
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

<style scope>
.input-box {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  color: black;
  border: 0px;
  background-color: none;
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
  border-bottom: 2px solid #57b0d4;
}
.input-box:focus {
  outline: none;
  border-bottom: 2px solid #57b0d4;
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
  color: #6dcef5;
  text-align: left;
  width: 300px;
  height: 20px;
  margin: auto;
}
</style>
