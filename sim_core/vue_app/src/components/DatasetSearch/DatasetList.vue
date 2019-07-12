<template>
  <el-table :data="datasets">
    <el-table-column prop="name" label="Name"></el-table-column>
    <el-table-column prop="organizationName" label="Organization"></el-table-column>
    <el-table-column prop="ownerName" label="Owner"></el-table-column>
    <el-table-column prop="updatedAt" label="Last modification"></el-table-column>
    <el-table-column label="Actions" fixed="right">
      <template slot-scope="scope">
        <router-link :to="{ name: 'dataset-detail', params: { id: scope.row.id } }">
          <el-button size="small">Detail</el-button>
        </router-link>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'dataset-list',
  computed: mapState({
    datasets: state => Object.values(state.entities.datasets || {})
  })
}
</script>
