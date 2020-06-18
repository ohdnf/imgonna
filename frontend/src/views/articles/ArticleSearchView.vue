<template>
  <div class="article-search container my-4">
    <p class="text-center">검색 결과 창입니다.</p>
    <p v-if="articles.length==0">
      검색 결과를 찾을 수 없습니다.
    </p>
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
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "ArticleSearchView",
  props: ['searchString', 'selected'],
  data() {
    return {
      articles: [],
      perPage: 10,
      currentPage: 1,
      fields: [
        { key: 'id', label: 'ID'},
        { key: 'title', label: 'Title' },
        { key: 'user.username', label: 'Username'},
        { key: 'created_at', label: '작성일'}
      ]
    }
  },
  computed: {
    rows() {
      return this.articles.length
    },
  },
  methods: {
    searchArticle() {
      axios.get(SERVER_URL+'/articles/', {params: {searchString: this.searchString, selected: this.selected}})
        .then(res => {this.articles = res.data})
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
  mounted() {
    this.searchArticle()
  },
}
</script>

<style>

</style>