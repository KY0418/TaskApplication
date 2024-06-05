<template lang="pug">
p.mt-4.ml-4.text-2xl 職員一覧
    router-link(:to="{name:'staffadd'}").border-solid.border-white.rounded-10px.bg-blue-8.p-1.text-xl.text-white.addst 職員を追加
    StaffTable(@updflg="changeFlg" :flg="changeGetFlg" )

</template>

<style lang="scss" scoped>
.boxtitle {
  border: 0.5px solid rgb(75, 73, 73);
  background-color: dimgray;
}

h1 {
  letter-spacing: 0.1em;
  margin: 5px;
  color: white;
  font-weight: normal;
}

.home {
  background-color: dimgray;
  border-style: none;
  text-decoration: none;
}

.tr {
  border-top: solid 1px gray;
}

.ipt {
  text-decoration: none;
  border-style: none;
}

.ipt:focus {
  outline: none;
}

table {
  border-collapse: separate;
  border-radius: 5px;
  overflow: hidden;
  width: 80%;
}

.btnw {
  border-top: solid 1px black;
  width: 20%;
}

.t1,
.t2 {
  border-right: 1px solid black;
}
.d1,
.d2 {
  border-top: solid 1px black;
  border-right: solid 1px black;
}

.addst {
  letter-spacing: 0.15rem;
  text-decoration: none;
  margin-left: 70%;
  min-width: 20%;
}
</style>
<script setup lang="ts">
import { inject, onMounted, ref, watch, reactive, computed, onUpdated } from 'vue'
import StaffTable from '../components/Staff/StaffTable.vue'
import StaffUpdModal from '@/components/Staff/StaffUpdModal.vue'
import router from '@/router'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { useGetStaffStore } from '@/stores/getStaffData'
import type { Ref } from 'vue'

const get_staff = useGetStaffStore()

const flg = ref(false)

const getflg = ref(false)

const globalListStaff = ref([])

const toast = useToast()

const staffName = ref('')
interface emit {
  emit(event: 'toastFlg', msg: string): void
}
let apiUrl = import.meta.env.VITE_TASK_URL

const toStaffAdd = (): void => {
  router.push({ name: 'staffadd' })
}

const changeFlg = () => {
  flg.value = !flg.value
}

const changeGetFlg = (): boolean => {
  getflg.value = !getflg.value
  return getflg.value
}

let stData = ref(get_staff.$state.data)

const staffUpdate = async (): Promise<void> => {}

const updflg = ref()

watch(flg, async (): Promise<void> => {
  await get_staff.get()
})

onMounted(async (): Promise<void> => {
  changeGetFlg()
  await get_staff.get()
  stData.value = get_staff.data
})
</script>
