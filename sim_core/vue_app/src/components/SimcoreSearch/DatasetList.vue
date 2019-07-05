<template>
  <el-table :data="datasets">
    <el-table-column prop="name" label="Name"></el-table-column>
    <el-table-column prop="organizationName" label="Organization"></el-table-column>
    <el-table-column prop="ownerName" label="Owner"></el-table-column>
    <el-table-column prop="updatedAt" label="Last modification"></el-table-column>
    <el-table-column label="Actions" fixed>
      <template slot-scope="scope">
        <el-button type="text" size="small" @click="e => onDetailClick(e, scope.row)">Detail</el-button>
        <el-button type="text" size="small" @click="e => onOpenClick(e, scope.row)">Open in oSPARC</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'dataset-list',
  computed: mapState({
    datasets: state => state.entities.datasets
  }),
  methods: {
    onDetailClick(e, rowData) {
      const { id } = rowData;
      console.log(id);
    },
    onOpenClick(e, rowData) {
      const { id } = rowData;
      console.log(id);
    }
  }
}
</script>
