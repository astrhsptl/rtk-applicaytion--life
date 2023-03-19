import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom';
import getCookies from '../../utils/cookies';
import '../../styles/register.css'
import Header from '../../UI/Header';
import Footer from '../../UI/Footer';

export default function ApplicationList() {
    const [user, setUser] = useState(getCookies());
    const [searchApplications, setSearchApplications] = useState([]);

    const [statuses, setStatuses] = useState([]);
    
    useEffect(()=>{
        async function getData(setApp, setStat){
            let applications = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/');
            let statuses = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/status/');
        
            await setApp(applications.data);
            await setStat(statuses.data);
        }
        getData(setSearchApplications, setStatuses)
        setUser(getCookies());
    }, []);


  return (
    <div className='main' style={{display: "grid"}}>
      <Header/>
      <div className='wrapper wrapper__acc'>
        <div className='int_aa'>
          <input type="text" className='input' placeholder='Номер заявки' onChange={(e)=>{loadCurrentData('number', e.target.value, setSearchApplications)}} />
        </div>
        <div className='acc__wrap'>
        {(searchApplications.concat(searchApplications))?.map(app => 
          <span className='element'>
            <div>Номер заявки: {app.number}</div>
            <div>Дата: {new Date(app.finaled_date).toUTCString()}</div>
            <div>Статус: {statuses.find(st => st.id == app.current_status).title}</div>
          </span>)}

        </div>
      </div>
   
      <Footer />
   
    </div>
  )
}

async function loadCurrentData(param, value, setApp){
  let applications = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/?${param}=${value}`);
  await setApp(applications.data);
}