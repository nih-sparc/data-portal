<template>
  <div class="pagination">
    <el-pagination
      :page-size="pageSize"
      :pager-count="pageCount"
      layout="prev, pager, next"
      :total="totalCount"
      @current-change="selectPage"
    ></el-pagination>
  </div>
</template>

<script>
export default {
  name: "pagination",
  props: {
    selected: {
      type: "Number",
      default: 1
    },
    pageSize: {
      type: "Number",
      default: 20
    },
    totalCount: {
      type: "Number"
    }
  },
  computed() {
    return {
      pageCount: function() {
        return Math.ceil(this.totalCount / this.pageSize);
      }
    };
  },
  methods: {
    selectPage: page => {
      $this.emit("selectPage", page);
    }
  }
};
</script>

<style lang="scss">
.pagination {
  padding-top: 1em;
  text-align: center;

  button.btn-prev {
    background: none;
  }

  button.btn-next {
    background: none;
  }

  li.more,
  li.number {
    background: none;
  }
}
</style>
