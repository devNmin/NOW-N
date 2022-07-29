<template>
    <div class="followbar">
        <div id="followbar-title">팔로우 중인 채널</div>
        <div class="followbar-container">
            <div class="fb-first"><img id="container-image" src="@/assets/logo.png" /></div>
            <div class="fb-second">
                <div class="fb-nickname">닉네임</div>
                <div class="fb-info">팔로워, 팔로우</div>
            </div>
        </div>
        <div id="followbar-title">추천 채널</div>
        <div class="followbar-container">
            <div class="fb-first"><img id="container-image" src="@/assets/logo.png" /></div>
            <div class="fb-second">
                <div class="fb-nickname">닉네임</div>
                <div class="fb-info">팔로워, 팔로우</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'FollowBarView',
  components: {
  },
  data () {
    return {
    }
  },
  setup () {},
  mounted () {},
  unmounted () {},
  methods: {}
}
</script>
<style scoped>

.followbar{
    background-color: #EFEFF1;
    width: 350px;
    height: 980px;
    position: absolute;
    top: 87.7px;
}

.followbar #followbar-title{
    font-size:20px;
    font-weight: bold;
    text-align: left;
    padding:5px;
}

.followbar-container{
    display:grid;
    height: 50px;
    grid-template-columns: 50px 300px;
}

.fb-first #container-image{
    height: 50px;
    align-content: center;
}

.fb-second{
    display:flex;
    flex-direction: column;
    border: none;
}

.fb-nickname{
    width: 100%;
    flex: 20;
    background-color: black;
}

.fb-info{
    width: 100%;
    flex: 4;
    background-color: white;
}
</style>
