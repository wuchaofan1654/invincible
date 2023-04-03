<template>
  <div class="app-container">
    <el-table v-loading="loading" :data="recordings">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="编号" prop="id" />
      <el-table-column label="host" prop="host" :show-overflow-tooltip="true" />
      <el-table-column label="path" prop="path" :show-overflow-tooltip="true" />
      <el-table-column label="唯一标识" prop="unique_name" :show-overflow-tooltip="true" />
      <el-table-column label="创建人" prop="creator_name" />
      <el-table-column label="创建时间" align="center" prop="create_datetime" />
    </el-table>
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />
  </div>
</template>
<script>
import { getRecording } from "@/api/custom/recording/recording";

const defaultQueryParams = {
  status: undefined,
  start: "",
  end: "",
  pageNum: 1,
  pageSize: 20
};

export default {
  name: "Index",
  components: {},
  data() {
    return {
      total: 0,
      recordings: [],
      single: true,
      // 非多个禁用
      multiple: true,
      dateRange: null,
      statusOptions: [],
      queryParams: Object.assign({}, defaultQueryParams),
      loading: true,
    };
  },
  created() {
    this.getList();
  },
  methods: {
    getList() {
      this.loading = true;
      getRecording(this.queryParams).then(response => {
        this.loading = false;
        this.recordings = response.data.results;
        this.total = response.data.count;
      });
    }
  }
};
</script>
<style>
</style>
