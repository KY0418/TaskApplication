import { ref, computed } from 'vue'
import { defineStore, type StateTree } from 'pinia'

export const useCounterStore = defineStore({
  id:'counter',
  state: (): StateTree => {
    return{
      counter:0
    }
  },
getters: {
  doublecount: (state): number => state.counter * 2
},
actions: {
  increment(): void {
    this.counter++
  }
}
})
