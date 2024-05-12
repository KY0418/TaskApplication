<template lang="pug">
div.block.border-solid.border-white.rounded-20px.bg-white.m-3.p-3
    ul 
        li(v-show="props.status==false").border-solid.border-white.rounded-8px.bg-red.text-white.p-1.text-xs.st {{ taskStatus }}
        li(v-show="props.status==true").border-solid.border-white.rounded-8px.bg-blue.text-white.p-1.text-xs.st {{ taskStatus }}
        li.block.mt-2.mb-2 {{ props.title }}
        li
            button(type="button" @click="retAllEmit").border-solid.border-white.rounded-5px.text-white.bg-green.text-sm.ml-28.p-1 編集
            button(type="button" @click="delt").block.float-right.border-solid.border-white.rounded-5px.text-white.bg-red.text-sm.ml-4.mr-4.p-1 削除
</template>
<style lang="scss" scoped>
.st {
    width: 18%;
    text-align: center;
}
div {
    min-width: 50%;
}
</style>

<script setup lang="ts">
import axios, { Axios, type AxiosResponse } from 'axios'
import type { responseData} from '@/interfaces'
import { onMounted, ref } from 'vue';


interface taskContentData {
    title: string,
    status: boolean,
    popupstatus:boolean,
    id: number,
}

interface Emits {
    (event:"changeState",status:boolean):void
    (event:"createTitle",title:string):void
    (event:"changePopupStatus",popstatus:boolean):void
    (event:"updateId",id:number):void
    (evenet:"showtoast",msg:string):void
}

const props = defineProps<taskContentData>()

const emit = defineEmits<Emits>()

// API側のタスクステータス
const status = ref()
// Web側のタスクステータス表示
const taskStatus = ref('未着手')
// タスクのタイトル
const tasktitle = ref(props.title)
const tsMsg = ref("")
const gid = ref(props.id)
const tList = []

let apiUrl = 'http://localhost:8000/tasks/'

// タスクステータスの値を決定
if(props.status == true){
  taskStatus.value = "完了"
}else if(props.status == false){
  taskStatus.value = "未着手"
}

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

// Emitで親にそれぞれのデータを渡す
const retAllEmit = (): void => {
  emit("changePopupStatus",props.popupstatus)
  emit("changeState",status.value)
  emit("createTitle",tasktitle.value)
  emit("updateId",props.id)
}

// DELETE関数
const delt = async (): Promise<void> => {
  console.log(gid.value)
  apiUrl = `${apiUrl}${gid.value}`
  console.log(apiUrl)
  await axios.delete(apiUrl)
  .then(response =>{
    if(response.status == 200 || response.status == 201){
      console.log("deleteが成功しました")
      tsMsg.value = "削除完了"
      emit("showtoast",tsMsg.value)
    }
  })
  .catch(error => {
    console.error("Failrd to delete error:",error)
    tsMsg.value = "削除失敗"
    emit("showtoast",tsMsg.value)
  })
}
</script>