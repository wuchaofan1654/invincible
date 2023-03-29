<!--<template>-->
<!--  <div class="app-container" :style=bodyStyle>-->
<!--    <el-tabs v-model="activeName">-->
<!--      <el-tab-pane label="环境配置" name="env">-->
<!--        <el-form :model="apiInfo.basic">-->
<!--          <el-form-item label="*场景名称">-->
<!--            <el-input v-model='apiInfo.basic.name' placeholder="场景名称必填～"></el-input>-->
<!--          </el-form-item>-->
<!--          <el-form-item style="padding-right: 2em" label="*请求方式">-->
<!--            <el-table :data="apiInfo.basic.method">-->
<!--              <el-table-column label="master/slave" prop="type" width="120px" :show-overflow-tooltip="true"/>-->
<!--              <el-table-column label="服务器IP" prop="host" :show-overflow-tooltip="true"/>-->
<!--              <el-table-column label="端口" prop="port" :show-overflow-tooltip="true"/>-->
<!--              <el-table-column label="操作" :show-overflow-tooltip="true">-->
<!--                <template slot-scope="scope">-->
<!--                  <el-button type="text" icon="el-icon-delete" />-->
<!--                </template>-->
<!--              </el-table-column>-->
<!--            </el-table>-->
<!--          </el-form-item>-->
<!--        </el-form>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="变量配置" name="variable">-->
<!--        <el-form :model="apiInfo.basic">-->
<!--          <el-form-item label="*场景名称">-->
<!--            <el-input v-model='apiInfo.basic.name' placeholder="场景名称必填～"></el-input>-->
<!--          </el-form-item>-->
<!--          <el-form-item style="padding-right: 2em" label="*请求方式">-->
<!--            <el-table :data="apiInfo.basic.method">-->
<!--              <el-table-column label="master/slave" prop="type" width="120px" :show-overflow-tooltip="true"/>-->
<!--              <el-table-column label="服务器IP" prop="host" :show-overflow-tooltip="true"/>-->
<!--              <el-table-column label="端口" prop="port" :show-overflow-tooltip="true"/>-->
<!--              <el-table-column label="操作" :show-overflow-tooltip="true">-->
<!--                <template slot-scope="scope">-->
<!--                  <el-button type="text" icon="el-icon-delete" />-->
<!--                </template>-->
<!--              </el-table-column>-->
<!--            </el-table>-->
<!--          </el-form-item>-->
<!--        </el-form>-->
<!--      </el-tab-pane>-->
<!--      <el-tab-pane label="场景配置" name="scene">-->
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
<!--      <el-tab-pane label="监控配置" name="monitor">-->
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
<!--      <el-tab-pane label="压测报告" name="report">-->
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
<!--  name: "Scene",-->
<!--  props: {-->
<!--    activeName: {-->
<!--      type: String,-->
<!--      default: 'env'-->
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
