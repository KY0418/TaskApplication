<template lang="pug">
div.boxtitle.pt-1
    router-link(:to="{name:'apphome'}").prose.text-3xl.pt-2 タスク管理システム
        div.float-right
            router-link(:to="{name:'apphome'}").text-xl.mt-2.text-white.mr-4.home Home
            router-link(:to="{name:'managementstaff'}").text-xl.mt-2.mr-2.text-white.home 職員一覧
            router-link(:to="{name:'calender'}").text-xl.mt-2.text-white.mr-4.home カレンダー
</template>
<style lang="scss" scoped>

.boxtitle {
    border: 0.5px solid rgb(75, 73, 73);
    background-color: dimgray
}

.prose {
    letter-spacing: 0.1em;
    margin: 5px;
    color: white;
    font-weight: normal;
    text-decoration: none;
    
}

.home {
    background-color:dimgray ;
    text-decoration: none;
    margin-left: 0%;
}

.add {
    text-decoration: none;
    width:15%;
}
</style>
