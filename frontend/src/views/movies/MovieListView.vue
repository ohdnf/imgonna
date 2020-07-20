<template>
  <div>
    <h1 class="text-center my-4">영화 목록</h1>
    <b-container class="d-flex justify-content-around">
      <b-row>
        <b-col cols="4" v-for="movie in movies" :key="`movie_${movie.backdrop_path}`">
          <b-card
            :title="movie.title"
            :img-src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
            @click="onMovieClick(movie)"
          >
            <b-card-text>
              {{ `${movie.overview.slice(0, 40)}...` }}
            </b-card-text>

            <!-- <b-button @click="onMovieClick(movie)" variant="primary">상세 정보</b-button> -->
          </b-card>
        </b-col>
        <infinite-loading @infinite="infiniteHandler"></infinite-loading>
      </b-row>
    </b-container>

    <!-- <div id="bottomSensor"></div> -->
  </div>
</template>

<script>
import axios from "axios";
import InfiniteLoading from 'vue-infinite-loading'

// const SERVER_URL = "http://localhost:8000"
const TMDB_API_URL = "https://api.themoviedb.org/3"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
// const scrollMonitor = require("scrollmonitor")

export default {
  name: "MovieListView",
  data() {
    return {
      movies: [],
      page: 1,
    };
  },
  components: {
    InfiniteLoading,
  },
  methods: {
    // fetchMovies() {
    //   axios.get(SERVER_URL + "/movies/")
    //     .then(res => this.movies = res.data)
    //     .catch(err => console.error(err))
    // },
    fetchMovies() {
      axios.get(TMDB_API_URL+ `/movie/popular?api_key=${API_KEY}&language=ko-KR&page=${this.page++}`)
        .then(res => {
          // console.log(res.data)
          this.movies = res.data.results
        })
        .catch(err => console.error(err))
    },
    onMovieClick(movie) {
      this.$router.push({
        name: 'MovieDetail',
        params: {
          movieId: movie.id
        }
      })
    },
    infiniteHandler() {
      axios.get(TMDB_API_URL+ `/movie/popular?api_key=${API_KEY}&language=ko-KR&page=${this.page++}`)
        .then(res => {
          setTimeout( () => {
            this.movies = this.movies.concat(res.data.results)
            // console.log(res)
          // if (res.data.results.length) {
          //   $state.loaded
          //   this.page += 1
          //   if (this.movies.length / 10 == 0) {
          //     $state.complete()
          //   }
          // } else {
          //   $state.complete()
          // }
        }, 1000)
      })
      .catch(err => console.error(err))
    }
  },
  created() {
    this.fetchMovies()
    // this.getPopulars()
  },
  mounted() {
  },
  updated() {
  },
};
</script>

<style>
</style>
