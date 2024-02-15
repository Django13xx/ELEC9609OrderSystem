import { createApp } from 'vue'
import App from './pages/App.vue'
import router from './router/router';

const app = createApp(App);
app.use(router);
app.mount('#app');

window.onload = function() {
    var images = document.getElementsByTagName('img');
    for (var i = 0; i < images.length; i++) {
        images[i].onerror = function() {
            this.onerror = null; // prevent never-ending loops
            this.src = '{% static "images/placeholder.jpg" %}'; // use static in Django
        }
    }
}
//set placeholder image when loading error