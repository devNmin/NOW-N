<template>
  <TrainerCalendar/>
  <TrainerScheduleItem class="schedule-item"/>

</template>

<script>
import TrainerCalendar from '@/components/trainer/TrainerCalendar.vue'
import TrainerScheduleItem from '@/components/trainer/TrainerScheduleItem.vue'
export default {
  components: { TrainerCalendar, TrainerScheduleItem }

}
</script>

<style scope>
.schedule-item {
display: flex;
box-sizing: border-box;
position: relative;
width: 938px;
height: 103px;

background: #FFFFFF;
border: 2px solid #6DCEF5;
border-radius: 15px;}
</style>
