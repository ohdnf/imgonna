<template>
  <div class="movie-detail-view">
    <b-media my-4>
      <template v-slot:aside>
      <!-- <b-media-aside vertical-align="center"> -->
        <b-img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" width="300" alt="Responsive image"></b-img>
      <!-- </b-media-aside> -->
      </template>
      <b-media-body class="ml-3">
        <h4>{{ movie.title }}</h4>
        <p>{{ movie.overview }}</p>
        <Rating :movieId="movie.id"/>
      </b-media-body>
    </b-media>
    <div class="credits">
      <h5>출연/제작</h5>
      <ul>
        <!-- <li>{{crews[0].name}}</li> -->
        <li v-for="cast in casts.slice(0,4)" :key="`cast_${cast.order}`">{{cast.name}}</li>
      </ul>
    </div>

    <div class="recommendations">
      <b-container fluid>
        <b-row>
          <b-col cols="3" v-for="recommendation in recommendations" :key="`rec_${recommendation.id}`">
            <b-card
              :title="recommendation.title"
              :img-src="`https://image.tmdb.org/t/p/w500${recommendation.poster_path}`"
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

    <div class="similar-movies">

    </div>
    <b-button @click="backToList">뒤로</b-button>
  </div>
</template>

<script>
import Rating from '@/components/Rating.vue'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'
const TMDB_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const GENRES = {28:"액션",12:"모험",16:"애니메이션",35:"코미디",80:"범죄",99:"다큐멘터리",18:"드라마",10751:"가족",14:"판타지",36:"역사",27:"공포",10402:"음악",9648:"미스터리",10749:"로맨스",878:"SF",10770:"TV 영화",53:"스릴러",10752:"전쟁",37:"서부"}

export default {
  name: 'MovieDetailView',
  components: {
    Rating,
  },
  data() {
    return {
      movie: null,
      genre: [],
      recommendations: [],
      similarMovies: [],
      casts: [],
      crews: [],
    }
  },
  methods: {
    backToList() {
      this.$router.push({ name: 'MovieList' })
    },
    fetchMovie() {
      axios.get(SERVER_URL + `/movies/${this.$route.params.movieId}/`)
        .then(res => {
          // console.log(res.data)
          this.movie = res.data
          let temp = []
          for (let genreId of Object.values(this.movie.genres)) {
            temp.push(GENRES[genreId])
          }
          this.genre = temp
        })
        .catch(err => {
          console.error(err)
        })
    },
    getGenre() {
      console.log(Object.values(this.movie.genres))
      let temp = []
      for (let genreId of Object.values(this.movie.genres)) {
        temp.push(GENRES[genreId])
      }
      this.genre = temp
    },
    getRecommendations() {
      axios.get(TMDB_URL + `/movie/${this.movie.id}/recommendations?api_key=${API_KEY}&language=ko-KR&page=1`)
        .then(res => {
          this.recommendations = res.data.results
          // console.log(res)
        })
    },
    getSimilarMovies() {
      axios.get(TMDB_URL + `/movie/${this.movie.id}/similar?api_key=${API_KEY}&language=ko-KR&page=1`)
        .then(res => {
          this.similarMovies = res.data.results
          // console.log(res)
        })
    },
    getCredits() {
      axios.get(TMDB_URL + `/movie/${this.movie.id}/credits?api_key=${API_KEY}`)
        .then(res => {
          this.casts = res.data.cast
          this.crews = res.data.crew
        })
    },
  },
  beforeMount() {
    this.fetchMovie()
    // this.getGenre()
  },
  mounted() {
    this.getRecommendations()
    this.getSimilarMovies()
    this.getCredits()
  },
}
</script>

<style>

</style>