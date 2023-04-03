<!--<template> -->
<!--  <div class="app-container">-->
<!--    <el-row :gutter="22">-->
<!--      <el-col :span="16">-->
<!--        <div class="main-content">-->
<!--          <el-card class="boxed">-->
<!--            <div slot="header" style="margin-bottom: 5px">-->
<!--              <i class="el-icon-setting"></i>-->
<!--              <span> 选择环境/方法</span>-->
<!--              <div style="float: right; padding-right: 5px">-->
<!--                <el-button-->
<!--                  style="float: right; margin: 0 5px 5px 0"-->
<!--                  type="success"-->
<!--                  :size="configDict.size"-->
<!--                  @click="submitForm">-->
<!--                  开始执行-->
<!--                </el-button>-->
<!--              </div>-->
<!--            </div>-->
<!--            <el-row style="margin: 10px 0 20px 0; font-size: 14px">-->
<!--              <span>选择环境：</span>-->
<!--              <el-radio-group v-model="formData.env">-->
<!--                <el-radio v-for="evn in evnOptions" :label="evn.host">{{ evn.name }}</el-radio>-->
<!--              </el-radio-group>-->
<!--            </el-row>-->
<!--            <el-row style="margin: 0 0 10px 0; font-size: 14px">-->
<!--              <span>选择rpc方法：</span>-->
<!--              <rpc-cas @getSelectedItems="updateSelectedItems" style="width: 80%"></rpc-cas>-->
<!--            </el-row>-->
<!--          </el-card>-->
<!--          <el-card class="boxed" style="margin-top: 20px">-->
<!--            <div slot="header" style="margin-bottom: 5px">-->
<!--              <i class="el-icon-rank"></i>-->
<!--              <span> 请求参数</span>-->
<!--              <div style="float: right; padding-right: 5px">-->
<!--                <el-button :size="configDict.size" type="primary" @click="addGlobalVariable">添加参数</el-button>-->
<!--                <el-button :size="configDict.size" @click="resetGlobalVariable">重置参数</el-button>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="variable-config">-->
<!--              <el-row class="variable-config-header">-->
<!--                <el-col class="variable-config-header-title" :span="8">变量名称</el-col>-->
<!--                <el-col class="variable-config-header-title" :span="4">类型</el-col>-->
<!--                <el-col class="variable-config-header-title" :span="10">值（value)</el-col>-->
<!--              </el-row>-->
<!--              <el-row-->
<!--                class="variable-config-body"-->
<!--                :gutter="22"-->
<!--                v-for="(item, index) in dynamicValidateForm.globalVariables"-->
<!--                :key="item.name"-->
<!--                :prop="'globalVariables.' + index + '.value'">-->
<!--                <el-col :span="8">-->
<!--                  <el-input :size="configDict.size" :value="item.name" placeholder="变量名称"></el-input>-->
<!--                </el-col>-->
<!--                <el-col :span="4">-->
<!--                  <el-select :size="configDict.size" v-model="item.type" placeholder="请选择">-->
<!--                    <el-option key="1" label="string" value="string"/>-->
<!--                    <el-option key="2" label="int" value="int"/>-->
<!--                    <el-option key="3" label="file" value="file"/>-->
<!--                  </el-select>-->
<!--                </el-col>-->
<!--                <el-col :span="10">-->
<!--                  <el-input :size="configDict.size" :value="item.value" placeholder="值"></el-input>-->
<!--                </el-col>-->
<!--                <el-col :span="2">-->
<!--                  <el-button :size="configDict.size" icon="el-icon-delete" @click="removeGlobalVariable(item)"/>-->
<!--                </el-col>-->
<!--              </el-row>-->
<!--            </div>-->
<!--          </el-card>-->
<!--          <div v-if="result" style="margin-top: 20px">-->
<!--            <el-card>-->
<!--              <div slot="header">-->
<!--                <span class="color-gray"><i class="el-icon-chat-dot-square"> 输出结果信息</i></span>-->
<!--              </div>-->
<!--              <pre style="padding-left: 10px">{{ result }}</pre>-->
<!--            </el-card>-->
<!--          </div>-->
<!--        </div>-->
<!--      </el-col>-->
<!--      <el-col :span="8">-->
<!--        <exe-list @getExeResult="updateResult" :evn="this.formData.env" ref="exeRecordList"></exe-list>-->
<!--      </el-col>-->
<!--    </el-row>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--import rpcCascader from "@/views/custom/api/components/rpcCascader.vue";-->
<!--import exeRecordList from "@/views/custom/api/components/exeRecordList.vue";-->

