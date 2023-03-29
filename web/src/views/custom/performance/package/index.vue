<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-form-->
<!--      ref="queryForm"-->
<!--      :model="queryParams"-->
<!--      :inline="true"-->
<!--      style="float: right"-->
<!--      label-width="68px"-->
<!--    >-->
<!--      <el-form-item>-->
<!--        <el-select-->
<!--          size="mini"-->
<!--          v-model="queryParams.mobiles"-->
<!--          @change="getList"-->
<!--          placeholder="请选择">-->
<!--          <el-option key="0" label="全部" value=""/>-->
<!--          <el-option key="1" label="iOS" value="1"/>-->
<!--          <el-option key="2" label="Android" value="2"/>-->
<!--        </el-select>-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-input-->
<!--          v-model="queryParams.version"-->
<!--          placeholder="支持输入版本号过滤～"-->
<!--          size="mini"-->
<!--          clearable-->
<!--          @keyup.enter.native="getList"-->
<!--        />-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button size="mini" type="primary" @click="compare">开始对比</el-button>-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button size="mini" type="primary" @click="upload.visible = true">上传</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--    <el-table-->
<!--      v-loading="loading"-->
<!--      ref="multipleTable"-->

<!--      @selection-change="onSelectChange"-->
<!--      :data="publishes"-->
<!--    >-->
<!--      <el-table-column type="selection" width="55" align="center"/>-->
<!--      <el-table-column-->
<!--        label="机型"-->
<!--        align="center"-->
<!--        prop="mobiles"-->
<!--        sortable-->
<!--        :show-overflow-tooltip="true">-->
<!--        <template v-slot="scope">-->
<!--          <el-tag size="mini">{{ scope.row.mobiles }}</el-tag>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        label="版本号"-->
<!--        align="center"-->
<!--        prop="version"-->
<!--        sortable-->
<!--        :show-overflow-tooltip="true"-->
<!--      >-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        label="build编号"-->
<!--        align="center"-->
<!--        sortable-->
<!--        prop="build_no"-->
<!--        :show-overflow-tooltip="true"-->
<!--      >-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        label="分支名"-->
<!--        align="center"-->
<!--        sortable-->
<!--        prop="branch"-->
<!--        :show-overflow-tooltip="true"-->
<!--      >-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        label="创建时间"-->
<!--        align="center"-->
<!--        :show-overflow-tooltip="true"-->
<!--      >-->
<!--        <template v-slot="scope">-->
<!--          <span size="mini" style="color: #606266; font-size: 12px">-->
<!--            <i class="el-icon-time"/>-->
<!--            {{ scope.row.create_datetime }}</span-->
<!--          >-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-table-column-->
<!--        label="操作"-->
<!--        align="center"-->
<!--        :show-overflow-tooltip="true">-->
<!--        <template v-slot="scope">-->
<!--          <el-button-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-delete"-->
<!--            @click="deletePub(scope.row)">-->
<!--            删除-->
<!--          </el-button>-->
<!--          <el-button-->
<!--            size="mini"-->
<!--            type="text"-->
<!--            icon="el-icon-download"-->

<!--            @click="downloadJsonfile(scope.row)">-->
<!--            下载json-->
<!--          </el-button>-->
<!--        </template>-->
<!--      </el-table-column>-->
<!--      <el-form-item>-->
<!--      </el-form-item>-->
<!--    </el-table>-->
<!--    <pagination-->
<!--      v-show="total > 0"-->
<!--      :total="total"-->
<!--      :page.sync="queryParams.pageNum"-->
<!--      :limit.sync="queryParams.pageSize"-->
<!--      @pagination="getList"-->
<!--    />-->
<!--    <el-dialog-->
<!--      :title="upload.title"-->
<!--      :visible.sync="upload.visible"-->
<!--      width="500px"-->
<!--      append-to-body>-->
<!--      <el-form :model="form" label-width="80px" :rules="rules">-->
<!--        <el-form-item label="版本号" prop="version">-->
<!--          <el-input v-model="form.version" clearable/>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="build号" prop="build_no">-->
<!--          <el-input v-model="form.build_no" clearable/>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="构建分支" prop="branch">-->
<!--          <el-input v-model="form.branch" clearable/>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="终端" prop="mobiles">-->
<!--          <el-radio v-model="form.mobiles" label="1">iOS</el-radio>-->
<!--          <el-radio v-model="form.mobiles" label="2">Android</el-radio>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="json文件" prop="filepath">-->
<!--          <FileUpload :file-type="['json']" @input="getFileUrl"/>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--      <span slot="footer" class="dialog-footer">-->
<!--        <el-button @click="upload.visible = false">取 消</el-button>-->
<!--        <el-button type="primary" @click="submitAddPublish">确 定</el-button>-->
<!--      </span>-->
<!--    </el-dialog>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { listPublish, addPublish, deletePublish, download_json_file } from "@/api/custom/performance/publish";-->
<!--import FileUpload from "@/components/FileUpload/index.vue";-->

