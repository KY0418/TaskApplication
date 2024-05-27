<template lang="pug">
div.sample-popup-window
  div.sample-popup-background
    div.sample-popup-box
      div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
        div.boxcomp
          h2.text-white.text-2xl.bg-blue.text-center.poptitle 職員編集
          label.block.mt-4.ml-4 職員名
            div.mt-4.ml-10
              input(type="text" v-model="newname" ).w-60.tt
          label.block.mt-8
            div.mt-8.ml-17.rd
              button(type="button" @click="updAgree").border-solid.border-white.rounded-5px.bg-blue.mb-5.btn 更新
              button(type="button" @click="modClose").border-solid.border-white.rounded-5px.bg-red.ml-8.mb-5.float-right.btn  キャンセル
</template>

<style lang="scss" scoped>
.sample-popup-background {
	/* 画面全体を暗くする透過背景 */
	position: fixed;
	width: 100%;
	height: 100%;
	background: rgba(0,0,0,.5);
	top: 0;
	left: 0;
	z-index: 1000;
}
.sample-popup-content {
	/* ポップアップ本体 */
	display: inline-block;
	position: fixed;
	width: 50%;
	z-index: 1100;
	background: #fff;
	// padding: 2%;
  height:auto;
  width: 40%;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
  min-width: 30%;
}

.poptitle {
  border: 1px solid #ffffff;
  border-top-left-radius: 20px; /* 上左コーナーの半径を設定 */
  border-top-right-radius: 20px; /* 上右コーナーの半径を設定 */
}
.tt {
  width: 80%;
}
.rd {
  margin: auto;
  width:60%
}

.btn {
  width: 40%;
}
</style>
<script setup lang="ts">
import { ref } from 'vue';
import { useGetStaffStore } from '@/stores/getStaffData';

const store = useGetStaffStore()

interface Emits {
    (event:"close"):void
    (event:"updAgree",name:string,id:string):void
}

interface stName {
    name: string,
    id:string
}

const props = defineProps<stName>()

const emit = defineEmits<Emits>()

const newname = ref(props.name)

const updAgree = async (): Promise<void> => {
  await store.put(props.id,newname.value)
  emit("updAgree",newname.value,props.id)

}

const modClose = (): void => {
    emit("close")
}

</script>
