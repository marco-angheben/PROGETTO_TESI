<template>
  <div id="app">
    <site-navigation />
    <router-view />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import SiteNavigation from "@/components/SiteNavigation.vue";

@Component({
  components: { SiteNavigation }
})
export default class App extends Vue {}
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}

html,
body,
#app {
  width: 100%;
  height: 100%;
  background-color: #e4e4e4;
}

.site-title {
  font-size: 32px;
}
.site-description {
  text-align: center;
  font-size: 18px;
}
.site-placeholder {
  width: 300px;
  height: 300px;

  border: 1px dashed black;
  border-radius: 35px;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  font-size: 38px;
  cursor: pointer;
}
</style>
