import axios from 'axios';
import type { Deuda } from '../types/deudaTypes';

export const getDeudas = async () => {
    return await axios.get('api/deudas')
        .then((response) => {
            return response.data;
        })
        .catch(error => {
            console.log(error);
        })
}

export const postDeuda = async (deuda: Deuda) => {
    return await axios.post('api/deudas', deuda)
        .then((response) => {
            return response.data;
        })
        .catch(error => {
            console.log(error);
        })
}