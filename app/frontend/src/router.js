import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import AccountBalanceView from "./views/AccountBalanceView.vue";
import NotFound from "./views/NotFound.vue";


Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/account-balance",
      name: "account-balance",
      component: AccountBalanceView
    },

    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
