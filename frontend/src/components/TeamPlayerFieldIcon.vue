<script>
export default {
    props: {
        'playerLastName': String,
        'playerPicture': String
    },
    computed: {
    }
}
</script>
<template>

    <figure class="image is-48x48">
        <img class="is-rounded" :src="playerPicture" alt="PlayerPicture">
    </figure>
    <figcaption>{{ playerLastName }}</figcaption>

</template>