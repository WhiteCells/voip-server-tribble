import type { Account } from './Account'

export interface Client {
    id: number
    name: string
    status: '在线' | '离线'
    accounts: Account[]
}