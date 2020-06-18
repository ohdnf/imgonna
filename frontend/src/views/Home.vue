<template>
  <div class="home">
    <!-- img-src="https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569_960_720.jpg" -->
    <!-- https://cdn.pixabay.com/photo/2019/04/10/12/40/watercolour-4117017_960_720.png -->
    
      <!-- title="암거나" -->
      <!-- sub-title="영화 추천" -->
    <section class="banner-section">
    </section>
    <div class="row">
      <div class="col-lg-12 col-md-12 col-sm-12 post-title-block">
        <h1 class="text-center">IMGONNA</h1>
        <ul class="list-inline text-center">
          <h4>밤하늘의 별만큼이나 무수한 영화들.. 무슨 영화를 봐야할까?</h4>
          <h3>암거나 ㄴㄴ</h3>
          <h2> I'm gonna recommend</h2>
        </ul>
      </div>
      <div class="col-4 offset-4">
        <SearchBar/>
      </div>
    </div>

    <div class="now-playing container">
      <h3>현재 상영작</h3>
      <div class="d-flex m-4 overflow-auto">
        <b-card-group v-for="movie in nowPlaying" :key="`movie_${movie.id}`">
          <b-card
            :title="movie.title"
            :sub-title="`★ ${movie.vote_average}`"
            :img-src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
            img-alt="movie poster"
            img-top
            tag="similar-movies"
            style="width: 15rem;"
            class="mb-2"
            @click="onMovieClick(movie)"
          >
          </b-card>
        </b-card-group>
      </div>
    </div>

    <!-- <b-card
      overlay
      img-src="https://cdn.pixabay.com/photo/2016/12/29/18/44/background-1939128_960_720.jpg"
      img-alt="Card Image"
      text-variant="white"
    >
      <b-card-text class="m-5">
        밤하늘의 별만큼이나 무수한 영화들.. 무슨 영화를 봐야할까?
      </b-card-text>
      <b-card-text class="m-5">
        암거나 ㄴㄴ imgoona recommend
      </b-card-text>
      <b-card-text class="m-5">
        Some quick example text to build on the card and make up the bulk of the card's content.
      </b-card-text>
      <b-card-text class="m-5" v-text="' '">
          
      </b-card-text>
      <b-card-text class="m-5">
        Some quick example text to build on the card and make up the bulk of the card's content.
      </b-card-text>
    </b-card> -->
  </div>
  
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'

const TMDB_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'Home',
  components: {
    SearchBar
  },
  data() {
    return {
      nowPlaying: [],
    }
  },
  methods: {
    getNowPlaying() {
      axios.get(TMDB_URL + `/movie/now_playing?api_key=${API_KEY}&language=ko-KR`)
        .then(res => {
          this.nowPlaying = res.data.results
          // console.log(res)
        })
    },
    onMovieClick(movie) {
      this.$router.push({
        name: 'MovieDetail',
        params: {
          movieId: movie.id
        }
      })
    },
  },
  mounted() {
    this.getNowPlaying()
  },
}
</script>
<style scoped>
  .banner-section{background-image:url("https://cdn.pixabay.com/photo/2016/12/29/18/44/background-1939128_960_720.jpg"); background-size:cover; height: 380px; width: 100%; left: 0; position: absolute; top: 0; background-position:0;}
  .post-title-block{padding:53px 0;}
  .post-title-block h1 {color: #fff; font-size: 85px; font-weight: bold; text-transform: capitalize;}
  .post-title-block li{font-size:20px; color: #fff;}
</style>