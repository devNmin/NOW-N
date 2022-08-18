<template>
  <div class="modal-background">
    <div class="modal2 open" >
              <div @click="toggleModal" class="modal-x-button"><i class="fa-solid fa-xmark"></i></div>
      <div class="counsel-modal-box">
        <div class="counsel-list-box">
           <CounselListItem
           v-for="( counsel_item, i ) in counselList"
           :key="i"
           :counselItem="counsel_item"
           @click="get1Detail (counsel_item.id, counsel_item.comment)"
           />
        </div>
        <div class="middle-bar"></div>
        <div class="counsel-detail-box">
          {{commentData.comment}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import { useStore } from 'vuex'
import { computed } from '@vue/runtime-core'
import CounselListItem from '@/components/counselting/client/counselListItem.vue'
export default {
  components: {
    CounselListItem
  },
  setup (props, { emit }) {
    const store = useStore()
    const commentData = reactive({
      comment: ''
    })
    const data = ref(computed(() => store.getters.currentTrainer))
    const counselList = ref(computed(() => store.getters.counselList))
    function toggleModal (event) {
      emit('toggleModal', false)
    }
    function get1Detail (target, comment) {
      commentData.comment = comment
      store.dispatch('getCounselDetail', target)
    }
    return {
      commentData,
      data,
      counselList,
      toggleModal,
      get1Detail
    }
  }
}
</script>

<style scope>
.modal-background {
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0;
  background: rgba(0, 0, 0, 0.8);
}
.modal2 {
  min-height: 315px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  position: relative;
  display: none;
  z-index: 200;
  top: 10%;
  left: 20%;
  width: 60%;
  height: 70%;
  background: white;
  border: 1px solid #6dcef5;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}
.counsel-modal-box {
  display: flex;
  position: relative;
  margin: 5%;
  width: 90%;
  height: 90%;
}
.open {
  display: block !important;
}
.counsel-list-box {
  width: 100%;
  height: 100%;

}

.middle-bar {
  height: 95%;
  width: 10px;
  background: #6dcef5;
}
.counsel-detail-box {
  width: 100%;
  height: 100%;
}
.modal-box {

  margin: 5%;
  width: 90%;
  height: 90%;
}
.modal-x-button {
  position: absolute;
  top: 3%;
  left: 92%;
}
</style>
