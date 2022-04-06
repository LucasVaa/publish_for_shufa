
#### 项目运行
```bash
# 安装依赖
npm install
# 本地开发 启动项目
npm run serve
```
#### DC元数据
```
DCMeta = {
    "title": "test", // "啊",
    "date": "test", // "东汉",
    "creator": "test", // "赵佶",
    "subject": "test",
    "publisher": "test", // "中国艺术科技研究所"
    "type": "test", // "隶书",
    "description": "test",
    "contributor": "test",
    "format": "test", // "photo"
    "source": "test", // "西狭颂",
    "rights": "test",
    "identifier": "test",
    "language": "test", // "chinese"
    "relation": "test",
    "coverage": "test",
}
```
#### 书法资源元数据
```
additiondata = {
    "characterId": "AT2601000001",
    "fileName": "000001.a.donghan.lishu..xixiasong.4.jpg",
    "DCMeta": DCMeta,
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