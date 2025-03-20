import './assets/reset.css'
import 'uno.css'
import '@unocss/preset-uno'
import { VueElement, createApp } from 'vue'
import { createPinia } from 'pinia'
import ToastPlugin from 'vue-toast-notification'
import 'vue-toast-notification/dist/theme-default.css'
import App from './App.vue'
import router from './router'
import { createI18n } from 'vue-i18n'
import { ja } from 'vuetify/locale'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})

const i18n = createI18n({
  locale: 'ja',
  fallbackLocale: 'en',
  messages: {
    ja: ja
  },
  legacy: false
})

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(ToastPlugin)
app.use(vuetify)
app.use(i18n)
app.mount('#app')
