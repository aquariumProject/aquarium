import React from 'react'
import '../styles/register.css'
import sidefish from '../images/login/fish.png'
import logo from '../images/userfeed/logo.png'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

const Register = () => {
  let [id, setId] = useState('');
  let [pw, setPw] = useState('');
  let [repw, setRepw] = useState('');
  let [name, setName] = useState('');
  let [nickname, setNickname] = useState('');

  const idInput = (e) => {
    setId(e.target.value)
  }
  const pwInput = (e) => {
    setPw(e.target.value)
  }
  const repwInput = (e) => {
    setRepw(e.target.value)
  }
  const nameInput = (e) => {
    setName(e.target.value)
  }
  const nicknameInput = (e) => {
    setNickname(e.target.value)
  }

  //이메일 & 패스워드 & 닉네임 유효성 검사, 조건은 아래 폼 문구에 있는 내용과 동일
  //이름은 최소 2글자 이상 시에만 버튼 활성화
  const nicknameValidation = /^[가-힣a-z]{4,16}$/;
  const emailValidation = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
  const pwValidation = /^.*(?=^.{8,16}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[~,!,@,#,$,*,(,),=,+,_,.,|]).*$/;
  const [button, setButton] = useState(true);
  const changeButton = () => {
    (emailValidation.test(id.trim())) && (pwValidation.test(pw.trim())) && (pw === repw) && (nicknameValidation.test(nickname.trim()) && (name.length > 1))
    ? setButton(false) : setButton(true);
  }
  
  const navigate = useNavigate();
  const goToMain = () => {
    navigate('/');
  };

  // 계정 정보 중복은 어떻게 해결?
  // 일단 임시 서버 열어서 사용함
  const signUp = () => {
    const data = {
      username : name,
      password : pw,
      password2 : repw,
      email : id,
      nickname : nickname
    };
    axios.post("http://127.0.0.1:8000/members/register/" , data)
    .then((response) => {
      console.log(response);
      if(response.status === 201) {
        localStorage.setItem("userid", id);
        localStorage.setItem("userpw", pw);
        localStorage.setItem("username", name);
        localStorage.setItem("userNickname", nickname);
        alert('회원가입이 완료되었습니다! 환영합니다 :)');
        goToMain(); 
      }
    })
    .catch((error) => console.log(error.response));
  }
   
  return (
    <div>
       <section>
            <div className="section__login">
                <div className="section__login__side">
                    <div className="section__login__side__image">
                        <input className="section__login__side__image1" src={sidefish} type="image"/>
                        <input className="section__login__side__image2" src={sidefish} type="image"/>
                        <input className="section__login__side__image3" src={sidefish} type="image"/>
                    </div>
                </div>
            <div className="section__login__center">
                <input className="section__login__center--logo" src={logo} type="image"/>
                <div className="section__login__center--id">이메일<br/>
                    <input onChange={idInput} onKeyUp={changeButton} placeholder='아이디를 입력해주세요' className="section__login__center--idinput"/>
                </div>
                <div className="section__login__center--pw"><span>비밀번호</span><span className='section__login__center--side'>영문 대소문자/숫자/특수문자 포함 8자~16자</span><br/>
                    <input onChange={pwInput} onKeyUp={changeButton} maxLength="16" type="password" placeholder='비밀번호를 입력해주세요' className="section__login__center--idinput"/>
                </div>
                <div className="section__login__center--pw">비밀번호 확인<br/>
                    <input onChange={repwInput} onKeyUp={changeButton} maxLength="16" type="password" placeholder='비밀번호를 다시 한 번 입력해주세요' className="section__login__center--idinput"/>
                </div>
                <div className="section__login__center--pw">이름<br/>
                    <input onChange={nameInput} onKeyUp={changeButton} placeholder='이름을 입력해주세요' className="section__login__center--idinput"/>
                </div>
                <div className="section__login__center--pw"><span>닉네임</span><span className='section__login__center--side1'>영문 소문자&한글 아무렇게 4자~16자</span><br/>
                    <input onChange={nicknameInput} onKeyUp={changeButton} maxLength="16" placeholder='닉네임을 입력해주세요' className="section__login__center--idinput"/>
                </div>
                <button disabled={button} onClick={signUp} className="section__login__center--loginbtn">회원가입</button>
            </div>
          </div>
      </section>
    </div>
  )
}

export default Register