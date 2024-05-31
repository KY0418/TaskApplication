import { defineStore, type StateTree } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { reactive, ref } from 'vue'

const apiUrl = 'http://localhost:8000/tasks/'
const toast = useToast()

export const useGetStatusStore = defineStore({
  id:'getstatus',
  state: () => ({
    data:ref()
  }),
actions: {
  async get(id:number) : Promise<void>  {
    const apiurl = `${apiUrl}${id}/status`
    const response =  await axios.get(apiurl)
    .then(response =>{
      this.$state.data =  response.data
      console.log(this.data)
    }).catch(error =>{
      let msg = "失敗"
      toast.error(msg,{
        position:"top"
      })
    })
    console.log(apiurl)
   },
  },
})