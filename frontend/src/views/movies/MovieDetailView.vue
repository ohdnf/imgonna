<template>
  <div class="movie-detail-view">
    <b-media>
      <template v-slot:aside>
      <!-- <b-media-aside vertical-align="center"> -->
        <b-img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" width="300" alt="Responsive image"></b-img>
      <!-- </b-media-aside> -->
      </template>

      <Rating :movieId="movie.id"/>

      <b-media-body class="ml-3">
        <h5>{{ movie.title }}</h5>
        <p>{{ movie.overview }}</p>
      </b-media-body>
    </b-media>
    <b-button @click="backToList">뒤로</b-button>
  </div>
</template>

<script>
import Rating from '@/components/Rating.vue'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'MovieDetailView',
  components: {
    Rating,
  },
  data() {
    return {
      movie: null,
    }
  },
  methods: {
    backToList() {
      this.$router.push({ name: 'MovieList' })
    },
    fetchMovie() {
      axios.get(SERVER_URL + `/movies/${this.$route.params.movieId}/`)
        .then(res => {
          this.movie = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
  mounted() {
    this.fetchMovie()
  }
}
</script>

<style>

</style>