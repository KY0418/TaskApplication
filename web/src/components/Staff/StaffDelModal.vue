<template lang="pug">
div.modal
    div.backg
        div.modbox.border-solid.border-0.border-white.rounded-20px.ml-a
            p.text-white.text-2xl.bg-red.text-center.poptitle 削除確認
            p.mt-6.text-center 対象の職員を削除しますがよろしいですか？
            ul
                li.float-left.yes
                    button(@click="delt").border-solid.border-white.rounded-10px.p-2.mr-6.text-white.text-sm.bg-blue-500 はい
                li
                    button(@click="delCancel").ml-4.border-solid.border-white.text-white.rounded-10px.text-sm.p-2.bg-red-500 いいえ
</template>
<style lang="scss" scoped>
.backg {
  position: fixed;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  top: 0;
  left: 0;
  z-index: 1000;
}

.modbox {
  display: inline-block;
  position: fixed;
  width: 50%;
  z-index: 1100;
  background: #fff;
  // padding: 2%;
  height: 40%;
  width: 40%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 30%;
}

.poptitle {
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
}

ul {
  display: block;
  width: 40%;
  margin: 35px auto;
}

button {
  letter-spacing: 0.1em;
}
</style>
<script setup lang="ts">
import { useGetStaffStore } from '@/stores/getStaffData'
import { useGetTaskStore } from '@/stores/getTask'
import { useToast } from 'vue-toast-notification'

const taskStore = useGetTaskStore()

const store = useGetStaffStore()

const toast = useToast()

interface Props {
  id: string
}

interface Emits {
  (event: 'delclose'): void
  (event: 'delOk', id: string): void
}

const props = defineProps<Props>()

const emit = defineEmits<Emits>()

const delCancel = (): void => {
  emit('delclose')
}

const delt = async (): Promise<void> => {
  for (let item of taskStore.data) {
    console.log(item['staff_id'])
    if (item['staff_id'] === props.id) {
      toast.error('その職員はタスクが残っています', {
        position: 'top'
      })
      return
    }
  }
  await store.delete(props.id)
  emit('delOk', props.id)
}
</script>
