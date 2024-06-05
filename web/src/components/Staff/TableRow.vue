<template lang="pug">
tr
    td.text-center.d1 {{ st_id }}       
    td.d2.text-center {{ st_name }}
    td.btnw
        div.text-center 
            button(type="button" @click="showUpdModal").float-left.ml-4.mr-4.bg-green-3.border-white.rounded-5px 編集
            button(type="button" @click="showDelModal").float-right.mr-4.bg-red-4.border-white.rounded-5px 削除
div(v-show="showUpd")
    StaffUpdModal(@close="showUpdModal" @updAgree="put" @delclose="showUpdModal" :name="st_name" :id="st_id")
div(v-show="delShow")
    StaffDelModal(:id="st_id" @delclose="showDelModal" @delOk="delt")
</template>
<style lang="scss" scoped>
tr {
  width: 80%;
}
.d1 {
  width: 20%;
}

.d1,
.d2 {
  border-top: solid 1px black;
  border-right: solid 1px black;
}

.btnw {
  border-top: solid 1px black;
  width: 20%;
}
</style>
<script setup lang="ts">
import { ref, watch } from 'vue'
import StaffUpdModal from '../Staff/StaffUpdModal.vue'
import StaffDelModal from '../Staff/StaffDelModal.vue'
import { useGetStaffStore } from '@/stores/getStaffData'

const store = useGetStaffStore()

interface RowData {
  name: string
  st_id: string
}

const delShow = ref(false)

const props = defineProps<RowData>()

interface Emits {
  (event: 'putAgree', name: string, id: string): void
  (event: 'delAgree', id: string): void
}

const emit = defineEmits<Emits>()

const st_name = ref(props.name)

const st_id = ref(props.st_id)

const showUpd = ref(false)

watch(props, (newvalue) => {
  st_id.value = newvalue.st_id
  st_name.value = newvalue.name
})

const showUpdModal = (): void => {
  showUpd.value = !showUpd.value
}

const showDelModal = (): void => {
  delShow.value = !delShow.value
}

const put = async (name: string, id: string): Promise<void> => {
  showUpdModal()
  emit('putAgree', name, id)
}

const delt = (id: string) => {
  showDelModal()
  emit('delAgree', id)
}
</script>
