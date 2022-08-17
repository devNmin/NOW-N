<template>
  <div class="create-diet">
    <div class="regist-diet-container">
      <div class="diet-img" v-if="state.AIFlag">
        <label for="img" >
          AI<img class="food-img" :src="DietInfo.picture" alt="AI사진">
        </label>
        <input type="file" style="visibility:hidden;" id="img" multiple="multiple" @change="uploadFile">
        <button @click="AIFlagBtn">기본</button>
      </div>
      <div class="diet-img" v-else>
        <label for="img" >
          기본<img class="food-img" :src="DietInfo.picture" alt="AI사진">
        </label>
        <input type="file" style="visibility:hidden;" id="img" multiple="multiple" @change="uploadFile">
        <button @click="AIFlagBtn">AI모드</button>
      </div>
      <div>
        <fieldset class="food-search">
          <legend>음식 검색</legend>
          <div class="search">
            <input id="searchId" type="text" v-model="searchFoodname"  class="search-input" placeholder="음식이름을 입력하세요"><button @click="onClick(searchFoodname)">검색</button>
          </div>
          <div v-for=" item in state.searchData2" :key="item" :value="item">
            <div>{{item.name}} / <input id='gramId' type="text" v-model="testData" size="3" placeholder=''> g <button @click="addClick(item.name,testData)">추가</button> </div>
          </div>
        </fieldset>
      </div>
      <fieldset class="diet-moment">
          <legend>분 류</legend>
          <div v-for="item in options" :key="item.value" style="margin-top:7px">
              <label>
              <input type="radio" v-model="DietInfo.moment" :value="item.value" />
              {{item.text}}
              </label>
          </div>
      </fieldset>

      <fieldset class="diet-time">
          <legend>식사 시간</legend>
          <select>
            <option v-for="mer in time.meridiem" :key="mer.value" :value="mer.value">{{mer.text}}</option>
          </select>
          <select>
            <option v-for="h in time.hour" :key="h" :value="h">{{h}}시</option>
          </select>
          <select>
            <option v-for="m in time.minute" :key="m" :value="m">{{m}}분</option>
          </select>
      </fieldset>

      <fieldset class="diet-comment">
          <legend>Comment</legend>
          <input type="text" v-model="DietInfo.commet" style="width:98%; height:90%; font-size:25px;"/>
      </fieldset>

      <fieldset class="diet-category" >
          <legend>음식 종류</legend>
          <div style="text-align: center;" v-for=" (item, i) in DietInfo.foods" :key="i" :value="item">
          <div>{{DietInfo.foods[i].foodName}}<button @click="DeleteFoodList(i)">삭제</button></div>
          <div style="display:flex; justify-content:center;">{{DietInfo.foods[i].foodgram}}kcal</div>
          </div>
      </fieldset>
      <div class="diet-button">
        <button type="button" @click="regist">추가하기</button>
        <button type="button" @click="moveToDietDiary">취소</button>
      </div>
    </div>
  </div>
</template>

