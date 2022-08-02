<template>
  <!-- <div class="followerbox"></div> -->
  <div class="grid-container">
    <div class="leftbox">
      <FollowBar class="leftbox"></FollowBar>
    </div>
    <div class="middlebox">
      <h1 class="name1">
        <div class="content"></div> {{ name }} </h1>
      <h2 class="image1">
      </h2>
      <h3 class="follower1">팔로워 {{ follower }}</h3>
      <h4 class="following1">팔로잉 {{ following }}</h4>
      <h5 class="info">
        <div class="content"> {{ information }}</div>
      </h5>
    </div>
    <div class="rightbox">
      <h6 class="usertext">
        <div class="usertext-sex1">
          성별:
        </div>
        <div class="usertext-sex2">
          <input id="input1" type="text" v-model="sex2">
        </div>
        <div class="usertext-height1">
          신장:
        </div>
        <div class="usertext-height2">
          <input id="input1" type="text" v-model="height2">
          <input id="input2" type="text" v-model="cm">
        </div>
        <div class="usertext-weight1">
          체중:
        </div>
        <div class="usertext-weight2">
          <input id="input1" type="text" v-model="weight2">
          <input id="input2" type="text" v-model="kg">
        </div>
        <div class="usertext-goal1">
          목표체중:
        </div>
        <div class="usertext-goal2">
          <input id="input1" type="text" v-model="goal2">
          <input id="input2" type="text" v-model="kg">
        </div>
        <div class="fatgraph"></div>
      </h6>
      <button @click="changeprofile" class="fixbutton">수정하기</button>
      <h7 class="chart">차트</h7>
    </div>
  </div>
</template>

<script>
import FollowBar from '../common/FollowBar.vue'
export default {
  components: {
    FollowBar
  },
  setup () {
    const name = '조경민'
    const follower = '150k'
    const following = '10'
    const profile = '프로필'
    const information = '#글자 #설명 #예시'
    const sex1 = '남'
    const height1 = '174.4'
    const weight1 = '85.5'
    const goal1 = '75.5'
    // const sex2 = '남'
    // const height2 = '174.4'
    // const weight2 = '85.5'
    // const goal2 = '75.5'
    const sex2 = sex1
    const height2 = height1
    const weight2 = weight1
    const goal2 = goal1
    const cm = 'cm'
    const kg = 'kg'
    return {
      name,
      follower,
      following,
      profile,
      information,
      sex2,
      height2,
      weight2,
      goal2,
      sex1,
      height1,
      weight1,
      goal1,
      cm,
      kg
    }
  },
  methods: {
    changeprofile: function () {
      this.sex1 = this.sex2
      this.height1 = this.height2
      this.weight1 = this.weight2
      this.goal1 = this.goal2
    }
  }
}
//   data () {
//     return {
//       name: '조경민',
//       follower: '150k',
//       following: '10',
//       information: '#글자 #설명 #예시',
//       sex2: '남',
//       height2: '174.4cm',
//       weight2: '85.5kg',
//       goal2: '75.5kg'
//     }
//   }
// }
// export default {
//   name: 'Profile',
//   computed: {
//     currentUser() {
//       return this.$store.state.auth.user;
//     }
//   },
//   mounted() {
//     if (!this.currentUser) {
//       this.$router.push('/login');
//     }
//   }
// };
</script>

