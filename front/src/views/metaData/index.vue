<template>
  <div>
    <el-table :data="tableDataBook" style="width: 100%">
      <el-table-column prop="cid" label="cid" width="180"></el-table-column>
      <el-table-column prop="title" label="title" width="180"></el-table-column>
      <el-table-column prop="price" label="price" width="180"></el-table-column>
      <el-table-column
        prop="subject"
        label="subject"
        width="180"
      ></el-table-column>
      <el-table-column
        prop="description"
        label="description"
        width="180"
      ></el-table-column>
      <el-table-column prop="publisher" label="publisher"></el-table-column>
      <el-table-column prop="author" label="author"></el-table-column>
    </el-table>
  </div>
</template>

<script>
  import { getMetaData } from '@/api/metaData'

  export default {
    name: 'Goods',
    components: {},
    data() {
      return {
        tableDataBook: [],
        tableDataMusic: [],
      }
    },
    created() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        var temp = await getMetaData({ verb: 'ListRecords' }, '0009')
        this.tableDataBook = temp['data']
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
