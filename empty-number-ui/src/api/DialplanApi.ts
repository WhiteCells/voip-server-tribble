import { request } from "./request";
import type { CreateDialplanDto, PutDialplanDto } from "@/dto/DialplanDto";

export const createDialplan = (data: CreateDialplanDto) => {
    return request.post('/dialplans', data)
}

export const deleteDialplan = (id: number) => {
    return request.delete(`/dialplans/${id}`)
}

export const putDialplan = (id: number, data: PutDialplanDto) => {
    return request.put(`/dialplans/${id}`, data)
}

export const getDialplan = (id: number) => {
    return request.get('dialplans')
}
