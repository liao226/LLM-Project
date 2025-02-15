import {createRouter, createWebHistory} from 'vue-router';
import root from './root';


const router = createRouter({
    history: createWebHistory(),
    routes: root,
});

router.afterEach((_to) => {
    // 回到顶部
    let html = document.getElementById("html");
    if (html) {
        html.scrollTo(0, 0)
    }
});

export default router;
