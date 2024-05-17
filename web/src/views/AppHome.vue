<template lang="pug">
div.boxtitle
    h1.prose.text-3xl タスク管理システム
      router-link(:to="{name:'apphome'}").text-xl.mt-2.float-right.text-black.home Home
router-link(:to="{name:'taskadd'}" v-on:toastFlg="showToastPost").add.block.mt-4.ml-4.mb-4.bg-blue.text-xl.text-white.border-solid.border-white.rounded-10px.text-center ＋タスクを追加
div
  TaskBox(v-for="item in workListTr" v-bind:responseData="item" v-bind:flg="tList" v-bind:msg="'仕事'" v-on:handFlg="updFlgParent" v-on:delFlgs="delFlgParent")
//- div(v-if="privateTasks")
//-   TaskBox(v-bind:responseData="privateTasks" v-bind:flg="tList" v-bind:msg="'プライベート'" v-on:handFlg="updFlgParent" v-on:delFlgs="delFlgParent")
//- div(v-if="completeTasks")
//-   TaskBox(v-bind:responseData="completeTasks" v-bind:flg="tList" v-bind:msg="'完了'" v-on:handFlg="updFlgParent" v-on:delFlgs="delFlgParent")
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
  text-decoration: none;
}

.add {
  text-decoration: none;
  width:15%;
}
</style>

<script setup lang="ts">
import { RouterView} from "vue-router";
import {useRouter} from "vue-router"
import {computed, onMounted,reactive,ref, toValue, watch, getCurrentInstance, VueElement} from "vue"
import { useCounterStore } from "@/stores/counter";
import TaskBox from "./TaskBox.vue"
import TaskAdd from "./TaskAdd.vue";
import axios, { Axios, type AxiosResponse } from 'axios'
import { useToast } from 'vue-toast-notification';

const toast = useToast()
const updFlg = ref(false)
const delFlg = ref(false)
const tList = ref(false)
const globalList = ref([])
let apiUrl = 'http://localhost:8000/tasks/'
const completeTasks = ref([])
const privateTasks: {value: Task[]} = reactive({ value: [] })
const workTasks:{value: Task[]} = reactive({ value: [] })
const workListTr :{ value: Task[] } = ref([])
const upd = ref(1)


interface Task {
  title: string;
  due_date: string;
  done: boolean;
  category: string;
  id: number;
}


// タスク追加のトースト表示
const showToast = (msg: string): void => {
  toast.success(msg,{
    position:"top",
    queue:false
  })
}

// updateフラグの変更
const updFlgParent = (flg:boolean): void => {
  updFlg.value = flg
}

// GETで最新のデータを取得する
const initializeGettitle = async (): Promise<void> => {
  const response = await axios.get(apiUrl,{
    })
    .then(response =>{
      if (response.status === 200 || response.status === 201) {
        console.log('リクエストが成功しました');
        console.log('レスポンスデータ:', response.data);
        globalList.value = response.data
        const workList = ref([])
        console.log(workList.value)
        // completeTasks.value = globalList.value.filter((task) => task["category"] === "complete")
        privateTasks.value = globalList.value.filter((task) => task["category"] === "プライベート")
        workTasks.value = globalList.value.filter((task) => task["category"] === "仕事")
        if(workTasks.value.length > 0){
          workList.value.push(workTasks.value as never)
        }
        if(privateTasks.value.length > 0){
          workList.value.push(privateTasks.value as never)
        }
        console.log(workTasks.value,"work")
        console.log(privateTasks.value,"private")
        workListTr.value = workList.value
        tList.value = !tList.value
        console.log(workList.value,"送信データ")
        tList.value = !tList.value
        console.log(globalList.value,"GET OK")
    }
  })
    .catch(error => {
      console.error('GETリクエスト中にエラーが発生しました:', error);
      error.response.data.detail = "タスクがありません"
      toast.error(error.response.data.detail,{
        position:"top"
      })
    })   
}


// updateフラグ変数の監視
watch(updFlg,(newvalue) => {
  console.log(newvalue)
  tList.value = !tList.value
  initializeGettitle()
  console.log("emit Complete")
  window.location.reload()
  // methodThatForcesUpdate()
  updFlg.value = false
})
// deleteフラグ変数の監視
watch(delFlg,(newvalue) => {
    console.log("delemit complete")
    initializeGettitle()
    delFlg.value = false
    tList.value = !tList.value
})

const showToastPost = (msg: string): void => {
  toast.success(msg,{
    position:"top",
    queue:false
  })
}

const delFlgParent = (flg:boolean) => {
  delFlg.value = flg
}

// const methodThatForcesUpdate = () => {
//   const instance = getCurrentInstance();
//   instance.proxy.$forceUpdate()
//   console.log("test")
// };

onMounted(() => {
  console.log("test2222")
        initializeGettitle()
    }) 

</script>


