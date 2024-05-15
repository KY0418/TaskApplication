<template lang="pug">
div.modal
    div.backg
        div.modbox.border-solid.border-0.border-white.rounded-20px.ml-a
            p.text-white.text-2xl.bg-red.text-center.poptitle 削除確認
            p.mt-6.text-center 対象のタスクを削除しますがよろしいですか？
            ul
                li.float-left.yes
                    button(@click="delOk").border-solid.border-white.rounded-10px.p-2.mr-6.text-white.text-sm.bg-blue-500 はい
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

interface Emits {
    (event:"delAgree"):void
    (event:"delNotAgree"):void
}

const emit = defineEmits<Emits>()

const delCancel = (): void => {
    emit("delNotAgree")
}

const delOk = (): void => {
    emit("delAgree")
}

</script>

