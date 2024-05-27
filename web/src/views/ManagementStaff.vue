<template lang="pug">
div.boxtitle 
  h1.prope.text-3xl タスク管理システム
    router-link(:to="{name:'apphome'}").text-xl.mt-2.float-right.text-white.home Home
p.mt-4.ml-4.text-2xl 職員一覧
    router-link(:to="{name:'staffadd'}").border-solid.border-white.rounded-10px.bg-blue-8.p-1.text-xl.text-white.addst 職員を追加
    StaffTable(@updflg="changeFlg" :flg="changeGetFlg" )
    //- table.border-solid.border-black.rounded-5.ml-6.mt-4 
    //-     tr.border-solid
    //-         th.text-center.t1 職員No
    //-         th.text-center.t2 職員名
    //-         th.exclude
    //-     tr(v-for="i in stData")
    //-         td.text-center.d1   {{ i.staff_id }}           
    //-         td.d2
    //-             p.text-center {{ i.staff_name }}
    //-         td.btnw
    //-             div.text-center 
    //-                 button(type="button" @click="showUpdModal").float-left.ml-4.mr-4.bg-green-3.border-white.rounded-5px 編集
    //-                 button(type="button" ).float-right.mr-4.bg-red-4.border-white.rounded-5px 削除
//- div       
//-     StaffUpdModal(v-show="showUpd" @close="showUpdModal" @updAgree="")

</template>

<style lang="scss" scoped>
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
  border-style: none;
  text-decoration: none;
}

.tr {
    border-top:solid 1px gray;
}

.ipt {
    text-decoration: none;
    border-style: none;
}

.ipt:focus{
    outline: none;
}

table{
    border-collapse: separate;
    border-radius: 5px;
    overflow: hidden;
    width:80%;
}

.btnw{
    border-top: solid 1px black;
    width: 20%;
}

.t1,.t2{
    border-right: 1px solid black;
}
.d1,.d2 {
    border-top: solid 1px black;
    border-right: solid 1px black;
}

.addst {
    letter-spacing: 0.15rem;
    text-decoration: none;
    margin-left: 70%;
    min-width: 20%;
}
</style>
<script setup lang="ts">
import { inject, onMounted, ref, watch, reactive , computed,onUpdated} from 'vue';
import StaffTable from "../components/StaffTable.vue"
import StaffUpdModal from '@/components/StaffUpdModal.vue';
import router from '@/router';
import axios from 'axios';
import { useToast } from 'vue-toast-notification';
import { useGetStaffStore } from '@/stores/getStaffData';
import type {Ref} from "vue"

const get_staff = useGetStaffStore()

const flg = ref(false)

const getflg = ref(false)

const globalListStaff = ref([])

const toast = useToast()

const staffName = ref('')
interface emit {
    emit(event:"toastFlg",msg:string):void
}
let apiUrl = 'http://localhost:8000/tasks/'

const toStaffAdd = (): void =>{
    router.push({name:'staffadd'})
}

const changeFlg = () =>{
    flg.value = !flg.value 

}

const changeGetFlg = (): boolean =>{
    getflg.value = !getflg.value
    return getflg.value
}

let stData = ref(get_staff.$state.data)
// get_staff.get()
console.log(get_staff.$state.data)

const staffUpdate = async(): Promise<void> => {

}

const updflg = ref()
// updflg.value = window.localStorage.getItem("upd")
// if(updflg.value == "comp"){
//     get_staff.get()
//     window.localStorage.setItem("upd","reverse")
// }

watch(flg,async():Promise<void> =>{
    await get_staff.get()
    console.log("Emit Test")
})

onMounted(async (): Promise<void> => {
        console.log("test2222")
        changeGetFlg()
        // stData = computed(():any =>{
        //     return get_staff.$state.data
        // }) 
        await get_staff.get()
        stData.value = get_staff.data 
        console.log(stData.value)
    }) 
</script> 