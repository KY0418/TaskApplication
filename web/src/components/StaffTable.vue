<template lang="pug">
table.border-solid.border-black.rounded-5.ml-6.mt-4 
        tr.border-solid
            th.text-center.t1 職員No
            th.text-center.t2 職員名
            th.exclude
        TableRow(v-for="item in RowData" :name="item.staff_name" :st_id="item.staff_id" @putAgree="put" @delAgree="delt")
</template>
<style lang="scss" scoped>

.tr {
    border-top:solid 1px gray;
}

table{
    border-collapse: separate;
    border-radius: 5px;
    overflow: hidden;
    width:80%;
}

.btnw{
    border-top: solid 1px black;
    width: 20%;
}

.t1 {
    width:20%;
}

.t1,.t2{
    border-right: 1px solid black;
}


</style>
<script setup lang="ts">
import TableRow from './TableRow.vue';
import { onMounted, ref, watch } from 'vue';
import { useGetStaffStore } from '@/stores/getStaffData';


interface Emits {
    (event:"updflg"):void
}

// interface RowData {
//     RowData:{
//     name: string,
//     st_id:string,
// }[]
// }
// const props = defineProps<RowData>()

const emit = defineEmits<Emits>()

const get_staff = useGetStaffStore()

const RowData = ref(get_staff.data)

watch(get_staff.data,async ()=>{
    RowData.value = get_staff.$state.data
    console.log("test")
})

const put = async(name:string,id:string): Promise<void> => {
    // await get_staff.put(id,name)
    await get_staff.get()
    RowData.value = get_staff.$state.data
    console.log(RowData.value,"confirm put")
    window.localStorage.setItem("upd","comp")
}

const delt = async(id:string) => {
    await get_staff.get()
    RowData.value = get_staff.$state.data
    console.log("delete test")
}

onMounted(async (): Promise<void>=>{
    await get_staff.get()
    RowData.value = get_staff.$state.data
    console.log(RowData.value,"test")
})
</script>