import { request } from "./request";
import type { CreateClientDto, PutClientDto } from "@/dto/ClientDto";

export const createClient = (data: CreateClientDto) => {
    return request.post('/clients', data)
}

export const deleteClient = (id: number) => {
    return request.delete(`/clients/${id}`)
}

export const putClient = (id: number, data: PutClientDto) => {
    return request.put(`/clients/${id}`, data)
}

export const getClient = () => {
    return request.get('/clients')
}