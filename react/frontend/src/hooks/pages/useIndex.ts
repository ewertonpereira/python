import { useEffect, useState } from "react";
import Person from "../../@types/person";
import { ApiService } from "../../services/ApiService";

export function useIndex(){
    const [listPeople, setListPeople] = useState<Person[]>([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    
    useEffect(() => {
        ApiService.get('/people').then((answer) => {
            setListPeople(answer.data)
        })
    }), [];

    return {
        listPeople,
        name,
        setName,
        email,
        setEmail
    }
}