import React from "react";

import './Menu.css';

function Menu() {
    return (
        <section className="header">
            <section className="header__navbar">
                <a href="/" className="navbar-item">Домой</a>
                <a href="#" className="navbar-item">Записки</a>
                <a href="#" className="navbar-item">Профиль</a>
                <a href="#" className="navbar-item">Контакты</a>
            </section>

        </section>
    )

}

export default Menu;