<!--export default {-->
<!--  name: "Index",-->
<!--  components: { FileUpload },-->
<!--  data() {-->
<!--    return {-->
<!--      showSearch: true,-->
<!--      versionOptions: [],-->
<!--      selectList: [],-->
<!--      publishes: [],-->
<!--      loading: false,-->
<!--      total: 0,-->
<!--      filterText: "",-->
<!--      upload: {-->
<!--        title: "手动上传发布记录",-->
<!--        visible: false-->
<!--      },-->
<!--      queryParams: {-->
<!--        // status: 1,-->
<!--        pageNum: 1,-->
<!--        pageSize: 20,-->
<!--        version: "",-->
<!--        mobiles: ""-->
<!--      },-->
<!--      form: {-->
<!--        mobiles: "1"-->
<!--      },-->
<!--      rules: {-->
<!--        version: [-->
<!--          { required: true, message: "版本号不能为空", trigger: "blur" }-->
<!--        ],-->
<!--        build_no: [-->
<!--          { required: true, message: "build号不能为空", trigger: "blur" }-->
<!--        ],-->
<!--        branch: [-->
<!--          { required: true, message: "打包分支不能为空", trigger: "blur" }-->
<!--        ],-->
<!--        filepath: [-->
<!--          { required: true, message: "module文件不能为空", trigger: "blur" }-->
<!--        ]-->
<!--      }-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getList();-->
<!--  },-->
<!--  methods: {-->
<!--    getList() {-->
<!--      this.loading = true;-->
<!--      this.seleted = [];-->
<!--      listPublish(this.queryParams).then((res) => {-->
<!--        this.loading = false;-->
<!--        if (res.code === 200) {-->
<!--          this.publishes = res.data.results;-->
<!--        } else {-->
<!--          this.publishes = [];-->
<!--          this.$message.error("接口数据异常，请稍后再试～");-->
<!--        }-->
<!--      });-->
<!--    },-->
<!--    VClist(row) {-->
<!--      this.$router.push({-->
<!--        path: "vclist"-->
<!--      });-->
<!--      console.log(row);-->
<!--    },-->
<!--    compare() {-->
<!--      if (this.selectList.length !== 2) {-->
<!--        this.$message.error("请选择2条记录进行对比~");-->
<!--        return;-->
<!--      }-->
<!--      this.$router.push({-->
<!--        path: "compare",-->
<!--        query: { pk1: this.selectList[0]["id"], pk2: this.selectList[1]["id"] }-->
<!--      });-->
<!--    },-->
<!--    onSelectAll() {-->
<!--      this.$message.error("暂时只支持2条记录对比，不支持全选功能～");-->
<!--      this.$refs.multipleTable.clearSelection();-->
<!--    },-->
<!--    onSelectChange(rows) {-->
<!--      if (rows.length > 2) {-->
<!--        this.$refs.multipleTable.toggleRowSelection(rows[0], false);-->
<!--        rows.splice(0, 1); // 同时要把选中第一项移除-->
<!--      }-->
<!--      this.selectList = rows;-->
<!--    },-->
<!--    submitAddPublish() {-->
<!--      addPublish(this.form).then((res) => {-->
<!--        if (res.code === 200) {-->
<!--          this.$message.success("导入成功～");-->
<!--          this.upload.visible = false;-->
<!--          this.getList();-->
<!--        } else {-->
<!--          this.$message.error(res.msg);-->
<!--        }-->
<!--      });-->
<!--    },-->
<!--    getJumpUrl(version) {-->
<!--      return this.$router.push({ path: "module", query: { version: version }});-->
<!--    },-->
<!--    getFileUrl(fileUrl) {-->
<!--      this.form.filepath = fileUrl;-->
<!--    },-->
<!--    downloadJsonfile(row) {-->
<!--      // window.open(row.filepath)-->
<!--      const params = { filepath: row.filepath };-->
<!--      download_json_file(params).then((res) => {-->


<!--        const link = document.createElement("a");-->
<!--        const blob = new Blob([res], { type: "text/json" }); // 生成blob对象-->
<!--        const filename = row.version + "版本" + row.build_no + "build";-->
<!--        let objectUrl = URL.createObjectURL(blob);-->
<!--        // console.log(blob);-->
<!--        link.style.display = "none";-->
<!--        link.href = objectUrl;-->
<!--        link.setAttribute("download", filename + ".json"); // 下载的文件名以及文件格式-->
<!--        document.body.appendChild(link);-->
<!--        link.click();-->
<!--        document.body.removeChild(link);-->
<!--        URL.revokeObjectURL(blob)-->
<!--      });-->
<!--    },-->
<!--    deletePub(row) {-->
<!--      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {-->
<!--        confirmButtonText: "确定",-->
<!--        cancelButtonText: "取消",-->
<!--        type: "warning"-->
<!--      }).then(() => {-->
<!--        deletePublish(row.id).then(res => {-->
<!--          if (res.code === 200) {-->
<!--            this.$message.success("删除成功～");-->
<!--            this.getList();-->
<!--          } else {-->
<!--            this.$message.error("删除失败～");-->
<!--          }-->
<!--          console.log("yes");-->
<!--        });-->
<!--      }).catch(() => {-->
<!--        this.$message({-->
<!--          type: "info",-->
<!--          message: "已取消删除"-->
<!--        });-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--};-->

<!--</script>-->

<!--<style scoped></style>-->
