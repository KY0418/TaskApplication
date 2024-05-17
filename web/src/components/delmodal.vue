<template lang="pug">
div.modal
    div.backg
        div.modbox.border-solid.border-0.border-white.rounded-20px.ml-a
            p.text-white.text-2xl.bg-red.text-center.poptitle 削除確認
            p.mt-6.text-center 対象のタスクを削除しますがよろしいですか？
            ul
                li.float-left.yes
                    button(@click="delt").border-solid.border-white.rounded-10px.p-2.mr-6.text-white.text-sm.bg-blue-500 はい
                li
                    button(@click="delCancel").ml-4.border-solid.border-white.text-white.rounded-10px.text-sm.p-2.bg-red-500 いいえ
</template>
<style lang="scss" scoped>
.backg {
    position: fixed;
	width: 100%;
	height: 100%;
	background: rgba(0,0,0,.5);
	top: 0;
	left: 0;
	z-index: 1000;
}

.modbox{
    display: inline-block;
	position: fixed;
	width: 50%;
	z-index: 1100;
	background: #fff;
	// padding: 2%;
    height:40%;
    width: 40%;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
    min-width: 30%;
}

.poptitle {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

ul {
    display: block;
    width:40%;
    margin: 35px auto;
}

button{
    letter-spacing: 0.1em;
}

</style>
<script setup lang="ts">
import axios from 'axios';
import { ref,watch } from 'vue';

interface delData {
    id:number
    deltitle:string
}

interface Emits {
    (event:"delAgree"):void
    (event:"delNotAgree"):void
    (event:"delEmit",msg:string,flg:number):void
    (event:"delFlgOrigin",delflg:boolean):void
}
const props = defineProps<delData>()

const emit = defineEmits<Emits>()

const delCancel = (): void => {
    emit("delNotAgree")
}

const tsMsg = ref('')
const delCompFlg = ref(false)
let apiUrl = 'http://localhost:8000/tasks/'

watch(delCompFlg,() => {
  console.log("delemit1")
  emit("delFlgOrigin",delCompFlg.value)
  console.log(delCompFlg.value)
  delCompFlg.value = false
})

// DELETE関数
const delt = async (): Promise<void> => {
  console.log(apiUrl)
  console.log(props.id)
//   let merId = 
//   if(apiUrl.includes(String(props.id)) === false){
//     
//   }
apiUrl = `${apiUrl}${props.id}`
console.log(apiUrl)
const response = await axios.delete(apiUrl)
  .then(response =>{
    if(response.status == 200 || response.status == 201){
      console.log("deleteが成功しました")
      tsMsg.value = "削除完了"
      let tFlg = 0
      emit("delEmit",tsMsg.value,tFlg)
      delCompFlg.value = true
  }
})
  .catch(error => {
    console.error("Failrd to delete error:",error)
    let tFlg = 1
    tsMsg.value = error.response.data.detail
    emit("delEmit",tsMsg.value,tFlg)
  })
}

</script>

