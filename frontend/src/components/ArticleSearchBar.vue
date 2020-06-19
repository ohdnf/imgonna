<template>
  <div class="article-search-bar">
		<b-input-group class="mt-3">
				<select v-model="selected">
					<!-- <option disabled value=""></option> -->
					<option>제목</option>
					<option>내용</option>
					<option>작성자</option>
				</select>
			<b-form-input v-model="inputValue" @keypress.enter="onInput"></b-form-input>
			<b-input-group-append>
				<span v-if="inputValue!==''">
					<router-link :to="{name: 'MovieSearch', params: {searchString: inputValue}} ">
						<b-button>Search</b-button>
					</router-link>
				</span>
				<span v-else>
					<b-button>Search</b-button>
					<!-- <router-link tag="button">search</router-link> -->
				</span>
			</b-input-group-append>
		</b-input-group>
  </div>
</template>

<script>

export default {
    name: 'ArticleSearchBar',
    data() {
        return {
						inputValue: "",
						selected: "제목"
        }
    },
    methods: {
        onInput() {
            if (this.inputValue!=='') {
						this.$router.push({ name: 'ArticleSearch', params: { searchString: this.inputValue, selected: this.selected }})
            }
        }   
    }
}
</script>

<style scoped>
/* 
    scoped 옵션은 해당 컴포넌트에만 영향을 준다. 
    하지만, class 지정은 해야한다.
*/
/* div.search-bar {
    text-align: center;
    margin: 20px;
}

.form-input {
    width: 75%
} */
</style>