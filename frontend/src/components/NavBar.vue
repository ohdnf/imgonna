<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand to="/">imgonna</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'MovieList' }">영화</b-nav-item>
          <b-nav-item :to="{ name: 'ArticleList' }">자유</b-nav-item>
          <b-nav-item v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</b-nav-item>
          <b-nav-item v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</b-nav-item>
          <b-nav-item v-if="isLoggedIn" @click="logout">Logout</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  nama: "NavBar",
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
