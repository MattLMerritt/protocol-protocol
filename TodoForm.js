import React, {useState} from 'react'

export const TodoForm = ({addTodo}) => {
      const [value, setValue] = useState("")

      const handleSubmit = e => {
        e.preventDefault();

        addTodo(value)
        
        setValue("")
      }
    return (
        <form className='TodoForm' onSubmit={handleSubmit}>
            <input type = "text" classname= 'todo-input' value={value} placeholder='What is the task today?' onChange={(e) => setValue(e.target.setValue)}/>
            <button type='submit ' className='todo-btn'>AddTask</button>
        </form>
    )
}