<template lang="pug">
p.mt-5.ml-5.text-xl タスク追加
  div.border-solid.rounded-22px.border-gray.ml-6.mt-4.mb-4.w-145
    table
        tr
          td.pt-2.pb-2.pl-2.tr1
              label(for="postdata")  タスクタイトル：
                input(type="text" name="sample" id="postdata" v-model="defData.title").ml-8.w-93.te
        tr
          td.pt-2.pb-2.pl-2
            label(for="radioGroup") ステータス：
              input(type="radio" id="radioGroup" v-model="TrueOrFalse" value="1").ml-35
              span.mr-2 未着手
              input(type="radio" id="radioGroup" v-model="TrueOrFalse" value="2" )
              span 完了
div.ml-120
    button(type="button" @click="post").border-solid.rounded-15px.border-white.text-white.p-1 タスク追加
    
router-link(:to="{name:'apphome'}") ホーム画面へ   
</template>

<style lang="scss" scoped>
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
</style>

<script setup lang="ts">
import axios from 'axios'
import { ref,reactive} from 'vue';
import { useRouter } from 'vue-router';
import type {defData,Emits} from '../interfaces'

const router = useRouter()
let eveflg = false

const TrueOrFalse = ref(0)
const defData = reactive ({
  title: ref(''),
  due_date: "2024-05-07",
  done: false
})



const apiUrl = 'http://localhost:8000/tasks';

const post = async () : Promise<any> => {
  
  if (TrueOrFalse.value == 2){
    defData.done = true
  }else {
    defData.done = false
  }
  console.log(defData.done)
  await axios.post(apiUrl, defData)
  .then(response => {
    if (response.status === 200 || response.status === 201) {
      eveflg = true
      console.log(eveflg)
      console.log('POSTリクエストが成功しました');
      console.log('レスポンスデータ:', response.data);
    } else {
      console.error('POSTリクエストが失敗しました:', response.status, response.data);
    }
  })
  .catch(error => {
    eveflg = false
    console.error('POSTリクエスト中にエラーが発生しました:', error);
  })
  
  succeedAddTask(eveflg)
}
const InputTitle = (): void => {
  console.log(defData.title)
}

function succeedAddTask(flg: boolean): void  {
  if(flg == true){
    console.log("aaaaaa")
    router.push({name:"apphome"})
  }
}

</script>