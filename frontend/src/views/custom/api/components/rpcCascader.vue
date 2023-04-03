<!--<template>-->
<!--  <el-cascader-->
<!--    ref="rpcCas"-->
<!--    size="mini"-->
<!--    :props="casProps"-->
<!--    :options="options"-->
<!--    @change="handleChange">-->
<!--  </el-cascader>-->
<!--</template>-->

<!--<script>-->
<!--import {getRpcItems} from '@/api/api/api'-->
<!--export default {-->
<!--  name: 'rpcCascader',-->
<!--  data () {-->
<!--    return {-->
<!--      options: [{id: '', item_name: '', leaf: false}],-->
<!--      casProps: {-->
<!--        value: 'id',-->
<!--        label: 'item_name',-->
<!--        leaf: 'is_leaf',-->
<!--        lazy: true,-->
<!--        lazyLoad: (node, resolve) => {-->
<!--          if (node.data.id) this.fetchNotFirstLevelRpcItems(node.data, resolve)-->
<!--        }-->
<!--      }-->
<!--    }-->
<!--  },-->
<!--  mounted () {-->
<!--    this.fetchFirstLevelItems()-->
<!--  },-->
<!--  methods: {-->
<!--    handleChange (value) {-->
<!--      if (value.length > 0) {-->
<!--        let checkNode = this.$refs['rpcCas'].getCheckedNodes()-->
<!--        this.$emit('getSelectedItems', checkNode[0])-->
<!--      } else {-->
<!--        this.$emit('getSelectedItems', {}, [])-->
<!--      }-->
<!--    },-->
<!--    fetchFirstLevelItems () {-->
<!--      getRpcItems().then(res => {-->
<!--        if (res.code !== 200) {-->
<!--          this.$message.error('获取rpc services失败')-->
<!--        } else {-->
<!--          this.options = res.data-->
<!--        }-->
<!--      }).catch(error => console.log('获取rpc services失败', error))-->
<!--    },-->
<!--    // 获取子层数据-->
<!--    fetchNotFirstLevelRpcItems (data, resolve) {-->
<!--      let items = []-->
<!--      getRpcItems(data.id).then(res => {-->
<!--        if (res.code !== 200) {-->
<!--          this.$message.error('获取rpc方法失败')-->
<!--        } else {-->
<!--          items = res.data-->
<!--          resolve(items)-->
<!--        }-->
<!--      }).catch(error => {-->
<!--        this.$message.error(error)-->
<!--        resolve(items)-->
<!--      })-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->
