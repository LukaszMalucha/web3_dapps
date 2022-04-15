import Vuex from 'vuex';
import Vue from 'vue';
import common from './modules/common';

import account from './modules/account';
import tokens from './modules/tokens';
import transactions from './modules/transactions';

import greetings from './modules/greetings';

import user from './modules/user';

// Connect Vue with Vuex
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    common,
    account,
    greetings,
    tokens,
    transactions,
    user,
  }
});