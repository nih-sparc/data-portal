<template>
  <div class="sparc-dataset-filter">
    <div>
      <el-autocomplete
        class="input-with-select"
        size="medium"
        v-model="input"
        :fetch-suggestions="querySearch"
        :placeholder="placeHolder"
        :trigger-on-focus="false"
        @select="handleSelect">
        <el-select v-model="select" slot="prepend" placeholder="Select">
          <el-option label="Content" value="content"></el-option>
          <el-option label="Authors" value="authors"></el-option>
        </el-select>  
      </el-autocomplete>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sparc-dataset-filter',

  props: {
    authors: Array,
    tags: Array,
  },

  data() {
    return {
      input: '',
      select: 'content'
    }
  },
  computed: {
        placeHolder() {
          if (this.select == 'content') {
            return 'Find dataset...'  
          } else if (this.select == 'authors') {
            return 'Find dataset by author...' 
          }
        }
  },
  watch: {
    input: function(newValue, oldValue) {
      this.$emit('filterChanged', { type: this.select, value: newValue})
    },
    select: function(newValue, oldValue) {
      this.$emit('filterChanged', { type: newValue, value: this.input})
    }
  },
  methods: {
    querySearch(queryString, cb) {
        var terms
        if (this.select == 'content') {
          terms = this.tags;
        } else {
          terms = this.authors;
        }
        var results = queryString ? terms.filter(this.createFilter(queryString)) : terms;
        // call callback function to return suggestions
        cb(results);
      },
      createFilter(queryString) {
        return (author) => {
          return (author.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(value) {
      }
  }
}
</script>

<style lang="scss" scoped>
  @import '../../../../../static/css/_variables.scss';

  .sparc-dataset-filter {
    margin-bottom: 8px;
  }
  
  .el-autocomplete {
    display: flex;
  }

  .el-autocomplete .el-input {
    width: 110px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
