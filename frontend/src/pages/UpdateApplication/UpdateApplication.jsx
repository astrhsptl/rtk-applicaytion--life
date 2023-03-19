import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import ChangesBar from '../../Components/ChangesBar';
import getCookies from '../../utils/cookies';
import '../../styles/register.css';

export default function UpdateApplication() {
    const {id} = useParams(); 
    const [user, setUser] = useState();
    const [staff, setStaff] = useState([])
    const [application, setApplication] = useState({});
    const [statuses, setStatuses] = useState([]);
    const [states, setStates] = useState([]);
    const [changes, setChanges] = useState([]);
    const navigate = useNavigate();

    async function getData(setApp, setStat, setChanges, setStaff, setStates,  id){
        let application = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/${id}/`);
        let statuses = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/status/');
        let states = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/state/');
        let asd = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/change/make/?application=${id}`);        
        let staff = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/users/');

        await setStaff(staff.data)
        await setChanges(asd.data);
        await setStates(states.data);
        await setApp(application.data);
        await setStat(statuses.data);
    }

    useEffect(() => {
        getData(setApplication, setStatuses, setChanges, setStaff,setStates, id)
        setUser(getCookies());
    }, [])
    
    return (
        <div>
            <select
              value={application.current_status}
              onChange={e => setApplication({ ...application, current_status: e.target.value })}>
              {statuses.map(currentStatus => 
                <option value={currentStatus.id}>{currentStatus.title}</option>
                )}
            </select>

            <select
              value={application.current_state}
              onChange={e => setApplication({ ...application, state: e.target.value })}>
              {states.map(currentState => 
                <option value={currentState.id}>{currentState.title}</option>
                )}
            </select>
            <div className='content_button' onClick={(e) => {
                e.preventDefault()
                updateApplication(user, application);
                // getData(setApplication, setStatuses, setChanges, setStaff, setStates, id);
                navigate('/applications')
            }}>Обновить</div>

            <ChangesBar changes={changes} statuses={statuses} staff={staff}/>
        </div>
  )
}


async function updateApplication(user, application,) {
    const date = new Date();
    let newChainChage = await axios.post('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/change/make/', {
                "current_status": application.current_status,
                "application": application.id,
                "manager": user.id,
                "current_state": application.state,
                "create_date": date.toISOString()});
};