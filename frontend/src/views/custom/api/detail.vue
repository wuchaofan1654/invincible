<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-form ref="detailForm" :model="form" :inline="true" label-width="80px">-->
<!--      <el-card class="api__detail__card">-->
<!--        <div slot="header">-->
<!--          <span>基本属性</span>-->
<!--        </div>-->
<!--        <el-form-item label="接口名称">-->
<!--          <el-input-->
<!--            style="width: 400px"-->
<!--            v-model="form.name"-->
<!--            placeholder="请输入接口名称"-->
<!--            clearable-->
<!--            size="small"-->
<!--            @keyup.enter.native="checkIsApiNameUnique"/>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="接口url">-->
<!--          <el-input-->
<!--            style="width: 400px"-->
<!--            v-model="form.url"-->
<!--            placeholder="请输入接口url"-->
<!--            clearable-->
<!--            size="small"/>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="所属团队">-->
<!--          <el-select-->
<!--            v-model="form.dept"-->
<!--            placeholder="请选择">-->
<!--            <el-option v-for="item in deptOptions" :label="item.deptName" :value="item.id"/>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="所属模块">-->
<!--          <el-select-->
<!--            v-model="form.module"-->
<!--            placeholder="请选择">-->
<!--            <el-option v-for="item in moduleOptions" :label="item.moduleName" :value="item.id"/>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="接口状态">-->
<!--          <el-radio-group-->
<!--            v-model="form.status">-->
<!--            <el-radio v-for="item in statusOptions" :label="item.value">{{ item.label }}</el-radio>-->
<!--          </el-radio-group>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="核心接口">-->
<!--          <el-radio-group-->
<!--            v-model="form.key_yn">-->
<!--            <el-radio v-for="item in keyYnOptions" :label="item.value">{{ item.label }}</el-radio>-->
<!--          </el-radio-group>-->
<!--        </el-form-item>-->
<!--      </el-card>-->
<!--      <el-card class="api__detail__card">-->
<!--        <div slot="header">-->
<!--          <span>参数信息</span>-->
<!--          <el-button type="text" icon="el-icon-plus" @click="addParam">新增</el-button>-->
<!--        </div>-->
<!--        <el-table :data="form.params">-->
<!--          <el-table-column prop="type" label="参数类型" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-select v-model="scope.row.type">-->
<!--                <el-option v-for="item in paramTypeOptions" :label="item.label" :value="item.value"></el-option>-->
<!--              </el-select>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="key" label="参数key" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input v-model="scope.row.key"></el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="value" label="参数value" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input v-if="scope.row.type !== 5" v-model="scope.row.value"></el-input>-->
<!--              <FileUpload v-else @input="updateParamValue" :is-show-tip="false"></FileUpload>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button-group>-->
<!--                <el-button type="text" icon="el-icon-plus" @click="addParam"></el-button>-->
<!--                <el-button type="text" icon="el-icon-delete" @click="removeParam(scope.row)"></el-button>-->
<!--              </el-button-group>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-card>-->
<!--      <el-card class="api__detail__card">-->
<!--        <div slot="header">-->
<!--          <span>验证器</span>-->
<!--          <el-button type="text" icon="el-icon-plus" @click="addValidator">新增</el-button>-->
<!--        </div>-->
<!--        <el-table :data="form.validators">-->
<!--          <el-table-column prop="type" label="验证方式" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-select v-model="scope.row.expression_type">-->
<!--                <el-option v-for="item in expressionTypeOptions" :label="item.label" :value="item.value"></el-option>-->
<!--              </el-select>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="expression" label="表达式" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input v-model="scope.row.expression"></el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="symbol" label="比较符" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-select v-model="scope.row.symbol">-->
<!--                <el-option v-for="item in symbolOptions" :label="item.label" :value="item.value"/>-->
<!--              </el-select>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="excepted" label="期望值" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input v-model="scope.row.excepted"/>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button-group>-->
<!--                <el-button type="text" icon="el-icon-plus" @click="addValidator"></el-button>-->
<!--                <el-button type="text" icon="el-icon-delete" @click="removeValidator(scope.row)"></el-button>-->
<!--              </el-button-group>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-card>-->
<!--      <el-card class="api__detail__card">-->
<!--        <div slot="header">-->
<!--          <span>提取器</span>-->
<!--          <el-button type="text" icon="el-icon-plus" @click="addExtractor">新增</el-button>-->
<!--        </div>-->
<!--        <el-table :data="form.extractors">-->
<!--          <el-table-column prop="type" label="提取方式" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-select v-model="scope.row.expression_type">-->
<!--                <el-option v-for="item in expressionTypeOptions" :label="item.label" :value="item.value"></el-option>-->
<!--              </el-select>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="expression" label="表达式" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input v-model="scope.row.expression"></el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column prop="variable" label="赋值变量名" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input v-model="scope.row.variable"></el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" align="center">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button-group>-->
<!--                <el-button type="text" icon="el-icon-plus" @click="addExtractor"></el-button>-->
<!--                <el-button type="text" icon="el-icon-delete" @click="removeExtractor(scope.row)"></el-button>-->
<!--              </el-button-group>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-card>-->
<!--    </el-form>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->

