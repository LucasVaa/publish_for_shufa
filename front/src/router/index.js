/**
 * @author https://gitee.com/chu1204505056/vue-admin-better （不想保留author可删除）
 * @description router全局配置，如有必要可分文件抽离，其中asyncRoutes只有在intelligence模式下才会用到，vip文档中已提供路由的基础图标与小清新图标的配置方案，请仔细阅读
 */

import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/layouts'
import EmptyLayout from '@/layouts/EmptyLayout'
import { publicPath, routerMode } from '@/config'

Vue.use(VueRouter)
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true,
  },
  {
    path: '/register',
    component: () => import('@/views/register/index'),
    hidden: true,
  },
  {
    path: '/401',
    name: '401',
    component: () => import('@/views/401'),
    hidden: true,
  },
  {
    path: '/404',
    name: '404',
    component: () => import('@/views/404'),
    hidden: true,
  },
]

export const asyncRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/index',
    children: [
      {
        path: 'index',
        name: 'Index',
        component: () => import('@/views/index/index'),
        meta: {
          title: '首页',
          affix: true,
        },
      },
    ],
  },
  {
    path: '/shufalist',
    component: Layout,
    redirect: 'noRedirect',
    children: [
      {
        path: 'goodsList',
        name: 'GoodsList',
        component: () => import('@/views/mall/goodsList/index'),
        meta: {
          title: '历代书法',
          affix: true,
        },
      },
    ],
  },
  // {
  //   path: '/publish',
  //   component: Layout,
  //   redirect: 'noRedirect',
  //   children: [
  //     {
  //       path: 'publish',
  //       name: 'Publish',
  //       component: () => import('@/views/publish/index'),
  //       meta: {
  //         title: '发布',
  //         affix: true,
  //       },
  //     },
  //   ],
  // },
  {
    path: '/metaData',
    component: Layout,
    redirect: 'noRedirect',
    name: 'MetaData',
    meta: {
      title: '元数据收割',
      permissions: ['admin'],
    },

    children: [
      {
        path: 'metaDataBook',
        name: 'MetaDataBook',
        component: () => import('@/views/metaData/index'),
        meta: {
          title: '图书',
        },
      },
      {
        path: 'metaDataMusic',
        name: 'MetaDataMusic',
        component: () => import('@/views/metaData/index_music'),
        meta: {
          title: '音乐',
        },
      },
    ],
  },
  {
    path: '/all',
    name: 'all',
    component: () => import('@/views/mall/goodsList/index'),
    hidden: true,
  },
  {
    path: '*',
    redirect: '/404',
    hidden: true,
  },
]

const router = new VueRouter({
  base: publicPath,
  mode: routerMode,
  scrollBehavior: () => ({
    y: 0,
  }),
  routes: constantRoutes,
})

export function resetRouter() {
  location.reload()
}

export default router
