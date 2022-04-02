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
        <form @submit.prevent="sendEthereum()" enctype="multipart/form-data">
          <div class="col col-12 col-sm-12 col-md-8 plain-element">
            <div class="card insights-card insights-card-left">
              <div class="row plain-element">

                <div class="col col-12 col-sm-12 col-md-8 plain-element">
                  <div class="card-header">
                    <h6>Send Ethereum</h6>
                    <p>Ganache localhost only</p>
                  </div>
                </div>
                <div class="col col-12 col-sm-12 col-md-4 plain-element text-end">
                  <div class="card-header">
                    <button type="submit" class="btn btn-form">
                      Submit Transaction
                    </button>
                  </div>
                </div>

              </div>
              <p class="w-100"></p>
              <div class="row plain-element">
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      My Wallet:
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <textarea rows="1" cols="30" name="sender_address" v-model="sender_address" required></textarea>
                  </div>
                </div>
                                <p class="w-100"></p>
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      Private Key:
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <textarea style="font-size: 14px" rows="1" cols="30" name="private_key" v-model="private_key" required></textarea>
                  </div>
                </div>
                <p class="w-100"></p>
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      Send To:
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <textarea rows="1" cols="30" name="receiver_address" v-model="receiver_address" required></textarea>
                  </div>
                </div>
                <p class="w-100"></p>
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      Amount(ETH):
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-8 col-lg-4 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <input id="price" type="number" name="amount" v-model="amount" class="validate" min="0" max="10000"
                                                   step=".001" required>
                  </div>
                </div>
                <p class="w-100"></p>
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      Amount of Gas:
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-8 col-lg-4 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <input id="price" type="number" name="gas" v-model="gas" class="validate" min="0" max="10000000"
                                                   step="1" required>
                  </div>
                </div>
              </div>
                <p class="w-100"></p>
            </div>

          </div>
        </form>
      </div>

    </div>
  </div>
</template>




<script>
import { mapGetters, mapActions } from "vuex";


export default {
  name: 'TransactionView',
  components: {

  },
  data() {
    return {
     sender_address: null,
     private_key: null,
     receiver_address: null,
     amount: null,
     gas: null,
    }
  },
  methods: {
    ...mapGetters(["getFormError", ]),
    ...mapActions(["performSetFormError", "performSendEthereum"]),
    sendEthereum() {
      this.performSendEthereum({"sender_address": this.sender_address,
                                "private_key": this.private_key,
                                "receiver_address": this.receiver_address,
                                "amount": this.amount,
                                "gas": this.gas
                                })

    },
    hasHistory () {
      return window.history?.length > 1
    },

  },
  created() {
    document.title = "Transactions";
    this.performSetFormError(null);
  }
};

</script>