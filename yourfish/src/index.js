import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import axios from 'axios';
// axios withCredentials 전역설정, refreshToken 쿠키를 주고받기 위함
axios.defaults.withCredentials = true;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);