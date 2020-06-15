<template>
  <div>
    <h1>New Article</h1>
    <div>
      <label for="title">title:</label>
      <input v-model="articleData.title" id="title" type="text" />
    </div>
    <div>
      <label for="content">content:</label>
      <textarea v-model="articleData.content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
      <button @click="createArticle">Submit!</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "CreateView",
  data() {
    return {
      articleData: {
        title: null,
        content: null,
      }
    };
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `JWT ${this.$cookies.get('auth-token')}`
        }
      }
      // article 생성은 Header: Token / Body: { title: , content: }
      axios.post(SERVER_URL + '/articles/', this.articleData, config)
        .then(res => { 
          console.log(res.data) 
          this.$router.push({ name: 'List' })
        })
        .catch(err => console.log(err.response.data))
    },
    // checkLoggedIn() {
    //   if (!this.$cookies.isKey('auth-token')) {
    //     this.$router.push({ name: 'Login' })
    //   } 
    // }
  },

  // created() {
  //   this.checkLoggedIn()
  // },
};
</script>

<style>
</style>
