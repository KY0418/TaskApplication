import './assets/reset.css'
import 'uno.css' 
import '@unocss/preset-uno'
import { VueElement, createApp } from 'vue'
import { createPinia } from 'pinia'
import ToastPlugin from 'vue-toast-notification'
import 'vue-toast-notification/dist/theme-default.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(ToastPlugin)
app.mount('#app')