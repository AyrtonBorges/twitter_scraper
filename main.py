import snscrape.modules.twitter as sntwitter

pesquisa = "Bitcoin since:2022-05-22 until:2022-12-14"

attributes_container = []

with open('teste.csv', 'w', encoding='utf-8') as entrada_file: # Inicializa o arquivo do excel
    entrada = sntwitter.TwitterSearchScraper(pesquisa).get_items() # Entrada de pesquisa de tweets
    template = 'Username;Displayname;ID;Descrição\n' # Inserindo os nomes das colunas
    entrada_file.write(template) # Inserindo os nomes das colunas no Excel
    for i, tweet in enumerate(entrada):
        if i > 100:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.url, tweet.content])
        teste = sntwitter.TwitterUserScraper(tweet.user.username)._get_entity()
        temp = teste.username+";"+teste.displayname+';'+str(teste.id)+';'+teste.description.replace('\n',' ')+';'+'\n'
        entrada_file.write(temp)
        print(teste.username,teste.id,teste.displayname,tweet.date) # Faz printar o username, o id da pessoa e o nome de de faixada do perfil dela
    entrada_file.close()
print('')
print("Programa concluído com sucesso!")