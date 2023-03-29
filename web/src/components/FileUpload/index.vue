<template>
  <div class="upload-file">
    <el-upload
      ref="upload"
      :action="uploadFileUrl"
      :before-upload="handleBeforeUpload"
      :file-list="fileList"
      :limit="limit"
      :multiple="multiple"
      :on-error="handleUploadError"
      :on-exceed="handleExceed"
      :on-success="handleUploadSuccess"
      :show-file-list="show_file_list"
      :headers="headers"
      class="upload-file-uploader"
    >
      <el-button size="mini" type="primary">选取文件</el-button>
      <span v-if="showTip" slot="tip" class="el-upload__tip">
        请上传
        <template v-if="fileSize"> 大小不超过 <b style="color: #f56c6c">{{ fileSize }}MB</b> </template>
        <template v-if="fileType"> 格式为 <b style="color: #f56c6c">{{ fileType.join("/") }}</b> </template>
        的文件
      </span>
    </el-upload>

    <transition-group class="upload-file-list el-upload-list el-upload-list--text" name="el-fade-in-linear" tag="ul">
      <li v-for="(file, index) in list" :key="file.uid" class="el-upload-list__item ele-upload-list__item-content">
        <el-link :href="file.url" :underline="false" target="_blank">
          <span class="el-icon-document"> {{ getFileName(file.name) }} </span>
        </el-link>
        <div class="ele-upload-list__item-content-action">
          <el-link :underline="false" type="danger" @click="handleDelete(index)">删除</el-link>
        </div>
      </li>
    </transition-group>
  </div>
</template>

<script>
import { getToken } from "@/utils/auth";

export default {
  name: "FileUpload",
  props: {
    value: [String, Object, Array],
    fileSize: {
      type: Number,
      default: 5
    },
    fileType: {
      type: Array,
      default: () => ["json", "txt", "xls", "hav", "pdf", "csv"]
    },
    isShowTip: {
      type: Boolean,
      default: true
    },
    limit: {
      type: Number,
      default: 1
    },
    multiple: {
      type: Boolean,
      default: false
    },
    show_file_list: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      uploadFileUrl: process.env.VUE_APP_BASE_API + "/system/save_file/", // 上传的图片服务器地址
      headers: {
        Authorization: "Bearer " + getToken()
      },
      fileList: []
    };
  },
  computed: {
    // 是否显示提示
    showTip() {
      return this.isShowTip && (this.fileType || this.fileSize);
    },
    // 列表
    list() {
      let temp = 1;
      if (this.value) {
        // 首先将值转为数组
        const list = Array.isArray(this.value) ? this.value : [this.value];
        // 然后将数组转为对象数组
        return list.map((item) => {
          if (typeof item === "string") {
            item = { name: item, url: item };
          }
          item.uid = item.uid || new Date().getTime() + temp++;
          return item;
        });
      } else {
        this.fileList = [];
        return [];
      }
    }
  },
  created() {
    this.fileList = this.list;
  },
  methods: {
    // 上传前校检格式和大小
    handleBeforeUpload(file) {
      // 校检文件类型
      if (this.fileType && this.fileType[0] !== "ALL") {
        console.log(this.fileType);
        let fileExtension = "";
        if (file.name.lastIndexOf(".") > -1) {
          fileExtension = file.name.slice(file.name.lastIndexOf(".") + 1);
          console.log(fileExtension);
        }
        const isTypeOk = this.fileType.some((type) => {
          if (file.type.indexOf(type) > -1) {
                      console.log(file.type)
                      return true;
          }

          console.log(fileExtension && fileExtension.indexOf(type) > -1);
          return !!(fileExtension && fileExtension.indexOf(type) > -1);

        });
        if (!isTypeOk) {
          this.$message.error(`文件格式不正确, 请上传${ this.fileType.join("/") }格式文件!`);
          return false;
        }
      }

      // 校检文件大小
      if (this.fileSize) {
        const isLt = file.size / 1024 / 1024 < this.fileSize;
        if (!isLt) {
          this.$message.error(`上传文件大小不能超过 ${ this.fileSize } MB!`);
          return false;
        }
      }
      return true;
    },
    // 文件个数超出
    handleExceed() {
      this.$message.error('只允许上传' + this.limit + '个文件');
    },
    // 上传失败
    handleUploadError() {
      this.$message.error("上传失败, 请重试");
    },
    // 上传成功回调
    handleUploadSuccess(res, file) {
      if (res.code === 200) {
        this.$message.success("上传成功");
        this.$emit("input", res.data.file);
      } else {
        this.$message.error(res.msg);
      }
    },
    // 删除文件
    handleDelete(index) {
      this.fileList.splice(index, 1);
      this.$emit("input", "");
    },
    // 获取文件名称
    getFileName(name) {
      if (name.lastIndexOf("/") > -1) {
        return name.slice(name.lastIndexOf("/") + 1).toLowerCase();
      } else {
        return "";
      }
    }
  }
};
</script>

<style scoped lang="scss">
.upload-file-uploader {
  margin-bottom: 5px;
}
.upload-file-list .el-upload-list__item {
  border: 1px solid #e4e7ed;
  line-height: 2;
  margin-bottom: 10px;
  position: relative;
}
.upload-file-list .ele-upload-list__item-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: inherit;
}
.ele-upload-list__item-content-action .el-link {
  margin-right: 10px;
}
</style>
