<template>
  <div class="movie-search">
    <p class="text-center">검색 결과 창입니다.</p>
    <p v-if="movies.length==0">
      검색 결과를 찾을 수 없습니다.
    </p>
    <b-container fluid>
      <b-row>
        <b-col cols="3" v-for="movie in movies" :key="`rec_${movie.id}`">
          <b-card
            :title="movie.title"
            :img-src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "MovieSearchView",
  data() {
    return {
      movies: null
    }
  },
  props: ['searchString'],
  methods: {
    searchMovie() {
      axios.get(SERVER_URL+'/movies/', {params: {q: this.searchString}})
        .then(res => {this.movies = res.data})
    }
  },
  computed: {
  msg() {
    return `Searching for, ${this.searchString}!`;
    }
  },
  mounted() {
    this.searchMovie()
  },
  updated() {
    this.searchMovie()
  }
}
</script>

<style>

</style>