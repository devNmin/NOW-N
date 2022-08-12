<template>
  <div>
  <div class="middlebox">
      <div class="userName"> {{ UserInfoP.name }}<img src="@/assets/info_icon.png" @click="toggleModalInfo" style="margin-left: 10px; vertical-align:middle;" alt="123" width="35"> </div>
        <label for="img">
          <img class="userProfileImg" :src="UserInfoP.profile_url" alt="유저프로필URL">
        </label>
        <input type="file" style="visibility:hidden;" id="img" multiple="multiple" @change="uploadFile">
        <div style="display:flex; justify-content: space-between; ">
          <div style="display:flex;margin-top:-65px; margin-left:480px; font-weight: bolder; ">
            <div>
              <div style="margin: 0;" >팔로워</div><div style="text-align:center;"> {{ UserInfoP.follower }}</div>
            </div>
            <div style="margin-left:20px;">
              <div style="margin: 0;" >팔로잉</div><div style="text-align:center;"> {{ UserInfoP.following }}</div>
            </div>
          </div>
        </div>
      <div class="userTextbox" style="margin-top:1px">
        <div class="userText">{{ UserInfoP.information }}</div>
      </div>
      <button type="button" class='graphBtn' @click="toggleModalChart" ><img src="@/assets/radar_icon2.png" style="margin:auto;" width="40" alt="그래프아이콘"><div style="margin:auto;">운동 그래프</div></button>
    </div>
  <div class="modal__background">
  <div class="modalMyInfo">
    <div class="modalBox">
      <div style="display:flex;"><h1 >{{ UserInfoP.name }}</h1><img src="@/assets/boy.png" alt="성별아이콘" width="40" height="40" style="display:flex; margin-left:20px;margin-top:20px; "></div>
      <div @click="toggleModalInfo" class="modal-x-button"><i class="fa-solid fa-xmark"></i></div>
      <div class="MyInfoText">
        <div style="display: flex; justify-content: space-between; margin-bottom:10px">
          <div>신장 </div>
          <div>{{UserInfoP.height}} cm</div>
          <div>체중</div>
          <div>{{UserInfoP.weight}} kg</div>
        </div>
      <img src="@/assets/run.png" class="bmiIcon" style="width: 5%; height:5%" id="bmiId">
      <div style=" display: flex; height: 20%; margin-top:2px; ">
        <div>&nbsp;</div>
        <div class="box1"></div>
        <div class="box2"></div>
        <div class="box3"></div>
        <div class="box4"></div>
      </div>
      <div style="text-align: right; font-size:10px; margin-top:2px;">체질량지수:{{(UserInfoP.weight / ((UserInfoP.height / 100) * (UserInfoP.height / 100))).toFixed(2)}}</div>
        <div style=" display: flex; justify-content: space-between; " >
          <div style="margin-top:20px">목표체중 {{UserInfoP.weight2}} kg </div>
          <div style="margin-top:20px"> {{UserInfoP.weight - UserInfoP.weight2}} kg </div>
        </div>
    </div>
      <img src="@/assets/edit_icon.png" width="25" alt="" class="Modbutton">
    </div>
  </div>
  </div>
  <div class="modalChart">
    <div class="radarBox">
      <div class="modal-name-box"></div>
      <div @click="toggleModalChart" class="modal-x-button"><i class="fa-solid fa-xmark"></i></div>
      <RadarChart class="radarStyle"></RadarChart>
    </div>
  </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { onMounted } from 'vue'
import { getStorage, uploadBytes, ref, getDownloadURL } from 'firebase/storage'
import RadarChart from '../../components/user/RadarChart.vue'

