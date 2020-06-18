<template>
  <div id="app">
    <NavBar :isLoggedIn="isLoggedIn" @logout="logout"/>
    <router-view @submit-login-data="login" @submit-signup-data="signup"/>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/NavBar.vue'


const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  components: {
    NavBar
  },
  data() {
    return {
      isLoggedIn: false,
      errorMessages: null,
      movies: null,
    }
  },

  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },

    signup(signupData) {
       axios.post(SERVER_URL + '/rest-auth/signup/', signupData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home' })
        })
        .catch(err => this.errorMessages = err.response.data)
    },

    login(loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key)
          console.log(res)
          this.$router.push({ name: 'Home' })
        })
        .catch(err => this.errorMessages = err.response.data)
    },

    logout() {
      const config = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }

      axios.post(SERVER_URL + '/rest-auth/logout/', null, config)
        // .then(() => {})
        .catch(err => console.error(err.response))
        .finally(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          console.log(this.$router.currentRoute)
        })
        if (this.$router.currentRoute.name !== 'Home') {
          this.$router.push({ name: 'Home' })
        }
    },
  },
  mounted() {
    // cookie 에 auth-token 이 존재하는가 체크
    this.isLoggedIn = this.$cookies.isKey('auth-token')
    // if (this.$cookies.isKey('auth-token')) {
    //   this.isLoggedIn = true
    // } else {
    //   this.isLoggedIn = false
    // }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
