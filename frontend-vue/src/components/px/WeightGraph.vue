<template>
  <div class="diet-graph-container">
    <div class="graph-cycle">
      <div class="cy-radio" v-for="i in cyoptions" :key="i.id">
        <input type="radio" name="cy-radio" :value="i.value" v-model="data.cycle" :id="i.id"/>
        <label :for="i.id">{{i.value}}</label>
      </div>
    </div>
    <div class="graph-category">
      <div class="radio" v-for="i in caoptions" :key="i.id">
        <input type="radio" name="radio" :value="i.value" v-model="data.category" :id="i.id"/>
        <label :for="i.id">{{i.value}}</label>
      </div>
    </div>
    <div class="graph">
      <LineChart></LineChart>
    </div>
  </div>
</template>

<script>
import { reactive } from 'vue'
import LineChart from './Chart/LineChart'
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
.diet-graph-container{
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 1fr 5fr;
  grid-template-rows: 1fr 4fr;
  grid-template-areas:
  "graph-cycle graph-cycle"
  "graph-category graph"
}

.graph-cycle{
  grid-area: graph-cycle;
  display: flex;
  justify-content: center;
  gap: 100px;
}

.graph-cycle .cy-radio label {
  font-size: 30px;
  background: #fff;
  border: 1px solid #ddd;
  padding: 0.5rem 1.25rem;
  border-radius: 50px;
  cursor: pointer;
  color: #444;
  transition: box-shadow 400ms ease;
}
.graph-cycle .cy-radio label:hover {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
}
.graph-cycle .cy-radio input[type=radio] {
  display: none;
}
.graph-cycle .cy-radio input[type=radio]:checked + label {
  background: #2196F3;
  color: #fff;
  border-color: #2196F3;
}

.graph-category{
  grid-area: graph-category;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 50px;
}

.graph-category .radio label {
  font-size: 20px;
  background: #fff;
  border: 1px solid #ddd;
  padding: 0.5rem 1.25rem;
  border-radius: 5px;
  cursor: pointer;
  color: #444;
  transition: box-shadow 400ms ease;
}
.graph-category .radio label:hover {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
}
.graph-category .radio input[type=radio] {
  display: none;
}
.graph-category .radio input[type=radio]:checked + label {
  border-color: #2196F3;
  color: #2196F3;
}

.graph{
  width: 100%;
  grid-area: graph;
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>
