from sqlmodel import Session, select
from models import Pessoa, engine


def create_pessoa(idade: int, nome: str):
    pessoa = Pessoa(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(pessoa)
        session.commit()
        session.refresh(pessoa)

    return pessoa

def all_pessoa() -> list[Pessoa]:
    query = select(Pessoa)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result


