import pandera as pa
from pandera.typing import Series
from pandera import DataFrameModel


class ProdutoSchema(DataFrameModel):

    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int]
    preco: Series[float]
    categoria: Series[str]

    class Config:
        coerce = True