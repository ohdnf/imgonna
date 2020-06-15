<template>
  <div class="article-detail-view">
    <h1>Article Detail</h1>
    <b-button @click="updateData">수정</b-button>
    <div class="comments-list">
      <ul>
        <li :for="comment in this.articleData.article_comments" v-if="comment">{{ comment }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      articleData: null
    }
  },
  methods: {
    fetchArticle() {
      axios.get(SERVER_URL + `/articles/${this.$route.params.articleId}/`)
      .then(res => {
        this.articleData = res.data
        console.log(res)
      })
    },
    updateData() {
      this.$router.push({
        name: 'ArticleForm',
        params: {
          articleId: this.articleData.id
        }
      })
    },
  },
  created() {
    this.fetchArticle()
  }
}
</script>

<style>

</style>