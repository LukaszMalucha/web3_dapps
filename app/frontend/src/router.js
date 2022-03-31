import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import AccountBalanceView from "./views/AccountBalanceView.vue";
import TokenSupplyView from "./views/TokenSupplyView.vue";
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
      path: "/token-supply",
      name: "token-supply",
      component: TokenSupplyView
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
