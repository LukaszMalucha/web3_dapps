<template>
<div class="row plain-element">
  <div class="dashboard" v-cloak>
    <div  class="dashboard-cards">
      <div class="row row-title">

      </div>

      <div class="row row-cards">
        <div class="col col-12 col-sm-12 col-md-2 plain-element"></div>
        <div class="col col-12 col-sm-12 col-md-8 plain-element">
          <div class="card insights-card">
            <div class="row plain-element">

              <div class="col col-12 col-sm-12 col-md-12 plain-element">
                <div class="card-header text-center">
                  <h4>Transaction Successful</h4>
                  <p class="w-100"></p>
                  <span class="hash">{{ txHash }}</span>
                </div>
              </div>
            </div>

            <p class="w-100"></p>
            <div class="row">
              <div>
                <div class="row text-center">
                    <router-link :to="{name: 'home'}" type="submit" class="btn btn-success">Go to Homepage</router-link>
                </div>
              </div>
            </div>

            <p class="w-100"></p>
            <p class="w-100"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>


export default {
  name: "TransactionSuccess",
  components: {

  },
  props: {
    txHash: {
      type: String,
      required: true,
    },
  },
  data() {
    return {

    }
  },

  methods: {

  },
  created() {
    document.title = "Success";
    window.scrollTo(0,0);
  }
}


</script>
