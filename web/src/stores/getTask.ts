import { defineStore, type StateTree } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { ref } from 'vue'

let apiUrl = import.meta.env.VITE_TASK_URL
const toast = useToast()

export const useGetTaskStore = defineStore({
  id: 'gettask',
  state: () => ({
    data: ref([])
  }),
  actions: {
    async get(): Promise<void> {
      const response = await axios
        .get(apiUrl)
        .then((response) => {
          this.$state.data = response.data
        })
        .catch((error) => {
          let msg = 'GET失敗'
          toast.error(msg, {
            position: 'top'
          })
        })
    }
  }
})
