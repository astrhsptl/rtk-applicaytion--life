import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/register.css';

export default function Footer() {
  return (
    <footer className="footer">
        <div className="footer_conteiner">
            <div className="footer_text">
                <p className="text_pao text">© 2023 ПАО «Ростелеком». 18+</p>
                <p className="text_policy text">Продолжая использовать наш сайт, вы даете согласие на обработку файлов <br />
                    Cookies и других пользовательских данных, в соответствии с <Link to="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html">Политикой <br />
                        конфиденциальности</Link> и <Link to="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html">Пользовательским соглашением</Link></p>
                <div className="footer_support">
                    <div className="support_text text">Служба поддержки</div>
                    <div className="support_tel">8 800 100 0 800</div>
                </div>
            </div>
        </div>
    </footer>
  )
}
