<template lang="pug">
div.boxtitle
    h1.prose.text-3xl タスク管理システム
      button(@click="changehomeFlg").text-xl.mt-2.float-right.home Home
div(v-if="homeflg==1")  
  button( @click="addTask").add.mt-4.ml-4.bg-blue.text-xl.border-solid.rounded-10px ＋タスクを追加
  div(v-if="homeflg==1")
    taskCompo(v-bind:responseData="globalList")
div 
  TaskAdd(v-if="taskaddFlg==1" v-on:toastFlg="showToast" v-bind:responseData="tList")
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
}

.add {
  border-style: none;
}
</style>

<script setup lang="ts">
import {useRouter} from "vue-router"
import {computed, onMounted,ref} from "vue"
import { useCounterStore } from "@/stores/counter";
import taskCompo from "./taskCompo.vue"
import TaskAdd from "./TaskAdd.vue";
import axios, { Axios, type AxiosResponse } from 'axios'
import { useToast } from 'vue-toast-notification';

const toast = useToast()

const tList = ref([])
const taskaddFlg = ref(2)
const homeflg = ref(1)
const globalList = ref([])
let apiUrl = 'http://localhost:8000/tasks/'

const showToast = (msg: string): void => {
  taskaddFlg.value = 2
  homeflg.value = 1
  toast.success(msg,{
    position:"top",
    queue:false
  })
}

const addTask = () : void => {
  taskaddFlg.value = 1
  homeflg.value = 2
}

const changehomeFlg = (): void => {
  homeflg.value = 1
  taskaddFlg.value = 2
}

const initializeGettitle = async (): Promise<void> => {
  const response = await axios.get(apiUrl,{
    })
  globalList.value = response.data
  tList.value = response.data
  console.log(globalList.value)
}

onMounted(() => {
        initializeGettitle()
    }) 

</script>


