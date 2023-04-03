<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true" label-width="68px">-->
<!--      <el-form-item label="名称" prop="title">-->
<!--        <el-input-->
<!--          v-model="queryParams.title"-->
<!--          placeholder="请输入埋点集名称"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="状态" prop="status">-->
<!--        <el-select v-model="queryParams.status" placeholder="埋点集状态" clearable size="small">-->
<!--          <el-option-->
<!--            v-for="dict in pointSuiteStatusOptions"-->
<!--            :key="dict.dictValue"-->
<!--            :label="dict.dictLabel"-->
<!--            :value="dict.dictValue"/>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>-->
<!--        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--    <el-row :gutter="10" class="mb8">-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          type="primary"-->
<!--          plain-->
<!--          icon="el-icon-plus"-->
<!--          size="mini"-->
<!--          @click="handleAdd"-->
<!--        >新建埋点-->
<!--        </el-button>-->
<!--      </el-col>-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          type="success"-->
<!--          plain-->
<!--          icon="el-icon-edit"-->
<!--          size="mini"-->
<!--          @click="handleUpdate"-->
<!--        >修改-->
<!--        </el-button>-->
<!--      </el-col>-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          type="danger"-->
<!--          plain-->
<!--          icon="el-icon-delete"-->
<!--          size="mini"-->
<!--          @click="handleDelete"-->
<!--        >删除-->
<!--        </el-button>-->
<!--      </el-col>-->
<!--      <el-col :span="1.5">-->
<!--        <el-button-->
<!--          type="warning"-->
<!--          plain-->
<!--          icon="el-icon-download"-->
<!--          size="mini"-->
<!--          @click="handleExport"-->
<!--        >导出-->
<!--        </el-button>-->
<!--      </el-col>-->
<!--      <right-toolbar :show-search.sync="showSearch" @queryTable="getList"/>-->
<!--    </el-row>-->
<!--    <el-table v-loading="loading" :data="suiteList">-->
<!--      <el-table-column type="selection" width="55" align="center"/>-->
<!--      <el-table-column label="名称" align="center" prop="suite_name" sortable :show-overflow-tooltip="true"/>-->
<!--      <el-table-column label="状态" align="center" prop="status" sortable width="120" :formatter="statusFormat" />-->
<!--      <el-table-column label="创建时间" align="center" prop="create_datetime" sortable width="180">-->
<!--        <template v-slot="scope">-->
<!--          <span>{{ parseTime(scope.row.create_datetime) }}</span>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        label="操作"-->
<!--        align="center"-->
<!--        class-name="small-padding fixed-width">-->
<!--        <template v-slot="scope">-->
<!--          <el-button-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-edit"-->
<!--            @click="handleUpdate(scope.row)"-->
<!--          >修改-->
<!--          </el-button>-->
<!--          <el-button-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-delete"-->
<!--            @click="handleDelete(scope.row)"-->
<!--          >删除-->
<!--          </el-button>-->
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
<!--    <el-dialog-->
<!--      title="新建/修改埋点集合"-->
<!--      :visible.sync="dialogVisible"-->
<!--      width="60%">-->
<!--      <add-update-suite></add-update-suite>-->
<!--      <span slot="footer" class="dialog-footer">-->
<!--        <el-button @click="dialogVisible = false">取 消</el-button>-->
<!--        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>-->
<!--      </span>-->
<!--    </el-dialog>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { getSuite, listSuite } from "@/api/custom/point/suite";-->
<!--import {listPoint} from "@/api/custom/point/point";-->
<!--import addUpdateSuite from "@/views/custom/point/components/addUpdateSuite.vue";-->


