<template>
  <form @submit.prevent="search(data.searchValue)">
    <div class="search">
      <input id="searchId" type="text" v-model="data.searchValue" @change="onChange" class="search-input" placeholder="Search">
      <label for="searchId"><img class="search-icon" src="@\assets\search.png" alt="검색"></label>
    </div>
  </form>
</template>

<script>
export default {
  setup (props, { emit }) {
    const data = {
      searchValue: ''
    }
    function search () {
      emit('search', data.searchValue)
    }
    return {
      data,
      search
    }
  }

}
</script>

<style>
.search{
  display: flex;
  justify-content: center;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  box-sizing: border-box;
  background: #FFFFFF;
  border: 1px solid #6DCEF5;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  width: 250px;
  height: 30px;
  float: left;
}
.search-input {
  position: relative;
  top: 0px;
  left: 0px;
  padding: 0px;
  height: 100%;
  border: none;
  outline: none;
}
.search-icon {
  height: 30px;
  width: 30px;
  background: none;
}
.search-icon:hover {
  cursor: pointer;
}
</style>
