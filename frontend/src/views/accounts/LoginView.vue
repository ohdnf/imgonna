<template>
  <div class="container">
    <p class="h2 text-center my-4">Sign in</p>
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
					<b-form-input v-model="loginData.username" id="username" type="text" placeholder="Enter your username"></b-form-input>
				</b-input-group>
			</b-form-group>
			<b-form-group
				id="input-group-2"
				label="비밀번호"
				label-for="password"
				description="비밀번호를 입력해주세요."
			>
				<b-input-group>
					<b-input-group-prepend is-text>
							<b-icon icon="lock-fill"></b-icon>
						</b-input-group-prepend>
					<b-form-input v-model="loginData.password" id="password" type="password" placeholder="Enter your password"></b-form-input>
				</b-input-group>
			</b-form-group>
		</b-form>
		<div class="text-center">
				<b-button @click="login" @keypress.enter="login">Login</b-button>
		</div>
  </div>
</template>

<script>
import { BIcon } from 'bootstrap-vue'

export default {
		name: 'LoginView',
		components: {
			BIcon,
		},
    data() {
        return {
            loginData: {
                username: null,
                password: null,
            }
        }
    },
    methods: {
        login() {
            this.$emit('submit-login-data', this.loginData)
        }
    }
}
</script>

<style>

</style>
