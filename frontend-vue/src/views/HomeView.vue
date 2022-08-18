<template>
 <div class="homeGrid">
  <div class="homeDescription">
  </div>
 <div class="homeImg">
 <section class="carousel" aria-label="Gallery">
  <ol class="carousel__viewport">
    <li id="carousel__slide1"
        tabindex="0"
        class="carousel__slide">
      <div class="carouselText">
        <p class="text-Contents">
          <span class="weight-bold">G . X </span><br/><br/>

          <span class="sub">작심삼일...</span><br/>
          <span class="text-underline">혼자 하는</span> 운동 힘들지 않으신가요?<br/><br/>

          시간을 맞출 필요가 없습니다!<br/>
          운동하러 이동하지 않아도 됩니다!<br/><br/>
          <span class="text-red">언제, 어디서든</span>내가 운동하고 싶을때! 함께 운동해 보세요<br/><br/>
          <span>다양한 정보들을 공유할 수 있고,</span><br/>
          <span>사람들과 함께 즐겁게 운동이 가능해요!</span><br/>
        </p>
      </div>
      <!-- <div class="gx-main">
      </div> -->
      <div class="carousel__snapper">
        <a href="#carousel__slide3"
           class="carousel__prev">Go to last slide</a>
        <a href="#carousel__slide2"
           class="carousel__next">Go to next slide</a>
      </div>
    </li>
    <li id="carousel__slide2"
        tabindex="0"
        class="carousel__slide">
      <div class="carouselText">
        <p class="text-Contents">
          <span class="weight-bold">P . X</span><br/>
          <span class="sub">나만의 smart 다이어리</span><br/><br/>

          매일하는 식단관리 귀찮으시죠?<br/>
          <span style="color:#6dcef5; font-weight:bold;">NOW:N</span>에서 편리하고 꾸준하게 관리할 수 있습니다!<br/>

          사진만 등록하면 자동으로 칼로리를 계산해줘요!<br/>
          달력을 통해 기록을 한눈에 볼 수 있어요!<br/><br/>

          내 몸의 변화가 궁굼하시다고요?<br/>
          그래프를 통해 다양한 정보를 볼 수 있어요!<br/>
          내가 운동을 잘하고 있는지, 기간별 확인이 가능<br/>
        </p>
      </div>
      <!-- <div class="px-main">
      </div> -->
      <div class="carousel__snapper"></div>
      <a href="#carousel__slide1"
         class="carousel__prev">Go to previous slide</a>
      <a href="#carousel__slide3"
         class="carousel__next">Go to next slide</a>
    </li>
    <li id="carousel__slide3"
        tabindex="0"
        class="carousel__slide">
      <div class="carouselText">
        <p class="text-Contents">
          <span class="weight-bold">Trainer</span><br/>
          <span class="sub">나에게 꼭 맞는 트레이너</span><br/><br/>

          어떻게 운동해야 할지 모르겠다고요?<br/>
          식단 관리가 어려우시다고요?<br/><br/>

          내가 선택한 트레이너에게<br/>
          전문적인 코칭을 온라인으로 경험해 보세요<br/>
          오직 <span class="text-red">나에게 맞춘</span> 일정, 식단으로 효율적으로 운동할 수 있습니다<br/>
          트레이너와 함께라면 누구나 쉽게 <span class="text-red">목표 달성!</span><br/>
        </p>
      </div>
      <div class="carousel__snapper"></div>
      <a href="#carousel__slide2"
         class="carousel__prev">Go to previous slide</a>
      <a href="#carousel__slide1"
         class="carousel__next">Go to next slide</a>
    </li>
  </ol>
</section>
</div>
</div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style  scoped>
.homeGrid {
  display:grid;
  grid-template-columns: 100%;
  grid-template-areas:
    "homeDescription";
}
.homeDescription {
  margin: auto;

}
@keyframes tonext {
  75% {
    left: 0;
  }
  95% {
    left: 100%;
  }
  98% {
    left: 100%;
  }
  99% {
    left: 0;
  }
}

@keyframes tostart {
  75% {
    left: 0;
  }
  95% {
    left: -300%;
  }
  98% {
    left: -300%;
  }
  99% {
    left: 0;
  }
}

@keyframes snap {
  96% {
    scroll-snap-align: center;
  }
  97% {
    scroll-snap-align: none;
  }
  99% {
    scroll-snap-align: none;
  }
  100% {
    scroll-snap-align: center;
  }
}

