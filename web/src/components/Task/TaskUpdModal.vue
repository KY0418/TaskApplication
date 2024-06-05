<template lang="pug">
div.sample-popup-window
  div.sample-popup-background
    div.sample-popup-box
      div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
        div.boxcomp
          h2.text-white.text-2xl.bg-blue.text-center.poptitle タスクを編集
          label.block.mt-4.ml-4 タスクタイトル
            div.mt-4.ml-10
              input(type="text" v-model="newtitle" ).w-60.tt
          label.block.mt-4.ml-4 職員名
              div.mt-4.ml-10
                select(v-model="newname").tt
                  option(v-for="item of staffList" :value="item.staff_name") {{ item.staff_name }}
          label.block.mt-4.ml-4.mr-4.mb-6 優先度
            div.ml-10.mt-4
              select(v-model="priority").tt
                option( value="1" ) 緊急度高、緊急度高
                option( value="2" ) 緊急度高、緊急度低
                option( value="3" ) 緊急度低、緊急度高
                option( value="4" ) 緊急度低、緊急度低
          label.block.mt-4.ml-4 カテゴリー
            div.ml-10.mt-4
              select(v-model="category").tt
                option(value="仕事") 仕事
                option(value="プライベート") プライベート
          label.block.mt-4.ml-4.mr-4.mb-6 ステータス
              div.rd
                input(type="radio" v-model="TrueOrFalse" :value="1").float-left
                span.mt-2 未着手
                input(type="radio" v-model="TrueOrFalse" :value="2").ml-5
                span 完了
                input(type="radio" v-model="TrueOrFalse" :value="3").ml-5
                span 進行中
          label.block
            div.mt-4.ml-17.rd
              button(type="button" @click="put").border-solid.border-white.rounded-5px.bg-blue.mb-5.btn 更新
              button(type="button" @click="popupClose").border-solid.border-white.rounded-5px.bg-red.ml-8.mb-5.float-right.btn  キャンセル
</template>

<style lang="scss" scoped>
.sample-popup-background {
  /* 画面全体を暗くする透過背景 */
  position: fixed;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  top: 0;
  left: 0;
  z-index: 1000;
}
.sample-popup-content {
  /* ポップアップ本体 */
  display: inline-block;
  position: fixed;
  width: 50%;
  z-index: 1100;
  background: #fff;
  // padding: 2%;
  height: auto;
  width: 40%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 30%;
}

.poptitle {
  border: 1px solid #ffffff;
  border-top-left-radius: 20px; /* 上左コーナーの半径を設定 */
  border-top-right-radius: 20px; /* 上右コーナーの半径を設定 */
}
.tt {
  width: 80%;
}
.rd {
  margin: auto;
  width: 60%;
}

.btn {
  width: 40%;
}
</style>

<script setup lang="ts">
import axios from 'axios'
import { ref, reactive, computed, watch } from 'vue'
import type { responseData, eventFLG } from '@/interfaces'
import { useToast } from 'vue-toast-notification'
import { useGetTaskStore } from '@/stores/getTask'
import { useGetStaffStore } from '@/stores/getStaffData'
import dayjs from 'dayjs'

const taskStore = useGetTaskStore()

const staffStore = useGetStaffStore()

interface defData {
  title: string
  status: number
  id: number
  category: string
  pri_id: number
  st_id: string
  start_date: string
}

const staffList = ref(staffStore.data)
const props = defineProps<defData>()
const TrueOrFalse = ref(props.status)
const newtitle = ref(props.title)
const title = ref(props.title)
const priority = ref(props.pri_id)
const newname = ref()
const postStID = ref()
const toast = useToast()
let tasknum: number
const upflg = ref(false)

interface Emits {
  (event: 'changetitle', title: string): void
  (event: 'changeSwitch', flg: boolean): void
  (event: 'showtoast', msg: string, flg: number): void
  (event: 'taskstatus', status: string): void
  (event: 'updGet'): void
}

