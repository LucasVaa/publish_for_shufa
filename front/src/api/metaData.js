import request from '@/utils/request'

export function getMetaData(params, lib) {
  return request({
    url: 'http://4a8134663q.goho.co/x/' + lib,
    method: 'get',
    params,
    timeout: 10000,
    headers: {
      'router-auth':
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNodWZhX3VzZXIiLCJsaWQiOiIwMDA3In0.yCU7QPVz26gPd4gvk-FNx_Pe-MionOOb6fIw4XRvbEQ',
    },
  })
}
