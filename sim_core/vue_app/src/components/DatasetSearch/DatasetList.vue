<template>
  <el-row v-if="datasets.length" :gutter="20" type="flex" class="cards">
    <el-col :xs="24" :sm="12" :md="8" :lg="6" v-for="dataset in datasets" :key="dataset.id">
      <div class="card">
        <router-link :to="{ name: 'dataset-detail', params: { id: dataset.id } }">
          <div class="thumbnail-container">
            <el-row type="flex" justify="center">
              <el-image :src="dataset.banner" fit="scale-down"></el-image>
            </el-row>
          </div>
        </router-link>
        <div class="card-bottom">
          <div>
            <h3 class="title">{{ dataset.name }}</h3>
            <p class="description">{{ dataset.description }}</p>
          </div>
          <div class="link">
            <router-link :to="{ name: 'dataset-detail', params: { id: dataset.id } }">Explore</router-link>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
  <el-row v-else-if="!isFetching" type="flex" justify="center">
    <p class="no-results">No data was found for the given search terms.</p>
  </el-row>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'dataset-list',
  computed: mapState({
    datasets: state => Object.values(state.entities.datasets || {}),
    isFetching: state => state.simcoreSearch.simcoreSearchForm.isFetching
  })
}
</script>

<style lang="scss" scoped>
.thumbnail-container {
  height: 15em;
  display: flex;
  flex-direction: column;
  justify-content: center;

  > .el-row {
    height: 100%;
  }

  @media screen and (max-width: 768px) {
    height: auto;
  }
}

.cards {
  flex-wrap: wrap;

  .card {
    display: flex;
    flex-direction: column;
    width: 100%;
    box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
    border: 1px solid #EBEEF5;
    background-color: #FFF;
    border-radius: 4px;
    padding: 18px;
    margin-top: 20px;

    .link {
      a {
        text-transform: uppercase;
        text-decoration: none;
        color: #f4942b;
      }
    }
  }
  
  .card-bottom {
    margin: 1em 0;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  > .el-col {
    display: flex;
  }
}

.no-results {
  color: #525252;
}
</style>
