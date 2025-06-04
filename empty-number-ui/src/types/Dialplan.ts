export interface Dialplan {
    id: number
    phone: string
    status: '空闲' | '拨打中' | '已完成'
}