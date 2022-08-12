<template>
    <div class="diary-item">
        <div id="image">
        </div>
        <div id="info">
            <h1>아침</h1>
            <h3>오전 7:30 - 500kcal</h3>
            <h3>소스 안뿌리고 먹었습니다</h3>
        </div>
    </div>
</template>

<script>

export default {
}
</script>

<style scoped>
.diary-item{
    width: 500px;
    height: 180px;
    border-radius: 30px;
    display:grid;
    grid-template-columns: 30% 70%;
    background-color: #F9F9F9;
    padding: 20px;
}

.diary-item #image{
    background-color:#6DCEF5;
    margin: 20px 0px 0px 0px;
    height:80%;
    width:80%;
}
</style>
