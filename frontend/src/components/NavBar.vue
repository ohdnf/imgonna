<template>
  <div class="my-nav">
    <b-navbar class="home-nav" v-if=" $route.path =='/'" toggleable="sm" type="dark" variant="transparent">
      <b-navbar-brand to="/">imgonna</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'MovieList' }">영화 목록</b-nav-item>
          <b-nav-item :to="{ name: 'ArticleList' }">자유게시판</b-nav-item>
        </b-navbar-nav>
        
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown text="Account" right>
            <b-dropdown-item v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</b-dropdown-item>
            <b-dropdown-item v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</b-dropdown-item>
            <b-dropdown-item v-if="isLoggedIn">Profile</b-dropdown-item>
            <b-dropdown-item v-if="isLoggedIn" @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <b-navbar v-else toggleable="sm" type="light" variant="light">
      <b-navbar-brand to="/">imgonna</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'MovieList' }">영화 목록</b-nav-item>
          <b-nav-item :to="{ name: 'ArticleList' }">자유게시판</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <NavSearchBar class="mr-4"></NavSearchBar>

          <b-nav-item-dropdown text="Account" right>
            <b-dropdown-item v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</b-dropdown-item>
            <b-dropdown-item v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</b-dropdown-item>
            <b-dropdown-item v-if="isLoggedIn" :to="{ name: 'Profile' }">Profile</b-dropdown-item>
            <b-dropdown-item v-if="isLoggedIn" @click="logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  
</template>

<script>
import NavSearchBar from '@/components/NavSearchBar.vue'
export default {
  name: "NavBar",
  components: {
    NavSearchBar
  },
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {};
  },
  methods: {
    logout() {
      this.$emit('logout')
    }
  }
};
</script>

<style scoped>
.home-nav {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}
</style>