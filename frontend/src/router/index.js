import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import NewsFeed from '../views/NewsFeed.vue'
import Team from '../views/Team.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/team',
      name: 'team',
      component: Team
    },
    {
      path: '/',
      name: 'newsfeed',
      component: NewsFeed
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})

export default router
