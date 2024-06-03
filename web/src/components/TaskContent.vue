<template lang="pug">
div(v-if="tasktitle!==''").block.border-solid.border-white.rounded-20px.bg-white.m-3.p-3
    ul 
        li(v-show="taskStatus==='未完'").border-solid.border-white.rounded-8px.bg-red.text-white.p-1.text-xs.float-left.st {{ taskStatus }}
        li(v-show="taskStatus==='完了'").border-solid.border-white.rounded-8px.bg-blue.text-white.p-1.text-xs.float-left.st {{ taskStatus }}
        li(v-show="taskStatus==='進行中'").border-solid.border-white.rounded-8px.bg-yellow.text-white.p-1.text-xs.float-left.st {{ taskStatus }}
        span.ml-1.text-3.titletag {{ st_name }} 
        span(v-show="props.pri_id == 1").ml-4.bg-red-5.boder-solid.rounded-5px.text-3.imptag {{ importance  }}
        span(v-show="props.pri_id == 2").ml-4.bg-yellow-5.boder-solid.rounded-5px.text-3.imptag {{ importance }}
        span(v-show="props.pri_id == 3").ml-4.bg-blue-5.boder-solid.rounded-5px.text-3.imptag {{ importance }}
        span(v-show="props.pri_id == 4").ml-4.bg-gray-5.boder-solid.rounded-5px.text-3.imptag {{ importance }}
        li.block.mt-2.mb-2 {{ tasktitle }}
        li.text-xs.color-gray {{ props.start_date }}
        li
            button(type="button" @click="UpdMod").border-solid.border-white.rounded-5px.text-white.bg-green.text-sm.ml-28.p-1 編集
            button(type="button" @click="DelModal").block.float-right.border-solid.border-white.rounded-5px.text-white.bg-red.text-sm.ml-4.mr-4.p-1 削除
div(v-show="showUpd")
  popup(v-bind:title="props.title" v-bind:status="props.status" v-bind:id="props.id" v-on:changeSwitch="UpdMod" v-bind:category="props.category"
        @updGet="getFlgHanding" @showtoast="CaseSuccessTsMsg" v-on:taskstatus="watchStatus" v-on:changetitle="watchTitle" :pri_id= "props.pri_id")
div(v-show="showDel")
  delmodal(@delNotAgree="DelModal" @delEmit="prcAgree" @delFlgOrigin="detectDelFlg" @delflg="delGetflg" :id="props.id" :deltitle="tasktitle") 
</template>
<style lang="scss" scoped>
.st {
    width: 18%;
    text-align: center;
}
div {
    min-width: 50%;
}
.imp{
  padding: 1px;
}
.titletag {
  width: 10%;
}
</style>

<script setup lang="ts">
import axios, { Axios, type AxiosResponse } from 'axios'
import { onMounted, ref, watch } from 'vue';
import delmodal from './GlbDelModal.vue';
import popup from './TaskUpdModal.vue';
import { useGetStaffStore } from '@/stores/getStaffData';
import { usegetImportStore } from '@/stores/getImportance';
import { useGetTaskStore } from '@/stores/getTask';



interface taskContentData {
    title: string,
    status: number,
    id: number,
    category:string,
    st_id:string,
    pri_id:number
    start_date:string
}

interface Emits {
    (event:"changeState",status:boolean):void
    (event:"createTitle",title:string):void
    (event:"changePopupStatus",popstatus:boolean):void
    (event:"updateId",id:number):void
    (evenet:"showtoast",msg:string,flg:number):void
    (event:"showDelModal"):void
    (event:"handData",flg:boolean):void
    (event:"delFlg"):void
    (event:"updFlg"):void
}

const props = defineProps<taskContentData>()

const emit = defineEmits<Emits>()
const taskStore = useGetTaskStore()
const importance_store = usegetImportStore()
const emList:string[] = ["重要度高、緊急度高","重要度高、緊急度低","重要度低、緊急度高","重要度低、緊急度低"]
const p_id = ref(props.pri_id)
const importance = ref()
const swap = ref(props)
// API側のタスクステータス
const status = ref()
// Web側のタスクステータス表示
const taskStatus = ref('')
// タスクのタイトル
const tasktitle = ref(props.title)
const tsMsg = ref("")
const gid = ref(props.id)
const tList = []
const showUpd = ref(false)
const showDel = ref(false)
const updFlg = ref(false)
const pri = ref(props.pri_id)
const delCompFlg = ref(false)
const updWatch = ref(false)
const st_name = ref('')
let apiUrl = 'http://localhost:8000/tasks'

// タスクステータスの値を決定
const determine_status = async (status:number)=>{
  if(status == 1){
  taskStatus.value = "未完"
  watch((props.title,taskStatus),(): void => {
  console.log("画面が更新されているはず")
})
}else if(status == 2){
  taskStatus.value = "完了"
  watch((props.title,taskStatus),(): void => {
  console.log("画面が更新されているはず")
})}else if(status == 3){
  taskStatus.value = "進行中"
}}

determine_status(props.status)

const delGetflg = () =>{
  emit("delFlg")
}

const getFlgHanding = () =>{
  emit("updFlg")
}

const p_idGet = async (id:number): Promise<void> => {
  const importanceList = ref()
  for(let i of importance_store.whole_data){
    if(i["id"] == id){
      importanceList.value = i["importance"]
    }
  }

  if(importanceList.value === "重要度高、緊急度高"){
    importance.value = "緊急度高"
  }else if(importanceList.value === "重要度高、緊急度低"){
    importance.value = "緊急度中"
  }else if(importanceList.value === "重要度低、緊急度高"){
    importance.value = "緊急度低"
  }else if(importanceList.value === "重要度低、緊急度低"){
    importance.value = "緊急度無"
  }
}
p_idGet(props.pri_id)
watch(props,async (newvalue): Promise<void> => {
  tasktitle.value = newvalue.title
  await p_idGet(newvalue.pri_id)
  await determine_status(newvalue.status)
})



watch([taskStatus,tasktitle],() => {
  emit("handData",updFlg.value)
  updFlg.value = false
})

watch(delCompFlg,() => {
  emit("delFlg")
  delCompFlg.value = false
})

watch(updWatch,() => {
  emit("handData",updFlg.value)
  updFlg.value = false
})

const staffData = useGetStaffStore()
for(let i of staffData.data){
  if(i['staff_id'] == props.st_id){
    st_name.value = i['staff_name']
  }
}

const watchStatus = (status:string): void => {
  console.log(status)
  taskStatus.value = status
  if(updFlg.value == false){
    updFlg.value = true
  }
}

const watchTitle = (title:string): void => {
  tasktitle.value = title
  if(updFlg.value == false){
    updFlg.value = true
  }}

const getData = async () : Promise<void> => {
  const response = await axios.get(apiUrl)
  const titleList = ref(response.data)
  for(const item of titleList.value){
    tList.push({
      title:item.title
    }
    )
    console.log(item.title)
  }
}

const detectDelFlg = (delflg:boolean) => {
  delCompFlg.value = delflg
}

const UpdMod = (flg:boolean): void => {
  updWatch.value = flg
  showUpd.value = !showUpd.value
}

const CaseSuccessTsMsg = (msg:string,flg:number): void => {
  tsMsg.value = msg
  console.log(tsMsg.value)
  emit("showtoast",tsMsg.value,flg)
}

const DelModal = () => {
  showDel.value = !showDel.value
}

const prcAgree = (msg:string,flg:number) => {
  tasktitle.value = ''
  DelModal()
  emit("showtoast",msg,flg)
}
</script>