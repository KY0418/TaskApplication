<script setup lang="ts">
const title = "タスクタイトル"
const status = "unko"
const id = 1
const mainId = 1
const mainTitle = "タスクタイトル"
let show = false
interface Props {
  show : boolean,
  count: number,
}

const showPopup = () : boolean =>{
  show = !show
  return show
}
</script>

<template lang="pug">
div.border-solid.border-red.rounded-25px.m-4.w-70.taskBox
  table
    thead 
      tr
        th.block.text-red.mt-2.ml-2  {{mainTitle}} {{ mainId }}
    tbody.block.border-solid.border-white.rounded-20px.bg-white.m-3.p-3.w-auto
        tr
          td.block.border-solid.border-white.rounded-8px.bg-blue.text-white.p-1.w-8.text-xs {{ status }}
        tr 
          td.block.mt-2.mb-2 {{ title }}{{ id }}
        tr
          td
            button(@click="showPopup").block.float-left.border-solid.border-white.rounded-5px.text-white.bg-green.text-sm.ml-28.p-1 編集
            a(href="#",style="text-decoration: none").block.float-right.border-solid.border-white.rounded-5px.text-white.bg-red.text-sm.ml-4.mr-4.p-1 削除
</template>