import { Button } from "@mui/material";
import Person from "../../@types/person";
import { Description, EmptyList, Information, ItemList, ListStyled, Name, Picture, Value } from "./List.style";

interface ListProps{
    people: Person[],
}

const List = (props: ListProps) => {
    return  (
        <div>
            {props.people.length > 0 ? (
                <ListStyled>
                {props.people.map(person => (
                    <ItemList key={person.id}>
                    <Picture src={person.picture}></Picture>
                    <Information>
                        <Name>{person.name}</Name>
                        <Value>{person.hour_value.toLocaleString('pt-BR', {minimumFractionDigits: 2, style: 'currency', currency: 'BRL'})} por hora</Value>
                        <Description>{person.description}</Description>
                        <Button sx={{width: '70%'}}>Marcar encontro com {person.name}</Button>
                    </Information>
                </ItemList>
                ))}
            </ListStyled>
            ) : (
                <EmptyList>Nenhum item encontrado</EmptyList>
            )}
        </div>
    )
}

export default List;