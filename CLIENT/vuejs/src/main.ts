import Vue from 'vue';
import App from './App.vue';
import router from './router';

import VueSax from 'vuesax';
import 'vuesax/dist/vuesax.css';

Vue.use(VueSax);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
