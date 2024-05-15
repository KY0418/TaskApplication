<template lang="pug">
div.boxtitle
    h1.prose.text-3xl タスク管理システム
      router-link(:to="{name:'apphome'}").text-xl.mt-2.float-right.text-black.home Home
div
  p.mt-5.ml-5.text-xl タスク追加
    div.border-solid.rounded-22px.border-gray.ml-6.mt-4.mb-4.w-145
      table
          tr
            td.pt-2.pb-2.pl-2.tr1
                label(for="postdata")  タスクタイトル：
                  input(type="text" name="sample" id="postdata" v-model="defData.title").ml-8.w-93.te
          tr
            td.pt-2.pb-2.pl-2
              label ステータス：
                input(type="radio"  v-model="TrueOrFalse" value="false" checked).ml-35
                span.mr-2 未着手
                input(type="radio" v-model="TrueOrFalse" value="true" )
                span 完了
div.ml-120
    button(type="button" @click="post").border-solid.rounded-15px.border-white.text-white.p-1 タスク追加   
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

.tr1 {
  border-bottom-style:solid ;
  border-color: aliceblue;
}

button{
  background-color: #0000FF;
}

.te:focus {
  background-color: white;
}
</style>

<script setup lang="ts">
import axios from 'axios'
import { ref,reactive} from 'vue';
import ToastPlugin from 'vue-toast-notification';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toast-notification';

const toast = useToast()

interface Emits {
  (event:"toastFlg",msg:string):void
}

const emit = defineEmits<Emits>()

// Propsデータを受け取るためのinterface
interface defData {
  responseData: {
    title: string
    due_date: string
    id: number
    done: boolean
  }[]
}

const props = defineProps<defData>()

const tList = ref([""])

// トーストのメッセージ
const tsMsg = ref("")

// Routerのインスタンス
const router = useRouter()

// PUT成功・失敗フラグ
let eveflg = false
let eveflgno = false
// taskのステータス（ステータスが3個以上になったときのために数字で分別）
const TrueOrFalse = ref(false)

// タスクのステータス
const taskStatus = ref(false)

// リクエスト先のURL
const apiUrl = 'http://localhost:8000/tasks';

// POSTデータ
const defData = reactive ({
  title: ref(""),
  due_date: "2024-05-13",
  done:TrueOrFalse.value
})

// POST成功時にタスク一覧画面に遷移する　失敗時はERRORトーストを表示
function succeedAddTask(flg: boolean): void  {
  if(flg == false){
    tsMsg.value = "登録完了"
    router.push({name:"apphome"})
    emit("toastFlg",tsMsg.value)
  }
}

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
}

// POST関数
const post = async () : Promise<any> => {
  await getData()
  console.log(tList.value)
  console.log(defData.title)
  // eveflgno = defData.title === "" ? true : false
  // eveflg = tList.value.includes(defData.title)
  console.log(eveflg)
  if (TrueOrFalse.value == true){
    defData.done = true
  }else {
    defData.done = false
  }
    const resopnse = await axios.post(apiUrl, {
      title:defData.title,
      due_date:"2024-05-13",
      done:TrueOrFalse.value,
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
      error.response.data.detail = "タスクは既に存在しています"
      toast.error(error.response.data.detail,{
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