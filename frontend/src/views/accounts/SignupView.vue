<template>
  <div class="container">
		<p class="h2 text-center my-4">Sign up</p>
		<b-form>
			<b-form-group
				id="input-group-1"
				label="아이디"
				label-for="username"
				description="아이디를 입력해주세요."
			>
				<b-input-group>
					<b-input-group-prepend is-text>
						<b-icon icon="person-fill"></b-icon>
					</b-input-group-prepend>
					<b-form-input v-model="signupData.username" id="username" type="text" placeholder="Enter your username" trim></b-form-input>
				</b-input-group>
			</b-form-group>
			<b-form-group
				id="input-group-2"
				label="비밀번호"
				label-for="password1"
				description="비밀번호는 8자리 이상, 숫자와 문자를 혼합해야합니다."
			>
				<b-input-group>
					<b-input-group-prepend is-text>
							<b-icon icon="lock-fill"></b-icon>
						</b-input-group-prepend>
					<b-form-input v-model="signupData.password1" id="password1" type="password" placeholder="Enter your password"></b-form-input>
				</b-input-group>
			</b-form-group>
			<b-form-group
				id="input-group-3"
				label="비밀번호 확인"
				label-for="password2"
				description="비밀번호를 재입력해주세요."
			>
				<b-input-group>
					<b-input-group-prepend is-text>
							<b-icon icon="exclamation-triangle"></b-icon>
						</b-input-group-prepend>
					<b-form-input v-model="signupData.password2" id="password2" type="password" placeholder="Confirm your password"></b-form-input>
				</b-input-group>
			</b-form-group>
		</b-form>
	<div class="text-center">
			<b-button @click="signup" @keypress.enter="signup">Sign up</b-button>
	</div>
  </div>
</template>

<script>
export default {
    name: 'SignupView',
    data() {
        return {
            signupData: {
                username: null,
                password1: null,
                password2: null,
            }
        }
    },
    methods: {
        signup() {
            this.$emit('submit-signup-data', this.signupData)
        }
    },
}
</script>

<style>

</style>
