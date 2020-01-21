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


# Nombre de grupo

# Verificar que puedo crear private sin nombre y queda en null

# verificar que private con nombre queda en null tambien

# verificar que no puedo crear group sin nombre

# verificar que puros espacios cuenta como sin nombre

# verificar que grupo con nombre queda ok


# Recents

# si se crea un mensaje y no se ha visto en recents entonces se debe ver en mensajes pendientes

# si se crea un mensaje y se ve en recents -> no debe aparecer en pendientes


# Mark room as read

# Que efectivamente pueda marcar los mensajes de una room como leidos

# Que toda la room quede como leido para mi y no para los demás


# Delete room

# que se pueda eliminar la room si el usuario pertenece a ella

# que no lo pueda hacer si no pertenece

# que efectivamente si es private entonces la relacion de amistad se acabe


# Profile

# que si es privado entonces se retorne el perfil correcto del usuario contrario
