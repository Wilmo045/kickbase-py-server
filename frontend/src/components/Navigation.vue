<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <nav
    class="navbar is-fixed-top is-spaced is-dark"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <a class="navbar-item" href="https://de.kickbase.com/">
        <img
          src="https://assets.website-files.com/62c6f46289c7424b15fe2956/62c85be911cf58dec07bd203_kickbase-star.svg"
          width="112"
          height="28"
        />
      </a>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item"> <router-link to="/"> BASE </router-link> </a>
          
        <a class="navbar-item"> TRANSFERS </a>

        <a class="navbar-item"> <router-link to="/team"> TEAM </router-link> </a>

        <a class="navbar-item"> LIVE </a>

        <a class="navbar-item"> LIGA </a>

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
              <a class="button is-light"> Log in </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>