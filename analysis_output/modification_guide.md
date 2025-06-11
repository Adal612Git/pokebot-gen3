# Guía de Modificación

## Loop Principal & Lectura de Stats
El loop principal del bot se encuentra en `modules/main.py` dentro de la función `main_loop()`. Esta función gestiona los estados del juego y consulta `modules.memory.get_game_state()` y otras utilidades para leer la memoria.

La información de cada encuentro Pokémon se registra en `modules/encounter.py`, especialmente en `handle_encounter()` y `log_encounter()`.

## Ejemplo "Pidgey encontrado"
Para añadir un log en consola cuando se encuentre un Pidgey modifica `modules/encounter.py` en la función `handle_encounter()`:
```python
if pokemon.species.name == 'Pidgey':
    print(f'PIDGEY ENCONTRADO!! {pokemon.ivs}')
```

## Validación de Stats Personalizados
Puedes implementar límites de IVs/EVs en `modules/pokemon.py` o donde se crean los objetos `Pokemon`. Revisa las clases `Pokemon` y valida los valores al instanciar.

## Inyección de Botón GUI
La interfaz gráfica se gestiona principalmente en `modules/gui`. Puedes añadir un botón nuevo en los archivos de la GUI y conectar su acción con la lógica de stats utilizando las funciones de `modules.stats`.
