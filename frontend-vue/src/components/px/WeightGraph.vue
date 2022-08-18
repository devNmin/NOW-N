<template>
  <div class="diet-graph-container">
    <div class="graph">
      <LineChart></LineChart>
    </div>
  </div>
</template>

<script>
import LineChart from '@/components/px/Chart/LineChart.vue'
import { reactive } from 'vue'
export default {
  components: { LineChart },
  setup () {
    const caoptions = [
      { id: 'bmi', value: 'bmi 지수' },
      { id: 'kcal', value: '칼로리' },
      { id: 'nutrient', value: '영양소' }
    ]
    const cyoptions = [
      { id: 'daily', value: '일별' },
      { id: 'weekly', value: '주별' },
      { id: 'montly', value: '월별' }
    ]
    const data = reactive({
      cycle: '',
      category: ''
    })

    return { data, caoptions, cyoptions }
  }
}
</script>

<style scoped>
.button-container{
  display:block;
  margin:auto;
  /* display:inline-block; */
}
button{
  /* background-color: var(--color-grey-900); */
  color: #6dcef5;

  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  font-family: 'MaruBuriOTF';
  font-style: normal;
  border-width: 0;
  width: 70px;
  height: 30px;
  font-size: 20px;
  text-align: center;
  font-weight: bold;
}

button:hover {
  background-color: #6dcef5;
  color: white;
  font-weight: bold;
}

button.disabled{
  cursor: default;
  background-color: var(--color-grey-100);
  border: 2px solid var(--color-grey-500);
  color: var(--color-grey-500);
}
.diet-graph-container{
  width: 100%;
  height: 100%;
}

.graph-cycle{
  grid-area: graph-cycle;
  display: flex;
  justify-content: center;
  align-content: center;
}

.graph-category{
  grid-area: graph-category;
  display: flex;
  justify-content: center;
  align-content: center;
}

.graph{
  grid-area: graph;
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>
