import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import getCookies from '../utils/cookies';

export default function ChangesBar({changes, statuses, staff}) {
  let {id} = useParams(); 
  
  useEffect(() => {

  }, [])
  
  return (
    <div className='changes'>
        {changes.map(
            change => {
                return(
                <span className='change'>
                      <div>Наименование: { staff.find(st => st.id == change.manager).username }</div>
                      <div>Дата: {change.create_entry }</div>
                      <div>Прошлый статус: { statuses.find(st => st.id == change.former_status).title }</div>
                      <div>Текущий статус: { statuses.find(st => st.id == change.current_status).title}</div>
                </span>
              )
            }
        )}
    </div>
  )
}
