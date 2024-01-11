import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
// import TournamentView from "../views/TournamentView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/tournament",
      name: "tournament",
      component: () => import("../views/TournamentView.vue"), //for the lazy load
    },
  ],
});

export default router;
