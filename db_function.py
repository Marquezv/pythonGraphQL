from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from models import Pessoa, Livro, engine


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

def create_livro(titulo: str, pessoa_id: int):
    livro = Livro(titulo=titulo, pessoa_id=pessoa_id)
    with Session(engine) as session:
        session.add(livro)
        session.commit()
        session.refresh(livro)

    return livro



def all_livro() -> list[Livro]:
    query = select(Livro).options(joinedload('*'))
    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    # Force eager
    # import pdb; pdb.set_trace();
    # Nao faca isso

    return result


