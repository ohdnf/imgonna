<template>
  <div>
    <h1>Article List</h1>
    <b-button @click="createArticle">글 생성</b-button>
    <ul>
      <li v-for="article in articles" :key="`article_${article.id}`" @click="onArticleClick(article)">
        {{ article.title }}
      </li>
    </ul>
  </div>
</template>



<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "ArticleListView",
  data() {
    return {
      articles: []
    };
  },
  methods: {
    fetchArticles() {
      axios.get(SERVER_URL + "/articles/")
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
    onArticleClick(article) {
      this.$router.push({
        name: 'ArticleDetail',
        params: {
          articleId: article.id
        }
      })
    },
    createArticle() {
      this.$router.push({
        name: 'ArticleForm'
      })
    }
  },
  created() {
    this.fetchArticles()
  }
};
</script>

<style>
</style>
