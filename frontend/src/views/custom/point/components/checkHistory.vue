<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-table v-loading="loading" :data="historyList">-->
<!--      <el-table-column label="埋点名称" align="center" prop="en_name" width="300" :show-overflow-tooltip="true"/>-->
<!--      <el-table-column label="检查结果" align="center" prop="point_type" sortable >-->
<!--        <template v-slot="scope">-->
<!--          <el-tag :type='scope.row.errors.length > 0 ? "danger": scope.row.warnings.length > 0 ? "warning" : "success"'>-->
<!--            {{scope.row.errors.length > 0 ? "失败": scope.row.warnings.length > 0 ? "告警" : "通过"}}-->
<!--          </el-tag>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="错误信息" align="center" prop="errors" sortable >-->
<!--        <template v-slot="scope">-->
<!--          <el-tag v-for="error in scope.row.errors" type="danger" size="mini">-->
<!--            {{error}}-->
<!--          </el-tag>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="警告信息" align="center" prop="warnings" sortable >-->
<!--        <template v-slot="scope">-->
<!--          <el-tag v-for="warning in scope.row.warnings" type="warning" size="mini">-->
<!--            {{warning}}-->
<!--          </el-tag>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="创建时间" align="center" prop="create_datetime" sortable width="180">-->
<!--        <template v-slot="scope">-->
<!--          <span>{{ parseTime(scope.row.create_datetime) }}</span>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--    </el-table>-->
<!--    <pagination-->
<!--      v-show="total>0"-->
<!--      :total="total"-->
<!--      :page.sync="queryParams.pageNum"-->
<!--      :limit.sync="queryParams.pageSize"-->
<!--      @pagination="getList"-->
<!--    />-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { listIntercept } from "@/api/custom/point/intercept";-->


<!--export default {-->
<!--  name: "CheckHistory",-->
<!--  props: { unique_name: {type: String, default: ""} },-->
<!--  data() {-->
<!--    return {-->
<!--      loading: false,-->
<!--      total: 0,-->
<!--      historyList: [],-->
<!--      queryParams: {-->
<!--        pageNum: 1,-->
<!--        pageSize: 10,-->
<!--      },-->
<!--    };-->
<!--  },-->
<!--  watch:{-->
<!--    'unique_name'(newVal, oldVal){-->
<!--      this.queryParams.unique_name = newVal-->
<!--      this.getList()-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    /** 查询埋点列表 */-->
<!--    getList() {-->
<!--      this.loading = true;-->
<!--      listIntercept(this.addDateRange(this.queryParams)).then(response => {-->
<!--          this.historyList = response.data.results;-->
<!--          this.total = response.data.count;-->
<!--          this.loading = false;-->
<!--        }-->
<!--      );-->
<!--    },-->
<!--  }-->
<!--};-->
<!--</script>-->
