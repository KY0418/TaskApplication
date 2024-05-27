<template lang="pug">
div.whole
  div.border-solid.border-red.rounded-25px.ml-4.w-70.float-left.taskBox
      p.text-red.mt-2.ml-2.w-30.tb {{ catTitle }} 
      div
        TaskContent(v-for="item in props.responseData" v-bind:title="item.title" v-bind:status="item.status_id" :id="item.id" :category="item.category" :st_id="item.staff_id" :pri_id="item.priority_id"
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

.add {
  text-decoration: none;
  width:15%;
}


</style>      
<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue';
import TaskContent from "../components/TaskContent.vue"
import { useToast } from 'vue-toast-notification';
import { useGetTaskStore } from '@/stores/getTask';


const task_store = useGetTaskStore()
// 検索対象のタイトル
const tasktitle = ref("")     
// タスクのステータス
const taskstatus = ref("") 
const status = ref(false)
// カテゴリータイトル
const catTitle = ref('')
// レコードを検索するためのID
const searchId = ref(0)
// 編集ポップアップ表示のフラグ
let show = ref(false)
// トーストのインスタンス
const toast = useToast()
// updateフラグ
const updFlgSon = ref(false)
// deleteフラグ
const delFlgSon = ref(false)
// カテゴリーごとのタスクを検索するための配列
const categoryList = ['']
const getFlg = ref(false)
//　フラグ（名前変える）
let changetitle = ref(false)
const completeTaks = ref({})
// カテゴリーがプライベートのタスクを格納
const privateTaks = ref({})
// カテゴリーが仕事のタスクを格納
const workTasks = ref({})
// Propsデータを受け取るためのinterface
interface defData {
  responseData: {
    title: string
    id: number
    status_id: number
    category:string
    staff_id:string
    priority_id:number
  }[],
  flg:boolean
}

// Props受け取りデータ格納変数
const props = defineProps<defData>()
const catList = props.responseData.map((task) => task.category)
const catListSt = props.responseData.map((task) => task.status_id)
console.log(catList)
catTitle.value = catList[0]
if(catListSt[0] == 2){
  catTitle.value = "完了"
}
console.log(catTitle.value)
// 親コンポーネントでGETが完了したかどうか監視する
// const isFlgChanged = computed(() => props.flg);
// console.log(props.responseData)
// watch(isFlgChanged, () =>{
//   const catList = props.responseData.map((task) => task.category)
//   catTitle.value = catList[0]
//   console.log(catTitle.value)
  // for(const i of props.responseData){ 
  //   if(categoryList.includes(i.category) === false){
  //     categoryList.push(i.category)
  //   }
  // console.log(categoryList)
  // console.log(props.responseData,"test")
  // // completeTaks.value = props.responseData.filter((task) => task.category === "complete")
  // privateTaks.value = props.responseData.filter((task) => task.category === "private")
  // workTasks.value = props.responseData.filter((task) => task.category === "work")

  // console.log(workTasks.value)

  // changetitle.value = false
  // }
// })


const handingData = ref(props.responseData)

watch(props.responseData,(newvalue)=>{
  handingData.value = newvalue
  console.log("test watch")
})

interface Emits {
  (event:"handFlg",flg:boolean):void
  (event:"delFlgs",delflg:boolean):void
}

const emit = defineEmits<Emits>()

const getUpdFlg = (flg:boolean): void => {
  updFlgSon.value = flg
  console.log("emit2 ",flg)
}

// よく分からない
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


// リクエスト先のURL
let apiUrl = 'http://localhost:8000/tasks/'

// タスク追加のトースト表示
const showToastPost = (msg: string): void => {
  toast.success(msg,{
    position:"top",
    queue:false
  })
}

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

// showtoastに合わせれば消せる
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
  console.log("delemit3",delFlgSon.value)
  delFlgSon.value = false
})

const delFlgSecond = (delFlg:boolean) => {
  delFlgSon.value = delFlg
}

</script>
