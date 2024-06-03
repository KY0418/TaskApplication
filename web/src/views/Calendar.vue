<template lang="pug">
div.uu
    h2.text-center.mt-5 {{ year }} 年 {{ month }} 月
    div.mb-4
        button(type="button" @click="beforeMonth").bef.float-left.bg-red-1.rounded-5px.border-none {{ date.beforeyear }} 年 {{ date.beforemonth }} 月
        button(type="button" @click="nextMonth").af.bg-red-1.rounded-5px.border-none {{ date.nextyear }} 年 {{ date.nextmonth }} 月
    ul
        .flex.title
            p.br.first 
            p.br.second 職員No
            p.br.second 職員名	
            p.br.four タスクタイトル	
            p.br.second ステータス		 
            p.br.second 優先度
            p.btn 
        CalendarRow(v-for="day in dayList" :year="year" :month="month" :days="day" :getData="filData" :taskData="taskData" @getFlg="changeGetflg")   
</template>
<style lang="scss">
ul{
    width:100%;
}
p{
    text-align: center;
}
.first{
    width:30px;
}
.second{
    width:10%;
}
.btn{
    width:15%;
}
.four{
    width:40%;
}
.uu{
    width:70%;
    margin: auto;
}
.br{
    border-right: solid 1px ;
}

.title{
    width:100%;
    justify-content: space-around;
    border:solid 1px;
    border-bottom:none;
    margin:0;
    padding:0;
    font-size: 0.8rem;
    font-weight: bold;
}

.boxtitle {
  border: 0.5px solid rgb(75, 73, 73);
  background-color: dimgray
}

h1 {
  letter-spacing: 0.1em;
  margin: 5px;
  color: white;
  font-weight: normal;
  
}

.home {
  background-color:dimgray ;
  text-decoration: none;
  margin-left: 0%;
}

.bef {
    margin-left:10%;
    margin-right:30%;
    
}
.af{
    margin-left:27%;
}
</style>
<script setup lang="ts">
import CalendarRow from '@/components/CalendarRow.vue';
import { onMounted,ref, watch ,reactive} from 'vue';
import { useGetTaskStore } from '@/stores/getTask';
import dayjs from 'dayjs';
import { useGetStaffStore } from '@/stores/getStaffData';
import { usegetImportStore } from '@/stores/getImportance';
import {useGetStatusStore}  from '@/stores/getStatus';

const importance_store = usegetImportStore() 
const staffStore = useGetStaffStore()
const taskStore = useGetTaskStore()
const importanceStore = usegetImportStore()
const statusStore = useGetStatusStore()
const getFlg = ref(false)
const watchdata = ref(taskStore.data)
const year = ref(dayjs().year())
const month = ref(dayjs().month())
const DayOfWeek = ref(dayjs().day())
const days = ref(dayjs(`${year}-${month.value+1}`).daysInMonth())
const dayList  = ref<number[]>([])
const date = reactive({
    nextmonth :ref(month.value+1),
    nextyear :ref(year.value),
    beforeyear: ref(year.value),
    beforemonth:ref(month.value-1)
})

for(let i=1;i<=days.value;i++){
    dayList.value.push(i)
}

const listContent = ref([])
let yearCalendarTrue = ref([])
// const makeCalData = () =>{
//     const startYear = dayjs().year()-5
//     const endYear = dayjs().year()+5
//     for (let year = startYear; year <= endYear; year++) {
//     const months = [];
//     for (let month = 0; month < 12; month++) {
//         const currentMonth = dayjs(`${year}-${month + 1}-01`);
//         const daysInMonth = currentMonth.daysInMonth();

//         const monthCalendar = [];
//         for (let day = 1; day <= daysInMonth; day++) {
//         const currentDay = dayjs(`${year}-${month + 1}-${day}`);
//         monthCalendar.push({
//             day: day,
//         });
//         }
//         months.push({
//         month: month + 1,
//         days: monthCalendar,
//         });
//     }

