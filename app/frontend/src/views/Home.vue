<template>


  <div class="dashboard-cards">
    <div class="row row-title">

    </div>
    <div  class="row row-cards">
        <div class="col col-12 col-sm-12 col-md-6 col-lg-3">
          <router-link :to="{name: 'account-balance'}">
            <div class="card card-menu">
              <div class="card-image">
                <img src="https://flask-static-files.s3.eu-west-1.amazonaws.com/static/img/ethereum.jpg">
              </div>
              <div class="card-content">
                <span class="card-title">Ethereum Balance</span>
                <p>Check your account balance</p>
              </div>
            </div>
          </router-link>
        </div>
        <div class="col col-12 col-sm-12 col-md-6 col-lg-3">
          <router-link :to="{name: 'token-supply'}">
            <div class="card card-menu">
              <div class="card-image">
                <img src="https://flask-static-files.s3.eu-west-1.amazonaws.com/static/img/tokens.jpg">
              </div>
              <div class="card-content">
                <span class="card-title">Token Supply</span>
                <p>Check supply of most popular ETH tokens</p>
              </div>
            </div>
          </router-link>
        </div>
        <div class="col col-12 col-sm-12 col-md-6 col-lg-3">
          <router-link :to="{name: 'transactions'}">
            <div class="card card-menu">
              <div class="card-image">
                <img src="https://flask-static-files.s3.eu-west-1.amazonaws.com/static/img/transaction.jpg">
              </div>
              <div class="card-content">
                <span class="card-title">Send Ethereum</span>
                <p>Transfer ETH between wallets</p>
              </div>
            </div>
          </router-link>
        </div>

    </div>
  </div>
</template>





<script>

export default {
  name: 'home',
  components: {
  },
  created() {
    document.title = "Web3.py";
  }
};

</script>