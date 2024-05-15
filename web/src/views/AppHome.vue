<template lang="pug">
div.boxtitle
    h1.prose.text-3xl タスク管理システム
      router-link(:to="{name:'apphome'}").text-xl.mt-2.float-right.text-black.home Home
div  
  router-link(:to="{name:'taskadd'}" v-on:toastFlg="showToast").add.block.mt-4.ml-4.bg-blue.text-xl.text-white.border-solid.border-white.rounded-10px.text-center ＋タスクを追加
div
    taskCompo(v-bind:responseData="globalList" v-on:handFlg="updFlgParent" v-on:delFlgs="delFlgParent")
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
import {useRouter} from "vue-router"
import {computed, onMounted,ref, watch} from "vue"
import { useCounterStore } from "@/stores/counter";
import taskCompo from "./TaskBox.vue"
import TaskAdd from "./TaskAdd.vue";
import axios, { Axios, type AxiosResponse } from 'axios'
import { useToast } from 'vue-toast-notification';

const toast = useToast()
const updFlg = ref(false)
const delFlg = ref(false)
const tList = ref([])
const globalList = ref([])
let apiUrl = 'http://localhost:8000/tasks/'

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
        console.log('POSTリクエストが成功しました');
        console.log('レスポンスデータ:', response.data);
        globalList.value = response.data
        tList.value  =response.data
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
  if(newvalue == true){
    initializeGettitle()
  }
  console.log("emit Complete")
  updFlg.value = false
})

watch(delFlg,(newvalue) => {
  if(newvalue == true){
    initializeGettitle()
  }
  delFlg.value = false
})

const delFlgParent = (flg:boolean) => {
  delFlg.value = flg
}

onMounted(() => {
        initializeGettitle()
    }) 

</script>


