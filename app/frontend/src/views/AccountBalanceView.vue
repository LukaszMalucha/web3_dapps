<template>


  <div class="dashboard-cards">
    <div class="row row-title">

    </div>
    <div class="row row-cards">
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
            <form @submit.prevent="checkBalance()" enctype="multipart/form-data">
              <div class="row plain-element text-start">

                <div class="input-field  col col-12 col-sm-12 col-md-2 col-lg-3 col-form">
                  <h6 class="font-dark-grey">
                    Wallet Address:
                  </h6>

                </div>
                <div class="input-field  col col-12 col-sm-12 col-md-10 col-lg-9 col-form">
                  <textarea rows="1" cols="30" name="wallet_id" v-model="wallet_id"></textarea>
                </div>

              </div>


            </form>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>





<script>

export default {
  name: 'AccountBalance',
  components: {
  },
  created() {
    document.title = "Account Balance";
  }
};

</script>