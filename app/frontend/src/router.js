import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

import AccountBalanceView from "./views/AccountBalanceView.vue";
import TokenSupplyView from "./views/TokenSupplyView.vue";
import TransactionView from "./views/TransactionView.vue";
import TransactionSuccess from "./views/TransactionSuccess.vue";

import GreetingsView from "./views/GreetingsView.vue";

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
      path: "/transactions",
      name: "transactions",
      component: TransactionView
    },
    {
      path: "/transaction-success/:txHash",
      name: "transaction-success",
      component: TransactionSuccess,
      props: true
    },
    {
      path: "/greetings",
      name: "greetings",
      component: GreetingsView,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
