<template lang="pug">
div.listyle  
    li.l
        span(v-show="dayOfweek==0").block.text-center.bg-pink-3.day {{String(props.days).padStart(2,'0')}}
        span(v-show="dayOfweek==6").block.text-center.bg-blue.day {{String(props.days).padStart(2,'0')}}
        span(v-show="dayOfweek!=6 & dayOfweek!=0").block.text-center.day {{String(props.days).padStart(2,'0')}}

        div.block.debu
            span(v-show="isToday").dow.bg-green.rounded-5px.mr-2 {{ indicateDay }}
            span(v-show="isToday==false").dow.mr-2 {{ indicateDay }}
            div(@click="openAccordionMenu" ).inline
                p(v-if="nameList[0]").inline ▼
                p(v-for="item of nameList" id="dataRow").inline.ml-4 {{ item.staff_name }}
            div(v-show="menuFlg")
                accordion(v-for="item of taskData" :title="item.title" :status="item.status" :staff_name="item.staff_name" :priority="item.priority" :staff_id="item.staff_id" :id="item.id" :start_date="item.start_date"
                            @getflg="cruckGet")
</template>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Sacramento&display=swap');
span {
  font-family: 'Sacramento', cursive;
}

.debu {
  width: 100%;
  border-left: solid 1px black;
}

.listyle {
  width: 100%;
  margin: auto;
}
.l {
  list-style: none;
  border: solid 1px;
  border-bottom: none;
  display: flex;
}
.day {
  width: 30px;
  min-height: 30px;
  height: 100%;
  line-height: 30px;
}

.dow {
  float: right;
  width: 65px;
}

p {
  width: 100%;
  min-height: 30px;
}
</style>
<script setup lang="ts">
import { ref, watch } from 'vue'
import { useGetStaffStore } from '@/stores/getStaffData'
import accordion from './Accordion.vue'
import dayjs from 'dayjs'

const staffStore = useGetStaffStore()

interface CalendarData {
  taskData: {
    title: string
    staff_name: string
    status: string
    priority: string
    staff_id: string
    start_date: string
    id: string
  }[]
  getData: {
    staff_name: string
    start_date: string
  }[]
  year: number
  month: number
  days: number
}

interface getdata {
  staff_name: string | null
  start_date: string | null
}
interface tData {
  title: string
  staff_name: string
  status: string
  priority: string
  staff_id: string
}
interface Emits {
  (event: 'getFlg'): void
}
const emit = defineEmits<Emits>()
const props = defineProps<CalendarData>()
const compareDate = ref(dayjs().format('YYYY-MM-DD'))
const compareDateProp = ref(
  dayjs(`${props.year}-${props.month}-${props.days}`).format('YYYY-MM-DD')
)
const isToday = ref(compareDate.value === compareDateProp.value)
const gdata = ref<getdata[]>(props.getData)
const nameList = ref<getdata[]>([])
const menuFlg = ref(false)
const taskData = ref<tData[]>()
const date = ref(String(props.year) + '/' + String(props.month) + '/' + String(props.days))
const dayOfweek = ref(dayjs(date.value).day())
const indicateDay = ref()
// const rowContent = async() =>  {
//     let swap = ref<string>()
//     taskData.value = props.taskData.filter((search)=> search.start_date ===  String(props.year)+'-'+String(props.month).padStart(2,'0')+'-'+String(props.days).padStart(2,'0'))
//     const res = ref<getdata[] | null>([])
//     res.value = gdata.value.filter((search)=> search.start_date === String(props.year)+'-'+String(props.month).padStart(2,'0')+'-'+String(props.days).padStart(2,'0'))
//     console.log(res.value)
//     if(gdata.value.length >= 2 && gdata.value != undefined && res.value != undefined){
//         console.log(res.value)
//         for(let i:number = 0;i<gdata.value.length;i++){
//             swap.value = res.value[i].staff_name
//             if(nameList.value.includes(gdata.value[i].staff_name) == false){
//                 console.log(res.value[i])
//                 nameList.value.push(swap.value)
//             }
//         }
//     }else if(gdata.value.length <= 1 && gdata.value != undefined && res.value != undefined){
//         if(nameList.value.includes(gdata.value[0].staff_name) == false)
//             nameList.value.push(res.value[0].staff_name)
//     }
// }
const cruckGet = () => {
  emit('getFlg')
}

const rowContent = async () => {
  await indicateDayCompute()
  const formattedDate = `${props.year}-${String(props.month).padStart(2, '0')}-${String(props.days).padStart(2, '0')}`
  taskData.value = props.taskData.filter((task) => task.start_date === formattedDate)
  const res = gdata.value.filter((data) => data.start_date === formattedDate)
  nameList.value = []
  res.forEach((data) => {
    if (data.staff_name && !nameList.value.some((item) => item.staff_name === data.staff_name)) {
      nameList.value.push({ staff_name: data.staff_name, start_date: data.start_date })
    }
  })
}

const indicateDayCompute = async () => {
  const days = ['Sunday', 'Monday', 'Tuesdy', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  indicateDay.value = days[dayOfweek.value]
}
//修正前コード
// const indicateDayCompute = async() => {
//     switch(dayOfweek.value){
//         case 0:
//             indicateDay.value = "Sun"
//             break
//         case 1:
//             indicateDay.value = "Mon"
//             break
//         case 2:
//             indicateDay.value = "Tue"
//             break
//         case 3:
//             indicateDay.value = "Wed"
//             break
//         case 4:
//             indicateDay.value = "Thu"
//             break
//         case 5:
//             indicateDay.value = "Fri"
//             break
//         case 6:
//             indicateDay.value = "Sat"
//             break
//     }
// }

// const searchData = async() => {
//     listContent.value = []
//     pdata.value = props.dateData.filter((search)=> search.year == props.year)
//     let count = 0
//     let st_name: string
//     for(let i = 0; i < test.length;i++){
//         let date = String(props.year)+'-'+String(props.month).padStart(2,'0')+'-'+String(pdata.value[0].months[0].days[i].day).padStart(2,'0')
//         let ab = props.getData.filter((search)=> search.start_date === date)
//         if(ab.length > 0){
//             matchData.value.push(...ab)
//             await staffStore.search_staff(matchData.value[count].staff_id)
//             listContent.value.push({'staff_id':staffStore.search_data[0].staff_name,'start_date':matchData.value[count].start_date})
//             nameList.value.push(staffStore.search_data[0].staff_name)
//             count++
//         }
//         ab = []
//     }
//     console.log(nameList.value)
//     console.log(listContent.value)
// }
// searchData()
const openAccordionMenu = () => {
  menuFlg.value = !menuFlg.value
}
watch(props, async () => {
  // await searchData()
  date.value = String(props.year) + '/' + String(props.month) + '/' + String(props.days)
  dayOfweek.value = dayjs(date.value).day()
  gdata.value = props.getData
  await rowContent()
  compareDateProp.value = dayjs(`${props.year}-${props.month}-${props.days}`).format('YYYY-MM-DD')
  isToday.value = compareDate.value === compareDateProp.value
})
</script>
