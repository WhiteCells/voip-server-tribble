export interface CreateClientDto {
    name: string
    account_id: number[]
}

export interface PutClientDto {
    name?: string
    account_id?: number[]
}