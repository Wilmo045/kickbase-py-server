<script>
export default {
    props: {
        'playerFirstName': String,
        'playerLastName': String,
        'playerPicture': String,
        'playerNumber': Number,
        'playerPosition': Number,
        'playerDayStatus': Number,
        'playerMarketValue': Number,
        'playerTotalPoints': Number,
        'playerAveragePoints': Number
    },
    computed: {
        playerPositionName() {
            switch (this.playerPosition) {
               case 1: return 'TW';
               case 2: return 'ABW';
               case 3: return 'MF';
               case 4: return 'ANG';
               default: return 'NULL'
            }
        }
    }
}
</script>
<template>
    <div class="box">
        <div class="tile is-ancestor">
            <div class="tile is-2 is-parent">
                <figure class="image is-48x48 is-child is-centered">
                    <img :src="playerPicture" alt="PlayerPicture" class="image" width="100">
                </figure>
            </div>
            <div class="tile is-6 is-vertical">
                <div class="level-left">
                    <div class="level-item subtitle is-6">
                        <p>{{ playerNumber }}</p>
                    </div>
                    <div class="level-item subtitle is-6">
                        <p>{{ playerPositionName }}</p>
                    </div>
                    <div class="level-item subtitle is-6">
                        <p v-if="playerDayStatus==1">AUFGESTELLT</p>
                    </div>
                    <div class="level-item subtitle is-6"></div>

                </div>
                <p class="title is-4">{{ playerFirstName}} {{ playerLastName }}</p>
                <div class="level-left">
                    <div class="level-item"> {{ playerTotalPoints }} </div>
                    <div class="level-item"> {{ playerAveragePoints }} </div>
                </div>
            </div>
            <div class="tile">
                {{ playerMarketValue }}
            </div>
        </div>
    </div>
</template>