body {
  max-width: 37.5rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  font-family: 'Lato', sans-serif;
}

* {
  box-sizing: border-box;
  scrollbar-color: transparent transparent; /* thumb and track color */
  scrollbar-width: 0px;
}

*::-webkit-scrollbar {
  width: 0;
}

*::-webkit-scrollbar-track {
  background: transparent;
}

*::-webkit-scrollbar-thumb {
  background: transparent;
  border: none;
}

* {
  -ms-overflow-style: none;
}

ol, li {
  list-style: none;
  margin: 0;
  padding: 0;
}

.text-Contents{
  font-size: 20px;
  font-weight:bold;
}

.sub{
  font-size: 30px;
}

.weight-bold{
  font-size: 40px;
  font-weight:bold;
}

.text-underline{
  text-decoration: underline gray;
  text-underline-position: under;
  bottom: 2px;
}

.text-red{
  font-size: 25px;
  color: red;
}

.carousel {
  position: relative;
  padding-top: 45%;
  filter: drop-shadow(0 0 10px #0003);
  perspective: 100px;
}

.carousel__viewport {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  display: flex;
  overflow-x: scroll;
  counter-reset: item;
  scroll-behavior: smooth;
  scroll-snap-type: x mandatory;
}

.gx-main{
  position:absolute;
  width: 50%;
  height: 58%;
  top:30%;
  left: 45%;
  background-image: url("@/assets/gx_main.PNG");
  background-size: 100%;
}

.px-main{
  position:absolute;
  width: 50%;
  height: 58%;
  top:30%;
  left: 45%;
  background-image: url("@/assets/px_main.PNG");
  background-size: 100%;
}

.gx-main{
  position:absolute;
  width: 50%;
  height: 58%;
  top:30%;
  left: 45%;
  background-image: url("@/assets/gx_main.PNG");
  background-size: 100%;
}

.carousel__slide {
  position: relative;
  flex: 0 0 100%;
  width: 100%;
  height: 100%;
  /* 커버쓰면됨 */
  /* background-image: url("@/assets/home1.jpg"); */
  background-repeat: no-repeat;
  background-size: 100%;
  counter-increment: item;
  /* background-color: #99f; */
  background-image: url("@/assets/main5.jpg");
}

.carousel__slide:nth-child(even) {
}
.carouselText {
  /* background-color:white; */
  /* border: solid; */
  padding:30px;
  position: absolute;
  top: 10%;
  left: 10%;
}

.carousel__snapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  scroll-snap-align: center;
}

@media (hover: hover) {
  .carousel__snapper {
    animation-name: tonext, snap;
    animation-timing-function: ease;
    animation-duration: 4s;
    animation-iteration-count: infinite;
  }

  .carousel__slide:last-child .carousel__snapper {
    animation-name: tostart, snap;
  }
}

@media (prefers-reduced-motion: reduce) {
  .carousel__snapper {
    animation-name: none;
  }
}

.carousel:hover .carousel__snapper,
.carousel:focus-within .carousel__snapper {
  animation-name: none;
}

.carousel__navigation {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  text-align: center;
}

.carousel__navigation-list,
.carousel__navigation-item {
  display: inline-block;
}

.carousel__navigation-button {
  display: inline-block;
  width: 1.5rem;
  height: 1.5rem;
  background-color: #333;
  background-clip: content-box;
  border: 0.25rem solid transparent;
  border-radius: 50%;
  font-size: 0;
  transition: transform 0.1s;
}

.carousel::before,
.carousel::after,
.carousel__prev,
.carousel__next {
  position: absolute;
  top: 0;
  margin-top: 23%;
  width: 4rem;
  height: 4rem;
  transform: translateY(-50%);
  border-radius: 50%;
  font-size: 0;
  outline: 0;
}

.carousel::before,
.carousel__prev {
  left: -1rem;
}

.carousel::after,
.carousel__next {
  right: -1rem;
}

.carousel::before,
.carousel::after {
  content: '';
  z-index: 1;
  background-color: #333;
  background-size: 1.5rem 1.5rem;
  background-repeat: no-repeat;
  background-position: center center;
  color: #fff;
  font-size: 2.5rem;
  line-height: 4rem;
  text-align: center;
  pointer-events: none;
}

.carousel::before {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpolygon points='0,50 80,100 80,0' fill='%23fff'/%3E%3C/svg%3E");
}

.carousel::after {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpolygon points='100,50 20,100 20,0' fill='%23fff'/%3E%3C/svg%3E");
}

</style>
