import { defineStore, type StateTree } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { reactive, ref } from 'vue'

let apiUrl = 'http://localhost:8000/tasks'
const toast = useToast()
interface State {
    evlis: boolean
    flg:boolean
}

export const useGetTaskStore = defineStore({
  id:'gettask',
  state: () => ({
    data:ref([])
  }),
actions: {
  async get() : Promise<void>  {
    const response =  await axios.get(apiUrl)
    .then(response =>{
      this.$state.data =  response.data
    }).catch(error =>{
      let msg = "失敗"
      toast.error(msg,{
        position:"top"
      })
    })
    
   },
  },
})