<!--const defaultConfig = {-->
<!--  size: 'mini',-->
<!--  loading: false-->
<!--}-->

<!--export default {-->
<!--  components: {-->
<!--    'rpc-cas': rpcCascader,-->
<!--    'exe-list': exeRecordList-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      result: {-->
<!--        errorCode: 0,-->
<!--        responseData: {}-->
<!--      },-->
<!--      visible: false,-->
<!--      formData: {-->
<!--        env: 'http://api8.soyoung.com',-->
<!--        items: [],-->
<!--        params: '',-->
<!--      },-->
<!--      dynamicValidateForm: {-->
<!--        slaves: [-->
<!--          {-->
<!--            key: '',-->
<!--            value: ''-->
<!--          }-->
<!--        ],-->
<!--        globalVariables: [-->
<!--          {-->
<!--            name: '',-->
<!--            type: '',-->
<!--            value: ''-->
<!--          }-->
<!--        ],-->
<!--      },-->
<!--      evnOptions: [-->
<!--        {host: 'http://api.sy.soyoung.com', name: '测试环境'},-->
<!--        {host: 'http://api8.soyoung.com', name: '预发布环境'},-->
<!--        {host: 'http://api.soyoung.com', name: '生产环境'},-->
<!--      ],-->
<!--      configDict: Object.assign({}, defaultConfig),-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.updateSelectedItems()-->
<!--  },-->
<!--  methods: {-->
<!--    updateSelectedItems(node) {-->
<!--      if (!node) {-->
<!--        return-->
<!--      }-->
<!--      console.log(node)-->
<!--      let ids = node.path-->
<!--      let labels = node.pathLabels-->
<!--      let len = ids.length;-->
<!--      for (let i = 0; i < len; i++) {-->
<!--        let item = {};-->
<!--        item.id = ids[i];-->
<!--        item.item_name = labels[i];-->
<!--        this.formData.items.push(item);-->
<!--      }-->
<!--    },-->
<!--    updateResult(data) {-->
<!--      this.visible = true-->
<!--      this.result = data-->
<!--    },-->
<!--    submitForm() {-->
<!--      this.visible = true-->
<!--      if (this.formData.items.length > 1) {-->
<!--        this.result = this.$refs.exeRecordList.exeRpc(this.formData)-->
<!--      } else {-->
<!--        this.$message.error('请选择rpc服务及方法')-->
<!--      }-->
<!--    },-->
<!--    resetGlobalVariable() {-->
<!--      this.dynamicValidateForm.globalVariables = [-->
<!--          {-->
<!--            name: '',-->
<!--            type: '',-->
<!--            value: ''-->
<!--          }-->
<!--        ];-->
<!--    },-->
<!--    addGlobalVariable() {-->
<!--      this.dynamicValidateForm.globalVariables.push(-->
<!--        {-->
<!--          name: '',-->
<!--          type: '',-->
<!--          value: ''-->
<!--      });-->
<!--    },-->
<!--    removeGlobalVariable(item) {-->
<!--      let index = this.dynamicValidateForm.globalVariables.indexOf(item)-->
<!--      if (index !== -1) {-->
<!--        this.dynamicValidateForm.globalVariables.splice(index, 1)-->
<!--      }-->
<!--    },-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--.main-content {-->
<!--  padding-top: 20px;-->
<!--  padding-left: 20px;-->
<!--}-->

<!--.el-carousel__item h3 {-->
<!--  color: #475669;-->
<!--  font-size: 14px;-->
<!--  opacity: 0.75;-->
<!--  line-height: 150px;-->
<!--  margin: 0;-->
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
<!--  margin: 10px 0 10px 0;-->
<!--}-->
<!--</style>-->
