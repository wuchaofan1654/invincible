<!--<template>-->
<!--  <div class="app-container" :style=bodyStyle>-->
<!--    <el-tabs v-model="activeName">-->
<!--      <el-tab-pane label="基本请求信息" name="basic">-->
<!--        <el-form :model="apiInfo.basic">-->
<!--          <el-form-item label="*接口名称">-->
<!--            <el-input v-model='apiInfo.basic.name' placeholder="接口名称必填"></el-input>-->
<!--          </el-form-item>-->
<!--          <el-form-item label="*接口url">-->
<!--            <el-input v-model='apiInfo.basic.url' type="textarea" :row="8" placeholder="(必填)http://****"></el-input>-->
<!--          </el-form-item>-->
<!--          <el-container>-->
<!--            <el-form-item style="padding-right: 2em" label="*请求方式">-->
<!--              <el-select v-model="apiInfo.basic.method">-->
<!--                <el-option label="GET" value="get"/>-->
<!--                <el-option label="POST" value="post"/>-->
<!--                <el-option label="PUT" value="put"/>-->
<!--                <el-option label="DELETE" value="delete"/>-->
<!--              </el-select>-->
<!--            </el-form-item>-->
<!--            <el-form-item style="padding-right: 2em" label="超时时间">-->
<!--              <el-input v-model="apiInfo.basic.timeout" width="120">-->
<!--                <span slot="append">毫秒</span>-->
<!--              </el-input>-->
<!--            </el-form-item>-->
<!--            <el-form-item style="padding-right: 2em" label="允许code">-->
<!--              <el-input v-model="apiInfo.basic.errorCodes"></el-input>-->
<!--            </el-form-item>-->
<!--          </el-container>-->
<!--        </el-form>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="Header定义" name="header">-->
<!--        <el-table class="body-pane-table" :data="apiInfo.params" style="width: 100%" size="mini">-->
<!--          <el-table-column label="Key" prop="key" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__key" v-model="scope.row.key" @blur="addLine(scope.row)">-->
<!--                Key-->
<!--              </el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="Value" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" width="80">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button v-if="apiInfo.params.length > 1" type="text" icon="el-icon-delete" @click="rmLine(scope.row)"/>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="Body定义" name="body">-->
<!--        <div class="radio-box">-->
<!--          <span style="font-size: 13px; color: #333333; font-weight: bold">Content-Type：</span>-->
<!--          <el-radio v-model="contentType" label="form">form-urlencoded</el-radio>-->
<!--          <el-radio v-model="contentType" label="raw">raw</el-radio>-->
<!--        </div>-->
<!--        <el-table class="body-pane-table" :data="apiInfo.params" style="width: 100%" size="mini">-->
<!--          <el-table-column label="Key" prop="key">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__key" v-model="scope.row.key" @blur="addLine(scope.row)">-->
<!--                Key-->
<!--              </el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="Value" prop="value">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" width="80">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button v-if="bodyProperties.apiList.length > 1" type="text" icon="el-icon-delete" @click="rmLine(scope.row)"/>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="断言定义" name="validate">-->
<!--        <el-table class="body-pane-table" :data="apiInfo.params" style="width: 100%" size="mini">-->
<!--          <el-table-column label="检查项" prop="key" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__key" v-model="scope.row.key" @blur="addLine(scope.row)">-->
<!--                Key-->
<!--              </el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="检测方法" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="检测表达式" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="检查条件" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="期望值" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" width="80" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button v-if="apiInfo.params.length > 1" type="text" icon="el-icon-delete" @click="rmLine(scope.row)"/>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="提取参数" name="extract">-->
<!--        <el-table class="body-pane-table" :data="apiInfo.params" style="width: 100%" size="mini">-->
<!--          <el-table-column label="提取项" prop="key" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__key" v-model="scope.row.key" @blur="addLine(scope.row)">-->
<!--                Key-->
<!--              </el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="提取类型" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="提取表达式" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="赋值变量名" prop="value" :show-overflow-tooltip="true">-->
<!--            <template slot-scope="scope">-->
<!--              <el-input class="body-pane-table__value" v-model="scope.row.value">Value</el-input>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--          <el-table-column label="操作" width="80">-->
<!--            <template slot-scope="scope">-->
<!--              <el-button v-if="apiInfo.params.length > 1" type="text" icon="el-icon-delete" @click="rmLine(scope.row)"/>-->
<!--            </template>-->
<!--          </el-table-column>-->
<!--        </el-table>-->
<!--      </el-tab-pane>-->
<!--    </el-tabs>-->
<!--    <div class="handle-options">-->
<!--      <el-button size="mini" type="primary">调试</el-button>-->
<!--      <el-button size="mini" type="primary">保存</el-button>-->
<!--      <el-button size="mini" type="primary">取消</el-button>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: "Api",-->
<!--  props: {-->
<!--    activeName: {-->
<!--      type: String,-->
<!--      default: 'basic'-->
<!--    },-->
<!--    apiInfo: {-->
<!--      type: Object,-->
<!--      default: () => {}-->
<!--    },-->
<!--    contentType: {-->
<!--      type: String,-->
<!--      default: 'form'-->
<!--    },-->
<!--    bodyStyle: {-->
<!--      type: String,-->
<!--      default: 'background-color: #EBEEF5; font-size: 12px'-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    addLine(row) {-->
<!--      if (row.key) {-->
<!--        this.apiInfo.params.push({key: '', value: ''})-->
<!--      }-->
<!--    },-->
<!--    rmLine(row) {-->
<!--      let index = this.apiInfo.param.indexOf(row)-->
<!--      if (index !== -1 && this.apiInfo.param.length > 1) {-->
<!--        this.apiInfo.param.splice(index, 1)-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped lang="scss">-->

<!--.app-container {-->
<!--  font-size: 10px;-->
<!--  background-color: #42b983;-->
<!--}-->

<!--.main-body {-->
<!--  margin: 3px;-->
<!--}-->

<!--.radio-box {-->
<!--  padding: 10px 0;-->
<!--}-->

<!--.body-pane-table {-->

<!--  .body-pane-table__key {-->
<!--    border: none;-->
<!--  }-->
<!--}-->

<!--.handle-options {-->
<!--  margin: 10px;-->
<!--}-->
<!--</style>-->
