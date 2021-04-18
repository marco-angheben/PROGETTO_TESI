import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';

import Home from '@/views/Home.vue'
import SubmitImage from '@/views/SubmitImage.vue'
import SubmitVideo from '@/views/SubmitVideo.vue'

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/submit-image',
    name: 'submit-image',
    component: SubmitImage
  },
  {
    path: '/submit-video',
    name: 'submit-video',
    component: SubmitVideo
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
