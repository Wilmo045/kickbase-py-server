<script>
export default {
    props: {
        'playername': String,
        'playerpicture': String
    }
}
</script>
<template>
    <div class="box">
        <div class="tile is-ancestor">
            <div class="tile is-2 is-parent">
                <figure class="image is-48x48 is-child is-centered">
                    <img :src="playerpicture" alt="PlayerPicture" class="image" width="100">
                </figure>
            </div>
            <div class="tile is-6 is-vertical">
                <div class="level-left">
                    <div class="level-item subtitle is-6">
                        <p>NR</p>
                    </div>
                    <div class="level-item subtitle is-6">
                        <p>POS</p>
                    </div>
                    <div class="level-item subtitle is-6">
                        <p>AUFGESTELLT</p>
                    </div>
                    <div class="level-item subtitle is-6"></div>

                </div>
                <p class="title is-4">{{ playername }}</p>
                <div class="level-left">
                    <div class="level-item"> PKT </div>
                    <div class="level-item"> SCHNITT </div>
                </div>
            </div>
            <div class="tile">
                MARKTWERT
            </div>
        </div>
    </div>
</template>