import { defineStore, type StateTree } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'
import { ReactiveEffect, reactive, ref} from 'vue'

const toast = useToast()

const apiUrl = 'http://localhost:8000/importance'

export const usegetImportStore = defineStore({
    id: "getimp",
    state: () => ({
        data:ref(),
        whole_data:ref()
    }),
    actions:{
        async get(id:number): Promise<void> {
            let apiurl = `${apiUrl}/${id}`
            const response = await axios.get(apiurl)
            .then(response => {
                if(response.status == 200 || response.status == 201){
                    // console.log("Importance Get Complete") 
                    console.log(id)
                }
                this.$state.data = response.data
            }).catch(error => {
                toast.error(`${error.response.data.detaile}`,{
                    position:"top"
                }
                )
            })
        },
        async get_whole(): Promise<void> {
            let apiurl = `${apiUrl}`
            const response = await axios.get(apiurl)
            .then(response => {
                this.$state.whole_data = response.data
            }).catch(error => {
                toast.error("失敗",{
                    position:"top"
                }
                )
            })
        },
    }

})