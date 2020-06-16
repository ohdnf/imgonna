<template>
  <div class="search-bar">
      <input @keypress.enter="onInput" placeholder="작품 제목을 검색해보세요.">
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            // emit 1. 위로 커스텀 이벤트를 쏜다.
            this.$emit('input-change', event.target.value)
        }
    },
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