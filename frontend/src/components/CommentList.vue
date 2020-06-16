<template>
  <div class="comment-list">
    <ul>
      <li :key="comment.comment_id" v-for="comment in comments">{{comment.user.username}} | {{comment.content}}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "CommentList",
  props: {
    comments: Array,
    targetId: Number,
  },
  data() {
    return {
      // comments: []
    }
  },
  methods: {
    fetchComments() {
      axios.get(SERVER_URL + `/${this.targetId}/comments/`)
        .then(res => {
          console.log(res.data)
          this.comments = res.data
        })
    }
  },
  created() {
    this.fetchComments
  },
  computed: {
    
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