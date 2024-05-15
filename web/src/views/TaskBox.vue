<template lang="pug">
div.border-solid.border-red.rounded-25px.m-4.w-70.taskBox
    input(type="text" v-model="mainTitle").text-red.mt-2.ml-2.tb 
    div.taskCont
      taskContent(v-for="item in props.responseData" v-bind:title="item.title" v-bind:status="item.done" v-bind:id="item.id"
                  v-on:createTitle="changeTitle" v-on:changeState="changeStatus" v-on:changePopupStatus="changeSwitch" v-on:updateId="updateId" v-on:showtoast="showToast"
                  v-on:handData="getUpdFlg" v-on:delFlg="delFlgSecond")

</template>
<style lang="scss" scoped >
input {
  border: none;
  outline: none;
}
.taskBox {
  background-color: #FFE382;
}

.tb {
  outline: none;
  background-color: #FFE382;}

</style>      
<script setup lang="ts">
import { ref, watch } from 'vue';
import taskContent from "../components/TaskContent.vue"
import { useToast } from 'vue-toast-notification';

// 検索対象のタイトル
const tasktitle = ref("")
// タスクのステータス
const taskstatus = ref("") 
const status = ref(false)
// 新規タスクタイトル
const mainTitle = ref("タスクタイトル")
// レコードを検索するためのID
const searchId = ref(0)
// 編集ポップアップ表示のフラグ
let show = ref(false)
// トーストのインスタンス
const toast = useToast()
const updFlgSon = ref(false)
const delFlgSon = ref(false)
// Propsデータを受け取るためのinterface
interface defData {
  responseData: {
    title: string
    due_date: string
    id: number
    done: boolean
  }[]
}

interface Emits {
  (event:"handFlg",flg:boolean):void
  (event:"delFlgs",delflg:boolean):void
}

const emit = defineEmits<Emits>()

const getUpdFlg = (flg:boolean): void => {
  updFlgSon.value = flg
  console.log("emit2 ",flg)
}

const value:string | null = window.localStorage.getItem('tflg')
console.log(value)
if(value === "success"){
  toast.success("登録成功",{
    position:"top"
  })
  window.localStorage.setItem('tflg','def')
}

watch(updFlgSon,() => {
  emit("handFlg",updFlgSon.value)
  console.log("emit2")
  updFlgSon.value = false
})

const delshow = ref(false)

// Props受け取りデータ格納変数
const props = defineProps<defData>()

// リクエスト先のURL
let apiUrl = 'http://localhost:8000/tasks/'

// 以下の5つの関数はemitで受け取った値を処理する
const changeTitle = (newTitle:string): void => {
  console.log(newTitle)
  tasktitle.value = newTitle
  console.log(tasktitle.value)
}

const changeStatus = (newstatus: boolean) : void => {
  status.value = newstatus
}

const changeSwitch = (): void => {
  show.value = !show.value
}

const updateId = (newid: number): void => {
  searchId.value = newid
  console.log(searchId.value)
}

const showToast = (msg:string,flg:number): void => {
  if(flg == 0){
    toast.success(msg,{
      position:"top"
    })
  }else if(flg == 1){
    toast.error(msg,{
      position:"top"
    })
  }
}

const showToastPut = (msg:string): void => {
  if(msg === "更新完了"){
    toast.success(msg,{
      position:"top",
      pauseOnHover:false,
      queue:false
    })
  }else if(msg === "更新失敗"){
    toast.error(msg,{
      position:"top",
      pauseOnHover:false,
      queue: false

    })
  }
}

watch(delFlgSon,() => {
  emit("delFlgs",delFlgSon.value)
  console.log("emit2")
  delFlgSon.value = false
})

const delFlgSecond = (delFlg:boolean) => {
  delFlgSon.value = delFlg
}

</script>
