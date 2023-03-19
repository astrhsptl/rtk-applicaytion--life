import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate, Navigate, Link } from 'react-router-dom';
import Header from '../../UI/Header';
import getCookies from '../../utils/cookies';
import ClientAccount from '../../Components/AccountComponents/ClientAccount';
import ManagerAccount from '../../Components/AccountComponents/ManagerAccount';
import ChangesBar from '../../Components/ChangesBar';
import Footer from '../../UI/Footer';
import '../../styles/template_acc.css'


export default function AccountPage() {
    const [user, setUser] = useState(getCookies());
    const [staff, setStaff] = useState([]);
    const [statuses, setStatuses] = useState([]);
    const [changes, setChanges] = useState([]);
    const navigator = useNavigate();

    useEffect(() => {
        async function getData(setStat, setChanges, setStaff, id){
            let statuses = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/status/');
            let asd = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/change/make/?manager=${id}`);        
            let staff = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/users/');
    
            await setStaff(staff.data)
            await setChanges(asd.data);
            await setStat(statuses.data);
        }
        getData(setStatuses, setChanges, setStaff, user.id)
    }, [])

    if (user.id) {
    return (
        <div className='wrapper__home'>
            <Header></Header>
            {
                user.status == 2 ? 
                    <div className='template__account'>
                        <ManagerAccount user={user} />
                        <div className='wrap'>
                            <ChangesBar changes={changes} statuses={statuses} staff={staff}/>
                            <div className='button-conteiner'>
                            <button className='' onClick={()=>(navigator('/applications'))}>Заявки</button>
                            <button className='' onClick={()=>(navigator('/userlist'))}>Аккаунты</button>
                            </div>
                        </div>
                    </div>
                :

                <ClientAccount user={user} />
                
            }

          <Footer></Footer>
        </div>
    )
    }
    else {
        return (

        <div className='main'>
            <Header></Header>
            <button onClick={()=>{return navigator('/login')}}>Login</button>
            <Footer></Footer>
        </div>

        )
    }
}