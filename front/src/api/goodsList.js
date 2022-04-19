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
    url: 'http://10.10.1.124:8000/getShufaList',
    method: 'get',
    timeout: 10000,
  })
}

export function getShufaListById(params) {
  return request({
    url: 'http://10.10.1.124:8000/getShufaListById',
    method: 'get',
    params,
    timeout: 10000,
  })
}

export function getShufaTotal(params) {
  return request({
    url: 'http://10.10.1.124:8000/getShufaTotal',
    method: 'get',
    timeout: 10000,
    params,
  })
}
