<script setup lang="ts">
const title = "unko"
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
  console.log(show)
  return show
}
</script>

<template lang="pug">
div.popup-bg-cover
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
            
          
div.sample-popup-window
label テスト
  input(type="checkbox" id="sample-popup-switch")
  div.sample-popup-background
    div.sample-popup-box
      div.border-solid.border-0.border-white.rounded-20px.ml-a.sample-popup-content
        div.boxcomp
          h2.text-white.text-2xl.bg-blue.text-center.poptitle タスクを編集
          label.block.mt-4.ml-4 タスクタイトル
            div.mt-4.ml-10
              input(type="text").w-60
          label.block.mt-4.ml-4.mr-4 ステータス
            div.mt-4.ml-12
              input(type="radio").float-left
              span 未着手
              input(type="radio").ml-5
              span 完了
          label.block
            div.mt-4.ml-17
              button(type="button").border-solid.border-white.rounded-5px.bg-blue 更新
              button(type="button").border-solid.border-white.rounded-5px.bg-red.ml-8 キャンセル
        //- label(for="sample-popup-switch").sample-popup-close 閉じる
</template>

<style lang="scss">
sample-popup-switch {
	/* チェックボックスを非表示 */
	display: none;
}
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
  height:55%;
  width: 40%;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
}
.sample-popup-close {
	/* ポップアップ内の閉じるボタン */
	position: relative;
	display: inline-block;
	background: #09f;
	color: #fff;
	padding: 0 1em;
	border-radius: 3px;
	cursor: pointer;
	left: 50%;
	transform: translateX(-50%);
}
#sample-popup-switch:checked ~ .sample-popup-background, #sample-popup-switch:checked ~ .sample-popup-box {
	/* ポップアップ･透過背景を閉じる */
	display: none;
}
.poptitle {
  border: 1px solid #ffffff;
  border-top-left-radius: 20px; /* 上左コーナーの半径を設定 */
  border-top-right-radius: 20px; /* 上右コーナーの半径を設定 */
}

</style>