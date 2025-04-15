import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../pages/About.vue') // Lazy loading
  },
  {
    path: '/census',
    name: 'census',
    component: () => import('../pages/Padron/Census.vue')
  },
  {
    path: '/assembly',
    name: 'assembly',
    component: () => import('../pages/Asamblea/Assemblies.vue')
  },
  {
    path: '/debt',
    name: 'debt',
    component: () => import('../pages/Deudas/Debts.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
