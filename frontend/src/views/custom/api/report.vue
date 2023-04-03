<!--<template>-->
<!--  <div class="app-container">-->
<!--    <div id="myChart" />-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import echarts from 'echarts'-->
<!--import LineChart from "../../dashboard/LineChart.vue";-->
<!--import store from "@/store";-->
<!--export default {-->
<!--  name: 'DynamicLineChart',-->
<!--  components: {LineChart},-->
<!--  data () {-->
<!--        return {-->
<!--        	// 实时数据数组-->
<!--            date: [],-->
<!--            yieldAvgSuccess: [],-->
<!--            yieldAvgError: [],-->
<!--            yieldAvgTotal: [],-->
<!--            // 折线图echarts初始化选项-->
<!--            echartsOption: {-->
<!--                legend: {-->
<!--                    data: ['错误请求平均耗时', '成功请求平均耗时', '平均耗时'],-->
<!--                },-->
<!--                xAxis: {-->
<!--                    name: '执行时间',-->
<!--                    nameTextStyle: {-->
<!--                        fontWeight: 400,-->
<!--                        fontSize: 14-->
<!--                    },-->
<!--                    type: 'category',-->
<!--                    boundaryGap: false,-->
<!--                    data: this.date,	// 绑定实时数据数组-->
<!--                },-->
<!--                yAxis: {-->
<!--                    name: '平均耗时(ms)',-->
<!--                    nameTextStyle: {-->
<!--                        fontWeight: 400,-->
<!--                        fontSize: 14-->
<!--                    },-->
<!--                    type: 'value',-->
<!--                    scale: true,-->
<!--                    boundaryGap: ['15%', '15%'],-->
<!--                    axisLabel: {-->
<!--                        interval: 'auto',-->
<!--                        formatter: '{value}'-->
<!--                    }-->
<!--                },-->
<!--                tooltip: {-->
<!--                    trigger: 'axis',-->
<!--                },-->
<!--                series: [-->
<!--                    {-->
<!--                        name:'错误请求平均耗时',-->
<!--                        type:'line',-->
<!--                        color: '#F56C6C',-->
<!--                        smooth: true,-->
<!--                        data: this.yieldAvgError,	// 绑定实时数据数组-->
<!--                    },-->
<!--                    {-->
<!--                        name:'成功请求平均耗时',-->
<!--                        type:'line',-->
<!--                        color: '#67C23A',-->
<!--                        smooth: true,-->
<!--                        data: this.yieldAvgSuccess,	// 绑定实时数据数组-->
<!--                    },-->
<!--                  {-->
<!--                        name:'平均耗时',-->
<!--                        type:'line',-->
<!--                        smooth: true,-->
<!--                        data: this.yieldAvgTotal,	// 绑定实时数据数组-->
<!--                    }-->
<!--                ]-->
<!--            }-->
<!--        }-->
<!--    },-->
<!--    mounted () {-->
<!--      this.myChart = echarts.init(document.getElementById('myChart'), 'light');	// 初始化echarts, theme为light-->
<!--      this.myChart.setOption(this.echartsOption);	// echarts设置初始化选项-->
<!--      this.initWebSocket()-->

<!--        // setInterval(this.addData, 3000);	// 每三秒更新实时数据到折线图-->
<!--    },-->
<!--    methods: {-->
<!--      // 添加实时数据-->
<!--      getRealtimeData : function () {-->
<!--        return {-->
<!--          date: Math.round(new Date().getTime() / 1000),-->
<!--          avgError: Math.floor(100 + Math.random()*20),-->
<!--          avgSuccess: Math.floor(200 + Math.random()*20),-->
<!--          avgTotal: Math.floor(180 + Math.random()*20),-->
<!--        }-->
<!--      },-->
<!--      initWebSocket() {-->
<!--        const wsuri =-->
<!--          "ws://127.0.0.1:8000" +-->
<!--          "/ws/point/catch/1/";-->
<!--        this.websocket = new WebSocket(wsuri);-->
<!--        this.websocket.onopen = this.websocketonopen;-->
<!--        this.websocket.onerror = this.websocketonerror;-->
<!--        this.websocket.onmessage = this.websocketonmessage;-->
<!--        this.websocket.onclose = this.websocketclose;-->
<!--      },-->
<!--      websocketonmessage(e) {-->
<!--        this.addData()-->
<!--      },-->
<!--      addData : function() {-->
<!--        // 从接口获取数据并添加到数组-->
<!--        let data = this.getRealtimeData()-->
<!--        this.yieldAvgError.push(data.avgError);-->
<!--        this.yieldAvgSuccess.push(data.avgSuccess);-->
<!--        this.yieldAvgTotal.push(data.avgTotal);-->
<!--        this.date.push(data.date);-->
<!--        // 重新将数组赋值给echarts选项-->
<!--        this.echartsOption.xAxis.data = this.date;-->
<!--        this.echartsOption.series[0].data = this.yieldAvgError;-->
<!--        this.echartsOption.series[1].data = this.yieldAvgSuccess;-->
<!--        this.echartsOption.series[2].data = this.yieldAvgTotal;-->
<!--        this.myChart.setOption(this.echartsOption);-->
<!--      }-->
<!--    }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#myChart{-->
<!--  width: 100%;-->
<!--  height: 500px;-->
<!--  margin: 0 auto;-->
<!--}-->
<!--</style>-->
