import { Box } from '@mui/material'
import type { NextPage } from 'next'
import Person from '../src/@types/person';
import List from '../src/components/List/List'


const Home: NextPage = () => {
  const people: Person[] = [
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

  return (
    <Box sx={{backgroundColor: 'secondary.main'}}>
      <List people={people}></List>
    </Box>
  )
}

export default Home
