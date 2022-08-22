import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
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
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
