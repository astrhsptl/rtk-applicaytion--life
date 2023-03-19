import axios from 'axios';
import React, { useEffect, useState } from 'react'
import '../../styles/cp.css';
import logo from '../../images/image 3.png';
import Card from '../Card';

export default function ClientAccount({ user }) {
  const [finishApplications, setFinishTasks] = useState([]);
  const [activeApplications, setActiveApplications] = useState([]);
  const [stautses, setStautses] = useState([]);
  const [services, setServices] = useState([]);
  
  
  useEffect(()=>{
    async function getData(setActive, setFinished, setStautses, setServices, id){
      let finishTasks = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/?company_id=${id}&finaled=0`);        
      let ActiveTasks = await axios.get(`http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/?company_id=${id}&finaled=1`);
      let statuses = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/status/');
      let services = await axios.get('http://v1738409.hosted-by-vdsina.ru/api/v1/docs/application/service/');


      await setFinished(finishTasks.data)
      await setActive(ActiveTasks.data);
      await setServices(services.data);
      await setStautses(statuses.data);
      
  }
  getData(setFinishTasks, setActiveApplications, setStautses, setServices, user.id);
  }, []);

  return (

	<div className='template__account'>
	<Card user={user}/>
	<div className='client_wrap'>
		<h2>Текущие заявки</h2>
		<div className='changes'>
        {activeApplications.map(
            app => {
                return(
                <span className='change'>
                      <div>Номер: {app.number}</div>
                      <div>Услуга: { services.find(st => st.id == app.service).title }</div>
                      <div>Текущий статус: { stautses.find(st => st.id == app.current_status).title }</div>
                </span>)})}
		</div>
		<h2>Завершенные заявки</h2>
		<div className='changes'>
        {finishApplications.map(
            app => {
                return(
                <span className='change'>
                      <div>Номер: {app.number}</div>
                      <div>Услуга: { services.find(st => st.id == app.service).title }</div>
                      <div>Текущий статус: { stautses.find(st => st.id == app.current_status).title }</div>
                </span>)})}
		</div>
    </div>
	</div>
);
}



//{/*
//   return (
//     <div >
//         <div>
//             <div>{user.name} {user.patronymic} {user.surname}</div>
//             <div>{user.email}</div>
//         </div>
//         <div>
//             My applications
//             <div>
//               <h2>Active</h2>
//               <div>
//                 {
//                   activeApplications?.map( app => {
//                     return (
//                       <div>
//                         <span>{app.number}</span>||
//                         <span>{ services.find(st => st.id == app.service).title }</span>||
//                         <span>{ stautses.find(st => st.id == app.current_status).title ?  stautses.find(st => st.id == app.current_status).title : null }</span>||
//                       </div>
//                     )
//                   }
//                   )
//                 }
//               </div>
//             </div>
//             <div>
//               <h2>Closed</h2>
//               {
//                   finishApplications?.map( app => {
//                     return (
//                       <div>
//                         <span>{app.number}</span>||
//                         <span>{ services.find(st => st.id == app.service).title }</span>||
//                         <span>{ stautses.find(st => st.id == app.current_status).title ?  stautses.find(st => st.id == app.current_status).title : null }</span>||
//                       </div>
//                     )
//                   }
//                   )
//                 }
//             </div>
//         </div>
//   </div>
//   )
// }
 // /*} //