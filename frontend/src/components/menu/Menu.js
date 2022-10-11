import React from "react";
import {BrowserRouter, Route, Routes, Link, Navigator} from 'react-router-dom';

import './Menu.css';

function Menu() {
    return (
        <section className="header">
            <section className="header__navbar">
                <li className="navbar-item">
                    <Link to="/">Домой</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/projects">Проекты</Link>
                </li>
                <li className="navbar-item">
                    <Link to="/todos">Тикеты</Link>
                </li>

                {/* <a href="/" className="navbar-item">Домой</a>
                <a href="/projects" className="navbar-item">Проекты</a>
                <a href="#" className="navbar-item">Записки</a>
                <a href="#" className="navbar-item">Профиль</a>
                <a href="#" className="navbar-item">Контакты</a> */}
            </section>
        </section>
    )
}

export default Menu;