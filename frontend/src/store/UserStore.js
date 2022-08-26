import { defineStore } from 'pinia'

export const useUserStore = defineStore('userstore', {
    state: () => ({
        username: '',
        currentLeague: '',
        loggedIn: false
    }),
    getters: {
        getLoginStatus: (state) => {
            return (loggedInStatus) => state.loggedIn
        },
        getUsername: (state) => {
            return (username) => state.username
        },
        getCurrentLeague: (state) => {
            return (currentLeague) => state.currentLeague
        },
    },
    actions: {

    },
})
