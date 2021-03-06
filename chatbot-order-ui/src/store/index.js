import {createStore} from 'redux'
import addrReducer from './addrReducer'
import checkReducer from './checkReducer'
import payReducer from './payReducer'
import pricingReducer from './pricingReducer'

const store = createStore(addrReducer)

export default store
