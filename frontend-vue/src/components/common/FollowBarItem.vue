<template>
  <div class="follow-item-box">
    <div>
      <img class="follow-img" :src="followItemData.imgdata" alt="이미지">
    </div>
      <div class="follow-item-info-box">{{followItemData.namedata}}</div>
      <div class="follow-item-info-box">팔로워 수 : {{followItemData.followNumdata}}</div>
  </div>
</template>

<script>
export default {
  props: {
    imgdata: {
      type: String
    },
    namedata: {
      type: String
    },
    followNumdata: {
      type: String
    }
  },
  setup (props) {
    const followItemData = {
      imgdata: props.imgdata,
      namedata: props.namedata,
      followNumdata: props.followNumdata
    }
    return {
      followItemData
    }
  }
}
</script>

<style>
.follow-item-box {
  display: flex;
  width: 270px;
}
.follow-img {
  display: flex;
  background-size: cover;
  margin: 5px 10px 5px 10px;
  width: 50px;
  height: 50px;
  border-radius: 50%;

}
.follow-item-info-box {
  padding: 5px;
  margin: 5px 5px 5px 5px;
  width: 85px;
  height: 50px;
}
</style>
