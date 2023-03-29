<template>
  <div class="app-container">
    <el-form
      ref="queryForm"
      :inline="true"
      style="float: right"
      label-width="68px"
    >

      <el-form-item>
        <el-input
          v-model="alertParam.num"
          placeholder="发送小于该值类名～"
          size="mini"
          clearable
        />
      </el-form-item>

      <el-form-item>
        <el-input
          v-model="alertParam.content"
          placeholder="填写报警内容～"
          size="mini"
          clearable
        />
      </el-form-item>

      <el-form-item label="" prop="">
       <el-button
          size="mini"
          type="primary"
          @click="sendshu">
          发送飞书
        </el-button>
      </el-form-item>
      </el-form>
      <el-form
      :inline="true"
      :model="formData"
      >
        <el-form-item >
          <el-select v-model="formData.white" placeholder="是否白名单"  size="mini" clearable="">
            <el-option
              v-for="item in formData.is_white"
              :key="item.value"
              :label="item.label"
              :value="item.value"
              >
            </el-option>
          </el-select>
        </el-form-item>
      <el-form-item>
        <el-input
          v-model="formData.names"
          placeholder="仅支持单个名称搜索"
          size="mini"
          clearable
        />
      </el-form-item>
      <el-form-item  prop="">
       <el-button
          size="mini"
          type="primary"
          @click="search">
          搜索
        </el-button>
      </el-form-item>
      </el-form>
      <el-form
      :inline="true"
      style="float: right"
      >
      <el-form-item  prop="version">
       <el-button
          size="mini"
          type="primary"
          @click="uploadVC.visible = true">
          上传类名文件
        </el-button>
      </el-form-item>

       <el-form-item label="" prop="version">
       <el-button
          size="mini"
          type="primary"
          @click="uploadPoint.visible = true">
          上传埋点文件
        </el-button>
      </el-form-item>

    </el-form>
    <el-table
      v-loading="loading"
      :data="vclist">
      <el-table-column type="selection" width="45" align="center"/>

      <el-table-column label="VC_Name"
        align="center"
        sortable :show-overflow-tooltip="true"
        prop="VCname"
        >
      </el-table-column>
       <el-table-column label="点击量" align="center" sortable :show-overflow-tooltip="true" prop="points">
        <!-- <template v-slot="scope">
          <span>{{ scope.row.resource_size }}</span>
        </template>  -->
       </el-table-column>
      <el-table-column label="备注" align="center" sortable :show-overflow-tooltip="true" prop="reason">
        <!-- <template v-slot="scope">
          <span>{{ scope.row.code_size }}</span>
        </template> -->
      </el-table-column>
      <!-- <el-table-column label="版本号" align="center" sortable :show-overflow-tooltip="true" prop="version">
        <template v-slot="scope">
          <span>{{ scope.row.code_size }}</span>
        </template> -->
      <!-- </el-table-column> -->
      <el-table-column label="是否加入白名单" align="center" :show-overflow-tooltip="true">
        <template v-slot="scope">
          <el-button @click="dialogVisible = true; handleClick(scope.row)"  type="text" size="small">添加</el-button>
          <el-button @click="delWhite(scope.row)" type="text" size="small">删除</el-button>
        </template>

      </el-table-column>
    </el-table>
    <!-- 添加白名单 -->
    <el-dialog
      title="填写添加理由"
      :visible.sync="dialogVisible"
      width="30%"
      >
      <el-form :model="whiteReason" label-width="80px" :rules="rules">
          <el-form-item label="备注" prop="reason">
              <el-input v-model="whiteReason.reason" clearable/>
          </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false; addReason() ">确 定</el-button>
      </span>
     </el-dialog>
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />
    <el-dialog
      :title="uploadVC.title"
      :visible.sync="uploadVC.visible"
      width="500px"
      append-to-body>
      <el-form :model="VClistForm" label-width="80px" :rules="rules">
        <el-form-item label="JSON文件" prop="filepath">
          <FileUpload :file-type="['json']" @input="getVClistUrl"/>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="uploadVC.visible = false">取 消</el-button>
        <el-button type="primary" @click="submitVClist">确 定</el-button>
      </span>
    </el-dialog>

  <!-- 上传埋点记录弹窗 -->
    <el-dialog
      :title="uploadPoint.title"
      :visible.sync="uploadPoint.visible"
      width="500px"
      append-to-body>
      <span>请先确认已经上传最新的类名文件，否则可能会导致结果不准确</span>
      <el-form :model="VCpointList" label-width="80px" :rules="rules">
        <el-form-item label="CSV文件" prop="filepath">
          <FileUpload :file-type="['csv']" @input="getPointtUrl"/>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="uploadPoint.visible = false">取 消</el-button>
        <el-button type="primary" @click="submitPoint">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { listVc, addWhite, delWhite, addVClist, addPoints, sendFeishu  } from "@/api/custom/performance/vclist"
import { getVersionList  } from "@/api/custom/performance/publish"
import FileUpload from "@/components/FileUpload/index.vue"



