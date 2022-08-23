
<script >
import NewsMessage from '@/components/NewsMessage.vue'
import { mapState } from 'pinia'
import { useNewsFeedStore } from '@/store/NewsFeedStore';

export default {
    data() {
        return {};
    },
    methods: {},
    computed: {
        ...mapState(useNewsFeedStore, ["players"])
    },
    components: { NewsMessage }
};
</script>
<template>
  <NewsMessage v-for="player in players" :playername="player.name" :playerpicture="player.playerpicture"/>
</template>