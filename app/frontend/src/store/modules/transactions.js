import api from "../../api/api.js"
import router from "../../router.js"

const state = {
  txHash: null,
};


const getters = {
  getTexHash: state => state.texHash,
};


const actions = {
  async performSendEthereum({ commit }, payload) {
    const response = await api.sendEthereum(payload);
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    }
    else {
      try {
        if (response.error) {
          commit("setFormError", response.error);
          console.log(response.error);
          setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
        } else if (response.tx_hash) {
          console.log(response.tx_hash);
          commit("setTexHash", response.tx_hash);
          router.push(`/transaction-success/${response.tx_hash}`);

        }
      } catch (err) {
        commit("setFormError", "Something went wrong. Try again later");
        setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
      }

    }
  },
};


const mutations = {
  setTexHash: (state, texHash) => {
    state.texHash = texHash
  },

};


export default {
  state,
  getters,
  actions,
  mutations
}