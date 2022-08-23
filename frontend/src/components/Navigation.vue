<script >
import { login } from '../api';

export default {
  data() {
    return { showBurger: false }
  },
 methods: {
    loginUser(username, password){
        return login(username, password)
      }
    }
  };
</script>

<template>
  <nav class="navbar is-fixed-top is-spaced is-dark" role="navigation" aria-label="main navigation">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item">
          <router-link to="/"> BASE </router-link>
        </a>

        <a class="navbar-item"> TRANSFERS </a>

        <a class="navbar-item">
          <router-link to="/team"> TEAM </router-link>
        </a>

        <a class="navbar-item"> LIVE </a>

        <a class="navbar-item"> LIGA </a>



        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample"
          v-on:click="showBurger = !showBurger" v-bind:class="{ 'is-active': showBurger }">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu" v-bind:class="{ 'is-active': showBurger }">
        <div class="navbar-start">
          <a class="navbar-item"> 1. BUNDESLIGA </a>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link"> EINSTELLUNGEN </a>

            <div class="navbar-dropdown">
              <a class="navbar-item"> KICKBASE </a>
              <hr class="navbar-divider" />
              <a class="navbar-item"> SERVER </a>
            </div>
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-light"  v-on:click="loginUser"> Log in </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>