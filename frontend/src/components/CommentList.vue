<template>
  <div class="comment-list">
    <hr class="px-0">
    <ul class="p-2"> 
      <li class="row" :key="`comment_${comment.id}`" v-for="comment in comments">
        <div class="col-1 px-0" >
          {{comment.user.username}}  
        </div>
        <div class="col-8 px-0">
          {{comment.content}}  
        </div>
        <div class="col-2 px-0">
          {{comment.created_at}}  
        </div>
        <div class="col-1 px-0">
          <b-icon icon="x" @click="deleteComment(comment.id)"></b-icon>
        </div>
        <!-- <b-button variant="primary" @click="createArticle">댓글 수정</b-button> -->
      </li>
    </ul>
    <hr>
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
        .then(() => {
          const idx = this.comments.findIndex(function(item) {return item.id === comment_id})
          if (idx > -1) this.comments.splice(idx, 1)
        })
        .catch((err) => {console.log(err)})
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
* {
  padding: 0px;
}
  /* div.comment-list {
    border: 1px solid ddd;
  } */

  div.comment-list > ul {
    list-style: none;
  }
</style>