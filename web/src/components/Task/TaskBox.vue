<template lang="pug">
div.whole
  div.border-solid.border-red.rounded-25px.ml-4.w-70.float-left.taskBox
      p(v-if="categoryText").text-red.mt-2.ml-2.w-30.tb {{ categoryText }}
      div.content
        TaskContent(v-for="item in props.responseData" :title="item.title" :status="item.status_id" :id="item.id" :category="item.category" :st_id="item.staff_id" :pri_id="item.priority_id"
                    :start_date="item.start_date" @updFlg="handingUpdflg" @createTitle="changeTitle" @changeState="changeStatus" @changePopupStatus="changeSwitch" @updateId="updateId" @showtoast="showToast"
                    @handData="getUpdFlg" @delFlg="delFlgSecond")

</template>
<style lang="scss" scoped>
input {
  border: none;
  outline: none;
}
.taskBox {
  background-color: #ffe382;
}

.tb {
  outline: none;
  background-color: #ffe382;
}

.add {
  text-decoration: none;
  width: 15%;
}

.content {
  width: 100%;
}

.whole {
  width: 100%;
}
</style>
<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import TaskContent from './TaskContent.vue'
import { useToast } from 'vue-toast-notification'

// 検索対象のタイトル
const tasktitle = ref('')
// タスクのステータス
const status = ref(false)
// カテゴリータイトル
const catTitle = ref<string[]>([])
// レコードを検索するためのID
const searchId = ref(0)
// 編集ポップアップ表示のフラグ
let show = ref(false)
// トーストのインスタンス
const toast = useToast()
// updateフラグ
const updFlgSon = ref(false)
// Propsデータを受け取るためのinterface
interface defData {
  responseData: {
    title: string
    id: number
    status_id: number
    category: string
    staff_id: string
    priority_id: number
    start_date: string
  }[]
  flg: boolean
}

// Props受け取りデータ格納変数
const props = defineProps<defData>()
const catList = ref(props.responseData.map((task) => task.category))
const catListSt = ref(props.responseData.map((task) => task.status_id))
catTitle.value = catList.value
if (catListSt.value[0] == 2 || catList.value[0] === '完了') {
  catTitle.value[0] = '完了'
}
const categoryText = computed(() => {
  if (catListSt.value[0] == 2 || catList.value[0] === '完了') {
    return '完了'
  } else if (catList.value[0] === '仕事' && catListSt.value[0] != 2) {
    return '仕事'
  } else if (catList.value[0] === 'プライベート' && catListSt.value[0] != 2) {
    return 'プライベート'
  }
  return null
})

const handingData = ref(props.responseData)

const categeoryprovide = async () => {
  catList.value = props.responseData.map((task) => task.category)
  catListSt.value = props.responseData.map((task) => task.status_id)
  catTitle.value[0] = catList.value[0]
  if (catListSt.value[0] == 2 || catList.value[0] === '完了') {
    catTitle.value[0] = '完了'
  }
}

watch(props, async (newvalue) => {
  handingData.value = newvalue.responseData
  await categeoryprovide()
})

interface Emits {
  (event: 'handFlg'): void
  (event: 'delFlgs', delflg: boolean): void
  (event: 'delflgs'): void
  (event: 'updflg'): void
}

const emit = defineEmits<Emits>()

const getUpdFlg = (flg: boolean): void => {
  updFlgSon.value = flg
}

const handingUpdflg = () => {
  emit('updflg')
}

watch(updFlgSon, () => {
  emit('handFlg')
  updFlgSon.value = false
})

// タスク追加のトースト表示
const showToastPost = (msg: string): void => {
  toast.success(msg, {
    position: 'top',
    queue: false
  })
}

// 以下の5つの関数はemitで受け取った値を処理する
const changeTitle = (newTitle: string): void => {
  tasktitle.value = newTitle
}

const changeStatus = (newstatus: boolean): void => {
  status.value = newstatus
}

const changeSwitch = (): void => {
  show.value = !show.value
}

const updateId = (newid: number): void => {
  searchId.value = newid
}

const showToast = (msg: string, flg: number): void => {
  if (flg == 0) {
    toast.success(msg, {
      position: 'top'
    })
  } else if (flg == 1) {
    toast.error(msg, {
      position: 'top'
    })
  }
}

// showtoastに合わせれば消せる
const showToastPut = (msg: string): void => {
  if (msg === '更新完了') {
    toast.success(msg, {
      position: 'top',
      pauseOnHover: false,
      queue: false
    })
  } else if (msg === '更新失敗') {
    toast.error(msg, {
      position: 'top',
      pauseOnHover: false,
      queue: false
    })
  }
}

const delFlgSecond = () => {
  emit('delflgs')
}
</script>
