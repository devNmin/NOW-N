<template>
  <div >
    <div class="middlebox">
      <div class="userName"> {{ UserInfoP.name }} </div>
      <img class="userProfileImg" :src="UserInfoP.profile_url" alt="유저프로필URL">
      <!-- <input ref="image" id="input" type="file" name="image" accept="image/*" multiple="multiple" class="hidden" @change="uploadFile"> -->
      <div>
        <p class="follower1">Follower +{{ UserInfoP.follower }}</p>
        <p class="following1">Following +{{ UserInfoP.following }}</p>
      </div>
      <div class="userTextbox">
        <div class="userText">{{ UserInfoP.information }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { onMounted } from 'vue'
import { getStorage, uploadBytes, ref, getDownloadURL } from 'firebase/storage'
export default {
  components: {
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

.middlebox{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.userProfileImg{
  width: 25vw;
  height: 50vh;
  margin-left: 110px;
  border: 5px solid ;
  border-radius: 50%;
  /* background: url(https://upload.wikimedia.org/wikipedia/commons/e/e8/Flag-map_of_the_world_%282018%29.png) */
}
.userName{
  margin-left: 6.5vw;
  margin-top: 5vh;
  margin-bottom: 4vh;
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
.userTextbox{
  display: flex;
  margin-top: 10px;
  align-items: center;
  text-align: center;
  justify-content: center;
  width: 35vw;
  height: 10vh;

  background: #FEFCED;
  border-radius: 50px;
  font-size: 20px;
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

</style>
