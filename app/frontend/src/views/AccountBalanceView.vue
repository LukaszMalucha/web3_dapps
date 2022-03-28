<template>
  <div class="row plain-element">
    <div class="row text-start row-back">
      <a class="back-link" @click="hasHistory() ? $router.go(-1): $router.push('/')">
        <i class="fas fa-chevron-left"></i> Back To Menu
      </a>
    </div>
    <div class="dashboard-cards">
      <div class="row row-title">

      </div>

      <div class="row row-cards">

        <p class="error"  v-if="getFormError()">
          <span id="formError">{{ getFormError() }}</span>
        </p>
        <p class="error"  v-else>
        </p>
        <form @submit.prevent="accountBalance()" enctype="multipart/form-data">
          <div class="col col-12 col-sm-12 col-md-8 plain-element">
            <div class="card insights-card insights-card-left">
              <div class="row plain-element">

                <div class="col col-12 col-sm-12 col-md-8 plain-element">
                  <div class="card-header">
                    <h6>Check Account Balance</h6>
                    <p> Paste your Wallet Address</p>
                  </div>
                </div>
                <div class="col col-12 col-sm-12 col-md-4 plain-element text-end">
                  <div class="card-header">
                    <button type="submit" class="btn btn-form">
                      Check Balance
                    </button>
                  </div>
                </div>

              </div>
              <p class="w-100"></p>
              <div class="row plain-element">
                <div class="row plain-element text-start">

                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      Wallet Address:
                    </h6>

                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                    <span v-if="getDefaultWallet()" class="span-function" @click="pasteDefaultWallet()">Paste Env. Wallet</span>
                    <p v-else style="height: 18px; margin: 0px;"></p>
                    <textarea rows="1" cols="30" name="wallet_address" v-model="wallet_address" required></textarea>
                  </div>

                </div>
                <p class="w-100"></p>
                <p class="w-100"></p>
                <div class="table-content">
                  <table v-if="getAccountBalance()" class="table-crypto">
                    <tbody>
                    <tr>
                      <td>Ethereum</td>
                      <td class="text-start font-green">
                                      <i-count-up
                                              :start="0"
                                              :endVal="parseInt(getAccountBalance())"
                                              :duration="0.5"
                                              :callback="callback"
                                              :options="options"
                                      ></i-count-up>
                     </td>
                    </tr>
                    <tr style="display: none;">
                      <td>USD</td>
                      <td class="text-center">1037</td>
                    </tr>
                    </tbody>
                  </table>
                </div>


              </div>

            </div>

          </div>
        </form>
      </div>

    </div>
  </div>
</template>




<script>
import { mapGetters, mapActions } from "vuex";
import ICountUp from 'vue-countup-v2';

export default {
  name: 'AccountBalance',
  components: {
      ICountUp,
  },
  data() {
    return {
     error: null,
     wallet_address: null,
     options: {
       useEasing: true,
       useGrouping: true,
       separator: '',
       prefix: '0.00',
       suffix: ''
     }
    }
  },
  methods: {
    ...mapGetters(["getAccountBalance", "getFormError", "getDefaultWallet"]),
    ...mapActions([ "fetchAccountBalance", "performSetFormError"]),
    accountBalance() {
      this.fetchAccountBalance({"wallet_address": this.wallet_address})
    },
    pasteDefaultWallet() {
      this.wallet_address = this.getDefaultWallet()
    },
    callback: function (ins) {
        ins.update(ins.endVal + 100)
    },
    hasHistory () {
      return window.history?.length > 1
    },

  },
  created() {
    document.title = "Account Balance";
    this.performSetFormError(null);
  }
};

</script>