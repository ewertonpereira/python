import { styled } from "@mui/material";

export const ListStyled = styled('ul')`
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    padding: ${({theme}) => theme.spacing(10, 2, 10, 2)}; // base 8 -> 10x8=80, 2x8=16
    display: grid;
    grid-template-columns: 1fr 1fr;

`;

export const ItemList = styled('li')`
    list-style: none;
`;

export const Picture = styled('img')`
    width: 100%;
`;

export const Information = styled('div')`

`;

export const Name = styled('h3')`
    margin: ${({theme}) => theme.spacing(2, 0, 0, 0)};
    // margin: 16px 0 0 0;
`;

export const Value = styled('p')`
    margin: 0;
    font-weight: bold;
    color: ${({theme}) => theme.palette.primary.main } ;
`;

export const Description = styled('p')`
    word-break: break-word;
`;