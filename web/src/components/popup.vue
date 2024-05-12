<template lang="pug">
div.sample-popup-window
  div.sample-popup-background
    div.sample-popup-box
      div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
        div.boxcomp
          h2.text-white.text-2xl.bg-blue.text-center.poptitle タスクを編集
          label.block.mt-4.ml-4 タスクタイトル
            div.mt-4.ml-10
              input(type="text" v-model="newtitle" :placeholder="props.title").w-60.tt
          label.block.mt-8.ml-4.mr-4.mb-4 ステータス
            div.mt-4.ml-12.rd
              input(type="radio" v-model="TrueOrFalse" value="false" checked).float-left
              span 未着手
              input(type="radio" v-model="TrueOrFalse" value="true").ml-5
              span 完了
          label.block
            div.mt-4.ml-17.rd
              button(type="button" @click="put").border-solid.border-white.rounded-5px.bg-blue 更新
              button(type="button" @click="popupClose").border-solid.border-white.rounded-5px.bg-red.ml-8.float-right.sample-popup-close  キャンセル
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
  height:55%;
  width: 40%;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
  min-width: 30%;
}
.sample-popup-close {
	/* ポップアップ内の閉じるボタン */
	position: relative;
	background: rgb(255, 0, 0);
	padding: 0 1em;
	border-radius: 3px;
	cursor: pointer;

}
#sample-popup-switch:checked ~ .sample-popup-background, #sample-popup-switch:checked ~ .sample-popup-box {
	/* ポップアップ･透過背景を閉じる */
	display: none;
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
  margin: 0 auto;
  width:50%
}
</style>

<script setup lang="ts">
import axios from 'axios'
import { ref,reactive } from 'vue';
import type { responseData,eventFLG} from '@/interfaces'
import { useToast } from 'vue-toast-notification';

interface defData {
    title:string,
    status:boolean,
    popstatus:boolean,
    id: number
}

const props = defineProps<defData>()

const TrueOrFalse = ref(false)
const title  = ref(props.title)
const showSwitch = ref(props.popstatus)
const toast = useToast()

interface Emits {
	(event:"changetitle",title:string):void
	(event:"changeSwitch",showSwitch:boolean):void
	(event:"showtoast",msg:string):void

}
const newtitle = ref("")
const emit = defineEmits<Emits>()
// getで取得したIDを格納する　非同期関数内でreturnした値を使うとundefinedになる
let gid: number;
let recid: number;
const tsMsg = ref("")
let apiUrl = 'http://localhost:8000/tasks/'
const tList = ref([""])

const defData = reactive ({
  due_date: "2024-05-13",
  done: false,
})


const changeStatus = (status: boolean): string => {
  let retStr = ""
  if(status == true){
    retStr = "完了"
  }else if(status == false){
    retStr = "未着手"
  }
  return retStr
}

const getData = async () : Promise<void> => {
  const response = await axios.get(apiUrl)
  const titleList = response.data
  for(const title of titleList){
    tList.value.push(title.title)
    tList.value = tList.value.filter((title) => title !== props.title && title !== "")
    console.log(title.title)
    console.log(tList.value)
  }
}

const put = async () : Promise<void> => {
  await getData()
  let flg = tList.value.includes(newtitle.value)
  apiUrl = `${apiUrl}${props.id}`
  console.log(apiUrl)
  console.log(props.id)
  console.log(tList.value)
  if(flg == true){
    toast.error("そのタスクは既に存在しています" ,{
      position:"top"
    })
  }else if(flg == false){
    if(newtitle.value == ""){
      newtitle.value = props.title
    }
    console.log(TrueOrFalse.value)
    const response = await axios.put( apiUrl,{
      title: newtitle.value,
      due_date: "2024-05-13",
      done:TrueOrFalse.value,
    })
    .then(response => {
      console.log("PUTが成功しました")
      tsMsg.value = "更新完了"
    })
    .catch(error => {
      console.error("Failed to update error:",error)
      tsMsg.value = "更新失敗"
    })
    console.log(props.title)
    emit("changetitle",newtitle.value)
    emit("changeSwitch",props.popstatus)
    emit("showtoast",tsMsg.value)
  }
}

const popupClose = (): void => {
	emit("changeSwitch",props.popstatus)	
}
</script>

