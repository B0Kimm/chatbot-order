import React from 'react';
import { Provider } from 'react-redux'
//import TodoInput from './compoenets/Todoinput'
//import TodoList from './compoenets/TodoList'
import store from './store/index.js'
import AddressForm from './compoenets/AddressForm'
//import Checkout from './compoenets/Checkout'
//import PaymentForm from './compoenets/PaymentForm'
//import OrderReview from './compoenets/OrderReview'
//import Basket from './compoenets/Basket'


const App = () => {
  return <>
  <Provider store = {store}>
  <div style = {{width : "1000px", margin: "0 auto"}}>
      {/* <Basket/> */}
      <AddressForm/>
      {/* <Checkout/> */}
      {/* <PaymentForm/> */}
      {/* <OrderReview/> */}
    </div></Provider>
    </>
}

export default App;
