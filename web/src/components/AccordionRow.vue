<template lang="pug">
tr
    td.text-center.d1       
    td.d2.text-center 
    td.d3.text-center 
    td.d4.text-center 
    td.d4.text-center 
    td.btnw
        div.text-center 
            button(type="button" ).float-left.ml-2.mr-4.bg-green-3.border-white.rounded-5px 編集
            button(type="button").float-right.mr-2.bg-red-4.border-white.rounded-5px 削除
</template>
<style lang="scss" scoped>
    /* tr {
        width:100%;
    } */
    .d1 {
        width:10%;
    }
    .d2{
        width:10%;
    }
    .d3{
        width:30%;
    }
    .d4{
        width:15%;
    }

    .d1,.d2 {
        border-top: solid 1px black;
        border-right: solid 1px black;
    }
    
    .btnw{
        border-top: solid 1px black;
        width: 20%;
    }
</style>
<script setup lang="ts">
</script>