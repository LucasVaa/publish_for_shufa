import request from '@/utils/request'

export function getList(data) {
  return request({
    url: '/goodsList/getList',
    method: 'post',
    data,
  })
}

export function getShufaList() {
  return request({
    url: 'http://211.145.15.126:1024/backend-api/getShufaList',
    method: 'get',
    timeout: 10000,
  })
}

export function getShufaListById(params) {
  return request({
    url: 'http://211.145.15.126:1024/backend-api/getShufaListById',
    method: 'get',
    params,
    timeout: 10000,
  })
}

export function getShufaTotal(params) {
  return request({
    url: 'http://211.145.15.126:1024/backend-api/getShufaTotal',
    method: 'get',
    timeout: 10000,
    params,
  })
}
