<template lang="pug">
div.border-solid.border-red.rounded-25px.m-4.w-70.taskBox
    input(type="text" v-model="mainTitle").text-red.mt-2.ml-2.tb 
    div.taskCont
      taskContent(v-for="item in props.responseData" v-bind:popupstatus="show" v-bind:title="item.title" v-bind:status="item.done" v-bind:id="item.id"
                  v-on:createTitle="changeTitle" v-on:changeState="changeStatus" v-on:changePopupStatus="changeSwitch" v-on:updateId="updateId" v-on:showtoast="showToast")
div(v-show="show")
  popup( v-bind:title="tasktitle" v-bind:popstatus="show" v-bind:id="searchId" v-bind:status="false"  
        v-on:changetitle="changeTitle" v-on:changeSwitch="changeSwitch" v-on:showtoast="showToastPut")                      
            
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
import { ref } from 'vue';
import popup from "../components/popup.vue"
import taskContent from "../components/taskContent.vue"
import { useToast } from 'vue-toast-notification';

// 検索対象のタイトル
const tasktitle = ref("")
// タスクのステータス
const taskstatus = ref("") 
const status = ref()
// 新規タスクタイトル
const mainTitle = ref("タスクタイトル")
// レコードを検索するためのID
const searchId = ref(0)
// 編集ポップアップ表示のフラグ
let show = ref(false)
// トーストのインスタンス
const toast = useToast()
// Propsデータを受け取るためのinterface
interface defData {
  responseData: {
    title: string
    due_date: string
    id: number
    done: boolean
  }[]
}

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

const showToast = (msg:string): void => {
  if(msg === "削除完了"){
    toast.success(msg,{
      position:"top",
      pauseOnHover:false
    })
  }else if(msg === "削除失敗"){
    toast.error(msg,{
      position:"top",
      pauseOnHover:false
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
</script>
