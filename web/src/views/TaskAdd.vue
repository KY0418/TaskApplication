<template lang="pug">
div.boxtitle
    h1.prose.text-3xl タスク管理システム
      router-link(:to="{name:'apphome'}").text-xl.mt-2.float-right.text-black.home Home
div
  p.mt-5.ml-5.text-xl タスク追加
    div.border-solid.rounded-22px.border-gray.ml-6.mt-4.w-180
      div.tt.mt-2.mb-2
        span.pt-2.ml-2.bor タスクタイトル
        input(type="text" name="sample" id="postdata" v-model="defData.title").ml-8.w-90.te
      div.tr1
      div.ml-2.mt-2.mb-2
        span 職員名
          select(v-model="st_name" ).cat.rounded-8px.ml-47.w-30
            option(v-for="item in staffList" :value="item.staff_id" :selected="st_name") {{ item.staff_name }}
      div.tr1
      div.ml-2.mt-2.mb-2
        span カテゴリー        
        select(v-model="category").cat.rounded-8px.ml-35.w-30
          option(value="仕事") 仕事
          option(value="プライベート") プライベート
          option(value="完了") 完了
      div.tr1 
      
      div.ml-2.mt-2.mb-2
        span 優先度
          select(v-model="importanceId").cat.rounded-8px.ml-47.w-30
            option( value="1" ) 緊急度高、緊急度高
            option( value="2" ) 緊急度高、緊急度低
            option( value="3" ) 緊急度低、緊急度高
            option( value="4" ) 緊急度低、緊急度低
      div.tr1
      div.ts.mt-2.mb-2
        span.mt-2.ml-2.mb-2.bor ステータス
          input(type="radio"  v-model="statusNum" value="1" checked).ml-35
          span.mr-2 未着手
          input(type="radio" v-model="statusNum" value="2" )
          span 完了
          input(type="radio" v-model="statusNum" value="3" )
          span 進行中
div.ml-120
    button(type="button" @click="post").border-solid.rounded-10px.border-white.text-white.text-xl.mt-2.p-1.bg-blue-8 +タスクを追加   
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
  border-style: none;
  text-decoration: none;
}
#postdata{
  border: none;
}

#postdata:focus {
  outline: none;

}

.cat{
  text-align: center;
  width:30%;
}

.tr1 {
  border-top-style:solid;
  border-right: solid;
  border-color: rgb(9, 85, 151);
}

// .te::before{
//   content: "";
//   width:1px;
//   height: 5px;
//   border-right-style: solid;
//   border-color: rgb(9, 85, 151);
// }

button{
  margin-left: 27%;
}

.tr2{
  display: inline;
  border-right-style: solid;
  
}

// .bor{
//   display:inline;
//   border-right-style:solid;
// }

.te:focus {
  background-color: white;
}
</style>

<script setup lang="ts">
import axios from 'axios'
import { ref,reactive,onMounted} from 'vue';
import ToastPlugin from 'vue-toast-notification';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toast-notification';
import { useGetStaffStore } from '@/stores/getStaffData';
import { collapseTextChangeRangesAcrossMultipleVersions, isConditionalExpression } from 'typescript';
import type { Ref } from 'vue';
import { usegetImportStore } from '@/stores/getImportance';

const toast = useToast()

const importanceData = usegetImportStore()

const staffData = useGetStaffStore()

const aaa = (): string => {
  staffData.get()
  const a = ref([])
  for(let i of staffData.$state.data){
    console.log(i)
    if(a.value.length == 0){
      a.value = i['staff_name']
    }
  }
  console.log(a.value)
  return a.value[0]
}

const importanceId = ref(1)
console.log(importanceId.value)
// 職員の名前
const st_name = ref("職員を選んでください")
staffData.get()
const test = aaa()
st_name.value = test

console.log(st_name.value)

interface Emits {
  (event:"toastFlg",msg:string):void
}

const emit = defineEmits<Emits>()

const staffList = staffData.data

const tList = ref([""])

// トーストのメッセージ
const tsMsg = ref("")

// Routerのインスタンス
const router = useRouter()

// PUT成功・失敗フラグ
let eveflg = false
let eveflgno = false
// taskのステータス（ステータスが3個以上になったときのために数字で分別）
const statusNum = ref("1")

// タスクのステータス
const taskStatus = ref(false)

// タスクのカテゴリー
const category = ref('仕事')

const pri_sort = ref()

console.log(category.value)
// リクエスト先のURL
const apiUrl = 'http://localhost:8000/tasks';

// POSTデータ 画面のデータと連携している変数
const defData = reactive ({
  title: ref(""),
  id:statusNum.value
})

// POST成功時にタスク一覧画面に遷移する　失敗時はERRORトーストを表示
function succeedAddTask(flg: boolean): void  {
  if(flg == false){
    tsMsg.value = "登録完了"
    router.push({name:"apphome"})
    emit("toastFlg",tsMsg.value)
  }
}
const impData = ref()
const getData = async () : Promise<void> => {
  const response = await axios.get(apiUrl)
  const titleList = response.data
  console.log(titleList)
  for(const title of titleList){
    tList.value.push(title.title)
    tList.value = tList.value.filter((title) =>  title !== "")
    // console.log(title.title)
    // console.log(tList.value)
  }
  console.log(importanceId.value)
  await importanceData.get(importanceId.value as number)
  impData.value = importanceData.data[0].id
}

// const getStatus = async (stId:number): Promise<void> => {
//   const apiUrlStatusGet = `${apiUrl}${stId}`
//   const response = await axios.get(apiUrlStatusGet)
//   const stName = response.data
  
// }

// POST関数
const post = async () : Promise<any> => {
  await getData()
  console.log(tList.value)
  console.log(defData.title)
  console.log(st_name.value)
  console.log(impData.value)
  console.log(importanceId.value)
  // eveflgno = defData.title === "" ? true : false
  // eveflg = tList.value.includes(defData.title)
  console.log(statusNum.value)
    const resopnse = await axios.post(apiUrl, {
      title:defData.title,
      category:category.value,
      status_id:Number(statusNum.value),
      staff_id:st_name.value,
      priority_id:impData.value,
    })
    .then(response => {
      if (response.status === 200 || response.status === 201) {
        console.log('POSTリクエストが成功しました');
        console.log('レスポンスデータ:', response.data);
        window.localStorage.setItem('tflg',"success")
        succeedAddTask(eveflg)
    }
  })
    .catch(error => {
      console.error('POSTリクエスト中にエラーが発生しました:', error);
      // error.response.data.detail = "タスクは既に存在しています"
      toast.error(`${error.response.data.detail}`,{
        position:"top"
      })
    })
   
    // succeedAddTask(eveflg)
  // }else if(eveflg == true || eveflgno == true) {
  //   toast.error("そのタスクは既に存在しているか、タイトルが空になっています",{
  //     position:"top"
  //   })
  // }

}
</script>