
<script>
import TeamPlayerCard from '@/components/TeamPlayerCard.vue'
import TeamPlayerField from '@/components/TeamPlayerField.vue'
import { mapActions, mapState } from 'pinia'
import { useTeamStore } from '@/store/TeamStore';


export default {
    beforeMount() {
        this.fetchteam()
    },
    data() {
        return {};
    },
    methods: {
        ...mapActions(useTeamStore, ['fetchteam'])
    },
    computed: {
        ...mapState(useTeamStore, ["players"]),
        ...mapState(useTeamStore, ["lineup"]),
        goalkeepers() {
            return this.players.filter(elm => (elm.position == 1));
        },
        defenders() {
            return this.players.filter(elm => (elm.position == 2));
        },
        midfielders() {
            return this.players.filter(elm => (elm.position == 3));
        },
        strikers() {
            return this.players.filter(elm => (elm.position == 4));
        }
    },
    components: { TeamPlayerCard, TeamPlayerField }
};

</script>
<template>
     <TeamPlayerField :players="players" :lineup="lineup"/> 
    <p>Torwart</p>
    <TeamPlayerCard v-for="player in goalkeepers" :key="player.id" :playerFirstName="player.firstName"
        :playerLastName="player.lastName" :playerPicture="player.profileBig" :playerPosition="player.position"
        :playerNumber="player.number" :playerDayStatus="player.dayStatus" :playerAveragePoints="player.averagePoints"
        :playerTotalPoints="player.totalPoints" :playerMarketValue="player.marketValue" />
        <p>Abwehr</p>
    <TeamPlayerCard v-for="player in defenders" :key="player.id" :playerFirstName="player.firstName"
        :playerLastName="player.lastName" :playerPicture="player.profileBig" :playerPosition="player.position"
        :playerNumber="player.number" :playerDayStatus="player.dayStatus" :playerAveragePoints="player.averagePoints"
        :playerTotalPoints="player.totalPoints" :playerMarketValue="player.marketValue" />
        <p>Mittelfeld</p>
    <TeamPlayerCard v-for="player in midfielders" :key="player.id" :playerFirstName="player.firstName"
        :playerLastName="player.lastName" :playerPicture="player.profileBig" :playerPosition="player.position"
        :playerNumber="player.number" :playerDayStatus="player.dayStatus" :playerAveragePoints="player.averagePoints"
        :playerTotalPoints="player.totalPoints" :playerMarketValue="player.marketValue" />
        <p>Angriff</p>
    <TeamPlayerCard v-for="player in strikers" :key="player.id" :playerFirstName="player.firstName"
        :playerLastName="player.lastName" :playerPicture="player.profileBig" :playerPosition="player.position"
        :playerNumber="player.number" :playerDayStatus="player.dayStatus" :playerAveragePoints="player.averagePoints"
        :playerTotalPoints="player.totalPoints" :playerMarketValue="player.marketValue" />
</template>