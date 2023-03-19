import React from 'react'

import '../styles/cp.css';
import logo from '../images/image 3.png';


export default function Card({user}) {
  return (
<div className="column_card">
    <div className="item_card card-item">
        <div className="card-item_header">
            <div className="card-item_header__content">
                <img className="card_header-logo" src={logo} alt="#"/>
                <div className="card-item_header__content-data">
                    <div className="card-item_header__content-data_login">{ user.username }</div>
                    <div className="card-item_header__content-data_email">{ user.email }</div>
                </div>
            </div>
        </div>
        <div className="card_body-personal_date">
            <div className="card_body-conteiner">
                <div className="personal_date-item">
                    <div className="personal_date_block">
                        <div className="name">{ user.name=='' ? 'Имя' : user.name }</div>
                    </div>
                    <div className="personal_date_block">
                        <div className="name">{ user.surname=='' ? 'Фамилия' : user.surname }</div>
                    </div>
                    <div className="personal_date_block">
                        <div className="name">{ user.username=='' ? 'Компания' : user.username }</div>
                    </div>
                </div>
        </div>
    </div>
</div>
</div>
  )
}
