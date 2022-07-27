<template>
  <div class="input-container" :class="{readonly}">
    <div v-if="label" class="label">
      {{label}}
    </div>
    <input :type="password? 'password' : 'text'"
    v-model="inputValue"
    :placeholder="placeholder"
    :readonly="readonly"
    @change="onKeyup"
    @keyup.enter="onEnter"
    />
  </div>
</template>

<script>

export default {
  props: {
    value: {
      type: [String, Number],
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    },
    label: {
      type: String,
      default: ''
    },
    password: {
      type: Boolean,
      default: false
    },
    readonly: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    value: {
      immediate: true,
      handler (val) {
        this.inputValue = val
      }
    }
  },
  setup () {
    const inputValue = ''

    const onKeyup = () => {
      this.$emit('input', this.inputValue)
    }

    const onEnter = () => {
      this.$emit('enter')
    }

    return { inputValue, onKeyup, onEnter }
  }
}
</script>

<style>

.input-container{
  display: flex;
  flex-direction: column;
  gap: 8px;
}
input {
  font-family: 'MaruBuriOTF';
  font-style: normal;
  /* margin-top: 60px; */
  background-color: white;
  color: black;
  border-color: #6dcef5;
  border: solid 2px #6dcef5;
  border-radius: 8px;
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

.input-container.readonly input {
  color: var(--color-grey-300);
  border-bottom: 2px solid var(--color-grey-300);
}

.input-container.readonly input:hover,
.input-container.readonly input:focus {
  border-bottom: 2px solid var(--color-grey-300);
}
</style>
