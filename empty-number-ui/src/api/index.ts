import axios, { type InternalAxiosRequestConfig, type AxiosResponse, type AxiosError } from 'axios'

// 创建 axios 实例
const request = axios.create({
  baseURL: '/api',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
request.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // 可以在这里添加 token 等认证信息
    return config
  },
  (error: AxiosError) => {
    // 对请求错误做些什么
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  (response: AxiosResponse) => {
    // 对响应数据做点什么
    const res = response.data
    // 如果返回的状态码不是200，说明接口请求有误
    if (response.status !== 200) {
      return Promise.reject(new Error(res.message || '请求失败'))
    }
    return res
  },
  (error: AxiosError) => {
    // 对响应错误做点什么
    let message = '请求失败'
    if (error.response) {
      switch (error.response.status) {
        case 400:
          message = '请求错误'
          break
        case 401:
          message = '未授权，请重新登录'
          break
        case 403:
          message = '拒绝访问'
          break
        case 404:
          message = '请求地址出错'
          break
        case 408:
          message = '请求超时'
          break
        case 500:
          message = '服务器内部错误'
          break
        case 501:
          message = '服务未实现'
          break
        case 502:
          message = '网关错误'
          break
        case 503:
          message = '服务不可用'
          break
        case 504:
          message = '网关超时'
          break
        case 505:
          message = 'HTTP版本不受支持'
          break
        default:
          message = `请求失败(${error.response.status})`
      }
    } else if (error.request) {
      message = '服务器未响应'
    } else {
      message = error.message || '请求配置错误'
    }
    return Promise.reject(new Error(message))
  }
)

// 客户端相关接口
export const clientApi = {
  // 获取客户端列表
  getClients: () => request.get('/clients'),
  // 添加客户端
  addClient: (data: any) => request.post('/clients', data),
  // 更新客户端
  updateClient: (id: number, data: any) => request.put(`/clients/${id}`, data),
  // 删除客户端
  deleteClient: (id: number) => request.delete(`/clients/${id}`)
}

// 账号相关接口
export const accountApi = {
  // 获取账号列表
  getAccounts: () => request.get('/accounts'),
  // 添加账号
  addAccount: (data: any) => request.post('/accounts', data),
  // 更新账号
  updateAccount: (id: number, data: any) => request.put(`/accounts/${id}`, data),
  // 删除账号
  deleteAccount: (id: number) => request.delete(`/accounts/${id}`)
}

// 通话相关接口
export const callApi = {
  // 获取通话列表
  getCalls: () => request.get('/calls'),
  // 添加通话
  addCall: (data: any) => request.post('/calls', data),
  // 更新通话
  updateCall: (id: number, data: any) => request.put(`/calls/${id}`, data),
  // 删除通话
  deleteCall: (id: number) => request.delete(`/calls/${id}`)
}

export default request 