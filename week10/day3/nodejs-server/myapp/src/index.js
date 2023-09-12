import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Events from './Events';
import Phone from './Phone';
import Color from './Color';
// import Text from './Text';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Events />
    <Phone />
    <Color />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
