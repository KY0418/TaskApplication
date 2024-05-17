import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import AppHome from '@/views/AppHome.vue'
import TaskAdd from '@/views/TaskAdd.vue'
import TaskBox from '@/views/TaskBox.vue'

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
  },
  {
    path:'/TaskBox',
    name:'taskhome',
    component:TaskBox
  },
]

const router = createRouter({
  history: createWebHistory("App"),
  routes:routeSettings
})

export default router
