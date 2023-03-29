<!--<template> -->
<!--  <div class="app-container">-->
<!--    <el-tabs v-model="activeName" @tab-click="handleTabClick">-->
<!--      <el-tab-pane label="环境管理" name="first">-->
<!--        <el-card class="config-boxed-card">-->
<!--          <div slot="header">-->
<!--            <span><i class="el-icon-setting"></i> 环境配置</span>-->
<!--            <el-button-->
<!--              :size="configDict.size"-->
<!--              icon="el-icon-edit"-->
<!--              type="success"-->
<!--              style="float: right; margin: 0 20px 10px 0"-->
<!--              @click="addSlave">-->
<!--              添加slave-->
<!--            </el-button>-->
<!--          </div>-->
<!--          <el-table :data="serverList">-->
<!--            <el-table-column label="ip地址" prop="ip" align="center"></el-table-column>-->
<!--            <el-table-column label="端口号" prop="port" align="center"></el-table-column>-->
<!--            <el-table-column label="master/slave" prop="type" align="center"></el-table-column>-->
<!--            <el-table-column label="操作" align="center">-->
<!--              <template slot-scope="scope">-->
<!--                <el-button type="text" icon='el-icon-plus' @click="addSlave"></el-button>-->
<!--                <el-button type="text" icon='el-icon-delete' @click="removeSlave"></el-button>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--          </el-table>-->
<!--        </el-card>-->
<!--          <el-card class="config-boxed-card">-->
<!--          <div slot="header">-->
<!--            <span><i class="el-icon-setting"></i> 全局变量配置</span>-->
<!--            <el-button-->
<!--              :size="configDict.size"-->
<!--              icon="el-icon-edit"-->
<!--              type="success"-->
<!--              style="float: right; margin: 0 20px 10px 0"-->
<!--              @click="addSlave">-->
<!--              添加slave-->
<!--            </el-button>-->
<!--          </div>-->
<!--          <el-table :data="globalVariableList">-->
<!--            <el-table-column label="参数名" prop="name" align="center"></el-table-column>-->
<!--            <el-table-column label="参数类型" prop="type" align="center"></el-table-column>-->
<!--            <el-table-column label="参数值" align="center">-->
<!--              <template slot-scope="scope">-->
<!--                <el-input v-model="scope.row.value"></el-input>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--            <el-table-column label="操作" align="center">-->
<!--              <template slot-scope="scope">-->
<!--                <el-button type="text" icon='el-icon-plus' @click="addGlobalVariable"></el-button>-->
<!--                <el-button type="text" icon='el-icon-delete' @click="removeGlobalVariable"></el-button>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--          </el-table>-->
<!--          </el-card>-->
<!--          <el-card class="config-boxed-card">-->
<!--          <div slot="header">-->
<!--            <span><i class="el-icon-document"></i> 文件变量配置</span>-->
<!--            <el-button-->
<!--              :size="configDict.size"-->
<!--              icon="el-icon-edit"-->
<!--              type="success"-->
<!--              style="float: right; margin: 0 20px 10px 0"-->
<!--              @click="addSlave">-->
<!--              添加slave-->
<!--            </el-button>-->
<!--          </div>-->
<!--          <el-table :data="csvVariableList">-->
<!--            <el-table-column label="ip地址" prop="ip" align="center"></el-table-column>-->
<!--            <el-table-column label="端口号" prop="port" align="center"></el-table-column>-->
<!--            <el-table-column label="master/slave" prop="type" align="center"></el-table-column>-->
<!--            <el-table-column label="操作" align="center">-->
<!--              <template slot-scope="scope">-->
<!--                <el-button type="text" icon='el-icon-plus' @click="addSlave"></el-button>-->
<!--                <el-button type="text" icon='el-icon-delete' @click="removeSlave"></el-button>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--          </el-table>-->
<!--        </el-card>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="接口管理" name="second">-->
<!--        <el-card class="box-card">-->
<!--          <div slot="header">-->
<!--            <span>接口列表</span>-->
<!--            <el-button @click="transferVisible=true">添加接口</el-button>-->
<!--          </div>-->
<!--          <el-table v-loading="configDict.loading" :data="apiList" @selection-change="handleSelectionChange">-->
<!--          <el-table-column type="selection" width="55" align="center"/>-->
<!--          <el-table-column label="编号" prop="id" width="80"/>-->
<!--          <el-table-column label="接口名称" prop="name" :show-overflow-tooltip="true"/>-->
<!--          <el-table-column label="请求url" prop="url" :show-overflow-tooltip="true"/>-->
<!--          <el-table-column label="权重" prop="weight" width="100" :show-overflow-tooltip="true"/>-->
<!--          <el-table-column label="状态" align="center" width="100" sortable>-->
<!--            <template slot-scope="scope">-->
<!--              <el-switch-->
<!--                v-model="scope.row.status.toString()"-->
<!--                active-value="1"-->
<!--                inactive-value="0"-->
<!--                disabled-->
<!--                @change="handleStatusChange(scope.row)"-->
<!--              />-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column-->
<!--            label="操作"-->
<!--            align="center"-->
<!--            class-name="small-padding fixed-width"-->
<!--          >-->
<!--            <template slot-scope="scope">-->
<!--              <el-button-->
<!--                v-hasPermission="['permission:role:{id}:delete']"-->
<!--                size="mini"-->
<!--                type="text"-->
<!--                icon="el-icon-delete"-->
<!--                @click="handleDelete(scope.row)"-->
<!--              >删除-->
<!--              </el-button>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--        </el-card>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="运行监控" name="third">-->
<!--        <div>-->
<!--          <el-link href="http://baidu.com">外部链接</el-link>-->
<!--        </div>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="报告管理" name="forth">-->
<!--        <el-table v-loading="configDict.loading" :data="reportList" @selection-change="handleSelectionChange">-->
<!--          <el-table-column type="selection" width="55" align="center"/>-->
<!--          <el-table-column label="编号" prop="id" width="80"/>-->
<!--          <el-table-column label="报告名称" prop="name" :show-overflow-tooltip="true"/>-->
<!--          <el-table-column label="状态" prop="url" :show-overflow-tooltip="true"/>-->
<!--          <el-table-column label="创建时间" prop="weight" width="100" :show-overflow-tooltip="true"/>-->
<!--          <el-table-column-->
<!--            label="操作"-->
<!--            align="center"-->
<!--            class-name="small-padding fixed-width">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button-->
<!--                v-hasPermission="['permission:role:{id}:delete']"-->
<!--                :size="configDict.size"-->
<!--                type="text"-->
<!--                icon="el-icon-delete"-->
<!--                @click="handleDelete(scope.row)"-->
<!--              >删除-->
<!--              </el-button>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-tab-pane>-->
<!--    </el-tabs>-->
<!--    <el-dialog-->
<!--      title="选择添加的接口"-->
<!--      :visible="transferVisible"-->
<!--    >-->
<!--    <el-transfer-->
<!--      v-model="value"-->
<!--      filterable-->
<!--      :titles="['全部接口列表', '已选择接口']"-->
<!--      :props="{key: 'id', label: 'name'}"-->
<!--      :data="apiList" />-->
<!--      <span slot="footer" class="dialog-footer">-->
<!--        <el-button @click="transferVisible=false">取 消</el-button>-->
<!--        <el-button type="primary" @click="dialogVisible=false">确 定</el-button>-->
<!--      </span>-->
<!--    </el-dialog>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--import { getApi } from '@/api/custom/api'-->

