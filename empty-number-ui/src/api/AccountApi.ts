import { request } from "./request";
import type { CreateAccountDto, PutAccountDto } from "@/dto/AccountDto";

export const createAccount = (data: CreateAccountDto) => {
    return request.post('/accounts', data)
}

export const deleteAccount = (id: number) => {
    return request.delete(`/accounts/${id}`)
}

export const putAccount = (id: number, data: PutAccountDto) => {
    return request.put(`/accounts/${id}`, data)
}

export const getAccount = () => {
    return request.get('/accounts')
}