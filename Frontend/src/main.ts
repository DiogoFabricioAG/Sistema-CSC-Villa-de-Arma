import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// Set the base URL for axios
const pinia = createPinia()
axios.defaults.baseURL = 'http://127.0.0.1:5000/'

createApp(App).use(router).use(pinia).mount('#app')