<!--export default {-->
<!--  name: "Suite",-->
<!--  components: { addUpdateSuite },-->
<!--  data() {-->
<!--    const generateData = _ => {-->
<!--        const data = [];-->
<!--        for (let i = 1; i <= 15; i++) {-->
<!--          data.push({-->
<!--            value: i,-->
<!--            desc: `备选项 ${ i }`,-->
<!--            disabled: i % 4 === 0-->
<!--          });-->
<!--        }-->
<!--        return data;-->
<!--      };-->
<!--    return {-->
<!--      loading: true,-->
<!--      showSearch: true,-->
<!--      total: 0,-->
<!--      suiteList: [],-->
<!--      pointSuiteStatusOptions: [],-->
<!--      form: {},-->
<!--      points: generateData(),-->
<!--      dialogVisible: false,-->
<!--      queryParams: {-->
<!--        pageNum: 1,-->
<!--        pageSize: 10,-->
<!--        suite_name: undefined,-->
<!--      },-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getList();-->
<!--    this.getPointList();-->
<!--    this.getDicts("point_suite_status_options").then(response => {-->
<!--      this.pointSuiteStatusOptions = response.data;-->
<!--    });-->
<!--  },-->

<!--  methods: {-->
<!--    /** 查询埋点列表 */-->
<!--    getList() {-->
<!--      this.loading = true;-->
<!--      listSuite(this.addDateRange(this.queryParams)).then(response => {-->
<!--          this.suiteList = response.data.results;-->
<!--          this.total = response.data.count;-->
<!--          this.loading = false;-->
<!--        }-->
<!--      );-->
<!--    },-->
<!--    getPointList() {-->
<!--      listPoint().then(response => {-->
<!--          this.dataList = response.data.results;-->
<!--          console.log(this.dataList)-->
<!--        }-->
<!--      );-->
<!--    },-->
<!--    statusFormat(row) {-->
<!--      return this.selectDictLabel(this.pointSuiteStatusOptions, row.status);-->
<!--    },-->
<!--    // 取消按钮-->
<!--    cancel() {-->
<!--      this.open = false;-->
<!--      this.reset();-->
<!--    },-->
<!--    // 表单重置-->
<!--    reset() {-->
<!--      this.form = {}-->
<!--    },-->
<!--    /** 搜索按钮操作 */-->
<!--    handleQuery() {-->
<!--      this.queryParams.pageNum = 1;-->
<!--      this.getList();-->
<!--    },-->
<!--    /** 重置按钮操作 */-->
<!--    resetQuery() {-->
<!--      this.resetForm("queryForm");-->
<!--      this.handleQuery();-->
<!--    },-->
<!--    /** 新增按钮操作 */-->
<!--    handleAdd() {-->
<!--      this.reset();-->
<!--      this.dialogVisible = true-->
<!--    },-->
<!--    handleClose(done) {-->
<!--      this.$confirm('确认关闭？')-->
<!--        .then(_ => {-->
<!--          done();-->
<!--        })-->
<!--        .catch(_ => {});-->
<!--    },-->
<!--    /** 修改按钮操作 */-->
<!--    handleUpdate(row) {-->
<!--      if (row.id === 'undefined' || !row.id) {-->
<!--        this.$message.error('请勾选～')-->
<!--        return-->
<!--      }-->
<!--      this.reset();-->
<!--      this.dialogVisible = true-->
<!--      getSuite(row.id).then(response => {-->
<!--        this.form = response.data;-->
<!--      });-->
<!--    },-->
<!--    /** 提交按钮 */-->
<!--    submitForm: function () {-->
<!--      this.$refs["form"].validate(valid => {-->
<!--        if (valid) {-->
<!--        }-->
<!--      });-->
<!--    },-->
<!--    /** 删除按钮操作 */-->
<!--    handleDelete(row) {-->
<!--      const configIds = row.id || this.ids;-->
<!--      this.$confirm('是否确认删除埋点编号为"' + configIds + '"的数据项?', "警告", {-->
<!--        confirmButtonText: "确定",-->
<!--        cancelButtonText: "取消",-->
<!--        type: "warning"-->
<!--      }).then(function () {-->
<!--      }).then(() => {-->
<!--        this.getList();-->
<!--        this.msgSuccess("删除成功");-->
<!--      });-->
<!--    },-->
<!--    handleDetail(row) {-->
<!--      this.form = row-->
<!--      this.open = true-->
<!--    },-->
<!--    /** 导出按钮操作 */-->
<!--    handleExport() {-->
<!--      const queryParams = this.queryParams;-->
<!--      this.$confirm("是否确认导出所有数据项?", "警告", {-->
<!--        confirmButtonText: "确定",-->
<!--        cancelButtonText: "取消",-->
<!--        type: "warning"-->
<!--      }).then(function () {-->
<!--      }).then(response => {-->
<!--        this.download(response.data.file_url, response.data.name);-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->
