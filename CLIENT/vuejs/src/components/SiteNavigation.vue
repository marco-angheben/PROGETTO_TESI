<template>
  <div class="site-navigation">
    <vs-navbar fixed center-collapsed padding-scroll v-model="active">
        <template #left>
          <router-link class="home" to="/home" @click.native="active = Page.HOME">Home</router-link>
        </template>

        <vs-navbar-item style="display: none;" :active="active === Page.HOME">
          Home
        </vs-navbar-item>
        <vs-navbar-item :active="active === Page.SUBMIT_IMAGE" to="/submit-image" :id="Page.SUBMIT_IMAGE">
          Submit image
        </vs-navbar-item>
        <vs-navbar-item :active="active === Page.SUBMIT_VIDEO" to="/submit-video" :id="Page.SUBMIT_VIDEO">
           Submit video
        </vs-navbar-item>
      </vs-navbar>

  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

import { Page } from '@/types';

@Component
export default class SiteNavigation extends Vue {
  /* DATA */

  private active: Page = Page.HOME;
  private Page = Page;
}
</script>

<style lang="scss" scoped>
.site-navigation {
  .home {
    font-family: 'Merienda One', cursive;
    font-size: 21px;
    text-decoration: none;
    color: black;
  }
}
</style>
