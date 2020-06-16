<template>
  <div class="comment-list">
    <ul>
      <li :key="`comment_${comment.id}`" v-for="comment in comments">
        {{comment.user.username}} | {{comment.content}}
        <b-button variant="primary" size="sm" @click="deleteComment(comment.id)">댓글 삭제</b-button>
        <!-- <b-button variant="primary" @click="createArticle">댓글 수정</b-button> -->
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "CommentList",
  props: {
    targetId: Number,
  },
  data() {
    return {
      comments: [],
    }
  },
  methods: {
    fetchComments() {
      axios.get(SERVER_URL + `/articles/${this.targetId}/comments/`)
        .then(res => {
          this.comments = res.data
          console.log(res)
        })
        .catch(err => console.log(err))
    },
    deleteComment(comment_id) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.delete(SERVER_URL + `/articles/${this.targetId}/comments/${comment_id}/`, config)
        .then(res => {
          const idx = this.comments.findIndex(function(item) {return item.id === comment_id})
          if (idx > -1) this.comments.splice(idx, 1)
          console.log(res)
        })
    }
  },
  mounted() {
    this.fetchComments()
    this.$root.$on('submit', data => {
      this.comments.push(data)
    })
  }
}

</script>

<style scoped>
  div.comment-list {
    border: 1px solid ddd;
  }

  div.comment-list > ul {
    list-style: none;
  }
</style>