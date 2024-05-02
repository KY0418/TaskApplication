<template lang="pug">
p.mt-5.ml-5.text-xl タスク追加
  div.border-solid.rounded-22px.border-gray.ml-6.mt-4.mb-4.w-145
    table
        tr
            td.pt-2.pb-2.pl-2.tr1
                    label(for="sample" ) タスクタイトル：
                        input(type="text" name="sample").ml-8.w-100.te
        tr
            td.pt-2.pb-2.pl-2
                    label(for="radioGroup") ステータス：
                        input(type="radio" name="radioGroup" value="option1").ml-35
                        span.mr-2 未着手
                        input(type="radio" name="radioGroup" value="option1")
                        span 完了
div.ml-120
    button(type="button").border-solid.rounded-15px.border-white.text-white.p-1 タスク追加
    
router-link(:to="{name:'apphome'}") ホーム画面へ
</template>

<style lang="scss" scoped>
.te {
  border: none;
}

.tr1 {
  border-bottom-style:solid ;
  border-color: gainsboro;
}

button {
    background-color: #0000FF;
}

</style>