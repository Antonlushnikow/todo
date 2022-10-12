import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

import ProjectTodoList from "./ProjectTodos";


const ProjectDetails = () => {
    const [project, setProject] = useState();
    const [isLoading, setIsLoading] = useState(false);
    const {projectId} = useParams();
    console.log(projectId); 

    useEffect(() => {  
        setIsLoading(true);
        axios.get('http://127.0.0.1:8000/api/projects/' + projectId)
        .then(response => {       
            setProject(response.data);
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
    
    return project && (
        <div>
            <h2>Информация о проекте</h2>
            <p>Название проекта: {project.name}</p>
            <p>Ссылка на репозиторий: {project.repoLink}</p>
            <p>Участники: {project.users.join(', ')}</p>
            <br />
            <div>
                <h3>Тикеты</h3>
                <ProjectTodoList projectId={projectId} />
            </div>
        </div>
    )       
    
}

export default ProjectDetails;