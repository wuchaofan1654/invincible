<!--<template> -->
<!--  <div class="app-container">-->
<!--    <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true">-->
<!--      <el-form-item label="项目名称" prop="name">-->
<!--        <el-input-->
<!--          v-model="queryParams.name"-->
<!--          placeholder="请输入项目名称"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="负责人" prop="owner">-->
<!--        <el-input-->
<!--          v-model="queryParams.owner"-->
<!--          placeholder="请输入负责人名"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item label="项目状态" prop="status">-->
<!--        <el-select-->
<!--          v-model="queryParams.status"-->
<!--          placeholder="请选择项目状态"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--        >-->
<!--          <el-option-->
<!--            v-for="dict in statusOptions"-->
<!--            :key="dict.dictValue"-->
<!--            :label="dict.dictLabel"-->
<!--            :value="dict.dictValue"-->
<!--          />-->
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
<!--          v-hasPermission="['permission:role:post']"-->
<!--          type="primary"-->
<!--          plain-->
<!--          icon="el-icon-plus"-->
<!--          size="mini"-->
<!--          @click="dialogVisible = true"-->
<!--        >新增</el-button>-->
<!--      </el-col>-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          v-hasPermission="['permission:role:export:get']"-->
<!--          type="warning"-->
<!--          plain-->
<!--          icon="el-icon-download"-->
<!--          size="mini"-->
<!--          @click="handleExport"-->
<!--        >导出</el-button>-->
<!--      </el-col>-->
<!--      <right-toolbar :show-search.sync="showSearch" @queryTable="getList" />-->
<!--    </el-row>-->

<!--    <el-table v-loading="loading" :data="projects" @selection-change="handleSelectionChange">-->
<!--      <el-table-column type="selection" width="55" align="center" />-->
<!--      <el-table-column label="编号" prop="id" width="80" />-->
<!--      <el-table-column label="名称" prop="name" :show-overflow-tooltip="true">-->
<!--        <template slot-scope="scope">-->
<!--          <el-button type="text" @click="jumpToApiList(scope.row.id)">{{scope.row.name}}</el-button>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="接口数" width="80" :show-overflow-tooltip="true">-->
<!--        <template slot-scope="scope">-->
<!--          {{getApiCounts(scope.row.apis)}}-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="创建人" prop="creator_name" width="100"/>-->
<!--      <el-table-column label="状态" align="center" width="100" sortable>-->
<!--        <template slot-scope="scope">-->
<!--          <el-switch-->
<!--            v-model="scope.row.status"-->
<!--            active-value="1"-->
<!--            inactive-value="0"-->
<!--            disabled-->
<!--            @change="handleStatusChange(scope.row)"-->
<!--          />-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column label="创建时间" align="center" prop="create_datetime">-->
<!--        <template slot-scope="scope">-->
<!--          <span>{{ parseTime(scope.row.create_datetime) }}</span>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        v-if="hasPermission(['permission:role:{id}:put', 'permission:role:{id}:delete'])"-->
<!--        label="操作"-->
<!--        align="center"-->
<!--        class-name="small-padding fixed-width"-->
<!--      >-->
<!--        <template slot-scope="scope">-->
<!--          <el-button-->
<!--            v-hasPermission="['permission:role:{id}:put']"-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-edit"-->
<!--            @click="handleUpdate(scope.row)"-->
<!--          >修改</el-button>-->
<!--          <el-button-->
<!--            v-hasPermission="['permission:role:{id}:put']"-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-circle-check"-->
<!--            @click="handleDataScope(scope.row)"-->
<!--          >数据权限</el-button>-->
<!--          <el-button-->
<!--            v-hasPermission="['permission:role:{id}:delete']"-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-delete"-->
<!--            @click="handleDelete(scope.row)"-->
<!--          >删除</el-button>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--    </el-table>-->
<!--    <el-dialog-->
<!--      title="新建项目"-->
<!--      :center="true"-->
<!--      :visible.sync="dialogVisible"-->
<!--      width="40%">-->
<!--      <el-form ref="form" :model="form" label-width="80px">-->
<!--        <el-form-item label="项目名称">-->
<!--          <el-input v-model="form.name" placeholder="请输入项目名称" />-->
<!--        </el-form-item>-->
<!--        <el-form-item label="项目状态">-->
<!--          <el-radio-group v-model="form.status" placeholder="请输入项目名称">-->
<!--            <el-radio :label="1">正常</el-radio>-->
<!--            <el-radio :label="0">禁用</el-radio>-->
<!--          </el-radio-group>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--      <span slot="footer" class="dialog-footer">-->
<!--        <el-button @click="dialogVisible=false">取 消</el-button>-->
<!--        <el-button type="primary" @click="addProject">确 定</el-button>-->
<!--      </span>-->
<!--    </el-dialog>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--import {getProject} from '@/api/api/project'-->

