export interface CreateAccountDto {
    name: string
    pwd: string
    host: string
}

export interface PutAccountDto {
    name?: string
    pwd?: string
    host?: string
}
