<template>
  <div>
    <h1>Movie List</h1>
    <b-container fluid>
      <b-row>
        <b-col cols="6" v-for="movie in movies" :key="`movie_${movie.id}`">
          <b-card
            :title="movie.title"
            :img-src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              {{ `${movie.overview.slice(0, 40)}...` }}
            </b-card-text>

            <b-button @click="onMovieClick(movie)" variant="primary">Go somewhere</b-button>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000"
// const TMDB_POSTER_URL = ""

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
    onMovieClick(movie) {
      this.$router.push({
        name: 'MovieDetail',
        params: {
          movieId: movie.id
        }
      })
    }
  },
  created() {
    this.fetchMovies()
  }
};
</script>

<style>
</style>
