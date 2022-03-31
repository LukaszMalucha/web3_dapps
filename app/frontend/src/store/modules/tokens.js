import api from "../../api/api.js"

const state = {
  tokens: null,
  total_supply: null,
  symbol: null,
};


const getters = {
  getTokens: state => state.tokens,
  getTotalSupply: state => state.total_supply,
  getSymbol: state => state.symbol,
};


const actions = {
  async fetchTokens({ commit }) {
    const response = await api.tokens();
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    }
    else {
      commit("setTokens", response.results);
    }
  },
  async performRetrieveTotalSupply({ commit }, payload) {
    commit("setLoader", true);
    const response = await api.totalSupply(payload);
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    }
    else {
      commit("setTotalSupply", response.total_supply);
      commit("setSymbol", response.symbol);
      commit("setLoader", false);
    }
  },
  zeroTokens({ commit }) {
      commit("setTotalSupply", null);
      commit("setSymbol", null);
      commit("setLoader", false);
  },
};


const mutations = {
  setTokens: (state, tokens) => {
    state.tokens = tokens
  },
  setTotalSupply: (state, total_supply) => {
    state.total_supply = total_supply
  },
  setSymbol: (state, symbol) => {
     state.symbol = symbol
  },

};


export default {
  state,
  getters,
  actions,
  mutations
}