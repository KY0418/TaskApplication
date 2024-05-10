<template lang="pug">
div.block.border-solid.border-white.rounded-20px.bg-white.m-3.p-3
    ul 
        li.border-solid.border-white.rounded-8px.bg-blue.text-white.p-1.text-xs.st {{ status }}
        li.block.mt-2.mb-2 {{ props.title }}
        li.block.mt-2.mb-2 {{ tasktitle }}
        li
            button(type="button" @click="retAllEmit").border-solid.border-white.rounded-5px.text-white.bg-green.text-sm.ml-28.p-1 編集
            button(type="button" @click="delt").block.float-right.border-solid.border-white.rounded-5px.text-white.bg-red.text-sm.ml-4.mr-4.p-1 削除
            button(type="button" @click="aa") bbbb
            pre {{ props.title }}
</template>
<style lang="scss" scoped>
.st {
    width: 18%;
    text-align: center;
}
div {
    min-width: 50%;
}
</style>
<script setup lang="ts">
// import type { taskContentData } from '../interfaces'
import { ref } from 'vue';

const props = defineProps<taskContentData>()
interface taskContentData {
    title: string,
    status: string,
    popupstatus:boolean,
}



interface Emits {
    (event:"changeState",status:string):void
    (event:"createTitle",title:string):void
    (event:"changePopupStatus",popstatus:boolean):void
}

const emit = defineEmits<Emits>()
const status = ref("未着手")
const tasktitle =  ref(props.title)


const aa = (a:taskContentData): void => {
    console.log(props.title,"ssss")
    console.log(a.title)
    tasktitle.value = props.title
}

const retAllEmit = (): void => {
    emit("changePopupStatus",props.popupstatus)
    emit("changeState",status.value)
    emit("createTitle",tasktitle.value)
}

</script>