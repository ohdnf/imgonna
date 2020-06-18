<template>
  <div class="container">
    <p class="h3 mt-4 py-0">자유게시판</p>
    <hr class="mb-4 py-0">

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
    <div class="text-right">
      <b-button variant="primary" @click="createArticle">글 생성</b-button>
    </div>
    <div class="overflow-auto mt-3">
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>

      <!-- <p class="mt-3">Current Page: {{ currentPage }}</p> -->
      <b-row align-h="center">
        <b-col cols="6">
        <ArticleSearchBar></ArticleSearchBar>
        </b-col>
      </b-row>
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
import ArticleSearchBar from '@/components/ArticleSearchBar.vue'
const SERVER_URL = "http://localhost:8000";

export default {
  name: "ArticleListView",
  components: {
    ArticleSearchBar
  },
  data() {
    return {
      perPage: 10,
      currentPage: 1,
      articles: [],
      // 홍주표가 지려버린 곳
      fields: [
        { key: 'id', label: '번호'},
        { key: 'title', label: '제목' },
        { key: 'user.username', label: '글쓴이'},
        { key: 'created_at', label: '작성일'}
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
