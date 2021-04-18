<template>
  <div class="submit-image">
    <!-- TITLE -->
    <div class="site-title">Submit image</div>

    <!-- PLACEHOLDER / IMAGE -->
    <div
      class="site-placeholder placeholder"
      @click="selectFile"
      v-if="state === State.FILE_SELECTING"
    >+</div>
    <img class="image" :src="objectUrl" v-else />

    <!-- BUTTON -->
    <vs-button class="button" size="large" @click="buttonClicked">{{buttonText}}</vs-button>

    <!-- HIDDEN FILE INPUT -->
    <input
      class="input-file"
      type="file"
      ref="file"
      accept="image/jpeg"
      @change="fileSelected($event)"
    />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import axios from "axios";

import { State } from "@/types";

@Component
export default class SubmitImage extends Vue {
  /* DATA */

  private State = State;
  private state: State = State.FILE_SELECTING;
  private file: File | null = null;
  private objectUrl: string | null = null;
  private loadingObject: any = null;

  /* GETTERS */

  get buttonText(): string {
    switch (this.state) {
      case State.FILE_SELECTING:
        return "Select an image";
      case State.FILE_SELECTED:
        return "Upload the image";
      case State.FILE_UPLOADING:
        return "Uploading the image";
      case State.FILE_UPLOADED:
        return "Image uploaded!!!";
    }
  }

  get loading(): boolean {
    return this.state === State.FILE_UPLOADING;
  }

  /* METHODS */

  fileSelected(event: any): void {
    const input = event.target;

    if (input.files && input.files[0]) {
      this.file = input.files[0];
      this.objectUrl = `${URL.createObjectURL(this.file)}`;
      this.state = State.FILE_SELECTED;
    }
  }

  downloadBlob(blob: Blob): void {
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "image.jpg");
    document.body.appendChild(link);
    link.click();
  }

  startLoadingSpinner(): void {
    this.loadingObject = (this as any).$vs.loading({
      type: "circles",
      scale: "2",
      background: "#ffffffC1",
      opacity: 1,
      color: "primary",
      text: "Uploading"
    });
  }
  stopLoadingSpinner(): void {
    this.loadingObject.close();
  }

  buttonClicked(): void {
    switch (this.state) {
      case State.FILE_SELECTING:
        this.selectFile();
        break;
      case State.FILE_SELECTED:
        this.uploadFile();
        break;
    }
  }

  selectFile(): void {
    const input: any = this.$refs.file;
    input.click();
  }

  async uploadFile(): Promise<void> {
    if (this.state !== State.FILE_UPLOADING) {
      try {
        this.state = State.FILE_UPLOADING;
        this.startLoadingSpinner();

        const formData = new FormData();
        formData.append("image", this.file as File);
        const fileBlob = (
          await axios.post("http://localhost:5000/api/image", formData, {
            responseType: "blob"
          })
        ).data;
        this.state = State.FILE_UPLOADED;
        this.downloadBlob(fileBlob);
      } catch (error) {
        this.state = State.FILE_SELECTED;
        alert(`Errore nel server: ${error?.response?.data}`);
        console.error(error);
        console.error(error?.response);
      } finally {
        this.stopLoadingSpinner();
      }
    }
  }
}
</script>

<style lang="scss" scoped>
$mgy-content: 36px;
$mgy-button: 24px;
$maxheight-image: 400px;

.submit-image {
  margin-top: 84px;
  width: 100%;
  height: calc(100% - 84px);

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  .placeholder {
    margin: $mgy-content 0;
    transition: box-shadow 300ms;
  }
  .placeholder:hover {
    box-shadow: 0 0 14px 1px #b3b3b3;
  }

  .image {
    margin: $mgy-content 0;
    max-height: $maxheight-image;
  }

  .button {
    margin-top: $mgy-button;
  }

  .input-file {
    display: none;
  }
}
</style>
