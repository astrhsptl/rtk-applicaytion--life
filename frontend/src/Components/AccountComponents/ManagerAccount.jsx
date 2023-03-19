import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { useLocation, useNavigate, Navigate, Link } from 'react-router-dom';
import Footer from '../../UI/Footer';
import Header from '../../UI/Header';

import '../../styles/cp.css';
import logo from '../../images/image 3.png';
import Card from '../Card';

export default function ManagerAccount({ user }) {
  const navigator = useNavigate()


  return (
    <>
      <Card user={user}/>
      {/* <div>
        <button onClick={()=>(navigator('/applications'))}>Заявки</button>
        <button onClick={()=>(navigator('/userlist'))}>Аккаунты</button>
      </div> */}
    </>
  )
}
