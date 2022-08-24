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
        ...mapWritableState(useUserStore, { loggedIn: 'loggedIn' })
    },
    methods: {
        loginUser(username, password) {
            response = login(username, password)
            
            //console.log(login(username, password))
        }
    }
};
</script>
<template>
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
            <button type="submit" class="button is-success" v-on:click="loginUser(username, password)">
                Login
            </button>
        </p>
    </div>
</template>