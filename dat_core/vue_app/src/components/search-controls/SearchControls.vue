<template>
  <div class="controls">
    <el-row class="control-row" justify="center" type="flex" gutter="5">
      <el-col :xs="8" :sm="6">
        <div class="control">
          <el-select
            v-model="selectedType"
            size="large"
            style="width: 100%; height: 100%; margin: 0; padding: 0; border-radius: 0"
            placeholder="Select"
          >
            <el-option v-for="type in types" :key="type.key" :value="type.key" :label="type.label" />
          </el-select>
        </div>
      </el-col>
      <el-col :xs="16" :sm="18">
        <div class="control">
          <el-input placeholder="Start typing..." suffix-icon="el-icon-search" v-model="terms"></el-input>
        </div>
      </el-col>
      <el-col :xs="3" :sm="5">
        <div class="search-button">
          <el-button type="primary" class="view-search-results" @click.native="submit">View Results</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedType: "datasets",
      loading: false,
      terms: null,
      types: [
        {
          label: "Datasets",
          key: "datasets"
        },
        {
          label: "Files",
          key: "files"
        }
      ]
    };
  },
  methods: {
    submit() {
      this.$emit('query', this.selectedType, this.terms);
    }
  }
};
</script>

<style lang="scss" scoped>
.controls {
  padding-top: 1em;
  min-height: 4em;

  .control-row {
    align-items: baseline;
  }

  .control {
    display: inline-block;
    height: 100%;
    width: 100%;
    font-size: 2em;

    .search-type-selector {
      padding: 0.5em;
      border: 0;
      color: #8300bf;
      border-radius: 0;
      background: none;
      -webkit-appearance: none;
      width: 100%;
      height: 100%;

      > input {
        border-radius: 0 !important;
        border: 0 !important;
        background: none;
      }
    }

    .search-input {
      background: none;
      border: 0;
      padding: 0.5em;
      color: #8300bf;
      -webkit-appearance: none;
      width: 100%;
      height: 100%;

      > input {
        border-radius: 0 !important;
        border: 0 !important;
        background: none;
      }

      ::placeholder {
        color: #8300bf;
        opacity: 1;
      }
    }
  }
}

.search-button {

  .view-search-results {
    background: #24245b;
    text: #fff;
    border: 0;
  }
}
</style>
