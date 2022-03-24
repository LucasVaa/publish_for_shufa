
#### 项目运行
```bash
# 安装依赖
npm install
# 本地开发 启动项目
npm run serve
```
#### 书法资源元数据
```
import json

additiondata = {
    "characterId": "1",
    "dynasty": "东汉",
    "script": "隶书",
    "source": "西狭颂",
    "fileName": "000001.a.donghan.lishu..xixiasong.4.jpg",
    "imageNumber": 3
}

data = {
    "uid": '1',
    "lid": '2',
    "sourceType": 2,
    "author": "",
    "title": "",
    "description": "",
    "isencrypt": 0,
    "size": 109,
    'price': 12,
    "content_hash": content_hash,
    "publish_time": "2019-03-05 01:53:56",
    "additionalInformation": json.dumps(additiondata)
}

```