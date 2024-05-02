import { defineStore, type StateTree } from 'pinia'

interface State {
    evlis: boolean
    flg:boolean
}

export const useJudgingStore = defineStore({
  id:'judge',
  state: (): State => {
    return{
      evlis : false,
      flg:false
    }
  },
getters: {
  changeJud: (state): boolean => {
    if(state.flg == false){
        state.flg = true
    } else{
        state.flg = false
    }
    return state.flg
  }
},
actions: {
  changestate() : void  {
    if(this.flg == false){
        this.evlis = true
    } else{
        this.evlis = false
    }
   },
  },
})
