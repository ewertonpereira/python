import { Button } from "@mui/material";
import { Description, Information, ItemList, ListStyled, Name, Picture, Value } from "./List.style";

const List = () => {
    return  (
        <ListStyled>
            <ItemList>
                <Picture src="https://github.com/ewertonpereira.png"></Picture>
                <Information>
                    <Name>Ewerton Pereira</Name>
                    <Value>R$ 100,00 por hora</Value>
                    <Description>O cara mais foda que você irá conhecer!</Description>

                    <Button>Marcar encontro</Button>
                </Information>
            </ItemList>
            <ItemList>
                <Picture src="https://github.com/ewertonpereira.png"></Picture>
                <Information>
                    <Name>Ewerton Pereira</Name>
                    <Value>R$ 100,00 por hora</Value>
                    <Description>O cara mais foda que você irá conhecer!</Description>

                    <Button>Marcar encontro</Button>
                </Information>
            </ItemList>
        </ListStyled>
    )
}

export default List;