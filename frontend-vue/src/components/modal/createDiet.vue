<template>
    <div class="create-diet">
        <div class="regist-diet-container">
            <div class="diet-img">
                <label for="img">
                  <img class="food-img" :src="DietInfo.food_url" alt="식단 사진">
                </label>
                <input type="file" style="visibility:hidden;" id="img" multiple="multiple" @change="uploadFile">
            </div>
            <fieldset class="diet-moment">
                <legend>분 류</legend>
                <div class="radio" v-for="item in options" :key="item.value">
                    <input type="radio" name="radio" :value="item.value" v-model="DietInfo.moment" :id="item.id"/>
                    <label :for="item.id">{{item.value}}</label>
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

            <fieldset class="diet-category">
                <legend>음식 종류</legend>
            </fieldset>

        <div class="diet-button">
        <button type="button" @click="regist">추가하기</button>
        <button type="button" @click="moveToDietDiary">취소</button>
        <button type="button" @click="test">test</button>
        </div>
        </div>
    </div>
</template>

<script>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { getStorage, uploadBytes, ref, listAll, getDownloadURL } from 'firebase/storage'
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
    const DietInfo = reactive({
      moment: '아침',
      time: new Date(),
      picture: 'https://ibb.co/qg4XZZP',
      comment: '',
      food_url: require('@/assets/food4.jpg')
    })

    const options = [
      { id: '아침', value: '아침' },
      { id: '점심', value: '점심' },
      { id: '저녁', value: '저녁' },
      { id: '간식', value: '간식' },
      { id: '야식', value: '야식' }
    ]

    const time = reactive({
      meridiem: [
        { text: 'A.M', value: 0 },
        { text: 'P.M', value: 12 }
      ],
      hour: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
      minute: ['0', '10', '20', '30', '40', '50']
    })
    const test = () => {
      const listRef = ref(storage)

      // Find all the prefixes and items.
      listAll(listRef)
        .then((res) => {
          res.prefixes.forEach((folderRef) => {
            console.log('folderRef', folderRef)
            // All the prefixes under listRef.
            // You may call listAll() recursively on them.
          })
          res.items.forEach((itemRef) => {
            console.log('itemRef', itemRef)
            // All the items under listRef.
          })
        })
    }
    const uploadFile = (e) => {
      const file = e.target.files[0]
      // 현재 모멘트 개수 +1 해서 추가해줘야함
      const saveName = 'foods/' + localStorage.getItem('userPk') + '_' + DietInfo.moment
      const storageRef = ref(storage, saveName)
      uploadBytes(storageRef, file).then(() => {
        console.log('Uploaded a blob or file!')
        getDownloadURL(ref(storage, saveName))
          .then((url) => {
            DietInfo.food_url = url
          })
      })
    }

    async function regist () {
      const userPk = store.state.accounts.currentUserPk
      await store.dispatch('getDietList', userPk, DietInfo)
      router.push({ name: 'pxDiaries' })
    }

    function moveToDietDiary () {
      router.push({ name: 'pxDiaries' })
    }
    return { DietInfo, regist, moveToDietDiary, options, uploadFile, time, test }
  }
}
</script>

<style scoped>
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
    "diet-img diet-img"
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
    width:30%;
    margin: auto;
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
}

.diet-button{
  grid-area: diet-button;
  display: flex;
  justify-content: flex-end;
  gap: 50px;
}

.diet-moment .radio label {
  font-size: 18px;
  background: #fff;
  border: 1px solid #ddd;
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  cursor: pointer;
  color: #444;
  transition: box-shadow 400ms ease;
}
.diet-moment .radio label:hover {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
}
.diet-moment .radio input[type=radio] {
  display: none;
}
.diet-moment .radio input[type=radio]:checked + label {
  background: #2196F3;
  color: #fff;
  border-color: #2196F3;
}
</style>
