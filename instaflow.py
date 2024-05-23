pip install instaloader
import instaloader

# Crear una instancia de Instaloader
L = instaloader.Instaloader()

# Iniciar sesión en Instagram (necesitarás tus credenciales)
username = 'tu_usuario'
password = 'tu_contraseña'
L.login(username, password)

# Obtener el perfil de la cuenta deseada
target_profile = 'nombre_de_usuario_a_obtener'
profile = instaloader.Profile.from_username(L.context, target_profile)

# Obtener y guardar los seguidores en una lista
followers = []
for follower in profile.get_followers():
    followers.append(follower.username)

# Imprimir el listado de seguidores
print(f"Seguidores de {target_profile}:")
for follower in followers:
    print(follower)
