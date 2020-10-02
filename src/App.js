import React from 'react';
import { Provider } from 'react-redux'
//import TodoInput from './compoenets/Todoinput'
//import TodoList from './compoenets/TodoList'
import store from './store'
import Signup from './compoenets/Signup'


const App = () => {
  return <>
  <Provider store = {store}>
  <div style = {{width : "1000px", margin: "0 auto"}}>
      <Signup/>
    </div></Provider>
    </>
}

export default App;