export default {
  components: {
    RadarChart
  },
  setup () {
    const store = useStore()
    const UserInfoP = store.state.profile.UserInfo
    console.log(UserInfoP)
    onMounted(() => {
      console.log(UserInfoP)
      const storage = getStorage()
      getDownloadURL(ref(storage, UserInfoP.name))
        .then((url) => {
          console.log('org', url)
          // `url` is the download URL for 'images/stars.jpg'
          UserInfoP.profile_url = url
        })
      const bmiTag = document.getElementById('bmiId')
      console.log('bmiTagbmiTag', bmiTag)
      const bmiData = UserInfoP.weight / ((UserInfoP.height / 100) * (UserInfoP.height / 100))
      bmiTag.style.setProperty('left', (bmiData * 2) + 10 + '%')
    }
    )
    const clickImg = (e) => {
      console.log('클릭')
      const file = e.target.files[0]
      console.log(file)
    }
    const uploadFile = (e) => {
      const storage = getStorage()
      const file = e.target.files[0]
      console.log(file)
      const storageRef = ref(storage, UserInfoP.name)
      uploadBytes(storageRef, file).then(() => {
        console.log('Uploaded a blob or file!')
      })
    }
    function toggleModalInfo () {
      document.querySelector('.modalMyInfo').classList.toggle('open')
      document.querySelector('.modal__background').classList.toggle('open')
    }
    function toggleModalChart () {
      document.querySelector('.modalChart').classList.toggle('open')
      document.querySelector('.modal__background').classList.toggle('open')
    }
    return {
      uploadFile, UserInfoP, toggleModalInfo, toggleModalChart, clickImg
    }
  }
}
</script>

<style>
.modalBox{
  margin-left: 20px;
  margin-right: 20px;
}
.modal__background{
  display: none;
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0; z-index: 0;
  background: rgba(0, 0, 0, 0.65);
}

.radarBox {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top:30px;
}
.radarStyle{

  width: 500px;
  height: 500px;
}
.bmiIcon {
  position:relative;
}
.box1 {
  width: 37%;
  background-color: rgb(147, 180, 215);
  border-radius: 15px 0% 0% 15px;
}
.box2 {
  width: 15%;
  background-color: rgb(142,198,159)
}
.box3 {
  width: 10%;
  background-color: rgb(231,152,95);
}
.box4 {
  width: 48%;
  background-color: rgb(214,93,92);
  border-radius: 0 15px 15px 0;
}

.MyInfoText {
  display: flex;
  flex-direction: column;
  margin-top: 25px;
  font-size: 20px;
  font-weight: bolder;
}
.open {
  display: block !important;
}
.modal-x-button {
  position: absolute;
  top: 3%;
  left: 95%;
}
.Modbutton {
  position: absolute;
  bottom: 3%;
  left: 93%;
}
.modalMyInfo {
  min-height: 315px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  position: fixed;
  display: none;
  z-index: 200;
  top: 30%;
  left: 37.5%;
  width: 25%;
  height: 35%;
  background-color: rgba( 191, 229, 255, 0.95 );
  /* background-color: rgba( 191, 229, 255, 0.7 ); */
  /* background-color: rgba(109, 188, 230, 0.99); */
  /* background-color: rgba(191, 239, 255, 1); */
  border: 1px solid #6dcef5;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}
.modalChart {
  min-height: 315px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  position: fixed;
  display: none;
  z-index: 200;
  top: 20%;
  left: 30%;
  width: 40%;
  height: 60%;
  background: white;
  border: 1px solid #a1c6d4;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}

.graphBtn{
  display: flex;
  justify-items: center;
  color: #6dcef5;
  margin-top:20px;
  width: 250px;
  height: 50px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  font-size: 25px;
  text-align: center;
  font-weight: bolder;
}
.middlebox{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.userProfileImg{
  width: 25vw;
  height: 50vh;
  margin: auto;
  border: 5px solid ;
  border-radius: 50%;
}
.userName{
  margin: auto;
  margin-bottom: 4vh;
  margin-top: 5vh;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  font-size: 2rem;
}
.userTextbox{
  display: flex;
  margin-top: -30px;
  align-items: center;
  text-align: center;
  justify-content: center;
  width: 35vw;
  height: 10vh;
  background-color: rgba( 191, 229, 255, 0.4 );
  border-radius: 50px;
  font-size: 20px;
}
</style>
