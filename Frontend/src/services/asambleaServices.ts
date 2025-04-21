import axios from 'axios';

export const getAsambleas = async () => {
    return await axios.get('api/asambleas')
        .then((response) => {
            return response.data;
        })
        .catch(error => {
            console.log(error);
        })
}
export const loadAsambleas = async () => {
    return await axios.post('api/asambleas')
        .then((response) => {
            console.log(response.data);
        })
        .catch(error => {
            console.log(error);
        })
}