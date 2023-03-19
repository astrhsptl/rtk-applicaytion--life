import React, { useState } from 'react'
import axios from 'axios';
import Header from '../../UI/Header'
import Input from '../../UI/Input'
import api_paths from '../../utils/APIMap';
import capitalizeFirstLetter from '../../utils/utils';
import { Link, useNavigate } from "react-router-dom";
import Footer from '../../UI/Footer';
import '../../styles/register.css';

export default function RegisterPage() {
  const navigate = useNavigate();
  let [inputData, setInputData] = useState({
    name: '',
    surname: '',
    username: '',
    email: '',
    password: '',
    itn: '',
  });

  async function APIRequest() {
    inputData.status=1
    inputData.itn = parseInt(inputData.itn)
    let resp = await axios.post("http://v1738409.hosted-by-vdsina.ru/api/v1/docs/auth/register/", inputData);
    await resp.status === 200 ? Object.keys(resp.data).map( responseParametr => (document.cookie=`${responseParametr}=${resp.data[responseParametr]}`)) : console.log();

    await console.log(document.cookie); 
    return navigate('/account');
  };

  return (
    <div>
      <Header></Header>
      <div>
        {/* {Object.keys(inputData).map(currentInputName => (
          <Input 
            key={currentInputName}
            type={currentInputName} 
            placeholderName={capitalizeFirstLetter(currentInputName)} 
            onChange={e => setInputData({ ...inputData, [currentInputName]: e.target.value })}>  
          </Input>))}

        <button onClick={APIRequest}>Register</button> */}
		<main className="main">
			<div className="main_body">
				<div className="main_column main-1">
					<div className="main_item-left_block">
						<div className="left_block-content">
							<div className="content_circle"><img src="img/логотип без текста.png" alt="logo"/></div>
							<div className="content_text">
								<div className="text_title">Личный кабинет</div>
								<div className="text_subtitle">Персональный помощник<br/>в цифровом мире Ростелекома</div>
							</div>
						</div>
					</div>
				</div>
				<div className="main_column">
					<div className="main_item-right_block">
						<div className="right_block-content">
							<div className="content_title">Регистрация</div>
							<div className="content_block-input">
								<form action="#">
								<div className="content_subtitle-personaldata">Личные данные</div>
								<div className="block-input__input-name">
									<input className="input" type="text" name="Фамилия" id="Фамилия" placeholder="Фамилия" onChange={e => setInputData({ ...inputData, surname: e.target.value })} />
								</div>
								<div className="block-input__input-surname">
									<input className="input" type="text" name="ИНН" id="ИНН" placeholder="ИНН"  onChange={e => setInputData({ ...inputData, itn: parseInt(e.target.value) })}/>
								</div>
								<div className="block-input__input-company">
									<input className="input" type="text" name="company" id="company" placeholder="Название компании" onChange={e => setInputData({ ...inputData, username: e.target.value })} />
								</div>
								<div className="content_subtitle-logindata">Данные для входа</div>
								<div className="block-input__input-email">
									<input className="input" type="email" name="email" id="email" placeholder="E-mail" onChange={e => setInputData({ ...inputData, email: e.target.value })}/>
								</div>
								<div className="block-input__input-password">
									<input className="input" type="password" name="password" id="password" placeholder="Пароль" onChange={e => setInputData({ ...inputData, password: e.target.value })}/>
								</div>
								</form>
							</div>
							<button className="content_button" onClick={APIRequest}>
								<span>Зарегистрироваться</span>
							</button>
							<div className="content_conditions">
								Нажимая кнопку «Войти», вы принимаете условия <br/><Link to="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html">пользовательского соглашения</Link> 
							</div>
							
						</div>
					</div>
				</div>
			</div>
		</main>
      </div>  
      <Footer />
  </div>
  )
}