import React, {useState} from 'react'

export const TodoForm = () => {
      const [value, setValue] = useState("")

      const handleSubmit = e => {
        e.preventDefault();

        console.log(value)
      }
    return (
        <form className='TodoForm' onSubmit={handleSubmit}>
            <input type = "text" classname= 'todo-input' placeholder='What is the task today?' onChange={(e) => setValue(e.target.setValue)}/>
            <button type='submit ' className='todo-btn'>AddTask</button>
        </form>
    )
}