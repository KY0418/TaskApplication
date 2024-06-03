import { defineStore, type StateTree } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { ReactiveEffect, reactive, ref,computed, type ComputedRef} from 'vue'

const apiUrlSt = import.meta.env.VITE_URL
const toast = useToast()

export const useGetStaffStore = defineStore({
  id:'getst',
  state: () => ({
    data:ref([]) ,
    getflg: ref(0),
    delflg: ref(1),
    postflg:ref(false),
    search_data:ref()
  }),
  getters:{
    getStname: (data) => {
      return (): any =>{
        const st_name = ref('')
        for(let i of data.data){
          if(st_name.value=''){
            console.log(i['staff_name'])
            st_name.value = i['staff_name']
          }
        return st_name.value
        }
      }
      }
    },
actions: {
  async get(): Promise<void>{
    console.log(this.$state.getflg)
    const response =  await axios.get(apiUrlSt as string)
    .then(response =>{
      this.$state.data = response.data
    }).catch(error =>{
      let msg = error.response.data.detaile
    })
    
    },
  async search_staff(st_id:string): Promise<void>{
    console.log(this.$state.getflg)
    const apiURL = `${apiUrlSt}/${st_id}`
    const response =  await axios.get(apiURL as string)
    .then(response =>{
      this.$state.search_data = response.data
    }).catch(error =>{
      console.log("failed to get request")
    })
  },
  async post(st_name:string): Promise<void> {
    const response = await axios.post(apiUrlSt as string,{
      staff_name: st_name,
    })
    .then(response => {
      if(response.status == 200 || response.status == 201){
        toast.success("登録完了",{
          position:"top"
        })
      this.$state.getflg++
      this.$state.postflg = true
      }
    })
    .catch(error => {
      error.response.data.detaile = "入力した値を確認してください"
      toast.error(`${error.response.data.detaile}`,{
        position:"top",
      })
      this.$state.postflg = false
    })
  },
  async put(staff_id:string,st_name:string): Promise<void> {
    let apiUrlPut = `${apiUrlSt}/${staff_id}`
    const response = await axios.put(apiUrlPut,{
      staff_name: st_name,
    }).then(response => {
      if(response.status == 200 || response.status == 201){
        toast.success("更新完了",{
          position:"top"
        })
      }
    }).catch(error => {
      toast.error(`${error.response.data.detaile}`,{
        position:"top"
      })
    })
  },
  async delete(staff_id:string): Promise<void> {
    let apiUrlDel = `${apiUrlSt}/${staff_id}`
    const response = await axios.delete(apiUrlDel)
    .then(response => {
      if(response.status == 200 || response.status == 201){
        toast.success("削除完了",{
          position:"top"
        })
        this.$state.delflg++
      }
    }).catch(error => {
          toast.error(`${error.response.data.detaile}`,{
          position:"top"
        })
        this.$state.delflg++
      })
    }
  },
})
