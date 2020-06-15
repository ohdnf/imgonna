<template>
  <div>
    <h1>New Article</h1>

    <div>
      <label for="title">title:</label>
      <b-input v-model="article.title" id="title" type="text" />
    </div>
    <div>
      <label for="content">content:</label>
      <b-form-textarea v-model="article.content" id="content" cols="30" rows="10"></b-form-textarea>
    </div>
    <div>
      <b-button @click="formMode ? updateArticle() : createArticle()">저장</b-button>&nbsp;
      <b-button @click="cancel">취소</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "ArticleFormView",
  data() {
    return {
      article: {
        id: null,
        title: null,
        content: null,
      },
      formMode: this.$route.params.articleId > 0 ? true : false,
    };
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // article 생성은 Header: Token / Body: { title: , content: }
      axios.post(SERVER_URL + '/articles/', this.article, config)
        .then(res => { 
          console.log(res.data) 
          this.$router.push({
            name: 'ArticleDetail',
            params: {
              articleId: res.data.id
            }
          })
        })
        .catch(err => console.log(err.response.data))
    },
    fetchArticle() {
      axios.get(SERVER_URL + `/articles/${this.article.id}`)
        .then(res => {
          this.article.title = res.data.title
          this.article.content = res.data.content
        })
    },
    updateArticle() { // 수정
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.put(SERVER_URL + `/articles/${this.article.id}`, this.article, config)
      .then(res => {
        console.log(res.data)
        this.$router.push({
          name: 'ArticleForm',
          params: {
            articleId: this.article.id
          }
        })
      })
      .catch(err => {
        console.log(err.response.data)
        this.$router.push({ name: 'ArticleList' })
      })
      
    },
    cancel() {
      this.$router.push({ name: 'ArticleList' })
    },
    checkLoggedIn() {
      if (!this.$cookies.isKey('auth-token')) {
        this.$router.push({ name: 'Login' })
      }
    }
  },

  created() {
    this.checkLoggedIn()

    if(this.$route.params.articleId > 0) {
        this.article.id = Number(this.$route.params.articleId)
        this.fetchArticle()
      }
  },
};
</script>

<style>
</style>
