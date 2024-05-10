<template lang="pug">
div.bod
    div.boxtitle
      h1.prose.text-3xl タスク管理システム
        span.text-xl.mt-2.float-right Home
    //- span  HOME
    section.boxCompo
      RouterView 
      //- changeTask
button(type="button" @click="test") test
button(type="button" @click="ptest") testkkkk
  
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
<script setup lang="ts">
import { RouterView } from 'vue-router'
import changeTask from './components/changeTask.vue'
import axios from 'axios';
// import { taskApp } from './interfaces';

const title = "aaaaaaa"

// defineProps<taskApp>();

const apiUrl = 'http://localhost:8000/tasks';

const test = async (): Promise<any> => {
  try {
    const response = await axios.get<any>(apiUrl); // 型を指定
    const data = response.data;
    console.log(data); // データを処理して使用する
  } catch (error) {
    console.error(error);
  }
};

const pdata = {
  title:"いいいいいい",
}
const ptest = async () : Promise<any> => {
   axios.post(apiUrl, pdata)
  .then(response => {
    if (response.status === 200 || response.status === 201) {
      console.log('POSTリクエストが成功しました！');
      console.log('レスポンスデータ:', response.data);
    } else {
      console.error('POSTリクエストが失敗しました:', response.status, response.data);
    }
  })
  .catch(error => {
    console.error('POSTリクエスト中にエラーが発生しました:', error);
  });
interface APIResponse {
  title: string,
}
}
</script>
