import React from 'react'
import '../styles/nav.css'
import logo from '../images/userfeed/logo.png'
import search from '../images/userfeed/search.png'
import { Link } from 'react-router-dom'
//로그인 이후 보이는 네비바

const LoginNav = () => {
  return (
    <div>
        <header className="header">
        <div className="header__wrapper">
            <Link to="/"><img className="header__title" src={logo}/></Link>
           
            <div className="header__center">
                <form className="header__form" onsubmit="return false">
                    <input className="header__input--text" placeholder="검색어를 입력해주세요!"/>
                    <Link to="/Search"><input className="header__input--button" src={search} type="image"/></Link>
                </form>
            </div>

            <div className="header__end">
                <li>
                    <button className="header__end--btn"><Link to="/Store" style={{textDecoration:'none', color:'inherit'}}>스토어</Link></button>
                </li>
                <li>
                    <button className="header__end--btn"><Link to="/QA" style={{textDecoration:'none', color:'inherit'}}>질문게시판</Link></button>
                </li>
                <li>
                    <button className="header__end--btn custom-btn login"><Link to="/" style={{textDecoration:'none', color:'inherit'}}>로그아웃</Link></button>
                </li>
                <li>
                    <button className="header__end--btn custom-btn register"><span><Link to="/MyPage" style={{textDecoration:'none', color:'inherit'}}>마이페이지</Link></span></button>
                </li>
            </div>
        </div>
        </header>
    </div>
  )
}

export default LoginNav