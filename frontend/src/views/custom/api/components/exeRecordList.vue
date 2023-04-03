<!--<template>-->
<!--  <div class="app-container" style="background-color: #eaebee">-->
<!--    <span><i class="el-icon-timer">历史查询记录</i></span>-->
<!--    <el-button class="clear-bnt" type="text" icon="el-icon-delete">清空</el-button>-->
<!--    <div v-for="(record, index) in data.records">-->
<!--      <el-link class="el-rec-link" type="primary" @click="exeRpc(mergeQueryParams(record))">-->
<!--        {{index + 1}}.<span v-for="item in record.items">{{item.item_name}}.</span>-->
<!--      </el-link>-->
<!--      <p class="p-create-time"><i class="el-icon-time"> {{record.create_datetime}}</i></p>-->
<!--    </div>-->
<!--    <el-link-->
<!--      v-if="data.hasMore"-->
<!--      type="primary"-->
<!--      icon="el-icon-d-arrow-right"-->
<!--      :underline="false">-->
<!--      加载更多</el-link>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import {getRpcRecords, executeRpc} from "@/api/api/api";-->

<!--const defaultQueryListDict = {-->
<!--  pageSize: 20,-->
<!--  pageNum: 1,-->
<!--  uid: 0,-->
<!--}-->

<!--export default {-->
<!--  name: "exeRecordList",-->
<!--  props: ['evn'],-->
<!--  data() {-->
<!--    return {-->
<!--      data: {-->
<!--        records: [],-->
<!--        total: 0,-->
<!--        hasMore: 1-->
<!--      },-->
<!--    }-->
<!--  },-->
<!--  created() {-->
<!--    this.getList()-->
<!--  },-->
<!--  methods: {-->
<!--    getList(){-->
<!--      getRpcRecords().then(response => {-->
<!--        if (response.code === 200) {-->
<!--          this.data.records = response.data.results-->
<!--        } else {-->
<!--          this.data.records = []-->
<!--        }-->
<!--      })-->
<!--    },-->
<!--    mergeQueryParams(record) {-->
<!--      return {-->
<!--        evn: this.evn,-->
<!--        items: record.items,-->
<!--        params: record.params-->
<!--      }-->
<!--    },-->
<!--    exeRpc(params) {-->
<!--      let result-->
<!--      executeRpc(params).then(response => {-->
<!--        if (response.code === 200) {-->
<!--          result = response.data-->
<!--        } else {-->
<!--          result = response-->
<!--        }-->
<!--        this.$emit('getExeResult', result)-->
<!--      })-->
<!--    }-->
<!--  },-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--.clear-bnt {-->
<!--  padding-left: 10px;-->
<!--}-->
<!--.el-rec-link{-->
<!--  font-size: 12px;-->
<!--}-->
<!--.p-create-time {-->
<!--  font-size: 8px;-->
<!--  color: gray-->
<!--}-->

<!--</style>-->
