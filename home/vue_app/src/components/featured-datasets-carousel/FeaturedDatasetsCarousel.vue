<template>
  <div class="carousel">
    <el-row>
      <el-col>
        <h2 class="section-header">Featured datasets</h2>
      </el-col>
    </el-row>
    <div v-for="(dataset, index) in featured" v-bind:key="dataset.id">
      <el-row v-if="index === current" type="flex" justify="flex-start">
        <el-col :span="12" class="flush-column">
          <div
            class="featured-dataset-image"
            :style="{ backgroundImage: `url('${dataset.banner}')` }"
          ></div>
        </el-col>
        <el-col :span="12" class="flush-column">
          <div class="featured-dataset-description">
            <div class="content">
              <h2>{{ dataset.name }}</h2>
              <p>{{ dataset.description }}</p>
              <div class="actions">
              <a :href="`/browse/#/datasets/${dataset.id}`">
                <el-button type="primary" class="view-dataset">View dataset</el-button>
              </a>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <el-row>
      <el-col>
        <div class="featured-dataset-carousel-navigation">
          <ul>
            <li
              v-for="(elem, index) in featured"
              v-bind:key="index"
              :class="{active: index === current}"
              @click="current = index"
            ></li>
          </ul>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
const SLIDE_DURATION = 5000;

export default {
  name: "carousel",
  data: function() {
    return {
      featured: null,
      current: null,
      numElements: null
    };
  },
  methods: function() {
    return {
      select: function(index) {
        this.current = index;
      }
    };
  },
  mounted: function() {
    this.$http.get("https://api.blackfynn.io/discover/search/datasets?limit=5&offset=0&organization=SPARC%20Consortium").then(
      function(response) {
        const component = this;

        this.featured = response.data.datasets;
        this.current = 0;
        this.numElements = response.data.datasets.length;

        const scheduleTimeout = () => {
          setTimeout(() => {
            if (component.current === component.numElements - 1) {
              component.current = 0;
            } else {
              component.current = component.current + 1;
            }
            scheduleTimeout();
          }, SLIDE_DURATION);
        };

        scheduleTimeout();
      }.bind(this)
    );
  }
};
</script>

<style lang="scss" scoped>
.featured-dataset-image {
  min-height: 25em;
  background-size: cover;
  background-repeat: no-repeat;
  border-radius: 0.3em 0 0 0.3em;
}

.featured-dataset-carousel-navigation {
  width: 100%;
  text-align: center;
  user-select: none;
  margin: 0.2em 0;

  ul {
    padding: 0;
    margin: 0;
    height: 100%;

    li {
      cursor: pointer;
      padding: 0;
      display: inline-block;
      margin: 0 0.3em;
      min-width: 2em;
      border-bottom: 5px solid #909399;

      &.active,
      &:hover {
        border-bottom: 5px solid #24245b;
      }
    }
  }
}

.featured-dataset-description {
  height: 100%;
  background: #24245b;
  display: flex;
  justify-content: center;
  flex-direction: column;
  border-radius: 0 0.3em 0.3em 0;

  .content {
    padding: 3em 1.5em;
    color: white;

    h2 {
      font-size: 1.5em;
      word-break: break-all;
    }

    p {
    }

    .actions {
      margin-top: 2em;

      .view-dataset {
        background: #8300bf;
        text-transform: uppercase;
        border: 0;
      }
    }
  }
}
</style>
