<!--<template>-->
<!--  <el-container class="class-main-container">-->
<!--    <el-aside class="class-left-side">-->
<!--      <div class="class-left-side-filter">-->
<!--        <el-input-->
<!--          prefix-icon="el-icon-search"-->
<!--          placeholder="输入埋点名过滤~"-->
<!--          @change="filterPoints"-->
<!--          clearable-->
<!--          size="mini"-->
<!--          v-model="filterText">-->
<!--          <el-button slot="append" icon="el-icon-delete" @click="resetPoints"></el-button>-->
<!--        </el-input>-->
<!--      </div>-->
<!--        <div v-for="point in filteredPoints">-->
<!--          <el-link-->
<!--            :underline="false"-->
<!--            :type="point.errors.length > 0 ? 'danger': point.warnings.length ? 'warning': 'success'"-->
<!--            @click="selectedPoint=point">-->
<!--            <div class="left-side-point-title">-->
<!--              <i class="el-icon-document" v-if="parseInt(point.type)===2"></i>-->
<!--              <i class="el-icon-thumb" v-else></i>-->
<!--              <span>{{ point.en_name }}</span>-->
<!--            </div>-->
<!--          </el-link>-->
<!--        </div>-->
<!--    </el-aside>-->
<!--    <el-main class="class-right-side">-->
<!--      <div style="float: right; position: sticky; z-index: 2">-->
<!--        <el-select-->
<!--          size="mini"-->
<!--          v-model="filterType"-->
<!--          prefix-icon="el-icon-list"-->
<!--          style="width: 180px; margin-right: 20px"-->
<!--          @change="filterPoints"-->
<!--          clearable-->
<!--          :value="filterType">-->
<!--          <el-option-->
<!--            v-for="item in pointTypeOptions"-->
<!--            :key="item.dictLabel"-->
<!--            :label="item.dictLabel"-->
<!--            :value="item.dictValue"-->
<!--          />-->
<!--        </el-select>-->
<!--        <el-input-->
<!--          size="mini"-->
<!--          placeholder="请输入device_id~"-->
<!--          prefix-icon="el-icon-edit"-->
<!--          style="width: 180px; margin-right: 20px"-->
<!--          clearable-->
<!--          v-model="deviceId"-->
<!--        />-->
<!--        <el-button-->
<!--          size="mini"-->
<!--          :type='socketYn ? "danger": "success"'-->
<!--          icon="el-icon-video-camera-solid"-->
<!--          @click="deviceId ? socketYn = !socketYn : $message.error('请先输入device_id～')">-->
<!--          {{socketYn ? "结束录制": "开始录制"}}-->
<!--        </el-button>-->
<!--        <el-button-->
<!--          plain-->
<!--          size="mini"-->
<!--          type="text"-->
<!--          icon="el-icon-question"-->
<!--          @click="$notify({-->
<!--            title: '操作方法',-->
<!--            message: '1. 手机端配置代理，ip: 10.10.20.84  port: 9999; 访问mitm.it安装证书' +-->
<!--                     '2. 当前页面输入device_id再开始录制'-->
<!--            }-->
<!--          )"/>-->
<!--      </div>-->
<!--      <el-tabs v-model="activeName" type="card" @tab-click="">-->
<!--        <el-tab-pane label="实时/标准埋点" name="first">-->
<!--          <el-tag-->
<!--            class="check-result-tag"-->
<!--            size="mini"-->
<!--            v-for="error in selectedPoint.errors"-->
<!--            type="danger">-->
<!--            {{error}}-->
<!--          </el-tag>-->
<!--          <el-tag-->
<!--            class="check-result-tag"-->
<!--            size="mini"-->
<!--            v-for="warning in selectedPoint.warnings"-->
<!--            type="warning">-->
<!--            {{warning}}-->
<!--          </el-tag>-->
<!--          <view-point v-if="selectedPoint.type" :realtime-data="selectedPoint" />-->
<!--        </el-tab-pane>-->
<!--        <el-tab-pane label="检查记录" name="third">-->
<!--          <check-history :unique_name="selectedPoint.unique_name"></check-history>-->
<!--        </el-tab-pane>-->
<!--      </el-tabs>-->
<!--    </el-main>-->
<!--  </el-container>-->
<!--</template>-->

