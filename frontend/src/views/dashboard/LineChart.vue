<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from "echarts";

require("echarts/theme/macarons"); // echarts theme
import resize from "./mixins/resize";

export default {
  mixins: [resize],
  props: {
    className: { type: String, default: "chart" },
    title: { type: String, default: "" },
    width: { type: String, default: "100%" },
    height: { type: String, default: "300px" },
    autoResize: { type: Boolean, default: true },
    xAxis: { type: Array, default: () => [] },
    yAxis: { type: Object, default: () => {} }
  },
  data() {
    return {
      chart: null,
      colors: ["#67C23A", "#E6A23C", "#F56C6C", "#C6B148", "#909399"]
    };
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val);
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart();
    });
  },
  beforeDestroy() {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, "macarons");
      this.setOptions(this.chartData);
    },
    setLegend(legend) {
      const color = this.colors[Math.floor(Math.random() * this.colors.length)];
      return {
        name: legend, itemStyle: {
          normal: {
            color: color,
            lineStyle: { color: color, width: 2 }
          }
        },
        smooth: true,
        type: "line",
        data: this.yAxis[legend],
        animationDuration: 2800,
        animationEasing: "cubicInOut"
      };
    },
    setOptions() {
      this.chart.setOption({
        xAxis: { data: this.xAxis, boundaryGap: false, axisTick: { show: false }},
        grid: { left: 10, right: 10, bottom: 20, top: 30, containLabel: true },
        title: [{ left: "center", text: this.title }],
        tooltip: { trigger: "axis", axisPointer: { type: "cross" }, padding: [5, 10] },
        yAxis: { axisTick: { show: false }},
        legend: { data: Object.keys(this.yAxis) },
        series: Object.keys(this.yAxis).map(x => this.setLegend(x))
      });
    }
  }
};
</script>
