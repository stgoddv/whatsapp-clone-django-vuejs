# para private:

# que no se pueda crear si no están campos kind y / o participants

# que no se pueda crear si kind es incorrecto (no existe)

# que no se pueda crear si participants esta vacio

# que no se pueda crear si participants tiene ids inexistentes

# que no se pueda crear si participants solo tiene seleccionado al autor

# no se pueda crear si está seleccionado 2 o mas aparte del autor

# no se pueda crear si está seleccionado 2 o mas con autor

# si hay 1 seleccionado aparte de autor devolver ese uno + autor

# si hay 1 seleccionado + autor permitir creacion y devolver ese uno + autor

# si creo un grupo privado que ya existe, se devuelve ese grupo privado pero
# al hacer el get no aparece duplicado

# si creo un grupo privado que no existe, entonces ahora si aparece ese nuevo grupo
# al hacer el get


# para group:

# lo mismo que antes pero

# Si hay uno + autor permitir

# si hay uno aparte de autor permitir

# si hay 2 aparte de autor permitir

# si hay 2 con autor permitir

# Verificar creacion de varios grupos duplicados


# timestamp de actividad - verificar que el envio de mensaje actualiza el timestamp

# verificar que lo mas reciente llegue antes que lo menos reciente

# verificar que mensajes sobre el limite no llegan pero bajo el limite si

# verificar que efectivamente llegue el ultimo mensaje de cada room, y no otro

# verificar que el usuario pertenece a todas las rooms que llegan

# Verificar autorización
