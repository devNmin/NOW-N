<template>
  <!-- <div class="followerbox"></div> -->
  <div class="grid-container">
    <FollowBar class="leftbox"></FollowBar>
    <div class="middlebox">
      <div>
        <h1 class="name1">
          <div class="content"></div> {{ name }} </h1>
        <!-- <h1 class="name1"> {{ currentUser.username }} </h1> -->
        <h2 class="image1"></h2>
        <h3 class="follower1">팔로워 {{ follower }}</h3>
        <!-- <h3 class="follower1">팔로워 {{ currentUser.follower }}</h3> -->
        <h4 class="following1">팔로잉 {{ following }}</h4>
        <!-- <h4 class="following1">팔로잉 {{ currentUser.following }}</h4> -->
        <h5 class="info">
          <div class="content"> {{ information }}</div>
          <!-- <div> {{ currentUser.information }}</div> -->
        </h5>
      </div>
    </div>
    <div class="rightbox">
        <h6 class="usertext">
          <div> 프로필 </div>
          <div class="usertext-sex1">
            성별
          </div>
          <div class="usertext-sex2">
            {{ sex2 }}
            <!-- {{ currentUser.sex }} -->
          </div>
          <div class="usertext-height1">
            신장
          </div>
          <div class="usertext-height2">
            {{ height2 }}
            <!-- {{ currentUser.height }} -->
          </div>
          <div class="usertext-weight1">
            체중
          </div>
          <div class="usertext-weight2">
            {{ weight2 }}
            <!-- {{ currentUser.weight }} -->
          </div>
          <div class="usertext-goal1">
            목표체중
          </div>
          <div class="usertext-goal2">
            {{ goal2 }}
            <!-- {{ currentUser.goal }} -->
          </div>
          <div class="fatgraph"></div>
        </h6>
        <h7 class="chart">차트</h7>
    </div>
  </div>
</template>

<script>
import FollowBar from '../common/FollowBar.vue'
// import { mapGetters } from 'vuex'
export default {
  components: {
    FollowBar
  },
  // computed: {
  //   ...mapGetters([
  //     'currentUser'
  //   ])
  // },
  setup () {
    const name = '박승주'
    const follower = '150k'
    const following = '10'
    const profile = '프로필'
    const information = '#글자 #설명 #예시'
    return {
      name,
      follower,
      following,
      profile,
      information
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
  display: grid;
  grid-template-columns: 350px 600px 600px;
  column-gap: 50px;
  grid-template-areas:
    "leftbox middlebox rightbox"
}
.content{
  /* display: flex; */
  align-items: center;
  text-align: center;
  /* position: absolute; */
  margin: auto;
}
.leftbox{
  margin: auto
}
.middlebox{
  left: 100px;
  display: flex;
  align-items: center;
  text-align: center;
  /* margin-left: 300px; */
}
.rightbox{
  display: flex;
  align-items: center;
  text-align: center;
  /* margin-left: 50px; */
}
.image1{
  /* display: flex; */
  align-items: center;
  position: absolute;
  width: 25vw;
  height: 50vh;
  top: 150px;
  left: 500px;
  /* margin-left: 13vw; */
  /* margin-top: 23vh; */
  border: 5px solid ;
  border-radius: 50%;
  background: url(https://upload.wikimedia.org/wikipedia/commons/e/e8/Flag-map_of_the_world_%282018%29.png)
}
.name1{
  /* display: flex; */
  align-items: center;
  top: 13vh;
  position: absolute;
  margin-left: 10vw;
  /* margin-top: 11vh; */
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 2rem;
  left: 500px;
}
.follower1{
  position: absolute;
  margin-left: 20vw;
  /* margin-top: 80vh; */
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 1rem;
  top: 530px;
  left: 510px;
}
.following1{
  position: absolute;
  margin-left: 3vw;
  left: 450px;
  /* margin-top: 80vh; */
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 1rem;
  top: 530px;
}
.info{
  display: flex;
  align-items: center;
  text-align: center;
  position: absolute;
  width: 35vw;
  height: 10vh;
  /* margin-left: 8vw; */
  /* margin-top: 86vh; */
  top: 550px;
  left: 430px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  background: #FFEB3B;
  border-radius: 50px;
  font-size: 3vh;
}
.usertext{
  box-sizing: border-box;
  position: absolute;
  width: 30vw;
  height: 35vh;
  /* margin-left: 60vw; */
  top: 13vh;
  left: 1030px;
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
  position: absolute;
  width: 30vw;
  height: 30vh;
  /* margin-left: 60vw; */
  top: 60vh;
  left: 1030px;
  background: #FFFFFF;
  border: 1px solid #EEEEEE;
  box-shadow: 13.21px 4.95px 15px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
}
.usertext-sex1{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 1vw;
  top: 6vh;
  /* font-size: 20px; */
}
.usertext-sex2{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 6vw;
  top: 6vh;
  /* font-size: 20px; */
}
.usertext-height1{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 13vw;
  top: 6vh;
  /* font-size: 20px; */
}
.usertext-height2{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 20vw;
  top: 6vh;
  /* font-size: 20px; */
}
.usertext-weight1{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 1vw;
  top: 16vh;
  /* font-size: 20px; */
}
.usertext-weight2{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 6vw;
  top: 16vh;
  /* font-size: 20px; */
}
.usertext-goal1{
  box-sizing: border-box;
  position: absolute;
  width: 6vw;
  height: 3vh;
  left: 13vw;
  top: 16vh;
  /* font-size: 20px; */
}
.usertext-goal2{
  box-sizing: border-box;
  position: absolute;
  width: 3vw;
  height: 3vh;
  left: 20vw;
  top: 16vh;
  /* font-size: 20px; */
}
.fatgraph{
  position: absolute;
  width: 24vw;
  height: 6vh;
  left: 3vw;
  top: 25vh;
  background: black;
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
