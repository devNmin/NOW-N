<template>
<div class="search-bar">
  <img class="search-icon" src="@\assets\search.png" alt="검색">
  <input type="text" class="search-input" placeholder="Search">
</div>
</template>

<script>
export default {

}
</script>

<style>
.search-bar {
  top: 500px !important;
  display: flex;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  background-color: none;
  color: #6dcef5;
  border: 0px;
  height: 40px;
  font-size: 7px;
  padding: 0px;
  margin: 0px;
  border-bottom: 2px solid #6dcef5;
}
.search-input {
  border: none;
}
.search-icon {
  background: none;
}
</style>
