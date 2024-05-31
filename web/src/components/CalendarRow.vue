<template lang="pug">
div.listyle  
    li.l
        span.block.text-center {{String(props.days).padStart(2,'0')}}
        div.block.debu
            p(v-for="item of nameList" @click="openAccordionMenu" id="dataRow").inline.ml-4.bg-yellow-1 ▼ {{ item }}
            div(v-show="menuFlg")
                accordion(v-for="item of taskData" :title="item.title" :status="item.status" :staff_name="item.staff_name" :priority="item.priority" :staff_id="item.staff_id" :id="item.id" :start_date="item.start_date")


</template>
<style lang="scss" scoped>
 .debu{
    width:100%;
    border-left: solid 1px black;
 }

.listyle{
    width:100%;
    margin:auto;
}
.l {
    list-style: none;
    border: solid 1px;
    border-bottom: none;
    display: flex;
}
span{
    width:30px;
    min-height: 30px;
    height: 100%;
    line-height: 30px;
}


p{
    width:100%;
    min-height: 30px;
}

</style>
<script setup lang="ts">
import { ref,watch } from 'vue';
import { useGetStaffStore } from '@/stores/getStaffData';
import accordion from './Accordion.vue';

const staffStore = useGetStaffStore()

interface CalendarData {
    taskData:{
        title: string,
        staff_name: string,
        status: string,
        priority: string,
        staff_id: string,
        start_date:string,
        id:string
    }[],
    getData:{
        staff_name:string | null,
        start_date:string | null,
    }[],
    year: number,
    month: number,
    days:number,
   }

interface search{
    id: number; 
    title: string; 
    staff_id: string; 
    status: number; 
    category: string; 
    priority: number; 
    start_date: string;
}

interface listContentOrg{
    staff_id:string,
    start_date:string
}
interface getdata {
    staff_name:string | null,
    start_date:string | null,
}
interface tData {
        title: string,
        staff_name: string,
        status: string,
        priority: string,
        staff_id: string,
}
const listContent = ref<listContentOrg[]>([])
const props = defineProps<CalendarData>()
let gcount = ref(0)
let swap = 0
const gdata = ref<getdata[]>(props.getData)
const nameList = ref<getdata[]>([])
const matchData = ref<search[]>([])
const menuFlg = ref(false)
const res :getdata[] = []
const taskData = ref<tData[]>()
const rowContent = async() =>  {
    taskData.value = props.taskData.filter((search)=> search.start_date ===  String(props.year)+'-'+String(props.month).padStart(2,'0')+'-'+String(props.days).padStart(2,'0'))
    const res = ref<getdata[] | null>([]) 
    res.value = gdata.value.filter((search)=> search.start_date === String(props.year)+'-'+String(props.month).padStart(2,'0')+'-'+String(props.days).padStart(2,'0'))
    console.log(res)
    if(gdata.value.length >= 2 && gdata.value != undefined){
        for(let i:number = 0;i<gdata.value.length;i++){
            if(nameList.value.includes(gdata.value[i].staff_name) == false){
                console.log(res.value[i])
                nameList.value.push(res.value[i].staff_name)
            }
        }
    }else if(gdata.value.length <= 1){
        nameList.value.push(gdata.value[0]?.staff_name)
    }
}
rowContent()
console.log(props.taskData)
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
const openAccordionMenu = ()  => {
    menuFlg.value = !menuFlg.value
}
watch(props,async()=> {
    // await searchData()
    gdata.value = props.getData
    nameList.value = <string[]>([])
    await rowContent()
})
// String(parseInt(Object.values(i)[0],10)).padStart(2,'0')
</script>  