<!--const defaultQueryParams = {-->
<!--  name: null,-->
<!--  key_yn: null,-->
<!--  status: null,-->
<!--  pageNum: 1,-->
<!--  pageSize: 20-->
<!--};-->

<!--export default {-->
<!--  name: "project",-->
<!--  data() {-->
<!--    return {-->
<!--      projects: [],-->
<!--      showSearch: true,-->
<!--      single: true,-->
<!--      multiple: true,-->
<!--      dialogVisible: false,-->
<!--      form: {name: '', status: 1},-->
<!--      dateRange: null,-->
<!--      statusOptions: [],-->
<!--      queryParams: Object.assign({}, defaultQueryParams),-->
<!--      loading: true,-->
<!--    }-->
<!--  },-->
<!--  created() {-->
<!--    this.getList();-->
<!--  },-->
<!--  methods: {-->
<!--    getList() {-->
<!--      this.loading = true;-->
<!--      getProject(this.queryParams).then(response => {-->
<!--        this.loading = false;-->
<!--        this.projects = response.data.results;-->
<!--        this.total = response.data.count-->
<!--      });-->
<!--    },-->
<!--    /** 搜索按钮点击 */-->
<!--    handleQuery() {-->
<!--      this.getList()-->
<!--    },-->
<!--    pTypeFormat(row, column) {-->
<!--      return row.key_yn === 1 ? '事件': '页面'-->
<!--    },-->
<!--    // 埋点是否核心字典翻译-->
<!--    keyYnFormat(row, column) {-->
<!--      return row.key_yn === 1 ? '是': '否'-->
<!--    },-->
<!--    /** 重置按钮操作 */-->
<!--    resetQuery() {-->
<!--      this.dateRange = [];-->
<!--      this.resetForm("queryForm");-->
<!--      this.handleQuery();-->
<!--    },-->
<!--    handleSizeChange(val) {-->
<!--      this.queryParams.pageNum = 1;-->
<!--      this.queryParams.pageSize = val;-->
<!--      this.getList();-->
<!--    },-->
<!--    handleCurrentChange(val) {-->
<!--      this.queryParams.pageNum = val;-->
<!--      this.getList();-->
<!--    },-->
<!--    handleStatusChange() {-->
<!--      this.$router.push({path:'/apis/addApi'});-->
<!--    },-->
<!--    handleAdd() {-->

<!--    },-->
<!--    handleDelete() {-->

<!--    },-->
<!--    handleUpdate() {},-->
<!--    handleDataScope(){},-->
<!--    handleExport() {},-->
<!--    handleSelectionChange(){},-->
<!--    getApiCounts(apis) {-->
<!--      return apis.length-->
<!--    },-->
<!--    jumpToApiList(apiId) {-->
<!--      this.$router.push({path: '/api/index', query: {id: apiId}})-->
<!--    },-->
<!--    addProject() {-->
<!--      this.dialogVisible = true-->
<!--    }-->

<!--  }-->
<!--}-->
<!--</script>-->
<!--<style>-->
<!--</style>-->


