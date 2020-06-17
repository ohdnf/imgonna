<template>
  <div class="home">
    <h1>여기는 메인입니다!!!</h1>
    <SearchBar/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
export default {
  name: 'Home',
  components: {
    SearchBar
  }
}
</script>
