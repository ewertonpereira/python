class Customers:

    def __init__(self, name, email, plan )-> None:
        self.name = name
        self.email = email
        self.list_plan = ['basic', 'premium']
        if plan in self.list_plan:
            self.plan = plan
        else:
            raise Exception('Plano inválido.')

 
    def change_plan(self, new_plan) -> None:
        if new_plan in self.list_plan:
            self.plan = new_plan
        else:
            print('Plano inválido.')


    def watch_movie(self, movie, movie_plan) -> None:
        if self.plan == movie_plan:
            print(f'Ver filme {movie}')
        elif self.plan == 'premium':
            print(f'Ver filme {movie}')
        elif self.plan == 'basic' and movie_plan == 'premium':
            print(f'Faço um upgrade para premium para poder ver o filme {movie}')
        else:
            print('Plano inválido')
        

client = Customers('ewerton', 'ewerton@mail.com','basic')
client.change_plan('premium')
print(client.plan)
