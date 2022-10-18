import { useEffect, useState } from "react";
import Person from "../../@types/person";
import { ApiService } from "../../services/ApiService";

export function useIndex(){
    const [listPeople, setListPeople] = useState<Person[]>([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [personChoice, setPersonChoice] = useState<Person | null>(null);
    const [messagem, setMassage] = useState('');

    
    useEffect(() => {
        ApiService.get('/people').then((answer) => {
            setListPeople(answer.data)
        })
    }), [];

    useEffect(() => {
        cleanForm();
    }, [personChoice]) ;

    function markClass(){
        if(personChoice !== null){
            if(validateDataClass()){
                ApiService.post('/people/' + personChoice.id + '/matches', {
                    name,
                    email
                }).then(() => {
                    setPersonChoice(null);
                    setMassage('Cadastrado com sucesso!');
                }).catch((error) => {
                    setMassage(error.response?.data.message);
                });
            } else {
                setMassage('Preencha os dados corretamente.');
            }
        }
    }

    function validateDataClass(){
        return name.length > 0 && email.length > 0;
    }

    function cleanForm(){
        setName('');
        setEmail('');
    }

    return {
        listPeople,
        name,
        setName,
        email,
        setEmail,
        personChoice,
        setPersonChoice,
        markClass,
        messagem,
        setMassage
    }
}