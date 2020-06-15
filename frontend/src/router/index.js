import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'

import ArticleFormView from '../views/articles/ArticleFormView.vue'
import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleDetailView from '../views/articles/ArticleDetailView.vue'

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
  // 자유게시판
  {
    path: '/articles',
    name: 'ArticleList',
    component: ArticleListView,
  },
  {
    path: '/articles/:articleId',
    name: 'ArticleDetail',
    component: ArticleDetailView,
  },
  {
    path: '/articles/:articleId?',
    name: 'ArticleForm',
    component: ArticleFormView,
    beforeEnter(from, to, next) {
      console.log(from, to)
      if (!Vue.$cookies.isKey('auth-token')) {
        next('/accounts/login')
      } else {
        next()
      }
    }
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
