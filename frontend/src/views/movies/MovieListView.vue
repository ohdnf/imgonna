<template>
  <div>
    <h1>Movie List</h1>
    <ul>
      <li v-for="movie in movies" :key="`movie_${movie.id}`">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "MovieListView",
  data() {
    return {
      movies: []
    };
  },
  methods: {
    fetchMovies() {
      axios.get(SERVER_URL + "/movies/")
        .then(res => this.movies = res.data)
        .catch(err => console.error(err))
    },
  },
  created() {
    this.fetchMovies()
  }
};
</script>

<style>
</style>
