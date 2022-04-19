const { mock } = require('mockjs')

module.exports = [
  {
    url: '/goodsList/getList',
    type: 'post',
    response(config) {
      const { title = '', pageNo = 1, pageSize = 10, data = [] } = config.body
      count = config.body.data.length
      List = []
      for (let i = 0; i < config.body.data.length; i++) {
        List.push(
          mock({
            uuid: '@uuid',
            image:
              `http://10.10.1.124:8000/getImage/` +
              config.body.data[i].fileName,
            title: config.body.data[i].title,
            description: '@csentence',
            link: 'https://www.baidu.com',
            price: '@integer(100, 500)',
            'status|1': [1, 0],
            'isRecommend|1': [1, 0],
            date: config.body.data[i].date,
            source: config.body.data[i].source,
            creator: config.body.data[i].creator,
            type: config.body.data[i].type,
          })
        )
      }
      let mockList = List.filter((item) => {
        if (title && item.title.indexOf(title) < 0) return false
        return true
      })
      const pageList = mockList.filter(
        (item, index) =>
          index < pageSize * pageNo && index >= pageSize * (pageNo - 1)
      )
      return {
        code: 200,
        msg: 'success',
        totalCount: count,
        data: List,
      }
    },
  },
]