<!--<script>-->
<!--import CheckHistory from "@/views/custom/point/components/checkHistory.vue";-->
<!--import ViewPoint from "@/views/custom/point/components/compareView.vue";-->

<!--export default {-->
<!--  components: {-->
<!--    ViewPoint, CheckHistory-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      loading: false,-->
<!--      activeName: "first",-->
<!--      deviceId: "1977",-->
<!--      filterText: "",-->
<!--      filterType: "0",-->
<!--      points: [],-->
<!--      filteredPoints: [],-->
<!--      selectedPoint: {},-->
<!--      socketYn: false,-->
<!--      pointTypeOptions: [],-->
<!--      pointLimit: 200-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getDicts("point_type_options").then(response => {-->
<!--      this.pointTypeOptions = response.data;-->
<!--    });-->
<!--  },-->
<!--  watch: {-->
<!--    "socketYn": {-->
<!--      handler(val) { val ? this.initWebSocket() : this.closeWebsocket(); }-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    initWebSocket() {-->
<!--      const wsUri = process.env.VUE_APP_BASE_WS_API + "/ws/point/catch/" + this.deviceId + "/";-->
<!--      this.websocket = new WebSocket(wsUri);-->
<!--      this.websocket.onmessage = this.websocketOnMessage;-->
<!--      this.websocket.onerror = this.closeWebsocket;-->
<!--      this.websocket.onclose = this.closeWebsocket;-->
<!--    },-->

<!--    closeWebsocket() {-->
<!--      this.socketYn = false;-->
<!--      this.websocket.close();-->
<!--    },-->

<!--    websocketOnMessage(e) {-->
<!--      const point = JSON.parse(e.data).message;-->
<!--      if (this.points.length > this.pointLimit) {-->
<!--        this.points = this.points.slice(1, this.pointLimit);-->
<!--      }-->
<!--      this.points.unshift(point);-->
<!--      this.isPointFilterable(point) ? this.filteredPoints.unshift(point) : null;-->
<!--    },-->

<!--    isPointFilterable(point) {-->
<!--      if (point.en_name.indexOf(this.filterText) === -1) {-->
<!--        return false;-->
<!--      }-->
<!--      if (this.filterType === "0") {-->
<!--        return true;-->
<!--      }-->
<!--      return point.type.toString() === this.filterType;-->
<!--    },-->

<!--    filterPoints() {-->
<!--      this.filteredPoints = this.points.filter(-->
<!--        point => { this.isPointFilterable(point); }-->
<!--      );-->
<!--    },-->
<!--    resetPoints() {-->
<!--      this.selectedPoint = {};-->
<!--      this.filteredPoints = [];-->
<!--      this.points = [];-->
<!--    },-->
<!--  },-->
<!--  destroyed() {-->
<!--    console.log("destroyed");-->
<!--    this.websocket ? this.closeWebsocket() : null-->
<!--  }-->
<!--};-->
<!--</script>-->
<!--<style v-slot="scope">-->

<!--.class-main-container {-->
<!--  margin: 10px;-->
<!--  position: absolute;-->
<!--  width: 100%;-->
<!--  height: calc(100% - 0px);-->
<!--}-->

<!--.class-left-side {-->
<!--  padding: 0;-->
<!--  width: 320px;-->
<!--  height: calc(100% - 0px);-->
<!--}-->

<!--.class-right-side {-->
<!--  float: right;-->
<!--  width: calc(100% - 300px);-->
<!--  height: calc(100% - 0px);-->
<!--}-->

<!--.left-side-point-title {-->
<!--  padding: 0 10px;-->
<!--  width: 280px;-->
<!--  overflow: hidden;-->
<!--  white-space: nowrap;-->
<!--  text-overflow: ellipsis;-->
<!--}-->

<!--.class-left-side-filter {-->
<!--  width: 100%;-->
<!--  position: sticky;-->
<!--  padding: 3px 8px;-->
<!--  background-color: #eef1f6;-->
<!--  top: 0;-->
<!--  z-index: 2;-->
<!--}-->

<!--.check-result-tag {-->
<!--  margin: 2px 5px;-->
<!--  max-width: 300px;-->
<!--  overflow: scroll;-->
<!--}-->
<!--.check-result-tag::-webkit-scrollbar {-->
<!--  display: none;-->
<!--}-->
<!--</style>-->
