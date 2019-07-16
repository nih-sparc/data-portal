<template>
  <div>
    <p>
      <router-link to="/">
        <el-link type="primary" size="small">&lt; Back to search results</el-link>
      </router-link>
    </p>
    <div v-if="dataset">
      <el-row :gutter="18">
        <el-col :sm="8">
          <el-row type="flex" justify="center">
            <el-image :src="dataset.banner" fit="cover"></el-image>
          </el-row>
        </el-col>
        <el-col :sm="16">
          <h2>{{ dataset.name }}</h2>
          <h4><p>{{ dataset.description }}</p></h4>
          <div class="updated information">
            Updated on {{ updatedDate }}
          </div>
          <div class="information">
            <p>
              Organization: {{ dataset.organizationName }}<br>
              Owner: {{ dataset.ownerName }}<br>
              <div v-if="dataset.contributors.length">
                Contributors: <span v-for="(contributor, i) in dataset.contributors" :key="contributor">{{ contributor }}{{ i === dataset.contributors.length-1 ? "." : ", "}}</span>
              </div>
            </p>
          </div>
          <a v-if="dataset.study" :href="`https://discover.blackfynn.com/datasets/${this.dataset.id}`" target="_blank">
            <el-button type="warning">Get dataset</el-button>
          </a>
          <a v-if="dataset.study" :href="`http://master.osparc.io/study/${dataset.study.uuid}`" target="_blank">
            <el-button type="warning">Run simulation</el-button>
          </a>
        </el-col>
      </el-row>
      <el-row class="markdown">
        <el-col>
          <markdown :markdown="dataset.markdown" />
        </el-col>
      </el-row>
    </div>
    <div v-else>
      <p>Sorry, we couldn't retreive the dataset for the given id.</p>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import Markdown from '../Markdown/Markdown.vue';

export default {
  name: 'dataset-detail',
  props: ['dataset', 'isFetching'],
  computed: {
    updatedDate() {
      return moment.utc(this.dataset.updatedAt).format('MMMM D, YYYY')
    }
  },
  components: {
    Markdown
  }
}
</script>

<style lang="scss" scoped>
.markdown {
  margin-top: 30px;
}
.information {
  color: #525252;
}
.updated {
  font-size: 0.9em;
}
</style>
