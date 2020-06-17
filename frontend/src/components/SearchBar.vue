<template>
  <div class="search-bar">
		<b-input-group class="mt-3">
			<b-form-input v-model="inputValue" @keypress.enter="onInput" placeholder="작품 제목을 검색해보세요."></b-form-input>
			<b-input-group-append>
				<span v-if="inputValue!==''">
					<router-link :to="{name: 'MovieSearch', params: {searchString: inputValue}} ">
						<b-button>search</b-button>
					</router-link>
				</span>
				<span v-else>
					<b-button>search</b-button>
					<!-- <router-link tag="button">search</router-link> -->
				</span>
			</b-input-group-append>
		</b-input-group>
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
            if (this.inputValue!=='') {
						this.$router.push({ name: 'MovieSearch', params: { searchString: this.inputValue }})
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