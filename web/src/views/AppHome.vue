<template lang="pug">
div.boxtitle
    h1.prose.text-3xl タスク管理システム
      div.float-right
          router-link(:to="{name:'apphome'}").text-xl.mt-2.text-white.mr-4.home Home
          router-link(:to="{name:'managementstaff'}").text-xl.mt-2.mr-2.text-white.home 職員一覧
          router-link(:to="{name:'calender'}").text-xl.mt-2.text-white.mr-4.home カレンダー
router-link(:to="{name:'taskadd'}" v-on:toastFlg="showToastPost").add.block.mt-4.ml-4.mb-4.bg-blue.text-xl.text-white.border-solid.border-white.rounded-10px.text-center ＋タスクを追加
div
  TaskBox(v-for="item in workListTr" :responseData="item" :flg="tList" v-on:handFlg="updFlgParent" v-on:delFlgs="delFlgParent")
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
  text-decoration: none;
  margin-left: 0%;
}

.add {
  text-decoration: none;
  width:15%;
}
</style>

<script setup lang="ts">
import { RouterView} from "vue-router";
import {useRouter} from "vue-router"
import {computed, onMounted,reactive,ref, watch} from "vue"
import TaskBox from "../components/TaskBox.vue"
import TaskAdd from "./TaskAdd.vue";
import axios, { Axios, type AxiosResponse } from 'axios'
import { useToast } from 'vue-toast-notification';
import  {useGetStaffStore} from '../stores/getStaffData'
import { useGetTaskStore } from "@/stores/getTask";
import { usegetImportStore } from "@/stores/getImportance";

const get_staff = useGetStaffStore()
const importance_store = usegetImportStore()
const toast = useToast()
const updFlg = ref(false)
const delFlg = ref(false)
const tList = ref(false)
const globalList = ref([])
let globalListStaff = reactive([])
const completeTasks = ref([])
const privateTasks: {value: Task[]} = reactive({ value: [] })
const workTasks:{value: Task[]} = reactive({ value: [] })
const workListTr :{ value: Task[] } = ref([])

const get_task = useGetTaskStore()

interface Task {
  title: string;
  category: string;
  id: number;
  status_id:number;
  priority_id: number
}


// タスク追加のトースト表示
const showToast = (msg: string): void => {
  toast.success(msg,{
    position:"top",
    queue:false
  })
}

// updateフラグの変更
const updFlgParent = (flg:boolean): void => {
  updFlg.value = flg
}

// GETで最新のデータを取得する
const initializeGettitle = async (): Promise<void> => {
  console.log(get_task.data)
  globalList.value = get_task.$state.data
  console.log(globalList.value)
  completeTasks.value = globalList.value.filter((task) => task["category"] === "完了" || task["status_id"] == 2)
  completeTasks.value.sort((a,b)=>a["priority_id"]-b["priority_id"])
  privateTasks.value = globalList.value.filter((task) => task["category"] === "プライベート" && task["status_id"] != 2)
  privateTasks.value.sort((a,b)=>a["priority_id"]-b["priority_id"])
  workTasks.value = globalList.value.filter((task) => task["category"] === "仕事" && task["status_id"] != 2)
  workTasks.value.sort((a,b)=>a["priority_id"]-b["priority_id"])
  const workList = ref([])
  console.log("test")
  if(workTasks.value.length > 0){
      workList.value.push(workTasks.value as never)
  }
  if(privateTasks.value.length > 0){
      workList.value.push(privateTasks.value as never)
    }
  if(completeTasks.value.length > 0){
      workList.value.push(completeTasks.value as never)
      }
  workListTr.value = workList.value 
}

watch(get_task.data,async() => {
  await get_staff.get()
  await get_task.get()
  await initializeGettitle()
  console.log("watch test")
})

// updateフラグ変数の監視
watch(updFlg, async (newvalue) => {
  console.log(newvalue)
  tList.value = !tList.value
  await get_staff.get()
  await get_task.get()
  await initializeGettitle() 
  console.log(get_task.data)
  console.log("emit Complete")
  showToast("更新完了")
  updFlg.value = false
})

// deleteフラグ変数の監視
watch(delFlg,async (newvalue) => {
    console.log("delemit complete")
    await get_staff.get()
    await get_task.get()
    await initializeGettitle()
    delFlg.value = false
    tList.value = !tList.value
})

const showToastPost = (msg: string): void => {
  toast.success(msg,{
    position:"top",
    queue:false
  })
}

const delFlgParent = (flg:boolean) => {
  delFlg.value = flg
}

// interface componentPublicinstance {
//   $options: ComponentOptions
// }

// const methodThatForcesUpdate = () => {
//   const instance = getCurrentInstance();
//   instance.proxy.$forceUpdate()
//   console.log("test force")
// };

onMounted(async() => {
      await get_staff.get()
      await get_task.get()
      await importance_store.get_whole()
      console.log("test2222")
      await initializeGettitle()
    }) 
</script>


