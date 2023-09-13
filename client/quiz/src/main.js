import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '@/normalize.css'
import '@/main.css'

export const app = createApp(App);
export const appContext = app.use(router).mount('#app');
