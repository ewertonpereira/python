import { useEffect, useState } from "react";
import Person from "../../@types/person";
import { ApiService } from "../../services/ApiService";

export function useIndex(){
    const [listPeople, setListPeople] = useState<Person[]>([]);

    useEffect(() => {
        ApiService.get('/people').then((answer) => {
            setListPeople(answer.data)
        })
    }), [];

    return {
        listPeople
    }
}