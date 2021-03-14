import axios from "axios"

import { GET_EVENTS} from './types';

//GEt Events

export const getEvents =()=> dispatch => {
    axios.get('/event/')
    .then(res=>{
        dispatch({
            type:GET_EVENTS,
            payload:res.data
        });
    }).catch(err=>console.log(err));
}