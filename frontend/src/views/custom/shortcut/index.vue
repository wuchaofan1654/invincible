<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-form ref="queryForm" :model="queryParams" :inline="true">-->
<!--      <el-form-item label="名称" prop="name">-->
<!--        <el-input-->
<!--          v-model="queryParams.name"-->
<!--          placeholder="请输入名称"-->
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
<!--      <el-form-item label="状态" prop="status">-->
<!--        <el-select-->
<!--          v-model="queryParams.status"-->
<!--          placeholder="请选择状态"-->
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
<!--      <el-form-item>-->
<!--        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>-->
<!--        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--    <el-row>-->
<!--      <el-col :span="6" v-if="shortcuts.length > 0" v-for="item in shortcuts">-->
<!--          <el-card class="demo-card" shadow="hover" body-style="padding: 0 5px">-->
<!--            <div slot="header">-->
<!--              <el-col :sm="22" class="name">-->
<!--                <i class="el-icon-video-play"></i>-->
<!--                {{ item.name }}-->
<!--              </el-col>-->
<!--              <el-col :sm="2">-->
<!--                <el-dropdown style="float: right">-->
<!--                <el-button type="text" icon="el-icon-more" style="margin-bottom: 5px"/>-->
<!--                <el-dropdown-menu slot="dropdown">-->
<!--                  <el-dropdown-item>-->
<!--                    <el-button type="text" icon="el-icon-edit" @click="editDialogVisible=true">编辑</el-button>-->
<!--                  </el-dropdown-item>-->
<!--                  <el-dropdown-item>-->
<!--                    <el-button type="text" icon="el-icon-video-play" @click="resultDialogVisible=true">执行</el-button>-->
<!--                  </el-dropdown-item>-->
<!--                </el-dropdown-menu>-->
<!--              </el-dropdown>-->
<!--              </el-col>-->
<!--            </div>-->
<!--            <el-link-->
<!--              :underline="false"-->
<!--              @click="$message.error('00000000')">-->
<!--              <span class="desc">{{ item.desc }}</span>-->
<!--            </el-link>-->
<!--          </el-card>-->
<!--      </el-col>-->
<!--    </el-row>-->
<!--    <el-dialog-->
<!--      :title="selected.name"-->
<!--      :visible="editDialogVisible">-->
<!--      <pre>{{ selected.shell }}</pre>-->
<!--      <span slot="footer">-->
<!--              <el-button @click="editDialogVisible=false">取消</el-button>-->
<!--              <el-button @click="resultDialogVisible=true">执行</el-button>-->
<!--            </span>-->
<!--    </el-dialog>-->
<!--    <el-dialog-->
<!--      :title="selected.name"-->
<!--      width="95%"-->
<!--      :visible="resultDialogVisible">-->
<!--      <result :content="shortcuts"></result>-->
<!--      <span slot="footer">-->
<!--              <el-button @click="resultDialogVisible=false">取消</el-button>-->
<!--              <el-button @click="">执行</el-button>-->
<!--            </span>-->
<!--    </el-dialog>-->
<!--    <pagination-->
<!--      v-show="total>0"-->
<!--      :total="total"-->
<!--      :page.sync="queryParams.pageNum"-->
<!--      :limit.sync="queryParams.pageSize"-->
<!--      @pagination="getResult"-->
<!--    />-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import {getExecuteResult} from "@/api/custom/shortcut/shortcut";-->
<!--import Result from "@/views/custom/shortcut/result.vue";-->

<!--export default {-->
<!--  name: "index",-->
<!--  components: {Result},-->
<!--  data() {-->
<!--    return {-->
<!--      editDialogVisible: false,-->
<!--      resultDialogVisible: false,-->
<!--      selected: {},-->
<!--      queryParams: {},-->
<!--      total: 1,-->
<!--      shortcuts: [-->
<!--        {-->
<!--          name: '功能1功能1功能1功能1功能1功能1功能1功能1功能1功能1',-->
<!--          desc: '功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍',-->
<!--          shell: "9999"-->
<!--        },-->
<!--        {name: '功能1', desc: '功能1介绍', shell: "9999"},-->
<!--        {name: '功能1', desc: '功能1介绍', shell: "9999"},-->
<!--        {-->
<!--          name: '功能1',-->
<!--          desc: '功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍功能1介绍',-->
<!--          shell: "9999"-->
<!--        },-->
<!--        {name: '功能1', desc: '功能1介绍', shell: "9999"},-->
<!--        {name: '功能1', desc: '功能1介绍', shell: "9999"},-->
<!--      ]-->
<!--    }-->
<!--  },-->
<!--  created() {-->
<!--    this.getResult()-->
<!--  },-->
<!--  methods: {-->
<!--    handleQuery() {-->

<!--    },-->
<!--    getResult() {-->
<!--      getExecuteResult().then(res => {-->
<!--        this.content = res.data-->
<!--      })-->
<!--    },-->
<!--  },-->
<!--}-->
<!--</script>-->
<!--<style lang="scss" scoped>-->
<!--.app-container {-->
<!--  margin: 5px;-->

<!--  p {-->
<!--    font-size: 18px;-->
<!--    color: #606266;-->
<!--  }-->

<!--  .demo-card {-->
<!--    margin: 2px;-->

<!--    .name {-->
<!--      font-size: 16px;-->
<!--      color: #409EFF;-->
<!--      overflow: hidden;-->
<!--      display: -webkit-box;-->
<!--      -webkit-box-orient: vertical;-->
<!--      -webkit-line-clamp: 1;-->
<!--    }-->

<!--    .desc {-->
<!--      font-size: 12px;-->
<!--      overflow: hidden;-->
<!--      display: -webkit-box;-->
<!--      -webkit-box-orient: vertical;-->
<!--      -webkit-line-clamp: 2;-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</style>-->
