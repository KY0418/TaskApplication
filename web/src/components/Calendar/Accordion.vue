<template lang="pug">
div.accordion-container    
      table.border-black.rounded-5
        tr
              td.text-center.d1  {{ props.staff_id }} 
              td.d2.text-center  {{ props.staff_name }}
              td.d3.text-center  {{ props. title}}
              td(v-show="props.status==='未着手'").d4.text-center.bg-red-2  {{ props.status }}
              td(v-show="props.status==='完了'").d4.text-center.bg-blue-5  {{ props.status }}
              td(v-show="props.status==='進行中'").d4.text-center.bg-yellow-1  {{ props.status }}
              td(v-show="props.priority=='重要度高、緊急度高'").d4.text-center.bg-red  {{ props.priority }}
              td(v-show="props.priority=='重要度高、緊急度低'").d4.text-center.bg-yellow  {{ props.priority }}
              td(v-show="props.priority=='重要度低、緊急度高'").d4.text-center.bg-blue  {{ props.priority }}
              td(v-show="props.priority=='重要度低、緊急度低'").d4.text-center.bg-gray  {{ props.priority }}
              td.btnw 
                div.flex.justify-around 
                  button(type="button" @click="updFlgControll").ml-2.mr-1.bg-green-3.border-white.rounded-5px 編集
                  button(type="button" @click="delFlgControll" ).bg-red-4.border-white.rounded-5px 削除
div(v-show="updModFlg")
  CalendarUpdModal(@close="updFlgControll" @calendarUpd="retGetflg" :title="props.title" :staff_name="props.staff_name" :status="props.status" :priority="props.priority" :id="Number(props.id)" :staff_id="props.staff_id" :start_date="props.start_date")
div(v-show="delModFlg")
  delmodal(@delNotAgree="delFlgControll" @calendarDelFlg="retGetflg" :id="Number(props.id)" :deltitle="props.title")
</template>
<style lang="scss" scoped>
td {
  font-size: 0.8rem;
  text-align: center;
}

p {
  display: block;
  font-weight: bold;
  padding: 10px 15px;
  cursor: pointer;
  //   background-color: #787ea0;
  color: black;
}

.accordion-container {
  width: 100%;
  margin: 0 auto;
}

details {
  width: 100%;
}

tr {
  width: 100%;
}

.d1,
.d2 {
  border-top: solid 1px black;
  border-right: solid 1px black;
  width: 10%;
}
.d3 {
  border-top: solid 1px;
  border-right: solid 1px black;
  width: 40%;
}
.d4 {
  border-top: solid 1px;
  border-right: solid 1px black;
  width: 10%;
}
.btnw {
  border-top: solid 1px black;
  width: 15%;
}

table {
  border-collapse: separate;
  border-radius: 5px;
  overflow: hidden;
  width: 100%;
}

.t1 {
  width: 15%;
}

.t2 {
  width: 20%;
}
.t3 {
  width: 30%;
  border-right: solid 1px;
}
.t4 {
  width: 15%;
  border-right: solid 1px;
}
.t1,
.t2 {
  border-right: 1px solid black;
}
.ls {
  width: 15%;
}
</style>
<script setup lang="ts">
import delmodal from '../Common/GlbDelModal.vue'
import { ref, watch } from 'vue'
import CalendarUpdModal from './CalendarUpdModal.vue'

const updModFlg = ref(false)
const delModFlg = ref(false)
const delFlgControll = () => {
  delModFlg.value = !delModFlg.value
}

const updFlgControll = () => {
  updModFlg.value = !updModFlg.value
}
interface Emits {
  (event: 'getflg'): void
}

interface taskData {
  title: string
  staff_name: string
  status: string
  priority: string
  staff_id: string
  id: string
  start_date: string
}

const props = defineProps<taskData>()
const emit = defineEmits<Emits>()

const retGetflg = () => {
  emit('getflg')
}
</script>
