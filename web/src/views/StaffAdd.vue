<template lang="pug">
div
  h2.mt-4.ml-2.text-2xl 職員追加
  p.text-2xl.mt-4.ml-4 職員名
    ul.ml-4.mt-2.border-solid.border-gray.rounded-15px 
      li 
        input(type="text" v-model="newStaff").ml-4.w-180 
  button(type="button" @click="post").mt-4.bg-blue4.p-1.rounded-10px ＋職員を追加

</template>
<style lang="scss" scoped>
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

.home {
  background-color:dimgray ;
  border-style: none;
  text-decoration: none;
}

h2 {
  letter-spacing: 0.1rem;
}

ul{
  width:80%;
}

input{
  border: none;
  outline:none;
}

button {
  letter-spacing: 0.1rem;
  font-size: 18px;
  width: 15%;
  border: none;
  margin-left: 67%;
}
</style>
<script setup lang="ts">
import { ref } from 'vue';
import { useGetStaffStore } from '@/stores/getStaffData';
import { useRouter } from 'vue-router';

const router = useRouter()

const post_staff = useGetStaffStore()

const newStaff = ref('')

const movePage = ref(false)

interface Emits {
  (event:"getflg"):void
}

const emit = defineEmits<Emits>()

const post = async(): Promise<void> => {
  await post_staff.post(newStaff.value as string)
  movePage.value = post_staff.postflg
  if(movePage.value == true){
    console.log(post_staff.postflg)
    emit("getflg")
    router.push({name:"managementstaff"})

  }
  
}

</script>