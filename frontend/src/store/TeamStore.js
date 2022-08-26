import { defineStore } from 'pinia'
import { useUserStore } from '@/store/UserStore';
import { fetchTeam } from '../api';

export const useTeamStore = defineStore('teamstore', {
    state: () => ({ players: [{ "name": "Player1", "playerpicture": "/src/assets/img/player_simple.jpg" }, { "name": "Player2", "playerpicture": "/src/assets/img/player_simple.jpg" }, { "name": "Player3", "playerpicture": "/src/assets/img/player_simple.jpg" }] }),
    getters: {
        getPlayer: (state) => {
            return (playerId) => state.players.find((player) == playerId)
        }
    },
    actions: {
        fetchteam() {
            const userStore = useUserStore()
            fetchTeam(userStore.currentLeague).then((data) => {
                this.players = data.data.players
                console.log(this.players)
            })
        },
    },
})
