import React from 'react'
import Header from '../../UI/Header';
import { Link, useLocation } from 'react-router-dom'
import Footer from '../../UI/Footer';

import preview from '../../images/hp.png';
import '../../styles/register.css'
import '../../styles/home.css'


export default function HomePage() {
  return (
    <div className={'home'}>
      <Header path={useLocation().pathname}></Header>
      <div className='wrapper wrapper__home'>
        <div className='preview' style={{backgroundImage: preview}}>

          <div className='image__p'>
            <img src={preview} />
          </div>

          <div className='content__preview'>
              <div className='text__preview'>
                Сервис для менеджеров, уставших постоянно выглядывать данные из километровых табличек
              </div>
              <div className='button-conteiner'>
                <Link to='/login'><div className='button_preview'>Вход</div></Link>
                <Link to='/register'><div className='button_preview'>Регистрация</div></Link>
              </div>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </div>
  );
};