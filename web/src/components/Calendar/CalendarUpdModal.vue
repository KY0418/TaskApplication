<template lang="pug">
div.sample-popup-window
    div.sample-popup-background
        div.sample-popup-box
          div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
            div.boxcomp
              h2.text-white.text-2xl.bg-blue.text-center.poptitle タスクを編集
              label.block.mt-4.ml-4 タスクタイトル
                div.mt-4.ml-10
                  input(type="text" v-model="newtitle" ).tt
              label.block.mt-4.ml-4 職員名
                div.mt-4.ml-10
                  select(v-model="newname").tt
                    option(v-for="item of staffList" :value="item.staff_name") {{ item.staff_name }}
              label.block.mt-4.ml-4.mr-4.mb-6 優先度
                div.ml-10.mt-4
                  select(v-model="priority").tt
                    option( value="重要度高、緊急度高" ) 重要度高、緊急度高
                    option( value="重要度高、緊急度低" ) 重要度高、緊急度低
                    option( value="重要度低、緊急度高" ) 重要度低、緊急度高
                    option( value="重要度低、緊急度低" ) 重要度低、緊急度低
              label.block.mt-4.ml-4.mr-4.mb-6 ステータス
                  div.text-center
                    input(type="radio" v-model="TrueOrFalse" value="未着手")
                    span.mt-2 未着手
                    input(type="radio" v-model="TrueOrFalse" value="完了").ml-5
                    span 完了
                    input(type="radio" v-model="TrueOrFalse" value="進行中").ml-5
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
import { useToast } from 'vue-toast-notification'
import { useGetTaskStore } from '@/stores/getTask'
import { useGetStaffStore } from '@/stores/getStaffData'
import { usegetImportStore } from '@/stores/getImportance'
import { useGetStatusStore } from '@/stores/getStatus'
import dayjs from 'dayjs'

const importanceStore = usegetImportStore()

const staffStore = useGetStaffStore()

const taskStore = useGetTaskStore()

const statusStore = useGetStatusStore()
console.log(statusStore.data)
interface taskData {
  title: string
  staff_name: string
  status: string
  priority: string
  staff_id: string
  id: number
  start_date: string
}
const staffList = ref(staffStore.data)
const props = defineProps<taskData>()
const TrueOrFalse = ref(props.status)
const oldName = props.staff_name
let newtitle = ref(props.title)
const newname = ref(props.staff_name)
const priority = ref(props.priority)
const toast = useToast()
const upflg = ref(false)

interface Emits {
  (event: 'changetitle', title: string): void
  (event: 'changeSwitch', flg: boolean): void
  (event: 'showtoast', msg: string, flg: number): void
  (event: 'taskstatus', status: string): void
  (event: 'close'): void
  (event: 'calendarUpd'): void
}

const emit = defineEmits<Emits>()
// getで取得したIDを格納する　非同期関数内でreturnした値を使うとundefinedになる
const tsMsg = ref('')
let apiUrl = import.meta.env.VITE_TASK_URL
const taskState = ref('')
let tFlg: number

const changeStatus = (status: boolean): string => {
  let retStr = ''
  if (status == true) {
    retStr = '完了'
  } else if (status == false) {
    retStr = '未着手'
  }
  return retStr
}

watch(TrueOrFalse, (newvalue) => {
  if (newvalue === '未完') {
    taskState.value = '未完'
  } else if (newvalue === '完了') {
    taskState.value = '完了'
  } else if (newvalue === '進行中') {
    taskState.value = '進行中'
  }
})

watch(props, () => {
  staffList.value = staffStore.data
})

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
  if (props.start_date == nowDate) {
    dateFlg.value = true
    return
  } else if (idx == 0 && oldStatus.value != '2') {
    dateFlg.value = false
    return
  }
}

const put = async (): Promise<void> => {
  let putURL = apiUrl
  putURL = `${putURL}/${props.id}`
  console.log(putURL)
  let priority_id: number = 0
  let status_id: number = 0
  let staff_id: string = ''
  newtitle.value = newtitle.value.replace(/\s+/g, '')

  for (let i of importanceStore.whole_data) {
    if (i['importance'] == priority.value) {
      priority_id = i['id']
    }
  }
  for (let i of statusStore.wholeData) {
    if (i['status_name'] == TrueOrFalse.value) {
      status_id = i['status_id']
    }
  }
  for (let i of staffStore.data) {
    if (i['staff_name'] === newname.value) {
      staff_id = i['staff_id']
    }
  }
  if (apiUrl.includes(String(props.id)) === false) {
    apiUrl = `${apiUrl}${props.id}`
  }
  if (newtitle.value == '') {
    toast.error('タイトルを入力してください', {
      position: 'top'
    })
    return
  }
  if (status_id == 2) {
    await dateCheck()
  }

  if (dateFlg.value == false) {
    toast.error('今日より後のタスクを完了することはできません', {
      position: 'top'
    })
    return
  }
  const response = await axios
    .put(putURL, {
      title: newtitle.value,
      status_id: status_id,
      staff_id: staff_id,
      priority_id: priority_id
    })
    .then((response) => {
      tsMsg.value = '更新完了'
      tFlg = 0
      upflg.value = !upflg.value
      emit('close')
      emit('taskstatus', taskState.value)

      emit('calendarUpd')
      upflg.value = !upflg.value
      toast.success(tsMsg.value, {
        position: 'top'
      })
    })
    .catch((error) => {
      tFlg = 1
      tsMsg.value = error.response.data.detail
      toast.error(tsMsg.value, {
        position: 'top'
      })
    })
  emit('showtoast', tsMsg.value, tFlg)
  await taskStore.get()
}

const popupClose = (): void => {
  emit('changeSwitch', upflg.value)
  emit('close')
}
</script>
