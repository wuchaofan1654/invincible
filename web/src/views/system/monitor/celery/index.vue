<!--
@author: xuchi
@description: 应用列表页面
-->
<template>
  <div>
    <el-row>
      <el-col :span="8">
        <interval-index />
      </el-col>
      <el-col :span="8">
        <crontabe-index />
      </el-col>
    </el-row>
    <periodic-task />
  </div>
</template>
<script>
import PeriodicTask from "./periodic-task/periodic-index.vue";
import IntervalIndex from "./interval-task/interval-index.vue";
import CrontabeIndex from "./crontab-task/crontab-index.vue";
export default {
  components: { IntervalIndex, PeriodicTask, CrontabeIndex },
  props: {},
  data() {
    return {};
  },
  mounted() {
  },
  created() {
  },
  methods: {}
};
</script>

<style scoped>
  .el-table th {
    display: table-cell !important;
  }
</style>
