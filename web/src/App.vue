<template lang="pug">
Header
RouterView.tt
</template>
<style lang="css" scoped>
.tt {
  width: 100%;
  min-width: 600px;
  max-width: 80%;
}
</style>
<script setup lang="ts">
import { RouterView } from 'vue-router'
import AppHome from './views/AppHome.vue'
import Header from './Layout/Header.vue'
</script>
