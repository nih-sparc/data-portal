<template>
  <div v-if="dataset" class="dataset-landing-page">
    <div class="dataset-breadcrumb-gradient">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <div class="breadcrumb">
            <span class="segment">
              <a href="#">Data Core</a>
            </span>
            <span class="divider">/</span>
            <span class="segment">
              <a href="#">{{ dataset.name }}</a>
            </span>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="dataset-info-section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <el-row :gutter="20">
            <el-col :span="14">
              <div class="dataset-info">
                <h2>{{ dataset.name }}</h2>
                <p class="abstract">{{ dataset.description }}</p>
                <p class="updated-on">Updated on {{ dataset.updatedAt }}</p>

                <div class="authors">
                  <span class="name">{{ dataset.contributors.join(",") }}</span>
                </div>
                <div class="actions">
                  <el-button type="primary" class="get-dataset-button">Get Dataset</el-button>
                  <el-button type="secondary" class="view-simulations-button">View Simulations</el-button>
                </div>
                <div class="attributes">
                  <div class="attribute">
                    <img :src="filesIcon" />
                    <span class="label">
                      <strong>{{ dataset.fileCount }}</strong> files
                    </span>
                  </div>
                  <div class="divider">
                    <img :src="divider" />
                  </div>
                  <div class="attribute">
                    <img :src="fileSizeIcon" />
                    <span class="label">
                      <strong>{{ dataset.size / 1000 }}</strong> GB
                    </span>
                  </div>
                  <div class="divider">
                    <img :src="divider" />
                  </div>
                  <div class="attribute">
                    <img :src="licenseIcon" />
                    <span class="label">{{ dataset.license }}</span>
                  </div>
                </div>
              </div>
            </el-col>
            <el-col :span="10">
              <div class="dataset-image">
                <img :src="dataset.banner" />
              </div>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>
    <div class="about-this-dataset-section">
      <el-row type="flex" justify="center">
        <el-col :xs="22" :sm="22" :md="22" :lg="18" :xl="16">
          <h3 class="about-this-dataset-header">About this dataset</h3>
          <div class="updated-date">
            <p>{{ dataset.updatedAt }}</p>
            <p class="label">Last Updated</p>
          </div>
          <div class="cite-dataset">
            <h4>Cite this dataset</h4>
            <textarea v-model="citation" class="citation" readonly></textarea>
            <ul>
              <li>Formatted as:</li>
              <li>
                <a class="active" href>APA</a>
              </li>
              <li>
                <a href>Chicago</a>
              </li>
              <li>
                <a href>IEEE</a>
              </li>
              <li>
                <a href="https://datacite.org">More on Datacite.org</a>
              </li>
            </ul>
          </div>
          <div class="tags">
            <h4>Tags</h4>
            <ul>
              <li :key="tag.tag" v-for="tag in dataset.tags">{{ tag.tag }}</li>
            </ul>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import datasetAbstractImage from "../../assets/images/dataset-abstract-image.png";
import authorDivider from "../../assets/images/author-divider.svg";

import filesIcon from "../../assets/images/files-icon.svg";
import fileSizeIcon from "../../assets/images/file-size-icon.svg";
import licenseIcon from "../../assets/images/license-icon.svg";
import divider from "../../assets/images/divider.svg";

const citation =
  "Bartek Rajwa and Kevin Jackson. “Powley 2018 VNS-Gastric MRI Study.” https://doi.org/10.7939/r3m8ac11";

export default {
  name: "dataset-page",
  components: {},
  data: function() {
    return {
      loading: false,
      loaded: false,
      dataset: null,
      authorDivider,
      filesIcon,
      fileSizeIcon,
      licenseIcon,
      divider,
      citation
    };
  },
  mounted: function() {
    this.loading = true;
    this.$http.get(`/api/dataset/${this.$route.params.datasetId}`).then(
      function(response) {
        this.dataset = response.data;
        this.loaded = true;
        this.loading = false;
      }.bind(this)
    );
  }
};
</script>

<style lang="scss" scoped>
.get-dataset-button {
  background: #8300bf;
  text-transform: uppercase;
  border: 0px;
}

.view-simulations-button {
  background: #f9f2fc;
  border: 1px solid #8300bf;
  color: #8300bf;
  text-transform: uppercase;
}
.dataset-breadcrumb-gradient {
  padding: 1.5em 0;
  color: #f0f2f5;
  background-image: linear-gradient(90deg, #0026ff 0%, #00ffb9 100%);
}
h3.about-this-dataset-header {
  margin-bottom: 1em;
}
.attributes {
  .divider {
    display: inline;
    padding: 0 1em;
    max-height: 12pt;
    vertical-align: middle;
  }
  .attribute {
    display: inline;
    max-height: 15px;
    img {
      padding-right: 0.5em;
      max-height: 15px;
    }

    .label {
      vertical-align: unset;
      font-size: 12pt;
      line-height: 15pt;
    }
  }
}
.cite-dataset {
  .citation {
    font-size: 12pt;
    height: 3em;
    width: 30em;
    padding: 1em;
    margin-bottom: 0.5em;
    border-radius: 5px;
    color: #24245b;
  }
  ul {
    padding: 0;
    margin: 0;

    li {
      display: inline;
      font-size: 10pt;
      list-style-type: none;
      color: #c0c4cc;

      a {
        padding: 0 1em;
        text-decoration: underline;
        color: #c0c4cc;
        &.active {
          text-decoration: none;
          color: #fff;
        }
      }
    }
  }
}
.breadcrumb {
  .segment {
    a {
      text-decoration: none;
      color: white;
    }
  }

  .divider {
    padding: 0 0.5em;
  }
}
.tags {
  ul {
    padding: 0;
    margin: 0;
    li {
      display: inline;
      list-style-type: none;
      background: #f2f6fc;
      color: #24245b;
      padding: 0.5em 1em;
      border-radius: 5px;
      margin-right: 0.5em;
    }
  }
}
.dataset-landing-page {
  padding-top: 6em;
  background: #fff;
}

.dataset-info-section {
  padding: 2em 0em;
  color: #303133;

  .abstract {
    line-height: 18pt;
    font-size: 12pt;
    padding: 2em 0;
  }

  .updated-on {
    font-size: 10pt;
    padding: 0;
    margin: 0;
  }

  .authors {
    font-size: 10pt;

    .divider {
      padding: 0 0.5em;

      img {
        padding-top: 0.25em;
      }
    }

    p {
      padding: 0;
      margin: 0;
    }
  }
}

.dataset-info {
  overflow: hidden;

  h1 {
    margin-bottom: 1em;
  }
}

.dataset-image {
  overflow: hidden;
}

.actions {
  padding: 2em 0em;
}

.updated-date {
  font-size: 10pt;
  line-height: 12pt;
  margin: 0;

  p {
    margin: 0;
    padding: 0;
    font-size: 10pt;
  }

  p.label {
    text-transform: uppercase;
  }
}

.about-this-dataset-section {
  padding: 3em 0em;
  overflow: hidden;
  background: #24245b;
  color: white;
}
</style>