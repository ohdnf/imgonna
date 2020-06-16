<template>
  <div id="app">
    <NavBar :isLoggedIn="isLoggedIn" @logout="logout"/>
    <SearchBar @input-change="onInputChange"/>
    <router-view class="container mt-4" @submit-login-data="login" @submit-signup-data="signup"/>
  </div>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/NavBar.vue'
import SearchBar from '@/components/SearchBar.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  components: {
    NavBar,
    SearchBar
  },
  data() {
    return {
      isLoggedIn: false,
      errorMessages: null,
      inputValue: '',
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
    onInputChange(inputText) {
      this.inputValue = inputText
      // console.log(SERVER_URL+`/movies/?q=${this.inputValue}`)
      // console.log(encodeURI(SERVER_URL+`/movies/?q=${this.inputValue}`))
      axios.get(SERVER_URL+'/movies/', {
        params: {
          q: this.inputValue,
        }
      })
        .then(res => { 
          // res.data.items.forEach(item => {
          //   const parser = new DOMParser()
          //   const doc = parser.parseFromString(item.snippet.title, 'text/html')
          //   item.snippet.title = doc.body.innerText
          // })
          this.movies = res.data
          this.$router.push({ path: 'movies/search', query: { movies: this.movies} })
        })
        .catch(err => console.error(err))
    }
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
