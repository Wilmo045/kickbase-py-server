<script>
import TeamPlayerFieldIcon from '@/components/TeamPlayerFieldIcon.vue'
export default {
    props: {
        'players': Array,
        'lineup': Array
    },
    computed: {
        goalkeepers() {
            return this.players.filter(elm => ((elm.position == 1) && (this.lineup.includes(elm.id))));
        },
        defenders() {
            return this.players.filter(elm => ((elm.position == 2) && (this.lineup.includes(elm.id))));
        },
        midfielders() {
            return this.players.filter(elm => ((elm.position == 3) && (this.lineup.includes(elm.id))));
        },
        strikers() {
            return this.players.filter(elm => ((elm.position == 4) && (this.lineup.includes(elm.id))));
        }
    },
    components: {
        TeamPlayerFieldIcon
    }
}
</script>
<template>
    <div class="block">
        <div
            style="background-image: url(/src/assets/img/field.svg); background-repeat: no-repeat; background-attachment: scroll; background-size: cover;">
            <div class="level is-mobile">
                <TeamPlayerFieldIcon v-for="player in strikers" :key="player.id" :playerLastName="player.lastName"
                    :playerPicture="player.profileBig" />
            </div>
            <div class="level is-mobile">
                <TeamPlayerFieldIcon v-for="player in midfielders" :key="player.id" :playerLastName="player.lastName"
                    :playerPicture="player.profileBig" />
            </div>
            <div class="level is-mobile">
                <TeamPlayerFieldIcon v-for="player in defenders" :key="player.id" :playerLastName="player.lastName"
                    :playerPicture="player.profileBig" />
            </div>
            <div class="level is-mobile">
                <TeamPlayerFieldIcon v-for="player in goalkeepers" :key="player.id" :playerLastName="player.lastName"
                    :playerPicture="player.profileBig" />
            </div>
        </div>
    </div>
</template>