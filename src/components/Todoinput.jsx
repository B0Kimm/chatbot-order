import React, {useState} from 'react'
import uuid from 'uuid/v4'
import {useDispatch} from 'react-redux'
import {addTodoAction} from '../store/todoReducer'

const TodoInput = () => {
    //todo가 CRUD 대상(object)입니다. -> 속성이 된다.
    // es6 이전 모드 var
    // es6 이후 let, const 두가지로 정의/ 변수(let), 상수(const)
    // 함수는 const 타입에 할당합니다.
    // JSON = JavaScript Object Notation
    // object {a, b}, array []
    //const ['todo' : 'todo', setTodo : () => {}] = useState(0)의 축약 ver
    const [todo, setTodo] = useState('') // Todo의 타입결정함
    const dispatch = useDispatch()
    const submitForm = e => {
        e.preventDefault() //default 기능은 막고, 내가 정의한 기능을 구현하라
        const newTodo = {
            todoId: uuid(),
            name: todo,
            complete: false
        }
        addTodo(newTodo)
        setTodo("")
        document.getElementById('input').value = '' //버튼을 누르면 지워라
    }
    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }
    const addTodo = todo => {
        dispatch(addTodoAction(todo)) // 영속적으로 저장할 곳 state -> api -> db
    }
    return <>
    <h1>할일 등록</h1>
    <form onSubmit = {submitForm} method = "POST">
        <div>
            <input type="text" name="todo" id="input" onChange={handleChange}/><br/>
            <input type="submit" value="ADD TODO"/>
        </div>
    </form>
    </>
}

export default TodoInput