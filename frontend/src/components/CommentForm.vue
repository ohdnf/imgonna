<template>
  <div class="comment-form">
    <b-input-group class="mt-3">
      <b-form-input
        id="content"
        v-model="comment.content"
        placeholder="댓글을 입력하세요"
      ></b-form-input>
      <b-input-group-append>
        <b-button variant="outline-primary" @click="createComment">댓글 입력</b-button>
      </b-input-group-append>
    </b-input-group>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'CommentForm',
  props: {
    article: Object,
    targetId: Number,
  },
  data() {
    return {
      comment: {
        content: null,
      },
    }
  },
  methods: {
    createComment() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.comment.article = this.article
      axios.post(SERVER_URL + `/articles/${this.targetId}/comments/`, this.comment, config)
        .then(res => { 
          console.log(res.data)
        })
        .catch(err => {
          console.error(err)
        })
      
    },
  },
}
</script>

<style>
 
</style>