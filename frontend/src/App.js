import React from 'react';

import {BrowserRouter, Route, Routes, Link, Navigator} from 'react-router-dom';

import './App.css';
import UserList from './components/User';
import ProjectList from './components/Projects';
import ProjectDetails from './components/Project';
import TodoList from './components/Todo';
import NotFound404 from './components/NotFound404';
import { Menu, Footer } from './components';


class App extends React.Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
      <div className="container">            
        <BrowserRouter>
          <Menu />
          <Routes>
            <Route exact path='/' element={<UserList />} />

            <Route path='/projects'>
              <Route index element={<ProjectList />} />
              <Route path=':projectId' element={<ProjectDetails />} />
            </Route>
            
            <Route exact path='/todos' element={<TodoList />} />
            <Route path='*' element={<NotFound404 />} />
          </Routes>            
          <Footer />
        </BrowserRouter>              
      </div>
    )
  }
}

export default App;
