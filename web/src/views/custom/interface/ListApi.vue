<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true">-->
<!--      <el-form-item label="接口合集" prop="suite">-->
<!--        <el-input-->
<!--          v-model="queryParams.name"-->
<!--          placeholder="请输入接口名称"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="接口名称" prop="name">-->
<!--        <el-input-->
<!--          v-model="queryParams.name"-->
<!--          placeholder="请输入接口名称"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="负责人" prop="creator">-->
<!--        <el-input-->
<!--          v-model="queryParams.creator"-->
<!--          placeholder="请输入负责人名"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="接口状态" prop="status">-->
<!--        <el-select-->
<!--          v-model="queryParams.status"-->
<!--          placeholder="请选择接口状态"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px">-->
<!--          <el-option-->
<!--            v-for="dict in statusOptions"-->
<!--            :key="dict.dictValue"-->
<!--            :label="dict.dictLabel"-->
<!--            :value="dict.dictValue"/>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="创建时间">-->
<!--        <el-date-picker-->
<!--          v-model="dateRange"-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          value-format="yyyy-MM-dd"-->
<!--          type="daterange"-->
<!--          range-separator="-"-->
<!--          start-placeholder="开始日期"-->
<!--          end-placeholder="结束日期"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>-->
<!--        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->

<!--    <el-row :gutter="10" class="mb8">-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          v-hasPermission="['permission:api:post']"-->
<!--          type="primary"-->
<!--          plain-->
<!--          icon="el-icon-plus"-->
<!--          size="mini"-->
<!--          @click="jumperToDetail()"-->
<!--        >新增</el-button>-->
<!--      </el-col>-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          v-hasPermission="['permission:api:post']"-->
<!--          type="primary"-->
<!--          plain-->
<!--          icon="el-icon-plus"-->
<!--          size="mini"-->
<!--          @click="importApi"-->
<!--        >导入</el-button>-->
<!--      </el-col>-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          v-hasPermission="['permission:api:export:get']"-->
<!--          type="warning"-->
<!--          plain-->
<!--          icon="el-icon-download"-->
<!--          size="mini"-->
<!--          @click="handleExport"-->
<!--        >导出</el-button>-->
<!--      </el-col>-->
<!--      <right-toolbar :show-search.sync="showSearch" @queryTable="getList" />-->
<!--    </el-row>-->
<!--    <el-table :data="apiList" :row-class-name="tableRowClassName">-->
<!--      <el-table-column type="expand">-->
<!--        <template slot-scope="scope">-->
<!--          <api :api-info="scope.row"></api>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="编号" type="index" width="50"/>-->
<!--      <el-table-column label="请求方式" :formatter="formatMethod" width="80">-->
<!--        <template slot-scope="scope">-->
<!--          <div v-html="formatMethod(scope.row.method)"></div>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="接口名称" prop="name" :show-overflow-tooltip="true" min-width="80"/>-->
<!--      <el-table-column label="接口url" prop="url" :show-overflow-tooltip="true"/>-->
<!--      <el-table-column label="操作" :show-overflow-tooltip="true" width="120px">-->
<!--        <template slot-scope="scope">-->
<!--          <el-button type="text">删除</el-button>-->
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

<!--import Api from "@/views/custom/interface/cards/Api.vue";-->

<!--export default {-->
<!--  name: "ListApi",-->
<!--  components: {Api},-->
<!--  data() {-->
<!--    return {-->
<!--      total: 100,-->
<!--      showSearch: true,-->
<!--      queryParams: {},-->
<!--      apiList: [-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "接口1",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--        {-->
<!--          id: 2,-->
<!--          name: "接口2",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--        {-->
<!--          id: 3,-->
<!--          name: "接口3",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--        {-->
<!--          id: 4,-->
<!--          name: "接口4",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--        {-->
<!--          id: 5,-->
<!--          name: "接口5",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--        {-->
<!--          id: 6,-->
<!--          name: "接口6",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--        {-->
<!--          id: 7,-->
<!--          name: "接口7",-->
<!--          url: 'http://www.api.soyoung.com/v8/diary/detail',-->
<!--          method: 'GET',-->
<!--          basic: {},-->
<!--          params: [],-->
<!--          validators: [],-->
<!--          extractors: []-->
<!--        },-->
<!--      ],-->
<!--      apiSuites: [-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--        {-->
<!--          id: 1,-->
<!--          name: "评价核心接口集",-->
<!--        },-->
<!--      ]-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    tableRowClassName({row, rowIndex}) {-->
<!--      if (rowIndex % 2 === 0) {-->
<!--        return 'singular-row';-->
<!--      } else if (rowIndex % 2 === 1) {-->
<!--        return 'complex-row';-->
<!--      }-->
<!--      return '';-->
<!--    },-->
<!--    formatMethod(method) {-->
<!--      return '<el-tag type="success">' + method + '</el-tag>'-->
<!--    },-->
<!--    handleQuery() {-->

<!--    },-->
<!--    resetQuery() {-->

<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style lang="scss">-->
<!--.el-table__expanded-cell[class*=cell] {-->
<!--  padding: 5px 10px;-->
<!--}-->

<!--.el-table .singular-row {-->
<!--  background: #f0f9eb;-->
<!--}-->

<!--.el-table .complex-row {-->
<!--  background: #E4E7ED;-->
<!--}-->
<!--</style>-->
