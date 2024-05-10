<script setup lang="ts">
import axios, { Axios, type AxiosResponse } from 'axios'
import { ref,reactive,computed, onMounted } from 'vue';
import type { responseData,eventFLG,defData} from '@/interfaces'
import popup from "../components/popup.vue"
import taskContent from "../components/taskContent.vue"

// 検索対象のタイトル
const tasktitle = ref("")
const status = ref("")
// 新規タスクタイトル
const mainTitle = ref("タスクタイトル")
let show = ref(false)
// getで取得したIDを格納する　非同期関数内でreturnした値を使うとundefinedになる
let gid: number;
let recid: number;
let globalTitle: string

const defData = reactive ({
  title: ref(''),
  due_date: "2024-05-10",
  done: false
})

let apiUrl = 'http://localhost:8000/tasks/'
let apiUrlt = 'http://localhost:8000'

const initializeGettitle = async (): Promise<void> => {
  const response = await axios.get(apiUrl,{
    })
  const obj = response.data[0]
  console.log(obj.title)
  tasktitle.value = obj.title
}



// 後で戻り値をvoidにする
const getId = async (title:string): Promise<number> => {
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

const delt = async (): Promise<void> => {
  const id = await getId(tasktitle.value).then(id => {
    console.log('Idaaaa:',id,typeof(id))
    })
  apiUrl = `${apiUrlt}/tasks/${gid}`
  console.log(apiUrl)
  const response = await axios.delete(apiUrl)
  .then(response =>{
    console.log("deleteが成功しました")
  })
  .catch(error => {
    console.error("Failrd to delete error:",error)
  })
}

const changeTitle = (newTitle:string): void => {
  console.log(newTitle)
  tasktitle.value = newTitle
}

const changeStatus = (newstatus: string) : void => {
  if(status.value == newstatus && newstatus != null){
    console.log("no change")
  }else if(newstatus == "未着手"){
    newstatus = "完了"
  }else{
    newstatus = "未着手"
  }

}

const changeSwitch = (): void => {
  show.value = !show.value
}
onMounted(() => {
        initializeGettitle()
    })
</script>

<template lang="pug">
div.border-solid.border-red.rounded-25px.m-4.w-70.taskBox
    p.text-red.mt-2.ml-2 {{ mainTitle }}
    div.taskCont
      taskContent(v-bind:popupstatus="show" v-bind:title="tasktitle" v-bind:status="status" v-on:createTitle="changeTitle" v-on:changeState="changeStatus" v-on:changePopupStatus="changeSwitch" )
      button(type="button" @click="initializeGettitle") aaa
      pre {{ tasktitle }}
div(v-if="show")
  popup( v-bind:title="tasktitle" v-bind:popstatus="show" v-on:changetitle="changeTitle" v-on:changeSwitch="changeSwitch")                      
            
</template>
<style lang="scss" scoped>
input {
  border: none;
  outline: none;
}
.taskCont {
  margin:auto;
}
</style>