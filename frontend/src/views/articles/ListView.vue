<template>
  <div>
    <h1>Article List</h1>
    <ul>
      <li v-for="article in articles" :key="`article_${article.id}`">
        {{ article.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = "http://localhost:8000";

export default {
  name: "ListView",
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
  },
  created() {
    this.fetchArticles()
  }
};
</script>

<style>
</style>
