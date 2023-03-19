import React, { useState } from 'react'
import axios, { AxiosHeaders } from 'axios';
import { Link, useLocation, useNavigate } from 'react-router-dom'
import Header from '../../UI/Header'
import Input from '../../UI/Input'
import api_paths from '../../utils/APIMap';
import setCookie from '../../utils/cookies';
import capitalizeFirstLetter from '../../utils/utils';
import Button from '../../UI/Button';
import Footer from '../../UI/Footer';
import '../../styles/register.css';
import logo from '../../images/photo_2023-03-18_19-18-37.jpg'

export default function LoginPage() {
  let [inputData, setInputData] = useState({
    email: '',
    password: '',
  });
  let navigate = useNavigate()

  async function APIRequest(navigate, inputData) {
    let resp = await axios.post("http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/login/", inputData );
    await resp.status === 200 ? Object.keys(resp.data).map( responseParametr => (document.cookie=`${responseParametr}=${resp.data[responseParametr]}`)) : console.log();
    
    console.log(document.cookie);
    return navigate('/account')
  };


  return (
    <div class="wrapper">

      <Header path={useLocation().pathname}></Header>
      <main class="main">
        <div class="main_body">
          <div class="main_column main-1">
            <div class="main_item-left_block">
              <div class="left_block-content">
                <div class="content_circle"><img src={logo} alt="logo" /></div>
                <div class="content_text">
                  <div class="text_title">Личный кабинет</div>
                  <div class="text_subtitle">Персональный помощник<br />в цифровом мире Ростелекома</div>
                </div>
              </div>
            </div>
          </div>
          <div class="main_column">
            <div class="main_item-right_block">
              <div class="right_block-content">
                <div class="content_title">Авторизация</div>
                <div class="content_block-input">
                  <form action="#">
                  <div class="block-input__input-email">
                    <Input class="input" type="email" name="email" id="email" placeholderName="E-mail" onChange={e => setInputData({ ...inputData, email: e.target.value })} />
                  </div>
                  <div class="block-input__input-password">
                    <Input class="input" type="password" name="password" id="password" placeholderName="Пароль" onChange={e => setInputData({ ...inputData, password: e.target.value })} />
                  </div>
                  </form>
                </div>
                <button class="content_button" onClick={() => (APIRequest(navigate, inputData))}>
                  <span>Войти</span>
                </button>
                <div class="content_conditions">
                  Нажимая кнопку «Войти», вы принимаете условия <br /><Link to="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html">пользовательского соглашения</Link> 
                </div>
                <div class="content_registration">
                  Нет аккаунта? <Link to="/register">Зарегистрироваться</Link> {/* Перепилить!!! */}
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
  </div>
  )
}
