import React from "react";
import axios from 'axios';
import {Link} from "react-router-dom";
import { useState, useEffect } from "react";


const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>            
            <td>                
                {project.repoLink}
            </td>
        </tr>
    )
}


const ProjectList = () => {
    const [projects, setProjects] = useState();
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {  
        setIsLoading(true);
        axios.get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
            setProjects(response.data.results);
            setIsLoading(false);            
        }).catch(error => console.log(error));
    }, [])

    console.log(projects);

    if (isLoading) {
        return (
            <div>
                Загрузка...
            </div>
        );        
    }         
    
    return projects && (
        <table>
            <thead>            
                <tr>
                    <th>Название</th>
                    <th>Ссылка</th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem project={project} />)}
            </tbody>
        </table>
    )
}

export default ProjectList;