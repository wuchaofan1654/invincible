<template>
  <div class="app-container">
    <div class="myChart" ref="chart"/>
  </div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "DynamicLineChart",

  props: {
    className: { type: String, default: "chart" },
    title: { type: String, default: "" },
    width: { type: String, default: "100%" },
    height: { type: String, default: "400px" },
    autoResize: { type: Boolean, default: true },
    data: { type: Object, default: () => {} },
    xName: { type: String, default: "" },
    yName: { type: String, default: "" }
  },

  data() {
    return {
      // 折线图echarts初始化选项
      echartsOption: {
        legend: {
          data: []
        },
        title: {
          text: this.title
        },
        xAxis: {
          name: this.xName,
          nameTextStyle: {
            fontWeight: 400,
            fontSize: 14
          },
          type: "category",
          boundaryGap: false,
          data: this.data.xAxis
        },
        yAxis: {
          name: this.yName,
          nameTextStyle: {
            fontWeight: 400,
            fontSize: 14
          },
          type: "value",
          scale: true,
          boundaryGap: ["15%", "15%"],
          axisLabel: {
            interval: "auto",
            formatter: "{value}"
          }
        },
        tooltip: {
          trigger: "axis"
        },
        series: []
      }
    };
  },
  mounted() {
    // 初始化echarts, theme为light
    this.myChart = echarts.init(this.$refs.chart, "light");
    this.initECharts();
  },
  methods: {
    initECharts: function() {
      // 从接口获取数据并添加到数组
      const legends = [];
      const series = [];
      for (const data in this.data.yAxis) {
        console.log(data);
        legends.push(data);
        series.push({
          name: data,
          type: "line",
          smooth: true,
          data: this.data.yAxis[data]
        });
      }
      // 重新将数组赋值给echarts选项
      this.echartsOption.legend.data = legends;
      this.echartsOption.series = series;
      // echarts设置初始化选项
      this.myChart.setOption(this.echartsOption);
    }
  }
};
</script>

<style>
.myChart {
  width: 100%;
  height: 500px;
  margin: 0 auto;
}
</style>
