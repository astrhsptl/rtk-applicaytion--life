import React from 'react'
import { Link } from 'react-router-dom'
import paths from '../utils/paths'
import Button from './Button'

import '../styles/register.css'
import logo from '../images/photo_2023-03-18_19-18-54.jpg';

export default function Header(props) {
  return (
    <header className="header">
      <div className="header_container">
        <div className="header_img">
          <Link to=""><img src={logo} alt="лого" /></Link>
        </div>
      </div>
		</header>
  )
}
