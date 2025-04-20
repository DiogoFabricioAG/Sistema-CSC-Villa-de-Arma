import axios from 'axios';

export async function getOpinions() {
    return axios.get('api/opiniones')
        .then((response) => {
            console.log(123);
            return response.data;
        })
        .catch(error => {
            console.log(error);
        })
}