import { Button } from "@mui/material";
import Person from "../../@types/person";
import { FormatadorService } from "../../services/FormatadorService";
import { Description, EmptyList, Information, ItemList, ListStyled, Name, Picture, Value } from "./List.style";

interface ListProps{
    people: Person[],
    onSelect: (person: Person) => void
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
                        <Value>{FormatadorService.valorMonetario(person.hour_value)} por hora</Value>
                        <Description>{FormatadorService.limitarTexto(person.description, 200)}</Description>
                        <Button onClick={() => props.onSelect(person)} sx={{width: '70%'}}>Marcar encontro com {person.name}</Button>
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