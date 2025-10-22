import pandera as pa
from pandera.typing import Series
from pandera import DataFrameModel # usar esse ao invés de DataFrame


class ProdutoSchema(DataFrameModel): # usar DataFrameModel ao invés de SchemaModel

    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int]
    preco: Series[float]
    categoria: Series[str]

    class Config:
        coerce = True