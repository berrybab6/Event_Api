import axios from "axios"

import { DELETE_EVENT, GET_EVENTS, ADD_EVENT} from './types';

//GEt Events
export const getEvents =()=> dispatch => {
    axios.get('/event/')
    .then(res=>{
        dispatch({
            type:GET_EVENTS,
            payload:res.data
        });
    }).catch(err=>console.log(err));
};

//DELETE Event
export const deleteEvent =(id)=> dispatch => {
    axios.delete(`/event/${id}/`)
    .then(res=>{
        dispatch({
            type:DELETE_EVENT,
            payload:id
        });
    }).catch(err=>console.log(err));
};

// ADD Event
export const addEvent = (event) => (dispatch) => {
  axios
    .post('/event/', event)
    .then((res) => {
    //   dispatch(createMessage({ addLead: 'Lead Added' }));
      dispatch({
        type: ADD_EVENT,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};
