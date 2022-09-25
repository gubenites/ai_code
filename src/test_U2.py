from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from U2 import U2

def test_menor_caminho():
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g <= 17

def test_larry():
    '''
        Este teste leva em consideração que o integrante mais lento da banda é o unico que se
        encontra do lado da ponte em que esta a lampada, tornando então o tempo de resolução do
        problema maior do que o tempo em que os mesmos tem para chegar ao show.
    '''

    state = U2(False, False, False, False, True, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    assert result.g > 17

def test_lado_direito():
    '''
        Este teste faz a consideração que todos os membros da banda se encontram do lado direito
        da ponte, enquanto a lanterna esta do lado esquerdo, tornando então a solução impossivel. 
    '''

    state = U2(True, True, True, True, True, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    assert result == None

    
def test_lado_esquerdo():
    '''
        Este teste faz a consideração que todos os membros da banda se encontram do lado esquerdo
        da ponte, enquanto a lanterna esta do lado direito, tornando então a solução impossivel. 
    '''

    state = U2(False, False, False, False, False, True, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    assert result == None