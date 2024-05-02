import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import AppHome from '@/views/AppHome.vue'
import TaskAdd from '@/views/TaskAdd.vue'

const routeSettings :RouteRecordRaw[] = [
  {
    path:'/',
    name:'apphome',
    component: AppHome
  },
  {
    path:'/TaskAdd',
    name:"taskadd",
    component:TaskAdd
  }
]

const router = createRouter({
  history: createWebHistory("App"),
  routes:routeSettings
})

export default router
