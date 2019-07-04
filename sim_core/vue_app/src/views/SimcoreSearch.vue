<template>
  <div class="simcore-search">
    <el-row type="flex" justify="center">
      <el-col :span="18">
        <el-row>
          <el-col>
            <h2>Search and run simulations in the oSPARC platform</h2>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-form :inline="true" :model="simSearch" class="search-form" @submit.prevent.native="onSubmit">
              <el-form-item>
                <el-input v-model="simSearch.search" placeholder="Type your search"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onSubmit">Search</el-button>
              </el-form-item>
            </el-form>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      simSearch: {
        search: ''
      }
    }
  },
  methods: {
    onSubmit(e) {
      const {
        search
      } = this.simSearch;
      // Fetch discover
      fetch('/api/sim/datasets')
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          console.error("Couldn't fetch the data");
        }
      })
      .then(json => {
        this.renderDatasets(json);
      })
      .catch(error => {
        console.error("The request failed due to a network error");
      });
    },

    renderDatasets(datasets) {
      console.log(datasets);
    }
  }
}
</script>

<style lang="scss" scoped>
.simcore-search {
  padding-top: 7em;
}
form.search-form {
  margin: 2em 0;
}
</style>
