<template lang="pug">
div.border-solid.rounded-20px.border-gray.w-100.whole
    p.border-solid.rounded-20px.border-color-white.text-white.title タスクを編集
    div.mt-5.tabContent
        p.pr-28 タスクタイトル
        input(type="text" name="title").mt-2
        p.mt-4.mr-34 ステータス
          div.mt-4.radiog
            input(type="radio" name="aaa")
            span.mr-8 編集
            input(type="radio" name="aaa").ml-6
            span.mr-6 削除
        div.butg    
            button(type="button").mr-4.mt-6.text-4.border-solid.rounded-8px.up 更新
            button(type="button").ml-8.mb-5.text-4.border-solid.rounded-8px.can キャンセル

</template>
<style lang="scss" scoped>
.title {
    text-align: center;
    background-color:#0000FF  
}
.tabContent {
    text-align: center;
}
p {
    text-align: center;
}
.radiog {
    text-align: center;
}
.butg {
    text-align: center;
}
.up {
    background-color: indianred;
}
.whole {
    position:fixed;
    z-index: 100;
}
</style>
