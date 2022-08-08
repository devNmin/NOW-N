<template>
<button type="button" @click="makeModal">asdf</button>
  <div class="modal">
    <h1 class="modal-title">결제하시겠습니까?</h1>
    <div class="modal-actions">
      <a href="index.html" class="modal-action">예</a>
      <button class="modal-action modal-action--negative" type="button">
        아니오
      </button>
    </div>
  </div>
</template>

<script>
export default {
  setup () {
    function makeModal () {
      document.querySelector('.modal').classList.add('open')
    }
    return {
      makeModal
    }
  }

}
</script>

<style>
.modal {
  position: fixed;
  display: none;
  z-index: 200;
  top: 20%;
  left: 30%;
  width: 40%;
  height: 60%;
  background: white;
  padding: 1rem;
  border: 1px solid #6dcef5;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}

.modal-title {
  text-align: center;
  margin: 0 0 1rem 0;
}

.modal-actions {
  text-align: center;
}

.modal-action {
  border: 1px solid #0e4f1f;
  background: #0e4f1f;
  text-decoration: none;
  color: white;
  font: inherit;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.modal-action:hover,
.modal-action:active {
  background: #2ddf5c;
  border-color: #2ddf5c;
}

.modal-action--negative {
  background: red;
  border-color: red;
}
.open {
  display: block !important;
}
.modal-action--negative:hover,
.modal-action--negative:active {
  background: #ff5454;
  border-color: #ff5454;
}
</style>
