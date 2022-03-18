import api from "../../api/api.js"

const state = {
  token: window.localStorage.getItem('token'),
  username: window.localStorage.getItem('username'),
  admin: window.localStorage.getItem('admin'),
  error: null
};


const getters = {
// Check if token exists or not
  isLoggedIn: state => !!state.token || !!state.username,
  getUsername: state => state.username,
  getToken: state => state.token,
  getAdmin: state => state.admin,
  getError: state => state.error,
};


const actions = {
  async getUserInfo({ commit }) {
    const response = await api.userInfo();
    if (response["email"] || response["username"]) {
      const username = response["email"] || response["username"];
      window.localStorage.setItem('username', username);
      const admin = response["admin"];
      window.localStorage.setItem('admin', admin);
    }
    else {
      commit('setUsername', null);
      commit('setAdmin', null);
      window.localStorage.setItem('admin', null);
      window.localStorage.setItem('username', null);
    }

  },
};


const mutations = {
// Update user
  setUsername: (state, username) => {
    state.username = username
  },
  setAdmin: (state, admin) => {
    state.admin = admin
  }
};


export default {
  state,
  getters,
  actions,
  mutations
}