<style>
.grid-container {
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 23% 35% 42%;
  /* grid-template-rows: 20% 40% 40%;  */
  column-gap: 10px;
  grid-template-areas:
    "leftbox middlebox rightbox"
}
.content{
  align-items: center;
  text-align: center;
  padding: 20px;
}
.leftbox{
  margin: 0;
}
.middlebox{
  left: 100px;
  align-items: center;
  text-align: center;
}
.rightbox{
  align-items: center;
  text-align: center;
}
.image1{
  width: 25vw;
  height: 50vh;
  margin-left: 110px;
  border: 5px solid ;
  border-radius: 50%;
  background: url(https://upload.wikimedia.org/wikipedia/commons/e/e8/Flag-map_of_the_world_%282018%29.png)
}
.name1{
  margin-left: 4vw;
  margin-top: 11vh;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 2rem;
}
.follower1{
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 20px;
  float: right;
  margin-right: 50px;

}
.following1{
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 20px;
  margin-right: 190px;
  float: right;

}
.info{
  align-items: center;
  text-align: center;
  width: 35vw;
  height: 10vh;
  margin-left: 50px;
  margin-top: 100px;
  top: 550px;
  left: 430px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  background: #FFF89C;
  border-radius: 50px;
  font-size: 20px;
}
.usertext{
  box-sizing: border-box;
  width: 35vw;
  height: 35vh;
  margin-top: 120px;
  background: #FFFFFF;
  border: 1px solid #EEEEEE;
  box-shadow: 13.21px 4.95px 15px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 3vh;
}
.chart{
  box-sizing: border-box;
  width: 30vw;
  height: 20vh;
  margin-top: 50px;
  margin-left: 70px;
  background: #FFFFFF;
  border: 1px solid #EEEEEE;
  box-shadow: 13.21px 4.95px 15px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  padding: 20px;
  float: left;
}
.usertext-sex1{
  box-sizing: border-box;
  width: 6vw;
  height: 3vh;
  margin-left: 1vw;
  margin-top: 6vh;
  float: left;
}
.usertext-sex2{
  box-sizing: border-box;
  width: 3vw;
  height: 3vh;
  margin-left: 1vw;
  margin-top: 6vh;
  float: left;
}
.usertext-height1{
  box-sizing: border-box;
  width: 6vw;
  height: 3vh;
  margin-left: 6vw;
  margin-top: 6vh;
  float:left;
}
.usertext-height2{
  box-sizing: border-box;
  width: 8vw;
  height: 3vh;
  margin-left: 3vw;
  margin-top: 6vh;
  float: left;
}
.usertext-weight1{
  box-sizing: border-box;
  width: 6vw;
  height: 3vh;
  margin-left: 1vw;
  margin-top: 6vh;
  float: left;
}
.usertext-weight2{
  box-sizing: border-box;
  width: 8vw;
  height: 3vh;
  margin-left: 1vw;
  margin-top: 6vh;
  float: left;
}
.usertext-goal1{
  box-sizing: border-box;
  width: 10vw;
  height: 3vh;
  left: 14vw;
  margin-top: 6vh;
  float: left;
}
.usertext-goal2{
  box-sizing: border-box;
  width: 8vw;
  height: 3vh;
  left: 21vw;
  margin-top: 6vh;
  float: left;
}
.fatgraph{
  width: 28vw;
  height: 7vh;
  margin-left: 3vw;
  margin-top: 25vh;
  background: black;
}
#input1 {
  width: 40px;
  height: 30px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 2.5vh;
  float: left;
}
#input2 {
  width: 30px;
  height: 30px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 2.5vh;
  float: left;
}
.fixbutton{
  margin-left: 240px;
  float: left;
  Width: 100px;
  Height: 40px;
  justify-content: center;
  align-items: center;
  padding: 2px 10px;
  gap: 10px;
  background: #6dcef5;
  border-radius: 25px;
  color: white;
}
button:hover {
  background-color: var(--color-grey-900);
  color: white;
}

@media (max-width: 768px){
  .image1{
    height: 0;
    width: 0;
    border: 0;
    margin-left: 0;
    margin-top: 0;
  }
  .usertext{
    width: 30vw;
    height: 30vh;
    left: 33vw;
    margin-left: 3vw;
    margin-top: 20vh;
  }
  .name1{
    margin-left: 43vw;
    margin-top: 10vh;
    font-family: 'MaruBuriOTF';
    font-style: normal;
    font-size: 2rem;
  }
  .follower1{
    margin-left: 54vw;
    margin-top: 75vh;
    font-family: 'MaruBuriOTF';
    font-style: normal;
    font-size: 1rem;
  }
  .following1{
    margin-left: 34vw;
    margin-top: 75vh;
    font-family: 'MaruBuriOTF';
    font-style: normal;
    font-size: 1rem;
  }
  .info{
    width: 35vw;
    height: 10vh;
    margin-left: 33vw;
    margin-top: 86vh;
    background: yellow;
    border-radius: 50px;
  }
  .chart{
    height: 0;
    width: 0;
    border: 0;
    margin-left: 0;
    margin-top: 0;
  }
}
</style>
