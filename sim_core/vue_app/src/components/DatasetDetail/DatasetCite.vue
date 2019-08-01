<template>
  <el-row type="flex" justify="center">
    <el-col :span="24">
      <h4>Cite this dataset</h4>
      <div
        v-loading="citationLoading"
        class="info-citation"
        aria-live="polite"
        v-html="$sanitize(citationText, ['i'])"
      />
      <div class="info-citation-links mb-24">
        Formatted as:
        <button
          title="Format citation apa"
          :class="{active: activeCitation === 'apa'}"
          @click="handleCitationChanged('apa')"
        >APA</button>
        <button
          title="Format citation chicago"
          :class="{active: activeCitation === 'chicago-note-bibliography'}"
          @click="handleCitationChanged('chicago-note-bibliography')"
        >Chicago</button>
        <button
          title="Format citation ieee"
          :class="{active: activeCitation === 'ieee'}"
          @click="handleCitationChanged('ieee')"
        >IEEE</button>
        <a
          :href="`https://crosscite.org/?doi=${dataset.doi}`"
          target="_blank"
        >More on Crosscite.org</a>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: "dataset-cite",
  data () {
    return {
      citationText: '',
      activeCitation: '',
      citationLoading: false
    }
  },
  props: ['dataset'],
  created() {
    this.handleCitationChanged('apa');
  },
  methods: {
    /**
     * gets bibiolography based on citation type for current DOI
     * @param {String} citationType
     */
    handleCitationChanged: function (citationType) {
      if (citationType === this.activeCitation) {
        return;
      }
      this.citationLoading = true;
      this.activeCitation = citationType;
      // find all citation types at https://github.com/citation-style-language/style
      const doi = this.dataset.doi;
      const url = `https://citation.crosscite.org/format?doi=${doi}&style=${citationType}&lang=en-US`;
      return fetch(url)
        .then(response => {
          return response.text();
        })
        .then(text => {
          this.citationText = text;
        })
        .finally(() => {
          this.citationLoading = false;
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.info-citation {
  border-radius: 4px;
  background-color: #f2f6fc;
  padding: 16px;
  color: black;
  font-size: 14px;
  line-height: 24px;
  margin-bottom: 8px;
}

.info-citation-links {
  font-size: 14px;
  line-height: 16px;
  color: white;
  button, a {
    background: none;
    border: none;
    color: white;
    line-height: 16px;
    text-decoration: underline;
    font-size: 14px;
    cursor: pointer;
    padding: 0;
    margin-left: 11px;

    &.active {
      text-decoration: none;
      color: #fff;
    }
  }
}
</style>
