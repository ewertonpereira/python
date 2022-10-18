import { Box, Button, Dialog, DialogActions, Grid, Snackbar, TextField } from '@mui/material'
import type { NextPage } from 'next'
import List from '../src/components/List/List'
import { useIndex } from '../src/hooks/pages/useIndex';


const Home: NextPage = () => {
  const  { 
    listPeople, 
    name, 
    setName, 
    email, 
    setEmail, 
    personChoice, 
    setPersonChoice,
    markClass,
    message,
    setMassage
  } = useIndex();

  return (
    <div>
      <Box sx={{backgroundColor: 'secondary.main'}}>
        <List people={listPeople}
          onSelect={(person) => setPersonChoice(person)}
        ></List>
      </Box>

      <Dialog onClose={() => setPersonChoice(null)} open={personChoice != null} fullWidth PaperProps={{sx: {p: 5}}}>
        <Grid container spacing={2}>
          <Grid item xs={12}>
            <TextField
              label='Digite o nome'
              type='text'
              fullWidth
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              label = 'Digite o email'
              type='email'
              fullWidth
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </Grid>
        </Grid>

        <DialogActions sx={{mt: 5}}>
          <Button onClick={() => setPersonChoice(null)}>Cancelar</Button>
          <Button onClick={() => markClass()}>Marcar</Button>
        </DialogActions>
      </Dialog>

      <Snackbar 
        message={message} 
        open={message.length > 0}
        autoHideDuration={2500}
        onClose={() => setMassage('')}
      />
    </div>
  )
}

export default Home
