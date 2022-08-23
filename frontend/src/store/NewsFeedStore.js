import { defineStore } from 'pinia'

export const useNewsFeedStore = defineStore('newsfeedstore', {
    state: () => ({ players: [{ "name": "Player1", "playerpicture": "/src/assets/img/player_simple.jpg" }, { "name": "Player2", "playerpicture": "/src/assets/img/player_simple.jpg" }, { "name": "Player3", "playerpicture": "/src/assets/img/player_simple.jpg" }] }),
    getters: {
        getPlayer: (state) => {
            return (playerId) => state.players.find((player) == playerId)
        },
    },
    actions: {
        increment() {
            this.count++
        },
    },
})
