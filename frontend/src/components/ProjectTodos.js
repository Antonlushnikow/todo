import React, { useEffect, useState } from "react";
import axios from "axios";


const TodoItem = ({todo}) => {
    return(
        <tr>
            <td>{todo.body}</td>
            <td>{todo.project}</td>
            
        </tr>
    )

}


const ProjectTodoList = ({projectId}) => {
    const [todos, setTodos] = useState();

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/todo/')
        .then(response => {
          setTodos(response.data.results);
          console.log(response.data);
        }).catch(error => console.log(error));
    }, []);
    
    if (todos) {
        let filter_todos = todos.filter((todo) => todo.project.includes(parseInt(projectId)));  

        return (
            <table>
                <thead>            
                    <tr>
                        <th>Текст</th>
                        <th>Проект</th>
                    </tr>
                </thead>
                <tbody>
                    {filter_todos.map((todo) => <TodoItem todo={todo} />)}
                </tbody>
            </table>
        )
    }

}

export default ProjectTodoList;