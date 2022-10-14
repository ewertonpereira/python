import { useState } from "react";
import Person from "../../@types/person";

export function useIndex(){
    const [listPeople, setListPeople] = useState<Person[]>(
        [
            {
              id: 1,
              name: 'Ewerton 1',
              picture: "https://github.com/ewertonpereira.png",
              description: 'O cara mais foda que você irá conhecer!',
              hour_value: 100
            },
            {
              id: 2,
              name: 'Ewerton 2',
              picture: "https://github.com/ewertonpereira.png",
              description: 'O cara mais foda que você irá conhecer!',
              hour_value: 100
            },
            {
              id: 3,
              name: 'Ewerton 3',
              picture: "https://github.com/ewertonpereira.png",
              description: 'O cara mais foda que você irá conhecer!',
              hour_value: 100
            },
            {
              id: 4,
              name: 'Ewerton 4',
              picture: "https://github.com/ewertonpereira.png",
              description: 'O cara mais foda que você irá conhecer!',
              hour_value: 100
            },
        ]
    );
    return {
        listPeople
    }
}