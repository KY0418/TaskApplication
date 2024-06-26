import { defineStore, type StateTree } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { ref } from 'vue'

const apiUrl = import.meta.env.VITE_TASK_URL
const toast = useToast()

export const useGetStatusStore = defineStore({
  id: 'getstatus',
  state: () => ({
    data: ref(),
    wholeData: ref([])
  }),
  actions: {
    async get(id: number): Promise<void> {
      const apiurl = `${apiUrl}/${id}/status`
      const response = await axios
        .get(apiurl)
        .then((response) => {
          this.$state.data = response.data
        })
        .catch((error) => {
          let msg = '失敗'
          toast.error(msg, {
            position: 'top'
          })
        })
      console.log(apiurl)
    },
    async get_whole(): Promise<void> {
      const apiurl = `${apiUrl}/status`
      const response = await axios
        .get(apiurl)
        .then((response) => {
          this.$state.wholeData = response.data
          console.log(this.data)
        })
        .catch((error) => {
          let msg = '失敗'
          toast.error(msg, {
            position: 'top'
          })
        })
    }
  }
})
