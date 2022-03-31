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
        <form @submit.prevent="retrieveTotalSupply()" enctype="multipart/form-data">
          <div class="col col-12 col-sm-12 col-md-8 plain-element">
            <div class="card insights-card insights-card-left">
              <div class="row plain-element">

                <div class="col col-12 col-sm-12 col-md-8 plain-element">
                  <div class="card-header">
                    <h6>Check Token Supply</h6>
                    <p>Choose token from dropdown menu</p>
                  </div>
                </div>
                <div class="col col-12 col-sm-12 col-md-4 plain-element text-end">
                  <div class="card-header">
                    <button type="submit" class="btn btn-form">
                      Total Supply
                    </button>
                  </div>
                </div>

              </div>
              <p class="w-100"></p>
              <div v-if="getTokens()" class="row plain-element">
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      Ethereum Token:
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <div class="input-field  col col-12 col-sm-12 col-md-8 col-lg-8 col-form">
                        <select v-model="token" name="token" id="token" required>
                          <option v-for="(element, index) in getTokens()" :value="element.id" :key="index">
                            {{ element.name }} ({{element.ticker}})
                          </option>
                        </select>
                    </div>
                  </div>
                </div>
                <p class="w-100"></p>
                <p class="w-100"></p>
                <div class="table-content">
                  <div v-if="getLoader() == true" class="row">
                      <div class="loader" id="loader"></div>
                  </div>
                  <table v-if="getTotalSupply() &&  getLoader() == false" class="table-crypto">
                    <tbody>
                    <tr>
                      <td>Total Supply</td>
                      <td class="text-start font-green">
                                      <i-count-up
                                              :start="0"
                                              :endVal="parseInt(getTotalSupply())"
                                              :duration="0.5"
                                              :callback="callback"
                                              :options="options"
                                      ></i-count-up> {{getSymbol()}}
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
  name: 'TokenSupplyView',
  components: {
      ICountUp,
  },
  data() {
    return {
     error: null,
     token: null,
     options: {
       useEasing: true,
       useGrouping: true,
       separator: ',',
       prefix: '',
       suffix: ''
     }
    }
  },
  methods: {
    ...mapGetters(["getFormError", "getTokens", "getTotalSupply", "getSymbol", "getLoader"]),
    ...mapActions(["performSetFormError", "performSetLoader", "fetchTokens", "performRetrieveTotalSupply", "zeroTokens"]),
    fetchTokensDict() {
      this.fetchTokens()
    },
    retrieveTotalSupply() {
      this.performRetrieveTotalSupply({
        "token": this.token
      })
    },
    callback: function (ins) {
        ins.update(ins.endVal + 100)
    },
    hasHistory () {
      return window.history?.length > 1
    },

  },
  created() {
    document.title = "Token Supply";
    this.performSetFormError(null);
    this.fetchTokensDict();
    this.zeroTokens();
    this.performSetLoader(false);
  }
};

</script>