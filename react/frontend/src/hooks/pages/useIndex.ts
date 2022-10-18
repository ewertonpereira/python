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

    function markClass(){
        if(personChoice != null){
            if(validateDataClass()){
                ApiService.post('/people/' + personChoice.id + '/classes', {
                    name,
                    email
                }).then(() => {
                    setPersonChoice(null);
                    alert('Cadastrado com sucesso!')
                }).catch((error) => {
                    alert(error.response?.data.message);
                })
            }
        }
    }

    function validateDataClass(){
        return name.length > 0 && email.length > 0;
    }

    return {
        listPeople,
        name,
        setName,
        email,
        setEmail,
        personChoice,
        setPersonChoice,
        markClass
    }
}