<!--const defaultConfig = {-->
<!--  size: 'mini',-->
<!--  loading: false-->
<!--}-->

<!--const defaultQueryParams = {-->
<!--  name: null,-->
<!--  owner: null,-->
<!--  key_yn: null,-->
<!--  status: null,-->
<!--  pageNum: 1,-->
<!--  pageSize: 20-->
<!--};-->

<!--export default {-->
<!--  name: "index",-->
<!--  data() {-->
<!--    return {-->
<!--      html: '',-->
<!--      value: '',-->
<!--      transferVisible: false,-->
<!--      activeName: 'first',-->
<!--      serverList: [-->
<!--        {type: 'master', ip: '', port: ''}-->
<!--      ],-->
<!--      globalVariableList: [-->
<!--        {name: '', type: '', value: ''}-->
<!--      ],-->
<!--      csvVariableList: [-->
<!--        {name: '', filePath: ''}-->
<!--      ],-->
<!--      apiList: [],-->
<!--      reportList: [],-->
<!--      queryParams: Object.assign({}, defaultQueryParams),-->
<!--      configDict: Object.assign({}, defaultConfig),-->
<!--    }-->
<!--  },-->
<!--  created() {-->
<!--    this.getList();-->
<!--  },-->
<!--  mounted() {-->
<!--    this.load()-->
<!--  },-->
<!--  methods: {-->
<!--    handleAvatarSuccess(res, file) {-->
<!--      this.dynamicValidateForm.csvVariables[0].filePath = file.name;-->
<!--    },-->
<!--    getList() {-->
<!--      this.loading = true;-->
<!--      getApi(this.queryParams).then(response => {-->
<!--        this.loading = false;-->
<!--        this.apiList = response.data.results;-->
<!--        this.total = response.data.count-->
<!--      });-->
<!--    },-->
<!--    /** 搜索按钮点击 */-->
<!--    handleQuery() {-->
<!--      this.getList()-->
<!--    },-->
<!--    pTypeFormat(row, column) {-->
<!--      return row.key_yn === 1 ? '事件' : '页面'-->
<!--    },-->
<!--    // 埋点是否核心字典翻译-->
<!--    keyYnFormat(row, column) {-->
<!--      return row.key_yn === 1 ? '是' : '否'-->
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
<!--      this.$router.push({path: '/apis/addApi'});-->
<!--    },-->
<!--    handleAdd() {-->

<!--    },-->
<!--    handleDelete() {-->

<!--    },-->
<!--    handleUpdate() {-->
<!--    },-->
<!--    handleDataScope() {-->
<!--    },-->
<!--    handleExport() {-->
<!--    },-->
<!--    handleSelectionChange() {-->
<!--    },-->
<!--    submitForm(formName) {-->
<!--      this.$refs[formName].validate((valid) => {-->
<!--        if (valid) {-->
<!--          alert('submit!');-->
<!--        } else {-->
<!--          console.log('error submit!!');-->
<!--          return false;-->
<!--        }-->
<!--      });-->
<!--    },-->
<!--    resetForm(formName) {-->
<!--      this.$refs[formName].resetFields();-->
<!--    },-->
<!--    handleTabClick(event) {-->
<!--      console.log(event)-->
<!--    },-->
<!--    addSlave() {-->
<!--      this.dynamicValidateForm.slaves.push({-->
<!--        value: '',-->
<!--        key: Date.now()-->
<!--      });-->
<!--    },-->
<!--    removeSlave(item) {-->
<!--      let index = this.dynamicValidateForm.slaves.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.dynamicValidateForm.slaves.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--    addGlobalVariable() {-->
<!--      this.dynamicValidateForm.globalVariables.push(-->
<!--        {-->
<!--          name: '',-->
<!--          type: '',-->
<!--          value: ''-->
<!--        });-->
<!--    },-->
<!--    removeGlobalVariable(item) {-->
<!--      let index = this.dynamicValidateForm.globalVariables.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.dynamicValidateForm.globalVariables.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--    addCsvVariable() {-->
<!--      this.dynamicValidateForm.csvVariables.push(-->
<!--        {-->
<!--          name: '',-->
<!--          value: ''-->
<!--        }-->
<!--      );-->
<!--    },-->
<!--    removeCsvVariable(item) {-->
<!--      let index = this.dynamicValidateForm.csvVariables.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.dynamicValidateForm.csvVariables.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--    uploadSucceed(response, file, fileList) {-->
<!--      console.log(this.dynamicValidateForm.csvVariables)-->
<!--    },-->
<!--    load() {-->
<!--      this.html = '<el-input>1234567</el-input>'-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->
<!--<style>-->
<!--.config-boxed-card {-->
<!--  margin: 10px 0 20px 0;-->
<!--}-->

<!--.variable-config-header {-->
<!--  font-size: 12px;-->
<!--  color: #909399;-->
<!--  text-align: left;-->
<!--}-->

<!--.variable-config-header-title {-->
<!--  font-size: 12px;-->
<!--  color: #909399;-->
<!--  text-align: left;-->
<!--  padding-left: 10px;-->
<!--}-->

<!--.variable-config-body {-->
<!--  text-align: left;-->
<!--  margin-top: 10px;-->
<!--}-->
<!--</style>-->


