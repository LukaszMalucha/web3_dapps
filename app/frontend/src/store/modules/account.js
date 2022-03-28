import api from "../../api/api.js"

const state = {
  accountBalance: null,
  defaultWallet: null,
};


const getters = {
  getAccountBalance: state => state.accountBalance,
  getDefaultWallet: state => state.defaultWallet,
};


const actions = {
  async fetchAccountBalance({ commit }, payload) {
    const response = await api.accountBalance(payload);
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    }
    else {
      commit("setAccountBalance", response.account_balance);
    }
  },
  async fetchDefaultAccountInfo({ commit }) {
    const response = await api.defaultAccount();
    if (!response)  {
      console.log("No default wallet")
    }
    else {
     commit("setDefaultWallet", response.default_wallet)
   }
  }
};


const mutations = {
  setAccountBalance: (state, accountBalance) => {
    state.accountBalance = accountBalance
  },
  setDefaultWallet: (state, defaultWallet) => {
    state.defaultWallet = defaultWallet
  },
};


export default {
  state,
  getters,
  actions,
  mutations
}