<template>
  <div>
    <h1 class="text-center my-4">영화 목록</h1>
    <b-container class="d-flex justify-content-around">
      <b-row>
        <b-col cols="4" v-for="movie in movies" :key="`movie_${movie.id}`">
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
      </b-row>
    </b-container>

    <div id="bottomSensor"></div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000"
// const TMDB_API_URL = "https://api.themoviedb.org/3"
// const API_KEY = process.env.VUE_APP_TMDB_API_KEY
// const scrollMonitor = require("scrollmonitor")

export default {
  name: "MovieListView",
  data() {
    return {
      movies: [],
      page: 1,
    };
  },
  methods: {
    fetchMovies() {
      axios.get(SERVER_URL + "/movies/")
        .then(res => this.movies = res.data)
        .catch(err => console.error(err))
    },
    // getPopulars() {
    //   axios.get(TMDB_API_URL+ `/movie/popular?api_key=${API_KEY}&language=ko-KR&page=${this.page++}`)
    //     .then(res => {
    //       // console.log(res.data)
    //       this.movies = [...this.movies, ...res.data.results]
    //     })
    //     .catch(err => console.error(err))
    // },
    onMovieClick(movie) {
      this.$router.push({
        name: 'MovieDetail',
        params: {
          movieId: movie.id
        }
      })
    },
    // addScrollWatcher() {
    //   const bottomSensor = document.querySelector('#bottomSensor')
    //   const watcher = scrollMonitor.create(bottomSensor)
    //   watcher.fullyEnterViewport(() => {
    //     setTimeout(() => {
    //       this.getPopulars()
    //     }, 500)
    //   })
    // },
    // loadUntilViewportIsFull() {
    //   const bottomSensor = document.querySelector('#bottomSensor')
    //   const watcher = scrollMonitor.create(bottomSensor)
    //   if (watcher.fullyEnterViewport) {
    //     this.getPopulars()
    //   }
    // },
  },
  created() {
    this.fetchMovies()
    // this.getPopulars()
  },
  mounted() {
    // this.addScrollWatcher()
  },
  updated() {
    // this.loadUntilViewportIsFull()
  },
};
</script>

<style>
</style>
