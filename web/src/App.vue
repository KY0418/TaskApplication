<template lang="pug">
div.bod
    section.boxCompo
       RouterView  
    //- changeTask
      button(type="button" @click="test") test
      button(type="button" @click="ptest") testkkkk　テスト用ボタン
  
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import changeTask from './components/changeTask.vue'
import axios from 'axios';
import AppHome from './views/AppHome.vue';

// const title = "aaaaaaa" テスト用

// const apiUrl = 'http://localhost:8000/tasks';

// const test = async (): Promise<any> => {
//   try {
//     const response = await axios.get<any>(apiUrl); // 型を指定
//     const data = response.data;
//     console.log(data); // データを処理して使用する
//   } catch (error) {
//     console.error(error);
//   }
// };

// const pdata = {
//   title:"いいいいいい",
// }
// const ptest = async () : Promise<any> => {
//    axios.post(apiUrl, pdata)
//   .then(response => {
//     if (response.status === 200 || response.status === 201) {
//       console.log('POSTリクエストが成功しました！');
//       console.log('レスポンスデータ:', response.data);
//     } else {
//       console.error('POSTリクエストが失敗しました:', response.status, response.data);
//     }
//   })
//   .catch(error => {
//     console.error('POSTリクエスト中にエラーが発生しました:', error);
//   });
// interface APIResponse {
//   title: string,
// }
// }
</script>
