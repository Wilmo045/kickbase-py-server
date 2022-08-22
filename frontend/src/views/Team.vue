
<script>
import TeamPlayerCard from '@/components/TeamPlayerCard.vue'
import { mapState } from 'pinia'
import { useTeamStore } from '@/store/TeamStore';

export default {
    data() {
        return {};
    },
    methods: {},
    computed: {
        ...mapState(useTeamStore, ["players"])
    },
    components: { TeamPlayerCard }
};


</script>
<template>
    <TeamPlayerCard v-for="player in players" :playername="player.name" :playerpicture="player.playerpicture"/>
</template>

<!-- <template>
<TeamPlayerCard />
</template> -->