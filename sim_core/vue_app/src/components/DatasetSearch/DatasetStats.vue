<template>
  <div class="header-stats-section">
    <div class="header-stats-block">
      <div>
        <template v-if="dataset.fileCount > 0">
          <strong>{{ dataset.fileCount }}</strong> Files
        </template>
        <template v-else>No Files</template>
      </div>
    </div>
    <div class="header-stats-block">
      <div>
        <template v-if="datasetLicense">
          License: 
          <el-tooltip
            class="item"
            effect="dark"
            :content="dataset.license"
            placement="top"
            :visible-arrow="false"
          >
            <a :href="licenseLink" target="_blank">{{ datasetLicense }}</a>
          </el-tooltip>
        </template>

        <template v-else>No License Selected</template>
      </div>
    </div>
  </div>
</template>

<script>
import { getLicenseLink, getLicenseAbbr } from '../../../../../dat_core/vue_app/src/utils/license-util';

export default {
  name: "dataset-stats",
  props: ["dataset"],
  computed: {
    datasetLicense: function () {
      return getLicenseAbbr(this.dataset.license)
    },
    licenseLink: function () {
      return getLicenseLink(this.datasetLicense)
    }
  }
};
</script>

<style lang="scss" scoped>
.header-stats-section {
  display: flex;
}

.header-stats-block {
  align-items: center;
  display: flex;
  font-size: 14px;
  margin-right: 24px;
  &:not(:first-child) {
    border-left: 1px solid #909399;
    padding-left: 24px;
  }
  .svg-icon {
    margin-right: 8px;
  }
  a {
    &:focus {
      color: #1C46BD;
    }
  }
}
</style>
