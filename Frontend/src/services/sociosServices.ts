import axios from 'axios';
import type { SocioRequest, SocioResponse } from '../types/sociosTypes';

export const getSocios = async (): Promise<SocioResponse[]> => {
    return await axios.get('api/socios')
        .then((response) => {
            console.log(123);
            return response.data;
        })
        .catch(error => {
            console.log(error);
        })
}

export const postSocios = async (data: SocioRequest) => {
    return await axios.post('api/socios', data)
        .then((response) => {
            console.log(response.data)
        })
        .catch(error => {
            console.log(error);
        })
}

export const loadSocios = async () => {
    return await axios.post('api/socios/google')
        .then((response) => {
            console.log(response.data);
        })
        .catch(error => {
            console.log(error);
        })
}
