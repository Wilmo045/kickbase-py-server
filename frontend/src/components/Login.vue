<script>
import { login } from '../api';
import { mapWritableState } from 'pinia'
import { useUserStore } from '@/store/UserStore';
export default {
    data() {
        return {
            username: '',
            password: ''
        }
    },
    computed: {
        ...mapWritableState(useUserStore, { loggedIn: 'loggedIn' }),
        ...mapWritableState(useUserStore, { loggedInUser: 'username' }),
        ...mapWritableState(useUserStore, { selectedLeague: 'currentLeague' })
    },
    methods: {
        loginUser() {
            login(this.username, this.password).then((data) => {
                this.loggedInUser = data.data.email;
                this.selectedLeague = data.data.leagues[0].id
                this.loggedIn = true
            }).then(this.$router.push('/'))
        }
    }
};
</script>
<template>
    <form @submit.prevent="loginUser">
        <div class="field">
            <label class="label">Username</label>
            <p class="control has-icons-left has-icons-right">
                <input class="input" type="email" placeholder="Email" v-model="username">
                <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                </span>
                <span class="icon is-small is-right">
                    <i class="fas fa-check"></i>
                </span>
            </p>
        </div>
        <div class="field">
            <label class="label">Password</label>
            <p class="control has-icons-left">
                <input class="input" type="password" placeholder="Password" v-model="password">
                <span class="icon is-small is-left">
                    <i class="fas fa-lock"></i>
                </span>
            </p>
        </div>
        <div class="field">
            <p class="control">
                <button type="submit" class="button is-success">
                    Login
                </button>
            </p>
        </div>
    </form>
</template>