const emit = defineEmits<Emits>()
// getで取得したIDを格納する　非同期関数内でreturnした値を使うとundefinedになる
let gid: number
let recid: number
const tsMsg = ref('')
let apiUrl = 'http://localhost:8000/tasks/'
const tList = ref([''])
const taskState = ref('')
const category = ref(props.category)
let tFlg: number

for (let i of staffStore.data) {
  if (i['staff_id'] == props.st_id) {
    newname.value = i['staff_name']
  }
}

const searchStaff = async () => {
  for (let i of staffStore.data) {
    if (i['staff_name'] == newname.value) {
      postStID.value = i['staff_id']
    }
  }
}

watch(props, async () => {
  for (let i of staffStore.data) {
    if (i['staff_id'] == props.st_id) {
      newname.value = i['staff_name']
    }
  }
  newtitle.value = props.title
  priority.value = props.pri_id
  category.value = props.category
})

watch(TrueOrFalse, (newvalue) => {
  if (newvalue == 1) {
    taskState.value = '未完'
  } else if (newvalue == 2) {
    taskState.value = '完了'
  } else if (newvalue == 3) {
    taskState.value = '進行中'
  }
})

const titleFlg = ref(true)
const titleCheck = async (title: string) => {
  if (title === newtitle.value) {
    titleFlg.value = true
  } else {
    for (let item of taskStore.data) {
      if (item['title'] === newtitle.value) {
        titleFlg.value = false
        break
      }
    }
    return
  }
}
const dateFlg = ref(true)
const dateCheck = async () => {
  const oldStatus = ref(props.status)
  const year = dayjs().year()
  const month = dayjs().month()
  const day = dayjs().date()
  const compare = []
  const nowDate =
    String(year).padStart(2, '0') +
    '-' +
    String(month + 1).padStart(2, '0') +
    '-' +
    String(day).padStart(2, '0')
  const datea = new Date(props.start_date)
  const dateb = new Date(year, month, day)
  compare.push(datea, dateb)
  compare.sort((a, b) => a.getTime() - b.getTime())
  let idx = compare.indexOf(dateb)
  // console.log(idx)
  // console.log(oldStatus.value)
  // console.log(datea,dateb)
  if (props.start_date == nowDate) {
    dateFlg.value = true
    return
  } else if (idx == 0 && oldStatus.value != 2) {
    dateFlg.value = false
    return
  }
}
const put = async (): Promise<void> => {
  let oldTitle = props.title
  newtitle.value = newtitle.value.replace(/\s+/g, '')
  await titleCheck(oldTitle)
  if (titleFlg.value == false) {
    toast.error('そのタスクは既に存在しています', {
      position: 'top'
    })
    return
  }
  await searchStaff()
  if (TrueOrFalse.value == 2) {
    await dateCheck()
  }

  if (dateFlg.value == false) {
    toast.error('今日より後のタスクを完了することはできません', {
      position: 'top'
    })
    return
  }
  let putURL = apiUrl
  putURL = `${putURL}${props.id}`
  const response = await axios
    .put(putURL, {
      title: newtitle.value,
      category: category.value,
      status_id: TrueOrFalse.value,
      staff_id: postStID.value,
      priority_id: priority.value
    })
    .then((response) => {
      console.log('PUTが成功しました')
      tsMsg.value = '更新完了'
      tFlg = 0
      upflg.value = !upflg.value
      emit('changetitle', newtitle.value)
      emit('changeSwitch', upflg.value)
      emit('taskstatus', taskState.value)
      emit('updGet')
      emit('showtoast', tsMsg.value, tFlg)
      upflg.value = !upflg.value
      dateFlg.value = true
    })
    .catch((error) => {
      tFlg = 1
      tsMsg.value = error.response.data.detail
      toast.error(tsMsg.value, {
        position: 'top'
      })
    })
  // await taskStore.get()
}

const popupClose = (): void => {
  emit('changeSwitch', upflg.value)
}
</script>
