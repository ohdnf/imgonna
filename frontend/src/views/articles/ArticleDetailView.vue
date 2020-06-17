<template>
  <div class="article-detail-view">
    <b-card :title="article.title" :sub-title="article.user.username" v-if="article">
      <b-card-text>{{article.content}}</b-card-text>
    </b-card>
    <b-button @click="backToList">뒤로</b-button>
    <b-button variant="outline-primary" @click="editArticle">수정</b-button>
    <div class="comments-group" v-if="article">
      <CommentList :targetId="article.id"/>
      <CommentForm :targetId="article.id"/>
      <!-- <ul>
        <li :for="comment in this.article.article_comments" v-if="comment">{{ comment }}</li>
      </ul> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import CommentList from '@/components/CommentList.vue'
import CommentForm from '@/components/CommentForm.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentList,
    CommentForm,
  },
  data() {
    return {
      article: null,
    }
  },
  methods: {
    backToList() {
      this.$router.push({ name: 'ArticleList' })
    },
    editArticle() {
      this.$router.push({
        name: 'ArticleForm',
        params: {
          articleId: this.article.id
        }
      })
    },
    fetchArticle() {
      axios.get(SERVER_URL + `/articles/${this.$route.params.articleId}/`)
      .then(res => {
        this.article = res.data
      })
      .catch(err => {
        console.error(err)
      })
    },
  },
  
  mounted() {
    this.fetchArticle()
  }
}
</script>

<style>

</style>