<template>
  <main :class="{ background }">
    <router-view />
  </main>
</template>

<script>

export default {
  components: {
  }
}
</script>
<style>
:root {
  --color-primary: #198d4d;
  --color-danger: #c72e23;
  --color-gold: gold;
  --color-silver: silver;
  --color-bronze: #c05828;
  --color-grey-100: #dee1e7;
  --color-grey-300: #c0c5d1;
  --color-grey-500: #757880;
  --color-grey-700: #575a5f;
  --color-grey-900: #2e3033;

  --header-height: 1rem;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  text-align: center;
}

main {
  min-height: calc(100vh - var(--footer-height));
  width: 100vw;
}
main.background {
  background-size: cover;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin-top: var(--header-height);
  padding: 64px;
  box-sizing: border-box;
}

.container-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

v-application{
  font-family: 'MaruBuri';
}
</style>
