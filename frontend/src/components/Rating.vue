<template>
  <div class="rating d-flex flex-column">
    <!-- !!갓크렉!! https://jsfiddle.net/craig_h_411/992o7cq5/ 외쳐 갓갓!!-->
    <!-- <h2>영화 평점</h2> -->
    <small>평가하기</small>
    <star-rating :show-rating="false" :star-size="30" v-model="rating" :increment="0.5" @rating-selected="onClickScore"></star-rating>
    <!-- <h5>나의 평점: {{rating}}</h5> -->
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'Rating',
  components: {
    StarRating
  },
  props: {
    movieId: Number,  
  },
  data() {
    return {
      ratingId: null,
      rating: 0,
      setMode: null,
    }
  },
  methods: {
    onClickScore(rating) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if (this.setMode === 1) {
        // setMode === '수정'
        // put ==> Rating 수정
        axios.put(SERVER_URL + `/movies/${this.movieId}/rating/${this.ratingId}/`, {"score": rating}, config)
          .then(res => {
            console.log(res)
          })
      } else {
        // setMode === '생성'
        // post ==> Rating 생성
        axios.post(SERVER_URL + `/movies/${this.movieId}/rating/`, {"score": rating}, config)
          .then(res => {
            console.log(res)
          })
      }

    },
    fetchRating() {
      const config = {
        params: {},
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(SERVER_URL + `/movies/${this.movieId}/rating/`, config)
        .then(res => {
          console.log(res.data)
          if (res.data.length) {
            // 별점 매긴게 있다 ==> res.data == [Rating 객체 있음]
            // setMode를 '수정'으로
            this.setMode = 1
            this.rating = res.data[0].score
            this.ratingId = res.data[0].id
          } else {
            // 별점 매긴게 없으면 ==> res.data == Array(0)
            // setMode를 '생성'으로
            this.setMode = 0
          }

        })
    }
  },
  mounted() {
    this.fetchRating()
  },
}
</script>

<style>

</style>