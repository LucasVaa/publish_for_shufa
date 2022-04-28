<template>
  <div class="goods-list-container">
    <vab-query-form>
      <vab-query-form-right-panel :span="24">
        <el-form
          ref="form"
          :model="queryForm"
          :inline="true"
          @submit.native.prevent
        >
          <el-form-item>
            <el-input v-model="queryForm.title" placeholder="汉字" />
          </el-form-item>
          <el-form-item>
            <el-input v-model="queryForm.date" placeholder="朝代" />
          </el-form-item>
          <el-form-item>
            <el-input v-model="queryForm.creator" placeholder="作者" />
          </el-form-item>
          <el-form-item>
            <el-input v-model="queryForm.type" placeholder="字体" />
          </el-form-item>
          <el-form-item>
            <el-button
              icon="el-icon-search"
              type="primary"
              native-type="submit"
              @click="handleQuery"
            >
              查询
            </el-button>
          </el-form-item>
        </el-form>
      </vab-query-form-right-panel>
    </vab-query-form>
    <el-row :gutter="20">
      <el-col
        v-for="(item, index) in list"
        :key="index"
        :xs="24"
        :sm="8"
        :md="8"
        :lg="8"
        :xl="6"
      >
        <el-card :body-style="{ padding: '0px' }" shadow="hover">
          <div class="goods-list-card-body">
            <div class="goods-list-tag-group">
              <el-tag v-if="item.isRecommend" hit type="success">推荐</el-tag>
              <el-tag v-if="item.status === 0" hit type="danger">缺货</el-tag>
            </div>
            <div class="goods-list-image-group">
              <el-image
                :src="item.image"
                class="goods-list-image"
                :preview-src-list="[item.image]"
              />
            </div>
            <div class="goods-list-title">{{ item.title }}</div>
            <div class="goods-list-description">
              {{ '字体: ' + item.type + ' 作者: ' + item.creator }}
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-pagination
      background
      :current-page="queryForm.pageNo"
      :layout="layout"
      :page-size="queryForm.pageSize"
      :total="total"
      @current-change="handleCurrentChange"
      @size-change="handleSizeChange"
    ></el-pagination>
  </div>
</template>

<script>
  import {
    getList,
    getShufaList,
    getShufaTotal,
    getShufaListById,
  } from '@/api/goodsList'

  export default {
    name: 'Goods',
    components: {},
    data() {
      return {
        queryForm: {
          pageNo: 1,
          pageSize: 10,
          title: '',
          creator: '',
          date: '',
          type: '',
          data: '',
        },
        list: null,
        listLoading: true,
        layout: 'total, sizes, prev, pager, next, jumper',
        total: 0,
        elementLoadingText: '正在加载...',
      }
    },
    created() {
      this.initData()
    },
    methods: {
      handleSizeChange(val) {
        this.queryForm.pageSize = val
        this.fetchData()
      },
      handleCurrentChange(val) {
        this.queryForm.pageNo = val
        this.fetchData()
      },
      async handleQuery() {
        this.queryForm.pageNo = 1
        this.total = await getShufaTotal({
          title: this.queryForm.title,
          creator: this.queryForm.creator,
          date: this.queryForm.date,
          type: this.queryForm.type,
        })
        this.fetchData()
      },
      async initData() {
        this.listLoading = true
        this.total = await getShufaTotal()
        this.fetchData()
      },
      async fetchData() {
        this.queryForm.data = await getShufaListById({
          id: this.queryForm.pageNo,
          size: this.queryForm.pageSize,
          title: this.queryForm.title,
          creator: this.queryForm.creator,
          date: this.queryForm.date,
          type: this.queryForm.type,
        })
        this.listLoading = true
        const { data, totalCount } = await getList(this.queryForm)
        this.list = data
        // this.total = totalCount
      },
    },
  }
</script>
<style lang="scss" scoped>
  .goods-list-container {
    .goods-list-card-body {
      position: relative;
      text-align: center;
      cursor: pointer;

      .goods-list-tag-group {
        position: absolute;
        top: 10px;
        right: 5px;
        z-index: 9;
      }

      .goods-list-image-group {
        height: 500px;
        overflow: hidden;

        .goods-list-image {
          width: 100%;
          height: 500px;
          transition: all ease-in-out 0.3s;

          &:hover {
            transform: scale(1.1);
          }
        }
      }

      .goods-list-title {
        margin: 8px 0;
        font-size: 16px;
        font-weight: bold;
      }

      .goods-list-description {
        font-size: 14px;
        color: #808695;
      }

      .goods-list-price {
        margin: 8px 0;
        font-size: 14px;
        color: $base-color-orange;

        s {
          color: #c5c8ce;
        }
      }
    }
  }
</style>
