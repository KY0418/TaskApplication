<template lang="pug">
router-link(:to="{name:'taskadd'}"  data-cy="add").add.block.mt-4.ml-4.mb-4.bg-blue.text-xl.text-white.border-solid.border-white.rounded-10px.text-center ＋タスクを追加
div
  TaskBox(v-for="item in workListTr" :responseData="item" :flg="tList"  v-on:delFlgs="delFlgParent" @delflgs="delFlgParent" @updflg="watchUpdFlg")
</template>
<style lang="scss" scoped>
.add {
  text-decoration: none;
  width: 15%;
}
</style>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import { useRouter } from 'vue-router'
import { computed, onMounted, reactive, ref, watch } from 'vue'
import TaskBox from '../components/Task/TaskBox.vue'
import TaskAdd from './TaskAdd.vue'
import axios, { Axios, type AxiosResponse } from 'axios'
import { useToast } from 'vue-toast-notification'
import { useGetStaffStore } from '../stores/getStaffData'
import { useGetTaskStore } from '@/stores/getTask'
import { usegetImportStore } from '@/stores/getImportance'

const get_staff = useGetStaffStore()
const importance_store = usegetImportStore()
const toast = useToast()
const updFlg = ref(false)
const delFlg = ref(false)
const tList = ref(false)
const globalList = ref([])
const completeTasks = ref([])
const privateTasks: { value: Task[] } = reactive({ value: [] })
const workTasks: { value: Task[] } = reactive({ value: [] })
const workListTr: { value: Task[] } = ref([])

const get_task = useGetTaskStore()

interface Task {
  title: string
  category: string
  id: number
  status_id: number
  priority_id: number
}

// タスク追加のトースト表示
const showToast = (msg: string): void => {
  toast.success(msg, {
    position: 'top',
    queue: false
  })
}

// updateフラグの変更
const updFlgParent = (flg: boolean): void => {
  updFlg.value = flg
}

// GETで最新のデータを取得する
const initializeGettitle = async (): Promise<void> => {
  globalList.value = get_task.data
  completeTasks.value = globalList.value.filter((task) => task['status_id'] == 2)
  completeTasks.value.sort((a, b) => a['priority_id'] - b['priority_id'])
  privateTasks.value = globalList.value.filter(
    (task) => task['category'] === 'プライベート' && task['status_id'] != 2
  )
  privateTasks.value.sort((a, b) => a['priority_id'] - b['priority_id'])
  workTasks.value = globalList.value.filter(
    (task) => task['category'] === '仕事' && task['status_id'] != 2
  )
  workTasks.value.sort((a, b) => a['priority_id'] - b['priority_id'])
  const workList = ref([])
  if (workTasks.value.length > 0) {
    workList.value.push(workTasks.value as never)
  }
  if (privateTasks.value.length > 0) {
    workList.value.push(privateTasks.value as never)
  }
  if (completeTasks.value.length > 0) {
    workList.value.push(completeTasks.value as never)
  }
  workListTr.value = workList.value
}

watch(get_task.data, async () => {
  await get_staff.get()
  await get_task.get()
  await initializeGettitle()
})

const watchUpdFlg = async () => {
  updFlg.value = !updFlg.value
}

// updateフラグ変数の監視
watch(updFlg, async (newvalue) => {
  tList.value = !tList.value
  await get_staff.get()
  await get_task.get()
  await initializeGettitle()
  updFlg.value = false
})

// deleteフラグ変数の監視
watch(delFlg, async (newvalue) => {
  await get_staff.get()
  await get_task.get()
  await initializeGettitle()
  delFlg.value = false
  tList.value = !tList.value
})

const showToastPost = (msg: string): void => {
  toast.success(msg, {
    position: 'top',
    queue: false
  })
}

const delFlgParent = () => {
  delFlg.value = !delFlg.value
}

onMounted(async () => {
  await get_staff.get()
  await get_task.get()
  await importance_store.get_whole()
  await initializeGettitle()
})
</script>
