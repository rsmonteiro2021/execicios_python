"""
Perfil do Usuário: Comece com uma cópia de user_profile.py, da página 210. Crie
um perfil seu chamado build_profile(), usndo seu primeiro nome e o sobrenome,
além de três outros pares chave_valor que o descrevam.
"""
def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Roberto', 'Monteiro', Profissão = 'Engenheiro Civil', Idade = 42, Estado_Civil = 'Casado')
for key, value in user_profile.items():
    print(f'{key}: {value}')