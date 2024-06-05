import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import AppHome from '@/views/AppHome.vue'
import TaskAdd from '@/views/TaskAdd.vue'
import TaskBox from '@/components/Task/TaskBox.vue'
import ManagementStaff from '@/views/ManagementStaff.vue'
import StaffAdd from '@/views/StaffAdd.vue'
import Calendar from '@/views/Calendar.vue'

const routeSettings: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'apphome',
    component: AppHome
  },
  {
    path: '/TaskAdd',
    name: 'taskadd',
    component: TaskAdd
  },
  {
    path: '/ManagementStaff',
    name: 'managementstaff',
    component: ManagementStaff,
    props: true
  },
  {
    path: '/StaffAdd',
    name: 'staffadd',
    component: StaffAdd
  },
  {
    path: '/Calendar',
    name: 'calender',
    component: Calendar
  }
]

const router = createRouter({
  history: createWebHistory('App'),
  routes: routeSettings
})

export default router
