<!--<template>-->
<!--  <div class="app-container">-->
<!--    <el-row :gutter="22">-->
<!--      <div class="sub-title">-->
<!--        <i class="el-icon-rank">-->
<!--          每版本包大小变化趋势图-->
<!--        </i>-->
<!--      </div>-->
<!--      <el-col :span="16">-->
<!--        <el-card>-->
<!--          <line-stat-->
<!--            v-if="iosData.xAxis && iosData.xAxis.length > 0"-->
<!--            :data="iosData"-->
<!--            title="iOS包大小"-->
<!--            x-name="发布版本"-->
<!--            y-name="大小（Mb）"/>-->
<!--          <line-stat-->
<!--            v-if="androidData.xAxis && androidData.xAxis.length > 0"-->
<!--            :data="androidData"-->
<!--            title="Android包大小"-->
<!--            x-name="发布版本"-->
<!--            y-name="大小（Mb）"/>-->
<!--        </el-card>-->
<!--      </el-col>-->
<!--      <el-col :span="8">-->
<!--        <el-card class="box-card">-->
<!--          <div slot="header" class="clearfix">-->
<!--            <span>包大小增减明细</span>-->
<!--            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
<!--          </div>-->
<!--          <div class="pie-chart-title">-->
<!--            <i class="el-icon-sort-up">-->
<!--              iOS增加-->
<!--            </i>-->
<!--          </div>-->
<!--          <div class="chart-wrapper">-->
<!--            <pie-chart :data="downDataList"/>-->
<!--          </div>-->
<!--          <div class="pie-chart-title">-->
<!--            <i class="el-icon-sort-down">-->
<!--              iOS降低-->
<!--            </i>-->
<!--          </div>-->
<!--          <div class="chart-wrapper">-->
<!--            <pie-chart :data="downDataList"/>-->
<!--          </div>-->
<!--        </el-card>-->
<!--      </el-col>-->
<!--    </el-row>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { get_publish_stat } from "@/api/custom/performance/publish";-->
<!--import LineStat from "./components/LineStat.vue";-->
<!--import PieChart from "@/views/dashboard/PieChart.vue";-->

<!--export default {-->
<!--  name: "DynamicLineChart",-->
<!--  components: { LineStat, PieChart },-->
<!--  data() {-->
<!--    return {-->
<!--      queryParams: {-->
<!--        status: 1,-->
<!--        mobiles: 1,-->
<!--        build_no: ""-->
<!--      },-->
<!--      iosData: {},-->
<!--      androidData: {},-->
<!--      upDataList: [],-->
<!--      downDataList: [-->
<!--        { value: 244.29, name: "libSYMedicalCheck.a" },-->
<!--        { value: 828.8, name: "libReact-Core.a" },-->
<!--        { value: 402.2, name: "libRNReanimated.a" },-->
<!--        { value: 396.77, name: "libSYACNModule.a" },-->
<!--        { value: 396.77, name: "libSYOChat.a" },-->
<!--        { value: 396.77, name: "libSYMCNModule.a" },-->
<!--        { value: 291.81, name: "libSYOrgazationModule.a" }-->
<!--      ]-->
<!--    };-->
<!--  },-->
<!--  created() {-->
<!--    this.getLineChartData();-->
<!--  },-->
<!--  methods: {-->
<!--    async getLineChartData() {-->
<!--      // xAxis为横轴列表，需要按照顺序， yAxis为竖轴坐标列表，需要按照与x轴顺序相同的顺序排序-->
<!--      await get_publish_stat(this.queryParams).then(res => {-->
<!--        console.log(res.data);-->
<!--        if (res.data.ios.xAxis.length > 0) {-->
<!--          this.iosData = res.data.ios;-->
<!--        } else {-->
<!--          this.iosData = {};-->
<!--        }-->
<!--        if (res.data.android.xAxis.length > 0) {-->
<!--          this.androidData = res.data.android;-->
<!--        } else {-->
<!--          this.androidData = {};-->
<!--        }-->
<!--      });-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style>-->
<!--.sub-title {-->
<!--  font-size: 20px;-->
<!--  color: #606266;-->
<!--  margin: 20px 0;-->
<!--  font-weight: bold;-->
<!--}-->

<!--.pie-chart-title {-->
<!--  font-size: 15px;-->
<!--  color: #606266;-->
<!--  text-align: right;-->
<!--  margin: 25px 0;-->
<!--}-->
<!--</style>-->
