import axios from "axios";
import React, { useEffect, useState } from "react";


const UserItem = ({user}) => {
    return(
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>            
        </tr>
    )

}

const UserList = () => {
    const [users, setUsers] = useState();
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        setIsLoading(true);
        axios.get('http://127.0.0.1:8000/api/users/')
        .then(response => {
          setUsers(response.data);
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

    return users && (
        <table>
            <thead>            
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => <UserItem user={user} />)}
            </tbody>
        </table>
    )
}

export default UserList;