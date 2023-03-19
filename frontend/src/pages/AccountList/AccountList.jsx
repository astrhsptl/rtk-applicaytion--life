import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom';
import getCookies from '../../utils/cookies';
import '../../styles/register.css';
import Header from '../../UI/Header';
import Footer from '../../UI/Footer';

export default function AccountList() {
    const [user, setUser] = useState(getCookies());
    const [userList, setUserList] = useState([]);
    
    useEffect(()=>{
        async function getData(setUserList){
            let userList = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/users/');
        
            await setUserList(userList.data);
        }
        getData(setUserList)
        setUser(getCookies());
    }, []);
    
  return (
    <div style={{display: "grid"}}>
      <Header/>
      <div className='wrapper wrapper__acc'>
      <div className='int_aa'>
        <input type="text" className='input' placeholder='ИНН' onChange={(e)=>{loadCurrentData('itn', e.target.value, setUserList)}} />

      </div>
      <div className='acc__wrap'>
        {userList.map(app => <span className='element' >
          <div>E-mail: {app.email}</div>
          <div>Наименовани: {app.username}</div>
          <div>Инн: {app.itn ? app.itn : 'Нет' }</div>
        
        </span>)}
      </div>
      </div>

      <Footer />
    </div>
  )
}

async function loadCurrentData(param, value, setApp){
  let applications = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/users/search/?${param}=${value}`);
  await setApp(applications.data);
}