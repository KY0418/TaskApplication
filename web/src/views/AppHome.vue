<script setup lang="ts">
import {useRouter} from "vue-router"
import {computed} from "vue"
import { useCounterStore } from "@/stores/counter";
import taskCompo from "./taskCompo.vue"

</script>

<template lang="pug">
div 
    |
    router-link(:to="{name:'taskadd'}" style="text-decoration: none").ml-2.mt-4.taskAddbox ＋タスクを追加
    |
    taskCompo
</template>
<style lang="scss">
.taskAddbox {
  display: block;
  width: 15%;
  color:rgb(255, 255, 255);
  font-weight: bold;
  font-size: 20px;
  border-radius: 5px;
  border: white 1px;
  background-color: blue;
}
</style>


