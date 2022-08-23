import request from '@/utils/request'

export function getMetaData(params, lib) {
  return request({
    url: 'http://172.20.112.140:9000/x/' + lib,
    method: 'get',
    params,
    timeout: 10000,
    headers: {
      'router-auth':
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ilx1OTdmM1x1NGU1MFx1NTNkMVx1NWUwM1x1ODAwNSIsImxpZCI6IjAwMDQifQ.6Fhe3l5D9P5YRKtSy2pYxqRIbPchOikD6q-PJ8-jDm4',
    },
  })
}
