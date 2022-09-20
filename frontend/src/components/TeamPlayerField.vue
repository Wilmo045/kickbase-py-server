<script>
import TeamPlayerFieldIcon from '@/components/TeamPlayerFieldIcon.vue'
export default {
    props: {
        'players': Array,
        'lineup': Array
    },
    computed: {
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
    components: {
        TeamPlayerFieldIcon
    }
}
</script>
<template>
    <div class="block">
        <div style="background-image: url(/src/assets/img/field.svg);">  
        </div>
        <TeamPlayerFieldIcon v-for="player in goalkeepers" :key="player.id" :playerLastName="player.lastName" :playerPicture="player.profileBig"/> 
    </div>
</template>