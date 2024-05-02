<script setup lang="ts">
import { RouterView } from 'vue-router'
import changeTask from './components/changeTask.vue'
const title = "aaaaaaa"


</script>

<template lang="pug">
div.bod
    div.boxtitle
      h1.prose.text-3xl タスク管理システム
        span.text-xl.mt-2.float-right Home
    //- span  HOME
    section.boxCompo
      RouterView 
      //- changeTask
  
</template>

<style lang="scss">
.boxtitle {
  border: 0.5px solid rgb(75, 73, 73);
  background-color: dimgray
}

h1 {
  letter-spacing: 0.1em;
  margin: 5px;
  color: white;
  font-weight: normal;
}

.boxCompo {
  border:0.5px solid dimgray;
  
}

.taskBox {
  background-color: #FFE382;
}


</style>
