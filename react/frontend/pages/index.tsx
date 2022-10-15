import { Box } from '@mui/material'
import type { NextPage } from 'next'
import List from '../src/components/List/List'
import { useIndex } from '../src/hooks/pages/useIndex';


const Home: NextPage = () => {
  const  { listPeople } = useIndex();

  return (
    <Box sx={{backgroundColor: 'secondary.main'}}>
      <List people={listPeople}></List>
    </Box>
  )
}

export default Home
