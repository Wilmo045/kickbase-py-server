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
                <p class="title is-4">{{ playername }}</p>
                <p class="subtitle is-8"> Kickbase > Player </p>

            </div>
            <div class="tile is-vertical">
                <p>vor x h</p>
                <p><img src="/src/assets/img/speech_bubble.png" alt="Speech Bubble" class="image" width="20"> 0 </p>
            </div>
        </div>
    </div>
</template>