//     const yearCalendar = {
//         year: year,
//         months: months,
//     };
//         yearCalendarTrue.value.push(yearCalendar as never)
//     }
//     // カレンダーの表示処理
//     console.log(yearCalendarTrue.value)
//     console.log(yearCalendarTrue)
// }
// makeCalData()
interface getdata {
    id:number,
    title:string,
    staff_id:string,
    status_id:number,
    category:string,
    priority_id:number,
    start_date:string, 
}
interface staffData {
    id:number,
    staff_id:string,
    staff_name:string,
}
interface stdata {
    staff_name:string,
    start_date:string
}
const filData = ref<Record<string,string>[]>([])
const taskData = ref<Record<string,string>[]>([])

const changeGetflg = () => {
    getFlg.value = !getFlg.value
}

const dateUpd = async(): Promise<void> =>{
    dayList.value = []
    year.value = dayjs().year()
    month.value = dayjs().month()
    days.value = dayjs(`${year}-${month.value + 1}`).daysInMonth()
    for(let i=1;i<=days.value;i++){
        dayList.value.push(i)
    }
}

watch([year,month], async()=>{
    await getData()
})

// 年月日の引数渡す
const getData = async() => {
    await taskStore.get()
    await staffStore.get()
    const makeData = taskStore.data
    days.value = dayjs(`${year.value}-${month.value}`).daysInMonth()
    taskData.value = []
    filData.value = []
    dayList.value = []
    for(let i=1;i<=days.value;i++){
        dayList.value.push(i)
    }
    const li: getdata[] = []
    for(let i of makeData){
        li.push(i)
    }
    let staffSearch: staffData[] = []
    let staffList: staffData[] = []
    staffList = staffStore.data
    const searchRes = li.filter((search)=> search.start_date.includes(String(year.value)+'-'+String(month.value).padStart(2,'0'))) 
    for(let i = 0;i < searchRes.length; i++){
        let st = searchRes[0].staff_id
        staffSearch = staffList.filter((search)=> search.staff_id === searchRes[i].staff_id)
        console.log(staffSearch[0])
        await statusStore.get(searchRes[i].status_id)
        await importanceStore.get(searchRes[i].priority_id)
        filData.value.push({'staff_name':staffSearch[0].staff_name,'start_date':searchRes[i].start_date})
        taskData.value.push({'title':searchRes[i].title,'staff_name':staffSearch[0].staff_name,'status':statusStore.data[0].status_name,'priority':importanceStore.data[0].importance,'staff_id':searchRes[i].staff_id,'start_date':searchRes[i].start_date,'id':String(searchRes[i].id)}) 
        console.log(filData.value)
    }
}

// 変数増やして境界値を制御できるようにする
const nextMonth = () => {
    if(date.nextyear==2029 && date.nextmonth == 12){
        return 
    }
    if(date.nextmonth == 12){
        date.nextyear += 1
        date.nextmonth = 1
    }else{
        date.nextmonth += 1
    }
    if(month.value == 12){
        month.value = 1
        year.value += 1
        
    }else{
        month.value += 1
        
        }
    if(date.beforemonth == 12){
        date.beforemonth = 1
        date.beforeyear += 1
    }else{
        date.beforemonth += 1
    }
    
    days.value = dayjs(`${year}-${month.value + 1}`).daysInMonth()
    for(let i=1;i<=days.value;i++){
        dayList.value.push(i)
    }
}

watch(getFlg,async()=>{
    console.log("test")
    await taskStore.get()
    await staffStore.get()
    await getData()
})

// watch([year,month],async()=>{
//     await getData()
// })

const beforeMonth = () => {
    if(date.beforeyear == 2019 && date.beforemonth == 1){
        return
    }
    if(date.nextmonth == 1){
        date.nextyear -= 1
        date.nextmonth = 12
    }else{
        date.nextmonth -= 1
    }
    if(month.value == 1){
        month.value = 12
        year.value -= 1
        
    }else{
        month.value -= 1
        }
    if(date.beforemonth == 1){
        date.beforemonth = 12
        date.beforeyear -= 1
    }else{
        date.beforemonth -= 1
    }
    
}

onMounted(async() => {
    await importanceStore.get_whole()
    await taskStore.get()
    await staffStore.get()
    await statusStore.get_whole()
    await dateUpd()
    await getData()
})
</script>