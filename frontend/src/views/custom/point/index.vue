<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-form v-show="showSearch" ref="queryForm" :model="queryParams" :inline="true" label-width="68px">-->
<!--      <el-form-item label="埋点名称" prop="title">-->
<!--        <el-input-->
<!--          v-model="queryParams.title"-->
<!--          placeholder="请输入名称"-->
<!--          clearable-->
<!--          size="small"-->
<!--          style="width: 240px"-->
<!--          @keyup.enter.native="handleQuery"/>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="埋点类型" prop="point_type">-->
<!--        <el-select v-model="queryParams.point_type" placeholder="埋点类型" clearable size="small">-->
<!--          <el-option-->
<!--            v-for="dict in PointTypeOptions"-->
<!--            :key="dict.dictValue"-->
<!--            :label="dict.dictLabel"-->
<!--            :value="dict.dictValue"/>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="埋点状态" prop="status">-->
<!--        <el-select v-model="queryParams.status" placeholder="埋点状态" clearable size="small">-->
<!--          <el-option-->
<!--            v-for="dict in PointStatusOptions"-->
<!--            :key="dict.dictValue"-->
<!--            :label="dict.dictLabel"-->
<!--            :value="dict.dictValue"/>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="是否核心" prop="is_reviewed">-->
<!--        <el-select v-model="queryParams.is_reviewed" placeholder="是否核心" clearable size="small">-->
<!--          <el-option :key="true" label="是" :value="true"/>-->
<!--          <el-option :key="false" label="否" :value="false"/>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="埋点集合" prop="point_type">-->
<!--        <el-select v-model="queryParams.suite_id" placeholder="埋点集合" clearable size="small">-->
<!--          <el-option-->
<!--            v-for="suite in PointSuitesOptions"-->
<!--            :key="suite.name"-->
<!--            :label="suite.name"-->
<!--            :value="suite.id"/>-->
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
<!--          :disabled="single"-->
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
<!--          :disabled="multiple"-->
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
<!--    <el-table v-loading="loading" :data="configList">-->
<!--      <el-table-column type="selection" width="55" align="center"/>-->
<!--      <el-table-column label="埋点名称" align="center" prop="en_name" sortable :show-overflow-tooltip="true"/>-->
<!--      <el-table-column label="类型" align="center" prop="point_type" sortable width="120" :formatter="typeFormat"/>-->
<!--      <el-table-column label="curr_page" align="center" prop="curr_page" sortable :show-overflow-tooltip="true"/>-->
<!--      <el-table-column label="from_action" align="center" prop="from_action" sortable :show-overflow-tooltip="true"/>-->
<!--      <el-table-column label="埋点状态" align="center" prop="status" sortable width="100" :formatter="statusFormat"/>-->
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
<!--          <el-popover-->
<!--            placement="top-start"-->
<!--            width="500"-->
<!--            trigger="click">-->
<!--            <pre>{{JSON.parse(JSON.stringify(scope.row))}}</pre>-->
<!--            <el-button-->
<!--              slot="reference"-->
<!--              type="text"-->
<!--              icon="el-icon-document"-->
<!--              size="mini">详情-->
<!--            </el-button>-->
<!--          </el-popover>-->
<!--          <el-divider direction="vertical"></el-divider>-->
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
<!--    &lt;!&ndash; 添加或修改埋点配置对话框 &ndash;&gt;-->
<!--    <el-dialog :title="title" :visible.sync="open" width="780px" append-to-body>-->
<!--      <el-form ref="form" :model="form" label-width="80px">-->
<!--        <el-row>-->
<!--          <el-col :span="12">-->
<!--            <el-form-item label="中文名称" prop="title">-->
<!--              <el-input v-model="form.zh_name" placeholder="请输入中文名称"/>-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col :span="12">-->
<!--            <el-form-item label="埋点类型" prop="message_type">-->
<!--              <el-select v-model="form.point_type" placeholder="请选择">-->
<!--                <el-option-->
<!--                  v-for="dict in PointTypeOptions"-->
<!--                  :key="dict.dictValue"-->
<!--                  :label="dict.dictLabel"-->
<!--                  :value="dict.dictValue"-->
<!--                />-->
<!--              </el-select>-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col v-if="parseInt(form.point_type) === 1" :span="12">-->
<!--            <el-form-item label="事件名称" prop="from_action">-->
<!--              <el-input v-model="form.from_action" placeholder="from_action" />-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col v-if="parseInt(form.point_type) === 1" :span="24">-->
<!--            <el-form-item label="事件扩展" prop="from_action_ext">-->
<!--              <v-jsoneditor v-model="form.from_action_ext" :plus="false"/>-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col v-if="parseInt(form.point_type) === 2" :span="12">-->
<!--            <el-form-item label="当前页面" prop="curr_page">-->
<!--              <el-input v-model="form.curr_page" placeholder="curr_page" />-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col v-if="parseInt(form.point_type) === 2" :span="24">-->
<!--            <el-form-item label="页面扩展" prop="curr_page_ext">-->
<!--              <v-jsoneditor v-model="form.curr_page_ext"/>-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col :span="24">-->
<!--            <el-form-item label="状态" prop="status">-->
<!--              <el-radio-group v-model="form.status">-->
<!--                <el-radio-->
<!--                  v-for="dict in PointStatusOptions"-->
<!--                  :key="dict.dictValue"-->
<!--                  :label="dict.dictValue"-->
<!--                >{{ dict.dictLabel }}-->
<!--                </el-radio>-->
<!--              </el-radio-group>-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--          <el-col :span="24">-->
<!--            <el-form-item label="是否核心" prop="key_yn">-->
<!--              <el-radio-group v-model="form.key_yn">-->
<!--                <el-radio :label="true">是</el-radio>-->
<!--                <el-radio :label="false">否</el-radio>-->
<!--              </el-radio-group>-->
<!--            </el-form-item>-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--      </el-form>-->
<!--      <div slot="footer" class="dialog-footer">-->
<!--        <el-button type="primary" @click="submitForm">确 定</el-button>-->
<!--        <el-button @click="cancel">取 消</el-button>-->
<!--      </div>-->
<!--    </el-dialog>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import {-->
<!--  listPoint,-->
<!--  getPoint,-->
<!--  addPoint,-->
<!--  updatePoint,-->
<!--  deletePoint,-->
<!--} from "@/api/custom/point/point";-->


