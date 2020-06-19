<template>
  <b-nav-form>
    <b-form-input size="sm" class="mr-sm-2" v-model="inputValue" @keypress.enter="onInput" placeholder="작품 제목을 검색해보세요."></b-form-input>
    <span v-if="inputValue!==''">
      <router-link :to="{name: 'MovieSearch', params: {searchString: inputValue}} ">
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </router-link>
    </span>
    <span v-else>
      <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      <!-- <router-link tag="button">search</router-link> -->
    </span>
  </b-nav-form>
</template>

<script>

export default {
    name: "NavSearchBar",
    data() {
        return {
            inputValue: ""
        }
    },
    methods: {
        onInput() {
          if (this.inputValue!=='') {
          this.$router.push({ name: 'MovieSearch', params: { searchString: this.inputValue }})
          this.inputValue=""
          }
        }   
    }
}
</script>

<style scoped>
</style>