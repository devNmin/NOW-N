<template>
 <div></div>
</template>

<script>
import { useStore } from 'vuex'
export default {
  setup () {
    const store = useStore()
    const getCounselList = store.dispatch('getCounselList')
    const getCounselDetail = store.dispatch('getCounselDetail')
    return {
      getCounselList,
      getCounselDetail
    }
  }

}
</script>

<style>

</style>
