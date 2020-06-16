<template>
  <div class="search-bar">
      <input v-model="inputValue" @keypress.enter="onInput" placeholder="작품 제목을 검색해보세요.">
      <!-- <input v-model="inputValue" placeholder="작품 제목을 검색해보세요."> -->
      <!-- <router-link :to="'movies/search/'+inputValue" tag="button">search</router-link> -->
      <router-link :to="{name: 'MovieSearch', params: {searchString: inputValue}} " tag="button">search</router-link>
  </div>
</template>

<script>

export default {
    name: 'SearchBar',
    data() {
        return {
            inputValue: ""
        }
    },
    methods: {
        onInput() {
            this.$router.push({ name: 'MovieSearch', params: { searchString: this.inputValue }})
        }   
    }
}
</script>

<style scoped>
/* 
    scoped 옵션은 해당 컴포넌트에만 영향을 준다. 
    하지만, class 지정은 해야한다.
*/
div.search-bar {
    text-align: center;
    margin: 20px;
}

div.search-bar > input {
    width: 75%
}
</style>