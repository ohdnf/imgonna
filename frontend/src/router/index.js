import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'

import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ArticleListView from '../views/articles/ArticleListView.vue'

import MovieListView from '../views/movies/MovieListView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/articles/create',
    name: 'ArticleCreate',
    component: ArticleCreateView,
    // beforeEnter(from, to, next) {
    //   console.log(from, to)
    //   if (!Vue.$cookies.isKey('auth-token')) {
    //     next('/accounts/login')
    //   } else {
    //     next()
    //   }
    // }
  },
  {
    path: '/articles',
    name: 'ArticleList',
    component: ArticleListView,
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieListView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
