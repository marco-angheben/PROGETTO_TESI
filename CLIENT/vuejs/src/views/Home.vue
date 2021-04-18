<template>
  <div class="home grid">
    <div class="site-title">Home</div>
    <div class="site-description">Use the above navbar to choose if you want to submit an image or a video. After that, click on the button to properly select a file. You will se a preview of the file. Click again the button to upload the file to the server and wait (it could take a lot) until the server will respound and the analyzed file downloaded.</div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

@Component
export default class Home extends Vue {}
</script>

<style lang="scss" scoped>
$gap-title: 36px;
$width-description: 50%;
$color-description: #494949; 

.home {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  .site-description {
    margin-top: $gap-title;
    width: $width-description;
    color: $color-description;
  }
}
</style>
