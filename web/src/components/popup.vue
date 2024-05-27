<template lang="pug">
div.sample-popup-window
  div.sample-popup-background
    div.sample-popup-box
      div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
        div.boxcomp
          h2.text-white.text-2xl.bg-blue.text-center.poptitle タスクを編集
          label.block.mt-4.ml-4 タスクタイトル
            div.mt-4.ml-10
              input(type="text" v-model="newtitle" ).w-60.tt
          label.block.mt-4.ml-4.mr-4.mb-6 優先度
            div.ml-10.mt-4
              select(v-model="priority").tt
                option( value="1" ) 緊急度高、緊急度高
                option( value="2" ) 緊急度高、緊急度低
                option( value="3" ) 緊急度低、緊急度高
                option( value="4" ) 緊急度低、緊急度低
          label.block.mt-4.ml-4 カテゴリー
            div.ml-10.mt-4
              select(v-model="category").tt
                option(value="仕事") 仕事
                option(value="プライベート") プライベート
                option(value="完了") 完了
          label.block.mt-4.ml-4.mr-4.mb-6 ステータス
              div.rd
                input(type="radio" v-model="TrueOrFalse" :value="1").float-left
                span.mt-2 未着手
                input(type="radio" v-model="TrueOrFalse" :value="2").ml-5
                span 完了
                input(type="radio" v-model="TrueOrFalse" :value="3").ml-5
                span 進行中
          label.block
            div.mt-4.ml-17.rd
              button(type="button" @click="put").border-solid.border-white.rounded-5px.bg-blue.mb-5.btn 更新
              button(type="button" @click="popupClose").border-solid.border-white.rounded-5px.bg-red.ml-8.mb-5.float-right.btn  キャンセル
</template>

<style lang="scss" scoped>
.sample-popup-background {
	/* 画面全体を暗くする透過背景 */
	position: fixed;
	width: 100%;
	height: 100%;
	background: rgba(0,0,0,.5);
	top: 0;
	left: 0;
	z-index: 1000;
}
.sample-popup-content {
	/* ポップアップ本体 */
	display: inline-block;
	position: fixed;
	width: 50%;
	z-index: 1100;
	background: #fff;
	// padding: 2%;
  height:auto;
  width: 40%;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
  min-width: 30%;
}

.poptitle {
  border: 1px solid #ffffff;
  border-top-left-radius: 20px; /* 上左コーナーの半径を設定 */
  border-top-right-radius: 20px; /* 上右コーナーの半径を設定 */
}
.tt {
  width: 80%;
}
.rd {
  margin: auto;
  width:60%
}

.btn {
  width: 40%;
}
</style>

<script setup lang="ts">
import axios from 'axios'
import { ref,reactive, computed, watch } from 'vue';
import type { responseData,eventFLG} from '@/interfaces'
import { useToast } from 'vue-toast-notification';
import { useGetTaskStore } from '@/stores/getTask';

const taskStore = useGetTaskStore()

interface defData {
    title:string,
    status:number,
    id: number,
    category:string,
    pri_id:number,
}

const props = defineProps<defData>()
const TrueOrFalse = ref(props.status)
let newtitle = ref(props.title)
const title  = ref(props.title)
const priority = ref(props.pri_id)
const toast = useToast()
let tasknum : number
const upflg = ref(false)

interface Emits {
	(event:"changetitle",title:string):void
	(event:"changeSwitch",flg:boolean):void
	(event:"showtoast",msg:string,flg:number):void
	(event:"taskstatus",status:string):void
}

const emit = defineEmits<Emits>()
// getで取得したIDを格納する　非同期関数内でreturnした値を使うとundefinedになる
let gid: number;
let recid: number;
const tsMsg = ref("")
let apiUrl = 'http://localhost:8000/tasks/'
const tList = ref([""])
const taskState = ref("")
const category = ref(props.category)
let tFlg:number

const changeStatus = (status: boolean): string => {
  let retStr = ""
  if(status == true){
    retStr = "完了"
  }else if(status == false){
    retStr = "未着手"
  }
  return retStr
}

watch(TrueOrFalse,(newvalue) => {
    if(newvalue == 1){
      taskState.value = '未完'
    }else if(newvalue == 2){
      taskState.value = "完了"
    }else if(newvalue == 3){
      taskState.value = "進行中"
    }
  })

const put = async () : Promise<void> => {
console.log("111",newtitle.value == props.title && TrueOrFalse.value == props.status)
console.log("search ",apiUrl.includes(String(props.id)))
if(apiUrl.includes(String(props.id)) === false){
  apiUrl = `${apiUrl}${props.id}`
}
console.log(apiUrl,"  URL TEST",props.id,"  task NUMBER")
console.log(category.value,"val check")
const response = await axios.put( apiUrl,{
    title: newtitle.value,
    category: category.value,
    status_id:TrueOrFalse.value,
    priority_id:priority.value,
  })
  .then(response => {
    console.log("PUTが成功しました")
    tsMsg.value = "更新完了"
    tFlg = 0
    upflg.value = !upflg.value
    emit("changetitle",newtitle.value)
    emit("changeSwitch",upflg.value)
    emit("taskstatus",taskState.value)
    upflg.value = !upflg.value
  })
  .catch(error => {
    tFlg = 1
    console.log("Failed to update error:",error.response.data.detail)
    tsMsg.value = error.response.data.detail
    toast.error(tsMsg.value ,{
    position:"top"
  })
  })
  emit("showtoast",tsMsg.value,tFlg)
  await taskStore.get()
  }

const popupClose = (): void => {
	emit("changeSwitch",upflg.value)	

}
</script>

