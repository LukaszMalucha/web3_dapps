import { apiService } from "@/common/api.service.js";

export default {
// Get current user information
  userInfo() {
    let endpoint = "/auth/current-user/";
    return apiService(endpoint);
  },
//  Account
  defaultAccount() {
    let endpoint = "/api/account-balance/";
    return apiService(endpoint);
  },
  accountBalance(payload) {
    let endpoint = "/api/account-balance/";
    return apiService(endpoint, "POST", payload);
  },

//  Tokens
  tokens() {
    let endpoint = "/api/tokens/";
    return apiService(endpoint);
  },
  totalSupply(payload) {
    let endpoint = "/api/token-supply/";
    return apiService(endpoint, "POST", payload);
  },

//  Pagination
  nextPage(next) {
    let endpoint = next;
    return apiService(endpoint);
  }
}