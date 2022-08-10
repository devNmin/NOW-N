<template>
    <div class="diary-item">
        <div id="image">
            이미지
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
    width: 450px;
    height: 180px;
    border-radius: 30px;
    display:grid;
    grid-template-columns: 30% 70%;
    background-color: #F9F9F9;
}

.diary-item #image{
    margin: auto;
}
</style>
