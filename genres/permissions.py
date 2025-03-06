from rest_framework import permissions



class GenrePermissionClass(permissions.BasePermission): # classe de permissão personalizada
    # sobresscrevendo o método has_permission(polimorfismo)    
    def has_permission(self, request, view): # request é o obj de requisição que chega com varias infos
        # escrever a lógica de permissão/regra de negócio
        if request.method in ['GET','OPTIONS','HEAD']:
            return request.user.has_perm('genres.view_genres')
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genres') # verificando se o user tem permissão para adicionar um novo genre
        if request.method in ['PATCH','PUT']:
            return request.user.has_perm('genres.change_genres')
        if request.method == 'DELETE':
            return request.user.hs_perm('genres.delete_genres')
        return False
    

# print(request.user) saida: Jose \n Forbidden: /api/v1/genres/
# para saber se um user tem permissão para determinada ação, basta olhar no painel de admin, caso queira add uma permissão, é por lá tbm 