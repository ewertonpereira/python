import { useEffect, useState } from "react";
import Person from "../../@types/person";
import { ApiService } from "../../services/ApiService";

export function useIndex(){
    const [listPeople, setListPeople] = useState<Person[]>([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [personChoice, setPersonChoice] = useState<Person | null>(null);

    
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
        setEmail,
        personChoice,
        setPersonChoice
    }
}