<!--export default {-->
<!--  name: "Index",-->
<!--  components: {},-->
<!--  data() {-->
<!--    return {-->
<!--      // 遮罩层-->
<!--      loading: true,-->
<!--      // 选中数组-->
<!--      ids: [],-->
<!--      // 非单个禁用-->
<!--      single: true,-->
<!--      // 非多个禁用-->
<!--      multiple: true,-->
<!--      // 显示搜索条件-->
<!--      showSearch: true,-->
<!--      // 总条数-->
<!--      total: 0,-->
<!--      // 埋点表格数据-->
<!--      configList: [],-->
<!--      // 弹出层标题-->
<!--      title: "",-->
<!--      // 是否显示弹出层-->
<!--      open: false,-->
<!--      // 埋点类型字典-->
<!--      PointTypeOptions: [],-->
<!--      // 埋点状态字典-->
<!--      PointStatusOptions: [],-->
<!--      PointSuitesOptions: [{id: 1, name: '日记相关核心埋点'}],-->
<!--      // 查询埋点-->
<!--      queryParams: {-->
<!--        pageNum: 1,-->
<!--        pageSize: 10,-->
<!--        zh_name: undefined,-->
<!--        curr_page: undefined,-->
<!--        from_action: undefined,-->
<!--        key_yn: undefined,-->
<!--        point_type: undefined,-->
<!--        status: undefined,-->
<!--        suite_id: undefined,-->
<!--      },-->
<!--      // 表单埋点-->
<!--      form: {},-->
<!--      // 表单校验-->
<!--      rules: {-->
<!--        zh_name: [-->
<!--          {required: true, message: "埋点中文名称必填", trigger: "blur"}-->
<!--        ],-->
<!--        point_type: [-->
<!--          {required: true, message: "埋点类型必须按", trigger: "blur"}-->
<!--        ]-->
<!--      }-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getList();-->
<!--    this.getDicts("point_type_options").then(response => {-->
<!--      this.PointTypeOptions = response.data;-->
<!--    });-->
<!--    this.getDicts("point_status_options").then(response => {-->
<!--      this.PointStatusOptions = response.data;-->
<!--    });-->
<!--  },-->
<!--  watch: {-->
<!--    'form.point_type' : {-->
<!--      handler(newVal, oldVal) {-->
<!--      }-->
<!--    }-->
<!--  },-->
<!--  methods: {-->

<!--    /** 查询埋点列表 */-->
<!--    getList() {-->
<!--      this.loading = true;-->
<!--      listPoint(this.addDateRange(this.queryParams)).then(response => {-->
<!--          this.configList = response.data.results;-->
<!--          this.total = response.data.count;-->
<!--          this.loading = false;-->
<!--        }-->
<!--      );-->
<!--    },-->
<!--    // 埋点类型字典翻译-->
<!--    typeFormat(row, column) {-->
<!--      return this.selectDictLabel(this.PointTypeOptions, row.point_type);-->
<!--    },-->
<!--    // 埋点状态字典翻译-->
<!--    statusFormat(row, column) {-->
<!--      return this.selectDictLabel(this.PointStatusOptions, row.status);-->
<!--    },-->
<!--    // 埋点状态字典翻译-->
<!--    isReviewedFormat(row, column) {-->
<!--      return row.is_reviewed === true ? "是" : "否";-->
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
<!--    isFormChoosePageType() {-->
<!--      return this.form.point_type.toString() === '2'-->
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
<!--      this.open = true;-->
<!--      this.title = "新增埋点";-->
<!--    },-->
<!--    // 多选框选中数据-->
<!--    handleSelectionChange(selection) {-->
<!--      this.ids = selection.map(item => item.id);-->
<!--      this.single = selection.length !== 1;-->
<!--      this.multiple = !selection.length;-->
<!--    },-->
<!--    /** 修改按钮操作 */-->
<!--    handleUpdate(row) {-->
<!--      this.reset();-->
<!--      const id = row.id || this.ids;-->
<!--      getPoint(id).then(response => {-->
<!--        this.form = response.data;-->
<!--        this.open = true;-->
<!--        this.title = "修改埋点";-->
<!--      });-->
<!--    },-->
<!--    /** 提交按钮 */-->
<!--    submitForm: function () {-->
<!--      this.$refs["form"].validate(valid => {-->
<!--        if (valid) {-->
<!--          if (this.form.id !== undefined) {-->
<!--            updatePoint(this.form).then(response => {-->
<!--              this.msgSuccess("修改成功");-->
<!--              this.open = false;-->
<!--              this.getList();-->
<!--            });-->
<!--          } else {-->
<!--            addPoint(this.form).then(response => {-->
<!--              this.msgSuccess("新增成功");-->
<!--              this.open = false;-->
<!--              this.getList();-->
<!--            });-->
<!--          }-->
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
<!--        return deletePoint(configIds);-->
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
<!--        return exportMessage(queryParams);-->
<!--      }).then(response => {-->
<!--        this.download(response.data.file_url, response.data.name);-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->
