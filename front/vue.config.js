/**
 * @author https://gitee.com/chu1204505056/vue-admin-better （不想保留author可删除）
 * @description cli配置
 */

const path = require('path')
const {
  publicPath,
  assetsDir,
  outputDir,
  lintOnSave,
  transpileDependencies,
  title,
  abbreviation,
  devPort,
  providePlugin,
  build7z,
  donation,
} = require('./src/config')
const { webpackBarName, webpackBanner, donationConsole } = require('zx-layouts')

if (donation) donationConsole()
const { version, author } = require('./package.json')
const Webpack = require('webpack')
const WebpackBar = require('webpackbar')
const FileManagerPlugin = require('filemanager-webpack-plugin')
const dayjs = require('dayjs')
const date = dayjs().format('YYYY_M_D')
const time = dayjs().format('YYYY-M-D HH:mm:ss')
process.env.VUE_APP_TITLE = title || 'vue-admin-beautiful'
process.env.VUE_APP_AUTHOR =
  author || 'https://gitee.com/chu1204505056/vue-admin-better'
process.env.VUE_APP_UPDATE_TIME = time
process.env.VUE_APP_VERSION = version

const resolve = (dir) => path.join(__dirname, dir)
const mockServer = () => {
  if (process.env.NODE_ENV === 'development') return require('./mock')
  else return ''
}
module.exports = {
  publicPath,
  assetsDir,
  outputDir,
  lintOnSave,

  transpileDependencies,
  devServer: {
    hot: true,
    port: devPort,
    open: true,
    noInfo: false,
    overlay: {
      warnings: true,
      errors: true,
    },
    after: mockServer(),
    proxy: {
      '/api': {
        target: 'http://172.20.112.124:8000', // 配置访问的服务器地址
        pathRewrite: { '^/api': '' }, // 用于将请求中的 /api 字符串替换为空, 然后访问地址就能正确访问，若不添加此行配置，那么访问地址就变成了： http://localhost:5000/api/request_url，这样的请求就会出现 404 操作
        ws: true, // 是否支持 webstocket, 默认是 true
        changeOrigin: true, // 用于控制请求头中的 host 值, 默认是 ture
      },
    },
  },
  configureWebpack() {
    return {
      resolve: {
        alias: {
          '@': resolve('src'),
        },
      },
      plugins: [
        new Webpack.ProvidePlugin(providePlugin),
        new WebpackBar({
          name: webpackBarName,
        }),
      ],
    }
  },
  chainWebpack(config) {
    config.plugins.delete('preload')
    config.plugins.delete('prefetch')
    config.module
      .rule('svg')
      .exclude.add(resolve('src/remixIcon'))
      .add(resolve('src/colorfulIcon'))
      .end()

    config.module
      .rule('remixIcon')
      .test(/\.svg$/)
      .include.add(resolve('src/remixIcon'))
      .end()
      .use('svg-sprite-loader')
      .loader('svg-sprite-loader')
      .options({ symbolId: 'remix-icon-[name]' })
      .end()

    config.module
      .rule('colorfulIcon')
      .test(/\.svg$/)
      .include.add(resolve('src/colorfulIcon'))
      .end()
      .use('svg-sprite-loader')
      .loader('svg-sprite-loader')
      .options({ symbolId: 'colorful-icon-[name]' })
      .end()

    /*  config.when(process.env.NODE_ENV === "development", (config) => {
      config.devtool("source-map");
    }); */
    config.when(process.env.NODE_ENV !== 'development', (config) => {
      config.performance.set('hints', false)
      config.devtool('none')
      config.optimization.splitChunks({
        automaticNameDelimiter: '-',
        chunks: 'all',
        cacheGroups: {
          chunk: {
            name: 'vab-chunk',
            test: /[\\/]node_modules[\\/]/,
            minSize: 131072,
            maxSize: 524288,
            chunks: 'async',
            minChunks: 2,
            priority: 10,
          },
          vue: {
            name: 'vue',
            test: /[\\/]node_modules[\\/](vue(.*)|core-js)[\\/]/,
            chunks: 'initial',
            priority: 20,
          },
          elementUI: {
            name: 'element-ui',
            test: /[\\/]node_modules[\\/]element-ui(.*)[\\/]/,
            priority: 30,
          },
          extra: {
            name: 'vab-layouts',
            test: resolve('src/layouts'),
            priority: 40,
          },
        },
      })
      config
        .plugin('banner')
        .use(Webpack.BannerPlugin, [`${webpackBanner}${time}`])
        .end()
      config.module
        .rule('images')
        .use('image-webpack-loader')
        .loader('image-webpack-loader')
        .options({
          bypassOnDebug: true,
        })
        .end()
    })

    if (build7z) {
      config.when(process.env.NODE_ENV === 'production', (config) => {
        config
          .plugin('fileManager')
          .use(FileManagerPlugin, [
            {
              onEnd: {
                delete: [`./${outputDir}/video`, `./${outputDir}/data`],
                archive: [
                  {
                    source: `./${outputDir}`,
                    destination: `./${outputDir}/${abbreviation}_${outputDir}_${date}.7z`,
                  },
                ],
              },
            },
          ])
          .end()
      })
    }
  },
  runtimeCompiler: true,
  productionSourceMap: false,
  css: {
    requireModuleExtension: true,
    sourceMap: true,
    loaderOptions: {
      scss: {
        /*sass-loader 8.0语法 */
        //prependData: '@import "~@/styles/variables.scss";',

        /*sass-loader 9.0写法，感谢github用户 shaonialife*/
        additionalData(content, loaderContext) {
          const { resourcePath, rootContext } = loaderContext
          const relativePath = path.relative(rootContext, resourcePath)
          if (
            relativePath.replace(/\\/g, '/') !== 'src/styles/variables.scss'
          ) {
            return '@import "~@/styles/variables.scss";' + content
          }
          return content
        },
      },
    },
  },
}