<!--import {getApiDetail} from "@/api/api/api";-->
<!--import {listDept} from "@/api/permission/dept"-->
<!--import {listModule} from "@/api/permission/module"-->
<!--import FileUpload from "@/components/FileUpload/index.vue";-->

<!--const defaultForm = {-->
<!--  name: '',-->
<!--  url: '',-->
<!--  method: 'GET',-->
<!--  key_yn: 0,-->
<!--  status: 1,-->
<!--  dept: '',-->
<!--  module: '',-->
<!--  params: [],-->
<!--  validators: [],-->
<!--  extractors: []-->
<!--}-->
<!--export default {-->
<!--  name: "detail",-->
<!--  components: {FileUpload},-->
<!--  data() {-->
<!--    return {-->
<!--      id: this.$route.query.id,-->
<!--      form: Object.assign(defaultForm),-->
<!--      paramsFormDataYn: false,-->
<!--      validatorsFormDataYn: false,-->
<!--      extractorsFormDataYn: false,-->
<!--      paramTypeOptions: [-->
<!--        {label: '字符串', value: 1},-->
<!--        {label: '文件', value: 5}-->
<!--      ],-->
<!--      deptOptions: [],-->
<!--      moduleOptions: [],-->
<!--      symbolOptions: [-->
<!--        {label: 'equals', value: '='},-->
<!--        {label: 'equals as str', value: 'str='},-->
<!--        {label: 'equals as int', value: 'int='},-->
<!--        {label: 'in', value: 'in'},-->
<!--        {label: 'not in', value: 'not in'},-->
<!--        {label: 'contains', value: 'contains'},-->
<!--        {label: 'not contains', value: 'not contains'},-->
<!--        {label: 'is null', value: 'is null'},-->
<!--        {label: 'not null', value: 'not null'},-->
<!--      ],-->
<!--      expressionTypeOptions: [-->
<!--        {label: 'Json 路径', value: 1},-->
<!--        {label: '正则表达式', value: 2},-->
<!--        {label: 'Mysql表达式', value: 3}-->
<!--      ],-->
<!--      statusOptions: [{label: '正常', value: 1}, {label: '禁用', value: 0}],-->
<!--      keyYnOptions: [{label: '是', value: 1}, {label: '否', value: 0}]-->
<!--    }-->
<!--  },-->
<!--  created() {-->
<!--    this.getDetail()-->
<!--    this.getDept()-->
<!--    this.getModule()-->
<!--  },-->
<!--  methods: {-->
<!--    updateParamValue(data) {-->
<!--      console.log(data)-->
<!--    },-->
<!--    getDetail() {-->
<!--      if (this.id) {-->
<!--        getApiDetail(this.id).then(res => {-->
<!--          this.form = res.data-->
<!--          this.form.dept = res.data.dept.id-->
<!--          this.form.module = res.data.module.id-->
<!--        })-->
<!--      }-->
<!--    },-->
<!--    getDept() {-->
<!--      listDept().then(res => {-->
<!--        this.deptOptions = res.data.results-->
<!--      })-->
<!--    },-->
<!--    getModule() {-->
<!--      listModule().then(res => {-->
<!--        this.moduleOptions = res.data.results-->
<!--      })-->
<!--    },-->
<!--    checkIsApiNameUnique() {-->
<!--      return false-->
<!--    },-->
<!--    getApiStatusOptions() {-->

<!--    },-->
<!--    removeParam(item) {-->
<!--      let index = this.form.params.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.form.params.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--    addParam() {-->
<!--      this.form.params.push({-->
<!--        key: '',-->
<!--        type: '',-->
<!--        value: ''-->
<!--      });-->
<!--    },-->
<!--    removeValidator(item) {-->
<!--      let index = this.form.validators.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.form.params.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--    addValidator() {-->
<!--      this.form.validators.push({-->
<!--        expression: '',-->
<!--        expression_type: '',-->
<!--        symbol: '',-->
<!--        excepted: ''-->
<!--      });-->
<!--    },-->
<!--    removeExtractor(item) {-->
<!--      let index = this.form.extractors.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.form.params.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--    addExtractor() {-->
<!--      this.form.extractors.push({-->
<!--        expression: '',-->
<!--        expression_type: '',-->
<!--        variable: ''-->
<!--      });-->
<!--    },-->
<!--    submitForm() {-->
<!--      console.log(this.form)-->
<!--    },-->
<!--    resetForm() {-->
<!--      this.$confirm('此操作将清空已填写数据, 是否继续?', '提示', {-->
<!--        confirmButtonText: '确定',-->
<!--        cancelButtonText: '取消',-->
<!--        type: 'warning'-->
<!--      }).then(() => {-->
<!--        this.form = Object.assign(defaultForm)-->
<!--        this.$message({-->
<!--          type: 'success',-->
<!--          message: '已清空!'-->
<!--        });-->
<!--      }).catch(() => {-->
<!--        this.$message({-->
<!--          type: 'info',-->
<!--          message: '已取消'-->
<!--        });-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--.api__detail__card {-->
<!--  margin: 20px 0;-->
<!--}-->
<!--</style>-->
