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
    <div class="level-item is-flex-direction-column">
        <svg height="100" width="100">
            <defs>
                <clipPath id="circleView">
                    <circle cx="50" cy="50" r="35" />
                </clipPath>
            </defs>
            <circle cx="50" cy="50" r="35" stroke="white" stroke-width="3" fill="white" />
            <image width="100" height="100" :xlink:href="playerPicture" clip-path="url(#circleView)" />
        </svg>
        <p class="has-text-white has-text-weight-bold">{{ playerLastName }}</p>
    </div>
</template>