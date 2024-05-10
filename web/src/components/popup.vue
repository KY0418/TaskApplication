<template lang="pug">
div.sample-popup-window
  div.sample-popup-background
    div.sample-popup-box
      div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
        div.boxcomp
          h2.text-white.text-2xl.bg-blue.text-center.poptitle タスクを編集
          label.block.mt-4.ml-4 タスクタイトル
            div.mt-4.ml-10
              input(type="text" v-model="newtitle" placeholder="タスクタイトル").w-60.tt
          label.block.mt-4.ml-4.mr-4 ステータス
            div.mt-4.ml-12
              input(type="radio" v-model="TrueOrFalse" value="1").float-left
              span 未着手
              input(type="radio" v-model="TrueOrFalse" value="2").ml-5
              span 完了
          label.block
            div.mt-4.ml-17
              button(type="button" @click="put").border-solid.border-white.rounded-5px.bg-blue 更新
              button(type="button" @click="popupClose").border-solid.border-white.rounded-5px.bg-red.ml-8.sample-popup-close  キャンセル
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
}
.sample-popup-close {
	/* ポップアップ内の閉じるボタン */
	position: relative;
	background: rgb(255, 0, 0);
	color: #fff;
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
</style>

<script setup lang="ts">
import axios, { Axios, type AxiosResponse } from 'axios'
import { ref,reactive } from 'vue';
import type { responseData,eventFLG,defData} from '@/interfaces'

const props = defineProps<defData>()

const title  = ref(props.title)
const showSwitch = ref(props.popstatus)

interface Emits {
	(event:"changetitle",title:string):void
	(event:"changeSwitch",showSwitch:boolean):void
}
const newtitle = ref("")
const emit = defineEmits<Emits>()
// 新規タスクタイトル
const mainTitle = ref("タスクタイトル")
const TrueOrFalse = ref('')
let show = ref(false)
// getで取得したIDを格納する　非同期関数内でreturnした値を使うとundefinedになる
let gid: number;
let recid: number;
const eveflg = ref(false)
let apiUrl = 'http://localhost:8000/tasks/'
let apiUrlt = 'http://localhost:8000'

const defData = reactive ({
  due_date: "2024-05-07",
  done: false,
})

// 後で戻り値をvoidにする
const getId = async (title:string): Promise<number> => {
  console.log(props.title)
  let retId : number = 0;
  try {
    const response = await axios.get<responseData>(apiUrl,{
    })
   
    const record = Array.prototype.filter.call(response.data,user => {
      return user.title === title
    }) 
    const extractedParameters:{id:number}[] = []
    record.forEach(obj => {
      extractedParameters.push({
        id: obj.id,
      });
    });
    const id = extractedParameters.map(param => param.id)
    retId = id[0]
    gid = id[0]
    recid = gid
    console.log(typeof(retId))
  }catch(error){
    console.error('Failed to get users:', error);
  } 
  return retId
};

const put = async () : Promise<void> => {
  const id = await getId(props.title).then(id => {
    console.log('Idaaaa:',id,typeof(id))
    })
  // if(TrueOrFalse.value == "2"){
  //   props.done = true
  // }ステータスの選択肢が３つ以上になったら使う
  apiUrl = `${apiUrlt}/tasks/${gid}`
  console.log(apiUrl)
  console.log(props.title)
  const response = axios.put( apiUrl,{
    title: newtitle.value,
    due_date: "2024-05-08",
  })
  .then(response => {
    console.log("PUTが成功しました")
  })
  .catch(error => {
    console.error("Failrd to update error:",error)
  })
  console.log(props.title)
  emit("changetitle",newtitle.value)
  emit("changeSwitch",props.popstatus)
}

const popupClose = (): void => {
	emit("changeSwitch",props.popstatus)
	
}


</script>

