<template>
  <div>
    <h1>Article List</h1>
    <b-button variant="primary" @click="createArticle">글 생성</b-button>

    <b-table
      id="my-table"
      hover
      :items="articles"
      :per-page="perPage"
      :current-page="currentPage"
      :fields="fields"
      small
      @row-clicked="onArticleClick"
    ></b-table>

    <div class="overflow-auto mt-3">
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>

    


      <p class="mt-3">Current Page: {{ currentPage }}</p>
    </div>
    
    <!-- <b-list-group>
      <b-list-group-item button v-for="article in articles" :key="`article_${article.id}`" @click="onArticleClick(article)">
        <div class="d-flex w-100 justify-content-between">
          <h5>{{ article.title }}</h5>
          <small>{{ article.user.username }}</small>
        </div>
      </b-list-group-item>
    </b-list-group> -->
  </div>
</template>



<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "ArticleListView",
  data() {
    return {
      perPage: 10,
      currentPage: 1,
      articles: [],
      // 홍주표가 지려버린 곳
      fields: [
        { key: 'id', label: 'ID'},
        { key: 'title', label: 'Title' },
        { key: 'user.username', label: 'Username'},
      ],
    }
  },
  computed: {
    rows() {
      return this.articles.length
    }
  },
  methods: {
    createArticle() {
      this.$router.push({
        name: 'ArticleForm'
      })
    },
    fetchArticles() {
      axios.get(SERVER_URL + "/articles/")
        .then(res => {
          this.articles = res.data
        })
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
  },
  created() {
    this.fetchArticles()
  }
};
</script>

<style>
</style>
