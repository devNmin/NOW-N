<template>
  <div class="GX-grid ">
    <div class="GXcommunityContent">
      <div id="mainWrapper">
        <ul>
          <!-- 게시판 제목 -->
          <div>
            <ul class="GXcommunitymenu" id="mainWrapper">
              <li class="item" @click="clickTest(1)"> 전체글보기</li>
              <li class="item" @click="clickTest(2)"> 공지사항</li>
              <li class="item" @click="clickTest(3)"> 자유게시판</li>
              <li class="item" @click="clickTest(4)"> Q&A 게시판</li>
            </ul>
          </div>
          <!-- 게시판 목록  -->
          <li>
              <ul id ="ulTable">
                  <li>
                      <ul>
                          <li>No</li>
                          <li>제목</li>
                          <li>작성일</li>
                          <li>작성자</li>
                          <li>조회수</li>
                      </ul>
                  </li>
                  <!-- 게시물이 출력될 영역 -->
                  <li v-for="article in articleList" :key="article.id" :article="article">
                    <ul>
                      <li>{{article.pk}}</li>
                      <li class="left">{{article.title}}</li>
                      <li>{{article.created_at.slice(0,10)}}</li>
                      <li>{{article.user.pk}}</li>
                      <li>{{article.hits}}</li>
                    </ul>
                  </li>
              </ul>
          </li>
        </ul>
        <div style="text-align:right;">
          <button type="button" class='crateArticle' @click="CreateArticleBtn" >글 쓰기</button>
        </div>
          <div class="GXPagenation"> <PageNation @changePage="changePage"/></div>
          <li id='liSearchOption'>
                <div>
                    <select id='selSearchOption' >
                        <option value='A'>제목+내용</option>
                        <option value='T'>제목</option>
                        <option value='C'>내용</option>
                        <option value='W'>작성자</option>
                    </select>
                    <input id='txtKeyWord' />
                    <input type='button' value='검색'/>
                </div>
            </li>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { onMounted } from '@vue/runtime-core'
import PageNation from '@/components/common/PageNation.vue'
import { reactive, computed } from 'vue'
export default {
  components: {
    PageNation
  },
  setup () {
    const store = useStore()
    const router = useRouter()
    const articleList = computed(() => store.state.room.articleList)
    const optionsCategory = [
      { text: '공지사항', value: '공지사항' },
      { text: '자유게시판', value: '자유게시판' },
      { text: '질문게시판', value: '질문게시판' }
    ]
    const articleInfo = reactive({
      title: 'testtttt',
      content: 'ccccccc',
      category: '자유게시판'
    })
    function clickTest (categoryNumber) {
      store.dispatch('getArticleList', categoryNumber)
    }
    function deleteTest () {
      const ArticleId = 4
      store.dispatch('deleteArticle', ArticleId)
    }
    function CreateArticleBtn () {
      router.push({ name: 'GXCreateArticle' })
    }
    onMounted(() => {
      store.dispatch('getArticleList', 1)
    })
    return {
      articleInfo, store, articleList, clickTest, deleteTest, CreateArticleBtn, optionsCategory
    }
  }
}
</script>

<style scoped>
.GXPagenation {
  display: flex;
  justify-content: center;
}
.modalCreate {
  min-height: 315px;
  font-size: 16px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  position: fixed;
  display: none;
  z-index: 200;
  top: 30%;
  left: 30%;
  width: 40%;
  height: 40%;
  background-color: rgba(255,255,255,1 );
  /* background-color: rgba( 191, 229, 255, 0.7 ); */
  /* background-color: rgba(109, 188, 230, 0.99); */
  /* background-color: rgba(191, 239, 255, 1); */
  border: 1px solid #6dcef5;
  border-radius: 15px;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
}
.modal__background{
  display: none;
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0; z-index: 0;
  background: rgba(0, 0, 0, 0.65);
}
.open {
  display: block !important;
}
.GX-grid{
  display: grid;
  width:85%;
  height:100%;
  grid-template-rows: 1fr 7fr;
  position: relative;
  left: 150px;
  top: 15px;
}
.crateArticle{
  justify-items: center;
  background-color: white;
  color: #6dcef5;
  box-shadow: 0px 4 px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  font-size: 15px;
  text-align: center;
  font-weight: bolder;
}
.crateArticle:hover{
  /* background-color: #F4F4F4; */
  background-color: #6dcef5;
  color: white;
}
.GXcommunitymenu{
  display: flex;
  justify-content: center;
}
/* 게시판 CSS */
.GXcommunityContent{
        line-height:2em;
        font-family:"맑은 고딕";
}
ul, li{
    list-style:none;
    text-align:center;
    padding:0;
    margin:0;
}

#mainWrapper{
    width: 800px;
    margin: 0 auto; /*가운데 정렬*/
}

#mainWrapper > ul > li:first-child {
    text-align: center;
    font-size:14pt;
    height:40px;
    vertical-align:middle;
    line-height:30px;
}

#ulTable {margin-top:10px;}
#ulTable > li:first-child > ul > li {
        background-color:#c9c9c9;
        font-weight:bold;
        text-align:center;
}

#ulTable > li > ul {
    clear:both;
    padding:0px auto;
    position:relative;
    min-width:40px;
}
#ulTable > li > ul > li {
        float:left;
        font-size:10pt;
        border-bottom:1px solid silver;
        vertical-align:baseline;
}

    #ulTable > li > ul > li:first-child               {width:10%;} /*No 열 크기*/
    #ulTable > li > ul > li:first-child +li           {width:45%;} /*제목 열 크기*/
    #ulTable > li > ul > li:first-child +li+li        {width:20%;} /*작성일 열 크기*/
    #ulTable > li > ul > li:first-child +li+li+li     {width:15%;} /*작성자 열 크기*/
    #ulTable > li > ul > li:first-child +li+li+li+li{width:10%;} /*조회수 열 크기*/

#divPaging {
      clear:both;
    margin:0 auto;
    width:220px;
    height:50px;
}

#divPaging > div {
        float:left;
        width: 30px;
        margin:0 auto;
        text-align:center;
}

#liSearchOption {clear:both;}
#liSearchOption > div {
    margin:0 auto;
    margin-top: 30px;
    width:auto;
    height:100px;

}

.left {
        text-align : left;
}
.item{
  margin-right: 50px;
}

</style>
