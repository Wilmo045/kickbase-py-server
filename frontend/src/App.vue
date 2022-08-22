<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue';
import Home from './components/Home.vue';
</script>

<template>
  <section class="section">
  <header >
    <Navigation/>
  </header>
  </section>
  <section class="section">
  <main>
    <router-view>
    </router-view>
  </main>
  </section>
</template>
