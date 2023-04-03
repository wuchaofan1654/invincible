<!--<template>-->
<!--  <el-row>-->
<!--    <div style="float: right">-->
<!--      <el-button-->
<!--      type="text"-->
<!--      size="mini"-->
<!--      icon="el-icon-refresh"-->
<!--      @click="formatYn = !formatYn">-->
<!--      切换样式-->
<!--    </el-button>-->
<!--    <el-divider direction="vertical"></el-divider>-->
<!--    <el-button-->
<!--      v-if="realtimeData.errors.length > 0 || realtimeData.warnings.length > 0"-->
<!--      size="mini"-->
<!--      type="text"-->
<!--      icon="el-icon-upload"-->
<!--      @click="update"-->
<!--    >同步</el-button>-->
<!--  </div>-->
<!--    <el-col :span="12">-->
<!--      <json-viewer-->
<!--        :value="formatData(realtimeData)"-->
<!--        :expand-depth="5"-->
<!--        copyable-->
<!--        sort/>-->
<!--    </el-col>-->
<!--    <el-col :span="12">-->
<!--      <json-viewer-->
<!--        v-loading="loading"-->
<!--        :value="formatData(standerData)"-->
<!--        :expand-depth="5"-->
<!--        copyable-->
<!--        sort/>-->
<!--    </el-col>-->
<!--  </el-row>-->
<!--</template>-->

<!--<script>-->
<!--import JsonViewer from "vue-json-viewer";-->
<!--import { getPointByUniqueName } from "@/api/custom/point/point";-->
<!--import { updatePoint } from "@/api/custom/point/point";-->

<!--export default {-->
<!--  name: "viewPoint",-->
<!--  components: { JsonViewer },-->
<!--  props: {-->
<!--    realtimeData: {type: Object, default: () => ({})},-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      loading: false,-->
<!--      formatYn: true,-->
<!--      standerData: {}-->
<!--    }-->
<!--  },-->
<!--  created() {-->
<!--    this.getPoint()-->
<!--  },-->
<!--  watch:{-->
<!--    'realtimeData'(){-->
<!--      this.getPoint()-->
<!--    },-->
<!--  },-->
<!--  methods: {-->
<!--    getPoint() {-->
<!--      this.loading = true-->
<!--      getPointByUniqueName(this.realtimeData.unique_name).then(res => {-->
<!--        this.loading = false-->
<!--        this.standerData = res.data ? res.data : {}-->
<!--      })-->
<!--    },-->
<!--    update() {-->
<!--      updatePoint(this.realtimeData).then(res => {-->
<!--        this.$message.info(res.msg)-->
<!--      })-->
<!--    },-->
<!--    formatData(data) {-->
<!--      return this.formatYn ? {-->
<!--        type: data.type ? data.type : data.point_type,-->
<!--        from_page: data.from_page,-->
<!--        curr_page: data.curr_page,-->
<!--        curr_page_ext: data.curr_page_ext,-->
<!--        from_action: data.from_action,-->
<!--        from_action_ext: data.from_action_ext-->
<!--      } : data-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->

<!--</style>-->