<script>
import { onUpdated, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { getStorage, uploadBytes, ref, getDownloadURL } from 'firebase/storage'
import axios from 'axios'
export default {
  porps: {
    diary_pk: {
      type: Number
    }
  },
  setup (props) {
    const store = useStore()
    const router = useRouter()
    const storage = getStorage()
    const searchFoodname = ''
    const DietInfo = reactive({
      userID: store.state.accounts.currentUserPk,
      moment: '아침',
      time: '1250AM',
      picture: require('@/assets/food4.jpg'),
      comment: 'test중',
      total_calorie: 153.7,
      foods: []
    })
    onUpdated(() => {
    })
    const state = reactive({ testBase: '', AIFlag: false, searchData2: [] })
    const testData = null
    function AIFlagBtn () {
      state.AIFlag = ~state.AIFlag
    }
    function addClick (foodName, foodgram) {
      if (DietInfo.foods.length < 6) {
        DietInfo.foods.push({ foodName, foodgram })
      }
    }
    function DeleteFoodList (i) {
      DietInfo.foods.splice(i, 1)
    }
    async function onClick (searchingItem) {
      // searchDietName
      await store.dispatch('searchDietName', searchingItem)
      state.searchData2 = store.state.diet.searchingLists
    }
    const options = [
      { text: '아침', value: '아침' },
      { text: '점심', value: '점심' },
      { text: '저녁', value: '저녁' },
      { text: '간식', value: '간식' },
      { text: '야식', value: '야식' }
    ]

    const time = reactive({
      meridiem: [
        { text: 'A.M', value: 'AM' },
        { text: 'P.M', value: 'PM' }
      ],
      hour: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
      minute: ['0', '10', '20', '30', '40', '50']
    })
    const test = () => {
      document.querySelector('.modal__background').classList.toggle('open')
    }
    const uploadFile = (e) => {
      const file = e.target.files[0]

      if (state.AIFlag) {
        const saveName = 'foods/' + localStorage.getItem('userPk') + '_' + DietInfo.moment
        const storageRef = ref(storage, saveName)
        uploadBytes(storageRef, file)
        const foodDetection = async () => {
          // const file = document.querySelector('#myfile').files[0]
          const formData = new FormData()
          formData.append('files', file)

          await axios({
            method: 'post',
            url: 'http://localhost:8001/detect_files',
            data: formData,
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }).then(res => {
            // DietInfo.picture
            DietInfo.picture = 'data:image/png;base64,' + `${res.data}`
          })
        }
        foodDetection()
      } else {
        const saveName = 'foods/' + localStorage.getItem('userPk') + '_' + DietInfo.moment
        const storageRef = ref(storage, saveName)
        uploadBytes(storageRef, file).then(() => {
          console.log('Uploaded a blob or file!')
          getDownloadURL(ref(storage, saveName))
            .then((url) => {
              DietInfo.picture = url
            })
        })
      }
    }
    function regist () {
      store.dispatch('createDiet', DietInfo)
      router.push({ name: 'pxDiaries' })
    }

    function moveToDietDiary () {
      router.push({ name: 'pxDiaries' })
    }
    return { searchFoodname, AIFlagBtn, state, DeleteFoodList, addClick, DietInfo, testData, onClick, regist, moveToDietDiary, options, uploadFile, time, test }
  }
}
</script>

<style scoped>
.modal__background{
  display: none;
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0; z-index: 0;
  background: rgba(0, 0, 0, 0.65);
}
.open {
  display: block !important;
}
.create-diet{
  height:100%;
  width: 100%;
  display:flex;
  justify-content: center;
  align-items: center;
}
.regist-diet-container{
    display:grid;
    gap:30px;
    width:50%;
    height:70%;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 3fr 1fr 1fr 1fr 0.3fr;
    grid-template-areas:
    "diet-img food-search"
    "diet-moment diet-moment"
    "diet-time diet-comment"
    "diet-category diet-category"
    ". diet-button";
    border: 5px solid #6dcef5;
    padding: 20px;
    border-radius: 15px;
}

.diet-img{
    grid-area: diet-img;
    Justify-content: center;
}

.food-img{
    display: flex;
    Justify-content: center;
    margin: auto;
    width:50%;
    height:70%;
    object-fit: fill;
    border-radius: 20px;
}

.diet-moment{
    grid-area: diet-moment;
    display: flex;
    Justify-content: center;
    gap: 45px;
    background-color: #EEEEEE;
}

.diet-time{
    grid-area: diet-time;
    background-color: #EEEEEE;
    display: flex;
    justify-content: center;
    gap: 50px;
}

.diet-comment{
    grid-area: diet-comment;
    background-color: #EEEEEE;
}

.diet-category{
    grid-area: diet-category;
    background-color: #EEEEEE;
    display:flex;
    margin-left:20px;
    align-items: center;
}

.diet-button{
  grid-area: diet-button;
  display: flex;
  justify-content: flex-end;
  gap: 50px;
}
</style>
