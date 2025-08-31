import sys
import ast

def saddle_points(matrix):
    # Verificar si la cuadrícula es válida
    if not matrix:  # Si la cuadrícula está vacía, no hacemos nada
        return []
    
    expected_length = len(matrix[0])  # Longitud de la primera fila como referencia
    i = 1  # Índice para recorrer las filas restantes
    
    while i < len(matrix):
        if len(matrix[i]) != expected_length:
            raise ValueError('irregular matrix')
        i += 1  # Avanzamos a la siguiente fila

    # Diccionarios para almacenar los índices
    tall_trees = {}
    short_trees = {}
    
    # Encontrar los máximos en cada fila
    for row, fila in enumerate(matrix):
        max_value = max(fila)  # Usar max() para simplificar
        max_indices = [col for col, value in enumerate(fila) if value == max_value]
        tall_trees[row] = max_indices

    # Encontrar los mínimos en cada columna
    for col in range(len(matrix[0])):
        col_values = [matrix[row][col] for row in range(len(matrix))]
        min_value = min(col_values)  # Usar min() para simplificar
        min_indices = [row for row, value in enumerate(col_values) if value == min_value]
        short_trees[col] = min_indices

    # Encontrar los puntos de silla
    result = []
    for row, cols in tall_trees.items():
        for col in cols:
            if row in short_trees[col]:
                result.append({"row": row + 1, "column": col + 1})

    return result

if __name__ == "__main__":
    try:
        # Verificar si se proporcionó un argumento
        if len(sys.argv) != 2:
            print('Uso: python saddle_points.py "[[fila1], [fila2], ...]"')
            print('Ejemplo: python saddle_points.py "[[6, 7, 8], [5, 5, 5], [7, 5, 6]]"')
            sys.exit(1)
        
        # Convertir el argumento de la consola en una matriz
        matrix = ast.literal_eval(sys.argv[1])
        
        # Validar que la entrada sea una lista de listas de números
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError('La entrada debe ser una lista de listas')
        
        if not matrix or not all(len(row) > 0 for row in matrix):
            raise ValueError("La matriz no puede estar vacía")
        
        # Validar que todos los elementos sean números
        for row in matrix:
            for elem in row:
                if not isinstance(elem, (int, float)):
                    raise ValueError('Todos los elementos deben ser números')
        
        # Llamar a la función saddle_points
        result = saddle_points(matrix)
        
        # Mostrar resultados
        if result:
            print('Puntos de silla encontrados:')
            for point in result:
                print(f'Fila: {point["row"]}, Columna: {point["column"]}')
        else:
            print('No se encontraron puntos de silla.')
            
    except ValueError as e:
        print(f'Error: {e}')
    except SyntaxError:
        print('Error: Formato de entrada inválido. Use una lista de listas válida, como "[[6, 7, 8], [5, 5, 5], [7, 5, 6]]"')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')