<template>
<div class="search">
  <input id="searchId" type="text" class="search-input" placeholder="Search">
  <label for="searchId"><img class="search-icon" src="@\assets\search.png" alt="검색"></label>
</div>
</template>

<script>
export default {

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
  border: 1px solid #000000;
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
