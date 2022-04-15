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
        <form @submit.prevent="sendGreetings()" enctype="multipart/form-data">
          <div class="col col-12 col-sm-12 col-md-8 plain-element">
            <div class="card insights-card insights-card-left">
              <div class="row plain-element">

                <div class="col col-12 col-sm-12 col-md-8 plain-element">
                  <div class="card-header">
                    <h6>Send Greetings via Ethereum</h6>
                    <p>Set greetings phrase in ETH Blockchain</p>
                  </div>
                </div>
                <div class="col col-12 col-sm-12 col-md-4 plain-element text-end">
                  <div class="card-header">
                    <button type="submit" class="btn btn-form">
                      Send
                    </button>
                  </div>
                </div>

              </div>
              <p class="w-100"></p>
              <div class="row plain-element">
                <div class="row plain-element text-start">
                  <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                    <h6 class="font-dark-grey">
                      New Greetings:
                    </h6>
                  </div>
                  <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                    <p style="height: 18px; margin: 0px;"></p>
                    <div class="input-field  col col-12 col-sm-12 col-md-12 col-lg-12 col-form">
                        <textarea rows="1" cols="30" name="greetings" v-model="greetings" required></textarea>
                    </div>
                  </div>
                </div>
                <p class="w-100"></p>
                <p class="w-100"></p>
                <div class="table-content">
                  <div v-if="getLoader() == true" class="row">
                      <div class="loader" id="loader"></div>
                  </div>
                  <table v-if="getLoader() == false" class="table-crypto">
                    <tbody>
                    <tr>
                      <td v-if="getGreetings()" class="text-center">
                          {{ getGreetings() }}
                      </td>
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

export default {
  name: 'GreetingsView',

  data() {
    return {
     error: null,
     greetings: null,
    }
  },
  methods: {
    ...mapGetters(["getFormError", "getLoader", "getGreetings"]),
    ...mapActions(["performSetFormError", "performSetLoader", "performSendGreetings" ]),
    sendGreetings() {
      this.performSendGreetings({"greetings": this.greetings})
    },
    hasHistory () {
      return window.history?.length > 1
    },
  },
  created() {
    document.title = "Greetings";
    this.performSetFormError(null);
    this.performSetLoader(false);
  }
};

</script>