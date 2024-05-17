<template lang="pug">
div(v-if="tasktitle!==''").block.border-solid.border-white.rounded-20px.bg-white.m-3.p-3
    ul 
        li(v-show="taskStatus==='未着手'").border-solid.border-white.rounded-8px.bg-red.text-white.p-1.text-xs.st {{ taskStatus }}
        li(v-show="taskStatus==='完了'").border-solid.border-white.rounded-8px.bg-blue.text-white.p-1.text-xs.st {{ taskStatus }}
        li.block.mt-2.mb-2 {{ tasktitle }}
        li
            button(type="button" @click="UpdMod").border-solid.border-white.rounded-5px.text-white.bg-green.text-sm.ml-28.p-1 編集
            button(type="button" @click="DelModal").block.float-right.border-solid.border-white.rounded-5px.text-white.bg-red.text-sm.ml-4.mr-4.p-1 削除
div(v-show="showUpd")
  popup(v-bind:title="props.title" v-bind:status="props.status" v-bind:id="props.id" v-on:changeSwitch="UpdMod" v-bind:category="props.category"
        v-on:showtoast="CaseSuccessTsMsg" v-on:taskstatus="watchStatus" v-on:changetitle="watchTitle")
div(v-show="showDel")
  delmodal(v-on:delNotAgree="DelModal" v-on:delEmit="prcAgree" v-on:delFlgOrigin="detectDelFlg" v-bind:id="props.id" :deltitle="tasktitle") 
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
import { onMounted, ref, watch } from 'vue';
import delmodal from './delmodal.vue';
import popup from './popup.vue';
import { useToast } from 'vue-toast-notification';


interface taskContentData {
    title: string,
    status: boolean,
    id: number,
    category:string,
}

interface Emits {
    (event:"changeState",status:boolean):void
    (event:"createTitle",title:string):void
    (event:"changePopupStatus",popstatus:boolean):void
    (event:"updateId",id:number):void
    (evenet:"showtoast",msg:string,flg:number):void
    (event:"showDelModal"):void
    (event:"handData",flg:boolean):void
    (event:"delFlg",delFlg:boolean):void
}

const props = defineProps<taskContentData>()

const emit = defineEmits<Emits>()

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
const toast = useToast()
const tasktile = ref(props.title)
const delCompFlg = ref(false)
const updWatch = ref(false)

let apiUrl = 'http://localhost:8000/tasks/'

// タスクステータスの値を決定
if(props.status == true){
  taskStatus.value = "完了"
  watch((props.title,taskStatus),(): void => {
  console.log("画面が更新されているはず")
})
}else if(props.status == false){
  taskStatus.value = "未着手"
  watch((props.title,taskStatus),(): void => {
  console.log("画面が更新されているはず")
})
}

watch([taskStatus,tasktitle],() => {
  emit("handData",updFlg.value)
  console.log("emit1",updFlg.value)
  updFlg.value = false
})

watch(delCompFlg,() => {
  console.log("delemit2",delCompFlg.value)
  emit("delFlg",delCompFlg.value)
  delCompFlg.value = false
})

watch(updWatch,() => {
  emit("handData",updFlg.value)
  console.log("emit1",updFlg.value)
  updFlg.value = false
})

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

const detectch = (): void => {
  axios.get(apiUrl)
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

const DelModal = (): void => {
  showDel.value = !showDel.value
}

const prcAgree = (msg:string,flg:number) => {
  tasktitle.value = ''
  DelModal()
  emit("showtoast",msg,flg)
}

</script>