<template>
  <div>
    <h1>새 글 쓰기</h1>

    <b-form @submit="formMode ? updateArticle() : createArticle()" @cancel="onCancel">
      <!-- 제목 입력 -->
      <b-form-group
        id="title"
        label="제목"
        label-for="title-input"
        description=""
      >
        <b-form-input
          id="title-input"
          v-model="article.title"
          type="text"
          required
          placeholder="제목을 입력하세요"
        ></b-form-input>
      </b-form-group>
      
      <!-- 내용 입력 -->
      <b-form-group
        id="content"
        label="내용"
        label-for="content-input"
      >
        <b-form-input
          id="content-textarea"
          v-model="article.content"
          placeholder="내용을 입력하세요"
          rows="10"
          max-rows="30"
        ></b-form-input>
      </b-form-group>

      <!-- 파일 첨부 -->
      <b-form-file
        v-model="file"
        :state="Boolean(file)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
      <div class="mt-3">Selected file: {{ file ? file.name : '' }}</div>

      <!-- 버튼: 저장/취소 -->
      <b-button type="submit" variant="primary">저장</b-button>&nbsp;
      <b-button type="cancel">취소</b-button>
    </b-form>
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
      // 파일 첨부 추가 구현 필요
      file: null,
    }
  },
  methods: {
    createArticle() { // 생성
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
        .catch(err => console.error(err.response.data))
    },
    fetchArticle() {  // 수정 시 기존 데이터 불러오기
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
        console.error(err.response.data)
        this.$router.push({ name: 'ArticleList' })
      })
    },
    onCancel() {
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
