<template>
  <div >
    <div class="middlebox">
      <div class="userName"> {{ UserInfoP.name }} </div>
      <div>
        <img class="userProfileImg" :src="UserInfoP.profile_url" alt="유저프로필URL">
        <!-- <input ref="image" id="input" type="file" name="image" accept="image/*" multiple="multiple" class="hidden" @change="uploadFile"> -->
        <div class="bbbbox">
            <div style="display:flex; justify-content:space-between; margin-bottom: 5px;">
              <p style="margin: 0;" >팔로워 +{{ UserInfoP.follower }}</p>
              <button type="button" @click="toggleModalInfo">내 정보</button>
            </div>
            <div style="display:flex; justify-content:space-between;">
              <p style="margin: 0;" >팔로잉 +{{ UserInfoP.following }}</p>
              <button type="button" @click="toggleModalChart" >운동 그래프</button>
            </div>
        </div>
      </div>
      <div class="userTextbox">
        <div class="userText">{{ UserInfoP.information }}</div>
      </div>
    </div>
  </div>
  <div class="modalMyInfo">
    <div class="modal-box">
      <h1 >{{ UserInfoP.name }}</h1>
      <div @click="toggleModalInfo" class="modal-x-button"><i class="fa-solid fa-xmark"></i></div>
      <div class="MyInfoText">
        <div style="display: flex; justify-content: space-between;">
          <div>성별</div>
          <div>{{UserInfoP.sex}}</div>
          <div>신장</div>
          <div>{{UserInfoP.height}}</div>
        </div>
        <div style="display: flex; justify-content: space-between;">
          <div>체중</div>
          <div>{{UserInfoP.weight}}</div>
          <div>목표체중</div>
          <div>{{UserInfoP.weight2}}</div>
        </div>
      <i class="fa-solid fa-xmark bmiIcon" id="bmiId"></i>
      <div style="display: flex; height: 20%;">BMI
        <div class="box1"></div>
        <div class="box2"></div>
        <div class="box3"></div>
        <div class="box4"></div>
      </div>
    </div>
    <div  class="Modbutton">수정하기</div>
    </div>
  </div>
  <div class="modalChart">
    <div class="radarBox">
      <div class="modal-name-box"></div>
      <div @click="toggleModalChart" class="modal-x-button"><i class="fa-solid fa-xmark"></i></div>
      <RadarChart class="radarStyle"></RadarChart>
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
      // bmiTag.style.left = `${bmiData}` + 'px'
      bmiTag.style.setProperty('left', bmiData * 2 + '%')
    }

    )
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
      console.log('toggle')
      const aa = document.querySelector('.modalMyInfo')
      console.log(aa)
      document.querySelector('.modalMyInfo').classList.toggle('open')
    }
    function toggleModalChart () {
      console.log('toggle')
      const aa = document.querySelector('.modalChart')
      console.log(aa)
      document.querySelector('.modalChart').classList.toggle('open')
    }
    return {
      uploadFile, UserInfoP, toggleModalInfo, toggleModalChart
    }
  }
}
</script>

<style>
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
  background-color: blue;
}
.box2 {
  width: 15%;
  background-color: green;
}
.box3 {
  width: 10%;
  background-color: orange;
}
.box4 {
  width: 48%;
  background-color: red;
}

.MyInfoText {
  display: flex;
  flex-direction: column;
  margin-top: 50px;
  margin-left: 20px;
  margin-right: 20px;
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
  left: 95%;
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
  left: 35%;
  width: 30%;
  height: 40%;
  background: #FEFCED;
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

button{
  /* background-color: var(--color-grey-900); */
  color: #6dcef5;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;

  text-align: center;
  font-weight: bold;
}

.bbbbox {
  position:relative;
  bottom: 50px;
  right: 6px;
  flex-direction: column;
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
  /* background: url(https://upload.wikimedia.org/wikipedia/commons/e/e8/Flag-map_of_the_world_%282018%29.png) */
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

  background: #FEFCED;
  border-radius: 50px;
  font-size: 20px;
}
</style>
