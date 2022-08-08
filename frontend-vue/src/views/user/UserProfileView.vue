<template>
  <BaseHeader ></BaseHeader>
  <div class="grid-container">
    <div class="leftbox">
      <FollowBar ></FollowBar>
    </div>
    <div class="middlebox">
      <div class="name1 content">
        {{ UserInfoP.name }}
      </div>
      <img class="image1" :src="UserInfoP.profile_url" alt="유저프로필URL">
      <input ref="image" id="input" type="file" name="image" accept="image/*" multiple="multiple" class="hidden" @change="uploadFile">
      <div>
        <div class="follower1">Follower {{ UserInfoP.Follower }}</div>
        <div class="following1">Following {{ UserInfoP.Following }}</div>
      </div>
      <div class="infobox content"> {{ UserInfoP.information }}</div>
    </div>
    <div class="rightbox">
      <div>
        <div class="upperbox">
          <div class="upperbox1">
            <div class=""> 성별: {{UserInfoP.sex1}} </div>
            <div class="">  신장: {{UserInfoP.height1}} cm</div>
          </div>
          <div class="upperbox2"></div>
            <div class="">
              체중: {{UserInfoP.weight1}} kg
            </div>
            <div class="">
              목표체중: {{UserInfoP.goal1}} kg
            </div>
          <button class="fixbutton">수정하기</button>
        </div>
        <div class="downbox">
          <RadarChart ></RadarChart>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BaseHeader from '@/components/common/BaseHeader.vue'
import FollowBar from '@/components/common/FollowBar.vue'
import { useStore } from 'vuex'
import { onMounted } from 'vue'
import { getStorage, uploadBytes, ref, getDownloadURL } from 'firebase/storage'
import RadarChart from '@/components/user/RadarChart.vue'
export default {
  components: {
    BaseHeader, FollowBar, RadarChart
  },
  setup () {
    const store = useStore()
    const UserInfoP = store.state.profile.UserInfo
    onMounted(() => {
      console.log(UserInfoP)
      const storage = getStorage()
      getDownloadURL(ref(storage, UserInfoP.name))
        .then((url) => {
          console.log('org', url)
          // `url` is the download URL for 'images/stars.jpg'
          UserInfoP.profile_url = url
        })
    })
    const uploadFile = (e) => {
      const storage = getStorage()
      const file = e.target.files[0]
      console.log(file)
      const storageRef = ref(storage, UserInfoP.name)
      uploadBytes(storageRef, file).then(() => {
        console.log('Uploaded a blob or file!')
      })
    }

    return {
      uploadFile, UserInfoP
    }
  }
}
</script>

<style>
.grid-container {
  /* height: 1500px;
  width: 1600px; */
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 15% 42% 43%;
  /* grid-template-rows: 20% 40% 40%;  */
  column-gap: 10px;
  grid-template-areas:
    "leftbox middlebox rightbox"
}
.grid-container2 {
  display: grid;
  grid-template-rows: 50% 50%;
  column-gap: 10px;
  grid-template-areas:
    "upperbox downbox"
}
.grid-container3 {
  display: grid;
  grid-template-rows: 33% 33% 33%;
  grid-template-areas:
    "upperbox1 upperbox2 upperbox3"
}
.content{
  align-items: center;
  text-align: center;

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
  /* background: url(https://upload.wikimedia.org/wikipedia/commons/e/e8/Flag-map_of_the_world_%282018%29.png) */
}
.name1{
  margin-left: 6.5vw;
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
  margin-right: 0px;

}
.following1{
  font-style: normal;
  font-size: 20px;
  margin-right: 230px;
  float: right;

}
.infobox{
  align-items: center;
  text-align: center;
  width: 35vw;
  height: 10vh;

  background: #FEFCED;
  border-radius: 50px;
  font-size: 20px;
}
.usertext{
  box-sizing: border-box;
  width: 35vw;
  height: 35vh;

  background: #FFFFFF;
  border: 1px solid #EEEEEE;
  box-shadow: 13.21px 4.95px 15px rgba(0, 0, 0, 0.25);
  border-radius: 30px;

  font-size: 3vh;
}
.chart{
  box-sizing: border-box;
  width: 30vw;
  height: 20vh;

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
  float: right;
  Width: 100px;
  Height: 40px;
  justify-content: center;
  align-items: center;
  padding: 2px 10px;
  gap: 10px;
  background: #6dcef5;
  border-radius: 25px;
  color: white;
  border-width: 0;
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
}
</style>
