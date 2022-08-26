
<script>
import TeamPlayerCard from '@/components/TeamPlayerCard.vue'
import { mapActions, mapState } from 'pinia'
import { useTeamStore } from '@/store/TeamStore';
import { useUserStore } from '@/store/UserStore';


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
    },
    components: { TeamPlayerCard }
};

</script>
<template>
    <TeamPlayerCard v-for="player in players" :playerFirstName="player.firstName" :playerLastName="player.lastName"
        :playerPicture="player.profileBig" :playerPosition="player.position" :playerNumber="player.number" :playerDayStatus="player.dayStatus"
        :playerAveragePoints="player.averagePoints" :playerTotalPoints="player.totalPoints" :playerMarketValue="player.marketValue"/>
</template>

<!-- <template>
<TeamPlayerCard />
</template> -->