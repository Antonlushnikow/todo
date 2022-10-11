import axios from "axios";
import React, { useEffect, useState } from "react";

const TodoItem = ({todo}) => {
    return(
        <tr>
            <td>{todo.body}</td>
            <td>{todo.project}</td>
            
        </tr>
    )

}

const TodoList = () => {
    const [todos, setTodos] = useState();
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        setIsLoading(true);
        axios.get('http://127.0.0.1:8000/api/todo/')
        .then(response => {
          setTodos(response.data.results);
          console.log(response.data);
          setIsLoading(false);
        }).catch(error => console.log(error));
    }, []);

    if (isLoading) {
        return (
            <div>
                Загрузка...
            </div>
        );        
    } 

    return todos && (
        <table>
            <thead>            
                <tr>
                    <th>Текст</th>
                    <th>Проект</th>
                </tr>
            </thead>
            <tbody>
                {todos.map((todo) => <TodoItem todo={todo} />)}
            </tbody>
        </table>
    )
}

export default TodoList ;