export default {
  name: "vclist",
    components: { FileUpload },

  data() {
    return {
      formData:{
         versions:"",
        is_white: [{
          value: '0',
          label: '否'
        }, {
          value: '1',
          label: '是'
        }],
        time:"",
        white: "",
        ver: "",
        names:"",
        // pickerOptions: {
        //   disabledDate(time) {
        //     return time.getTime() > Date.now();
        //   },
        //   shortcuts: [{
        //     text: '7天前',
        //     onClick(picker) {
        //       const date = new Date();
        //       date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
        //       picker.$emit('pick', date);
        //     }
        //   },
        //   {
        //     text: '14天前',
        //     onClick(picker) {
        //       const date = new Date();
        //       date.setTime(date.getTime() - 3600 * 1000 * 24 * 14);
        //       picker.$emit('pick', date);
        //     }
        //   },
        //   {
        //     text: '30天前',
        //     onClick(picker) {
        //       const date = new Date();
        //       date.setTime(date.getTime() - 3600 * 1000 * 24 * 30);
        //       picker.$emit('pick', date);
        //     }
        //   },
        //   ]
        // },
      },
      total: 0,
      loading: false,
      moduleNameOptions: [],
      queryParams: {
        pageNum: 1,
        pageSize: 20,
        module_name: "",
        names: "",
        mobiles: "1",
        is_white: "",
        is_hand:'0'
      },
      dialogVisible: false,
      vclist:[],
      whiteReason:{
        vcname:"",
        reason: ""
      },
      rules: {
        reason:[
          {required:true}
          ]
      },
      uploadVC: {
        title: "手动上传VClist记录",
        visible: false
      },
      uploadPoint: {
        title: "手动上传VC埋点记录",
        visible: false
      },
      VClistForm: {
        is_hand:'0',
        mobiles: '1'
      },
      VCpointList: {
        mobiles: '1'

      },
      alertParam: {
        is_hand:'0',
        mobiles: '1'
      }
    };

  },
  watch: {},
  created() {
    this.getList();
    // this.getVersion();
  },
  methods: {
    getStatus(value) {
      return value > 0 ? "danger" : "success";
    },
    getList() {
      this.loading = true;
      console.log(this.queryParams);
      listVc(this.queryParams).then(res => {
        this.loading = false;
        if (res.code === 200) {
          console.log(res)
          this.vclist = res.data.results;
          this.total = res.data.count;
        } else {
          this.modules = [];
          this.$message.error("接口数据异常，请稍后再试～");
        }
      });
    },
    getVersion() {
      // console.log(this.queryParams.is_white, this.queryParams.versions)

      getVersionList().then(res => {
        this.loading = false;
        if (res.code === 200) {
          this.formData.versions = res.data;
          console.log(this.formData.versions);
        } else {
          this.$message.error("接口数据异常，请稍后再试～");
        }
      });
    },
    sendshu() {
      console.log(this.alertParam)
      sendFeishu(this.alertParam).then(res => {
        this.loading = false;
        if (res.code === 200) {
          // console.log(res)
          // this.vclist = res.data.results;
          this.$message("发送成功")

        } else if(res.code === 10003) {
          this.$message.error(res.msg);
        }
      })
    },

    addReason() {
      addWhite(this.whiteReason).then(res => {
        this.loading = false;
        console.log(this.whiteReason)
        if (res.code === 200) {
          // console.log(res)
          // this.vclist = res.data.results;
          this.getList()
        } else {
          this.$message.error("接口数据异常，请稍后再试～");
        }
      });
    },
    handleClick(row) {
      this.whiteReason.vcname = row.VCname
    },
    delWhite(row) {
      const data = {vcname: row.VCname}
      delWhite(data).then(res => {
        this.loading = false
        if (res.code==200) {
          console.log(res)
          this.$message("删除成功")
          this.getList()

        } else {
          this.$message.error("接口数据异常，请稍后再试～");
        }
      })
    },
    search() {
      this.queryParams.is_white = this.formData.white
      this.queryParams.names = this.formData.names

      console.log(this.queryParams)
      listVc(this.queryParams).then(res => {
        this.loading = false;
        if (res.code === 200) {
          console.log(res)
          this.vclist = res.data.results;
          this.total = res.data.count;
        } else {
          this.modules = [];
          this.$message.error("接口数据异常，请稍后再试～");
        }
      });
    },

    upoadVCname() {

    },
    getVClistUrl(fileUrl) {
      this.VClistForm.filepath = fileUrl;
      console.log(this.VClistForm.filepath)
    },

    getPointtUrl(fileUrl) {
      this.VCpointList.filepath = fileUrl;
    },

    showExtend() {
      this.dialogVisible = true;
    },
    // 添加VCname
    submitVClist(){
      console.log(this.VClistForm)
      addVClist(this.VClistForm).then((res) => {
        if (res.code === 200) {
          this.$message.success("导入成功～");
          this.uploadVC.visible = false;
          this.getList();
        } else {
          this.$message.error(res.msg);
        }
      });
    },
    // 添加point
    submitPoint() {
      addPoints(this.VCpointList).then((res) => {
        if (res.code === 200) {
          this.$message.success("导入成功～");
          this.uploadPoint.visible = false;
          this.getList();
        } else {
          this.$message.error(res.msg);
        }
      });
    }

  }
};
</script>

<style scoped>
</style>
