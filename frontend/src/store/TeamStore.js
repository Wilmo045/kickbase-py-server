import { defineStore } from 'pinia'
import { useUserStore } from '@/store/UserStore';
import { fetchTeam } from '../api';

export const useTeamStore = defineStore('teamstore', {
    state: () => ({ players: [], lineup: [], lineuptype: [] }),
    getters: {
        getPlayer: (state) => {
            return (playerId) => state.players.find((player) == playerId)
        }
    },
    actions: {
        fetchteam() {
            const userStore = useUserStore()
            fetchTeam(userStore.currentLeague).then((data) => {
                let unsortedplayers = data.data.players
                this.lineup = data.data.lineup
                this.lineuptype = data.data.lineuptype

                //LineUp first
                this.lineup.forEach(element => {
                    let linedupplayer = unsortedplayers.findIndex(arrelm => { return arrelm.id == element })
                    this.players.push(unsortedplayers[linedupplayer])
                    unsortedplayers.splice(linedupplayer, 1)
                });

                //Other players according to their position
                for (var i = 1; i < 5; i++) {
                    let positionplayers = unsortedplayers.filter(element => { return element.position == i });
                    positionplayers.forEach(element => {
                        if (i < 4) {
                            let inputposition = this.players.findIndex(element => {
                                return element.position == i + 1
                            })
                            this.players.splice(inputposition, 0, element)
                        }
                        else {
                            this.players.push(element)
                        }
                    });
                }
            })
        },
    },
})
