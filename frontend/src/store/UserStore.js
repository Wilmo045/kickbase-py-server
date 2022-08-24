import { defineStore } from 'pinia'

export const useUserStore = defineStore('userstore', {
    state: () => ({ loggedIn: false }),
    getters: {
        getLoginStatus: (state) => {
            return (loggedInStatus) => state.loggedIn
        },
    },
    actions: {

    },
})
