import requests
from django.http import HttpResponse
from magias.models import Classes, Componentes, Escolas, Fonte, Magias


def magias(request):
    # Dicionário de cores para cada escola
    escolas_cores = {
        'Abjuration': '#0000FF',  # Azul
        'Conjuration': '#FFA500',  # Laranja
        'Divination': '#FFD700',   # Dourado
        'Enchantment': '#800080',  # Roxo
        'Evocation': '#FF0000',    # Vermelho
        'Illusion': '#00FFFF',     # Ciano
        'Necromancy': '#808080',   # Cinza
        'Transmutation': '#008000',# Verde
    }

    response = requests.get('https://www.dnd5eapi.co/api/spells')
    if response.status_code != 200:
        print('Erro ao acessar a API')
        return HttpResponse('Erro ao acessar a API')

    magias_data = response.json()['results']

    fontes, _ = Fonte.objects.get_or_create(nome='Livro do Jogador')
    componentes_map = {c.nome: c for c in Componentes.objects.all()}
    classes_map = {c.nome: c for c in Classes.objects.all()}
    escolas_map = {e.nome: e for e in Escolas.objects.all()}

    for magia_data in magias_data:
        detalhes_response = requests.get(f'https://www.dnd5eapi.co{magia_data["url"]}')
        if detalhes_response.status_code != 200:
            print(f'Erro ao obter detalhes da magia {magia_data["name"]}')
            continue

        detalhes_magia = detalhes_response.json()

        # Obtém ou cria a escola, com a cor associada
        escola_nome = detalhes_magia['school']['name']
        cor = escolas_cores.get(escola_nome, '#FFFFFF')  # Cor padrão se não encontrada
        escola, _ = Escolas.objects.get_or_create(nome=escola_nome, defaults={'cor': cor})

        # Obtém ou cria a magia
        magia, created = Magias.objects.get_or_create(
            nome=detalhes_magia['name'],
            defaults={
                'nivel': detalhes_magia['level'],
                'tempo_conjuracao': detalhes_magia['casting_time'],
                'duracao': detalhes_magia['duration'],
                'alcance': detalhes_magia['range'],
                'descricao': detalhes_magia['desc'][0] if detalhes_magia['desc'] else '',
                'em_nivel_mais_alto': detalhes_magia.get('higher_level', ''),
                'ritual': detalhes_magia['ritual'],
                'concentracao': detalhes_magia['concentration'],
                'ataque_magico': False,
                'tipo_dado': '',  # Adicione lógica para definir o tipo_dado se necessário
                'savaguarda': '',  # Adicione lógica para definir a savaguarda se necessário
                'truque': detalhes_magia['level'] == 0,
                'alvo': '',  # Adicione lógica se necessário
                'escola': escola,
                'fonte': fontes,
            }
        )

        # Se a magia já existe, não adiciona novamente
        if created:
            # Adiciona componentes à magia
            componentes_traduzidos = [c for c in detalhes_magia['components'] if c in componentes_map]
            magia.componentes.set([componentes_map[c] for c in componentes_traduzidos])

            # Associar classes à magia
            if 'Mago' in classes_map:
                magia.classes.add(classes_map['Mago'])  # Adicione lógica se precisar de mais classes

            magia.save()

    print('Magias adicionadas com sucesso!')
    return HttpResponse('Magias adicionadas com sucesso!')  # Ensure a valid HttpResponse is returned
