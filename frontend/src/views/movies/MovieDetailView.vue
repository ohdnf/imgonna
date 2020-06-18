<template>
  <div class="movie-detail-view">

    <!-- 헤더 정보: 포스터, 제목 등 -->
    <div class="backdrop">
      <b-img :src="`https://image.tmdb.org/t/p/w1920_and_h800_multi_faces${movie.backdrop_path}`" fluid alt="backdrop image"></b-img>
    </div>
    <div class="d-flex m-4">
      <div class="poster m-4">
        <b-img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" width="300" alt="poster image"></b-img>
      </div>
      <div class="overview flex-column m-4">
        <div class="title p-2">
          <h2>{{ movie.title }}<b-badge variant="info">{{ movie.vote_average }}</b-badge></h2>
          <!-- <p><small v-for="genre in genres" :key="`genre_${genre.id}`">{{genre.name}}</small></p> -->
          <p><small>{{ movie.release_date }}</small> &bull; <small>{{ genres.toString() }}</small></p>
        </div>
        <div class="evaluation d-flex">
          <div class="add-to-cart mr-4">
            <b-button-group>
              <b-button><b-icon icon="plus"></b-icon>보고싶어요</b-button>
              <b-button><b-icon icon="caret-down-fill"></b-icon></b-button>
            </b-button-group>
          </div>
          <Rating :movieId="movie.id"/>
        </div>
        <div class="overview p-2">
          <h4>줄거리</h4>
          <p>{{ movie.overview }}</p>
        </div>
      </div>
    </div>

    <!-- 제작진 -->
    <div class="credits container">
      <h3>출연/제작</h3>
      <div class="d-flex m-4 overflow-auto">
        <b-card-group class="casts" v-for="cast in casts.slice(0, 10)" :key="`cast_${cast.order}`">
          <b-card
            :title="cast.name"
            :sub-title="cast.character"
            :img-src="`https://image.tmdb.org/t/p/w500${cast.profile_path}`"
            img-alt="Profile"
            img-top
            tag="article"
            style="width: 10rem;"
            class="mb-2"
          ></b-card>
        </b-card-group>
      </div>
    </div>

    <!-- 컨텐츠 제안 -->
    <!-- 추천 -->
    <div class="recommendation container">
      <h3>추천드리는 영화</h3>
      <div class="d-flex m-4 overflow-auto">
        <b-card-group v-for="recommendation in recommendations" :key="`rec_${recommendation.id}`">
          <b-card
            :title="recommendation.title"
            :sub-title="`★ ${recommendation.vote_average}`"
            :img-src="`https://image.tmdb.org/t/p/w500${recommendation.poster_path}`"
            img-alt="movie poster"
            img-top
            tag="recommendation"
            style="width: 15rem;"
            class="mb-2"
          ></b-card>
        </b-card-group>
      </div>
    </div>

    <!-- 유사 영화 -->
    <div class="similar-movies container">
      <h3>비슷한 영화</h3>
      <div class="d-flex m-4 overflow-auto">
        <b-card-group v-for="similarMovie in similarMovies" :key="`sim_${similarMovie.id}`">
          <b-card
            :title="similarMovie.title"
            :sub-title="`★ ${similarMovie.vote_average}`"
            :img-src="`https://image.tmdb.org/t/p/w500${similarMovie.poster_path}`"
            img-alt="movie poster"
            img-top
            tag="similar-movies"
            style="width: 15rem;"
            class="mb-2"
          >
          </b-card>
        </b-card-group>
      </div>
    </div>
    
    <div class="d-flex justify-content-center m-4">
      <b-button @click="backToList">뒤로</b-button>
    </div>
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
      genres: [],
      recommendations: [],
      similarMovies: [],
      casts: [],
      director: null,
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
          this.genres = temp
        })
        .catch(err => {
          console.error(err)
        })
    },
    getGenre() {
      console.log(Object.values(this.movie.genres))
      let temp = []
      for (let genreId of Object.values(this.movie.genres)) {
        // temp.push({id: genreId, name: GENRES[genreId]})
        temp.push(GENRES[genreId])
      }
      this.genre = temp
    },
    getRecommendations() {
      axios.get(TMDB_URL + `/movie/${this.$route.params.movieId}/recommendations?api_key=${API_KEY}&language=ko-KR&page=1`)
        .then(res => {
          this.recommendations = res.data.results
          // console.log(res)
        })
    },
    getSimilarMovies() {
      axios.get(TMDB_URL + `/movie/${this.$route.params.movieId}/similar?api_key=${API_KEY}&language=ko-KR&page=1`)
        .then(res => {
          this.similarMovies = res.data.results
          // console.log(res)
        })
    },
    getCredits() {
      axios.get(TMDB_URL + `/movie/${this.$route.params.movieId}/credits?api_key=${API_KEY}&language=ko-KR&page=1`)
        .then(res => {
          this.casts = res.data.cast
          // this.crews = res.data.crew
        })
    },
  },
  mounted() {
    this.fetchMovie()
    // this.getGenre()
    this.getRecommendations()
    this.getSimilarMovies()
    this.getCredits()
  },
}
</script>

<style scoped>
</style>