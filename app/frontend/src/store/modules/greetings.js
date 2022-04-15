import api from "../../api/api.js"

const state = {
  greetings: null,
};


const getters = {
  getGreetings: state => state.greetings,
};


const actions = {
  async performSendGreetings({ commit }, payload) {
    commit("setLoader", true);
    const response = await api.sendGreetings(payload);
    if (!response)  {
      commit("setFormError", "Something went wrong. Try again later");
      setTimeout(() => document.getElementById("formError").style.display = "none", 5000);
    }
    else {
      commit("setGreetings", response.greetings);
      commit("setLoader", false);
      console.log(response.greetings);
    }
  },
  zeroGreetings({ commit }) {
      commit("setGreetings", null);
      commit("setLoader", false);
  },
};


const mutations = {
  setGreetings: (state, greetings) => {
    state.greetings = greetings
  },
};


export default {
  state,
  getters,
  actions,
  mutations
}