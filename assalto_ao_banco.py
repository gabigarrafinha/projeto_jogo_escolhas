import time

#Função que inicia o jogo e contém a escolha de personagens
def jogo():
    personagem = ""
    opcoes = ["A", "B", "C"]

    print('''
    O Banco de Vale do Ouro, apesar de estar numa cidade pequena, movimenta uma grande de quantidade de dinheiro por ser muito utilizado por uma mineiradora da região.
    Em uma tarde do início do mês, período de maior movimento, um assaltante entra no banco e anuncia um assalto.
    Ele diz que todos os presentes são agora seus reféns e pede que todos levantem os braços
    ''')

    while personagem not in opcoes:
        personagem = input('''
        Escolha com quem você quer jogar:
        
        A-policial 
        B-refém 
        C-assaltante
        ''').upper()
        if personagem == "A":
            historia_policial()
        elif personagem == "B":
            historia_refem()
        elif personagem == "C":
            historia_assaltante()
        else:
            print("Por favor, digite A, B ou C")

#Função acionada ao fim do jogo
def fim_do_jogo():
    continua = input('''
    Deseja jogar novamente?
    Sim ou não?
    Digite S ou N
    ''').lower()
    if continua == "s":
        jogo()
    elif continua == "n":
        print("Até breve!")
    else: 
        fim_do_jogo()

#Função da escolha inicial do personagem policial 
def historia_policial():
    time.sleep(0.3)
    escolha1 = input('''
    Você está na delegacia e vê no sistema que o alarme de um banco foi acionado.
    O que você faz? 

    A-Sai imediatamente em direção ao banco
    B-Vai até o delegado relatar sobre o alarme

    Escolha A ou B
    ''').upper()
    
    if escolha1 == "A":
        policial_sozinho()
    elif escolha1 == "B":
        policial_com_reforcos()
    else:
        historia_policial()

#Função da escolha secundária do personagem policial - opção 1
def policial_sozinho():
    time.sleep(0.3)
    escolha2 = input('''
    Você chegou sozinho ao banco e viu que o assaltante tem cúmplices. 
    O que você faz?

    A- Se esconde e chama reforços
    B- Tenta atrair a atenção dos bandidos para longe do banco

    Escolha A ou B
    ''').upper()
    if escolha2 == "A":
        policial_chama_reforços()
    elif escolha2 == "B":
        policial_chama_atencao()
    else:
        policial_sozinho()

#Função da escolha secundária do personagem policial - opção 2
def policial_com_reforcos():
    time.sleep(0.3)
    escolha2 = input('''
    O delegado te orientou a levar reforços com você. 
    Você e alguns companheiros chegam ao banco e veem que o bandido tem cúmplices. 
    O que você faz?

    A- Pede que seus companheiros rendam os bandidos que estão do lado de fora enquanto você entra
    B- Orienta sua equipe a atirar nos bandidos

    Escolha A ou B
    ''').upper()
    if escolha2 == "A":
        render_bandidos()
    elif escolha2 == "B":
        atirar_bandidos()
    else:
        policial_com_reforcos()

#Função de terceira escolha do personagem policial - finais 1 e 2
def policial_chama_reforços():
    time.sleep(0.3)
    escolha3 = input('''
    Você liga para a delegacia e chama reforços. 
    Mas, enquanto espera, percebeu que que um dos bandidos está vindo em sua direção. 
    O que você faz?

    A- Joga sua arma e distintivo num arbusto próximo, já que está a paisana
    B- Corre

    Escolha A ou B 
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        O bandido não percebeu seu movimento e achou que você era um pedestre. 
        Você aproveitou para dristraí-lo enquanto seus companheiros chegavam e neutralizavam o resto dos criminosos.
        
        Parabéns, você ajudou a preender os criminosos e libertar os reféns!
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você tentou fugir, mas foi visto e levou um tiro nas costas. 

        Você morreu
        ''')
        fim_do_jogo()
    else:
        policial_chama_reforços()

#Função de terceira escolha do personagem policial - finais 3 e 4
def policial_chama_atencao():
    time.sleep(0.3)
    escolha3 = input('''
    Você decidiu agir sozinho e jogou uma pedra do outro lado da rua em que se encontra para distrair os bandidos. 
    A maioria deles vai até lá ver o que causou o barulho. Mas um segue na porta do banco. 
    O que você faz?

    A- Vai até lá e tenta desarmar o bandido que restou 
    B- Joga uma pedra em outra direção 

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você parte para cima do bandido e começa uma briga corporal.
        Só que quando você está quase conseguindo desarmá-lo, um dos outros bandidos reaparece.
        Ele te desarma e te amarra num poste próximo ao banco. 

        Você perdeu, os bandido fugiram com o dinheiro do banco.
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você jogou a pedra. De cara, o bandido até olhou para o outro lado. Mas depois deixou pra lá.
        Intrigado, ele resolve investigar os arredores e começa a andar na sua direção.
        Você até tenta se esconder atrás de um arbusto próximos, mas sua última lembrança é da mão do bandido se aproximando do seu rosto.
        Alguns minutos depois, você acorda numa ambulância e descobre que os bandido levaram todo o dinheiro do banco.

        Game over.
        ''')
        fim_do_jogo()
    else:
        policial_chama_atencao()

#Função de terceira escolha do personagem policial - finais 5 e 6
def render_bandidos():
    time.sleep(0.3)
    escolha3 = input('''
    Você pediu que seus comppanheiros rendenssem os bandidos e eles fizeram isso. Ou quase. 
    Um dos criminosos tinha se afastado do bando para fazer xixi. Ele volta e surpreende a ação dos policias. 
    O que você faz? 

    A- Parte para cima dele 
    B- Tenta chamar a atenção dele

    Escolha A ou B 
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você corre na direção do criminoso para tentar neutralizá-lo.
        Mas, para o seu azar, você tropeça em uma pedra e acaba caindo no chão. 
        O bandido consegue correr e se juntar ao outro assaltante dentro do banco.
        Além de fugirem com o dinheiro, eles ainda deixam reféns feridos.

        Você perdeu o jogo!
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você surge na rua falando muito alto e fingindo estar embreagado. 
        Imediatamente, o bandido se vira para você, que se apoia nele como se estivesse tentando se equilibrar.
        Ele tenta se desvencilhar da situação. Mas você, mais raṕido, pega a arma que está na cintura dele e o rende. 
        Com todos os vigias neutralizados, vocês e seus companheiros entram no banco e impedem o assalto.

        Você venceu!
        ''')
        fim_do_jogo()
    else:
        render_bandidos()

#Função de terceira escolha do personagem policial - finais 7 e 8
def atirar_bandidos():
    time.sleep(0.3)
    escolha3 = input('''
    Seus comppanheiros abriram fogo contra os criminos, mas ao invés de neutralizá-los, causarm um tiroteio generalizado. 
    O que você faz? 

    A- Aproveita a confusão para tentar entrar no banco
    B- Se junta ao tiroteio 

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        No meio da confusão, você se esqgueira até a porta do banco e entra de fininho.
        Lá dentro, você consegue surpreender o assaltando, que já se preparava para sair com os sacos de dinheiro. 
        Você algema o bandido e mantém tdos seguros dentro da agência até que os tiros parem. 
        Depois tira todos ali em seguranã e leva o criminoso preso.

        Parabéns, você impediu o assalto!
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você se junta a seus companheiros na troca de tiro com os criminosos. 
        A situação foge de controlo e, além de baixas de ambos os lados, pedestres acabam atingidos pelos tiros.
        Pessoas foram feridas por causa da sua imprudência.

        Você perdeu o jogo.
        ''')
        fim_do_jogo()
    else:
        atirar_bandidos()

#Função da escolha inicial do personagem refém
def historia_refem():
    time.sleep(0.3)
    escolha1 = input('''
    Você aproveitou a confusão do anúncio do assalto para apertar o botão do alarme.
    Mas depois, percebeu que o assaltante está te encarando. 
    O que você faz?

    A- Pega um terço na sua mesa e começa a rezar baixo.
    B- Tenta conversar com o assaltante

    Escolha A ou B 
    ''').upper()
    if escolha1 == "A":
        refem_reza()
    elif escolha1 == "B":
        refem_tenta_conversar()
    else:
        historia_refem()

#Função de escolha secundária do personagem refém - opção 1
def refem_reza():
    time.sleep(0.3)
    escolha2 = input('''
    Você começa a rezar baixinho.
    O assaltante se aproxima e pergunta no que você mexeu embaixo da mesa.
    O que você faz?

    A- Diz que estava apenas pegando o seu terço na gaveta.
    B- Nega que tenha mexido em alguma coisa.

    Escolha A ou B 
    ''').upper()
    if escolha2 == "A":
        refem_pegando_terco()
    elif escolha2 == "B":
        refem_mente()
    else:
        refem_reza()

#Função de escolha secundária do personagem refém - opção 2
def refem_tenta_conversar():
    time.sleep(0.3)
    escolha2 = input('''
    Você começa a falar para tentar despistar o bandido.
    Primeiro, você pergunta o nome dele, que ignora e olha feio. 
    Com medo, você começa a tagalerar várias coisas aleatórias.
    Irritado, o criminoso se aproxima e começa a mexer na sua mesa.
    O que você faz?

    A- Deixa o seu casaco cair por cima do botão do alarme.
    B- Começa a chorar muito.

    Escolha A ou B
    ''').upper()
    if escolha2 == "A":
        refem_derruba_casaco()
    elif escolha2 == "B":
        refem_comeca_chorar()
    else:
        refem_tenta_conversar()

#Função de terceira escolha do personagem refém - finais 1 e 2
def refem_pegando_terco():
    time.sleep(0.3)
    escolha3 = input('''
    Você mostra o terço para o assaltante e começa a contar a história do objeto. Sem querer perder tempo, ele vira as costas e começa a se afastar.
    O que você faz?

    A- Tenta se aproximar do segurança da agência, amarrado próximo a você.
    B- Parte para cima do assaltante e tenta desarmá-lo.

    Escolha A ou B 
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Discretamente, você se abaixa e desamarra o segurança da agência, que estava no chão perto de você.
        O homem tem uma segunda arma escondida na perna e que não foi descoberta pelo bandido.
        Ele tenta usar o elemento surpresa para neutralizar o ladrão, mas acaba numa troca de tiros com o criminoso. 

        Além de não conseguir impedir o assalto, o segurança fica ferido, bem como outras pessoas. 

        Você perdeu!
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você vê o ladrão de costas e pensa que é uma boa ideia resgatar seus conhecimentos de jiu-jitsu para tentar imobilizá-lo.
        Mas quando você dá o primeiro passo na diração do bandido, ele rapidamente se vira e atira em você.

        Você morreu.
        ''')
        fim_do_jogo()
    else:
        refem_pegando_terco()

#Função de terceira escolha do personagem refém - finais 3 e 4
def refem_mente():
    time.sleep(0.3)
    escolha3 = input('''
    Você mente para o bandido e diz que não mexeu em nada, levatando as mãos. 
    Não muito convencido, o ladrão pede que você vá até ele e diz que você o guiará pelo banco. 
    O que você faz?

    A- Obedece o assaltante.
    B- Finge que tem um problema na perna e vai mancando até o bandido.

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você vai até o ladrão, que pede que você mostre para ele a sala do cofre.
        No caminho, você lembra de uma sala que só tranca por fora e decide enganar o bandido e levá-lo até lá.
        Perto da porta, você desacelara o passo e fica um pouco para trás. 

        Mas, o ladrão percebe sua itenção e, no susto, atira em você. 

        Você perdeu o jogo. 
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você começa a mancar na direção do ladrão.
        Sua imitação é até convincente, mas provoca o riso de alguns companheiros de trabalho.
        O bandido logo percebe que você está mentindo e te dá um coronhada.

        Você acorda horas depois, no hospital, e descobre que o criminoso levou todo o dinheiro da agência e ainda matou policiais. 

        Você perdeu o jogo. 
        ''')
        fim_do_jogo()
    else:
        refem_mente()

#Função de terceira escolha do personagem refém - finais 5 e 6
def refem_derruba_casaco():
    time.sleep(0.3)
    escolha3 = input('''
    Você consegue esconder o botão, mas o bandido fica ainda mais encudado com o seus movimentos.
    Ele resolver abaixar e olhar debaixo da sua mesa.
    O que você faz?

    A- Aproveita o momento em que ele estiver abaixado para golpear a cabeça dele.
    B- Vira a xícara de café no bandido.

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você até consegue acertar o bandido. 
        Mas ele se vira para você como se não tivesse sentido nada.
        Ele te empurra para longe e percebe o botão escondido embaixo do casaco.
        O ladrão resolve fugir antes que a polícia chegue. 
        
        Mas, com raiva, atira em você antes de sair.
        
        Você morreu.
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        No susto, você pega a xícará de café já frio que estava na mesa e vira no bandido.
        Enxarcado, o homem se vira contra você enfurecido.
        Mas, antes que ele consiga reagir, sua pele é tomada por bolhas.
        Você não sabia, mas o ladrão é alérgico a café.

        Em sofrimento, o bandido larga a arma e corre para fora do banco.

        Você venceu.
        ''')
        fim_do_jogo()
    else:
        refem_derruba_casaco()

#Função de terceira escolha do personagem refém - finais 7 e 8
def refem_comeca_chorar():
    time.sleep(0.3)
    escolha3 = input('''
    Você começa a chorar muito e repete sem parar que não quer morrer.
    O bandido promete pupar sua vida, desde que você indique para ele quem pode abrir o cofre.
    Você lembra que cofre só abre uma vez no dia - pela manhã - e ninguém vai conseguir destrancá-lo.
    O que você faz?

    A- Diz a verdade.
    B- Mente e promete levar o homem até o gerente que teria o segredo.

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''Você começa a explicar para o ladrão tudo sobre o funcinando do cofre.
        Por fim, diz que o objeto ficará lacrado até a manhã seguinte.
        O bandido fica muito nervoso e desconfia da sua história.
        Você leva ele até o cofre para mostrar que está falando a verdade.

        Nesse meio tempo, a policia invade o local e o ladrão te usa de escudo humano. 

        Você e o bandido acabam morrendo. 
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você decide levar o ladrão até um companheiro de trabalho que tem grande experiência em artes marciais, mas não é o gerente.
        Para a sua sorte, o seu colega entende o seu plano e entra na sua farsa.
        O homem diz que o cofre só abre com as digitais dele e também tem um sistema de reconhecimento facial. 
        O bando acredita e leva seu amigo até a sala do cofre.

        Lá, o funcionário do banco consegue reagir e impedir o assalto.

        Você venceu. 
        ''')
        fim_do_jogo()
    else:
        refem_comeca_chorar()

#Função da escolha inicial do personagem assaltante
def historia_assaltante():
    time.sleep(0.3)
    escolha1 = input('''
    Depois de anunciar o assalto, você percebe que um dos funcionários fez um movimento estranho. 
    O que você faz? 

    A- Vai até ele verificar se apertou algum alarme.
    B- Ignora e segue recolhendo o dinheiro dos caixas.

    Escolha A ou B
    ''').upper()
    if escolha1 == "A":
        bandido_verifica_alarme()
    elif escolha1 == "B":
        bandido_ignora_movimento()
    else:
        historia_assaltante()

#Função de escolha secundária do personagem assaltante - opção 1
def bandido_verifica_alarme():
    time.sleep(0.3)
    escolha2 = input('''
    O funcionário nega que tenha apertado o alarme, mas você desconfia.
    Você olha ao redor e percebe um botão no chão e entende que ele está mentindo.
    O que você faz? 

    A- Pede que ele ligue para a polícia e diga que foi alarme falso.
    B- Resolve agir antes da polícia chegar

    Escolha A ou B
    ''').upper()
    if escolha2 == "A":
        bandido_liga_policia()
    elif escolha2 == "B":
        bandido__resolve_agir()
    else:
        bandido_verifica_alarme()

#Função de escolha secundária do personagem assaltante - opção 2
def bandido_ignora_movimento():
    time.sleep(0.3)
    escolha2 = input('''
    Você vai de caixa em caixa recolhendo o dinheiro.
    Depois, pergunta alto quem é o gerente da agência.
    Todos os presentes ficam em silêncio
    O que você faz? 

    A- Dispara um tiro para o alto para amendrontar os reféns.
    B- Decide confrontar um funcionário aleatório

    Escolha A ou B
    ''').upper()
    if escolha2 == "A":
        bandido_dispara_para_alto()
    elif escolha2 == "B":
        bandido_escolhe_funcionario()
    else:
        bandido_ignora_movimento()

#Função de terceira escolha do personagem assaltante - finais 1 e 2
def bandido_liga_policia():
    time.sleep(0.3)
    escolha3 = input('''
    Você ameaça o homem com uma arma enquanto ele liga. 
    Depois de alguns segundos, desconfia que algo esteja errado.
    O que você faz?

    A- Pede que ele coloque o telefone no viva voz.
    B- Pega o telefone para ligar você mesmo. 

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Ao mandar o homem colocar o telefone no viva voz, você descobre que ele não tinha discado.
        Você disca para a polícia e ordena que ele cancele o chamado e diga que apertou o botão sem querer.
        Com medo de morrer, ele obedece.

        Você amarra o homem e todos os outros funcionários e segue com o assalto.

        Você venceu.
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você disca para a polícia e tenta se passar por um funcionário.
        O polícial confere as informações da agência e você se atrapalha um pouco, mas responde.
        Achando que se livrou da polícia, você continua o assalto.
        Mas, depois de um tempo, é surpreendido pelos polícia, que te prendem.

        Você perdeu.
        ''')
        fim_do_jogo()
    else:
        bandido_liga_policia()

#Função de terceira escolha do personagem assaltante - finais 3 e 4
def bandido__resolve_agir():
    time.sleep(0.3)
    escolha3 = input('''
    Você recolhe o dinheiro dos caixas e avalia que ainda deve ter 10 minutos antes da polícia chegar. 
    Então, resolve também resolher os celulares e objetos de valor dos reféns. 
    Depois de uns minutos, você escuta uma sirene ao fundo.
    O que você faz? 

    A- Foge pela entrada do banco.
    B- Tenta procurar uma saída alternativa. 

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você sai pela entrada principal esperando encontrar os seus companheiros do lado de fora.
        De repente, é cercado por policiais e rendido.

        A sirene que ouviu era de uma ambulância, a polícia chegou discratamente.

        Você perdeu. 
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você procura uma saída pelos fundos e não encontra nenhuma.
        Sua úncia opção é entrar por uma tampa de esgoto que vê na área de serviço.

        Você até consegue sair do banco, mas é atacado por jacarés que moram nos esgotos.

        Você morreu.
        ''')
        fim_do_jogo()
    else:
        bandido__resolve_agir()

#Função de terceira escolha do personagem assaltante - finais 5 e 6
def bandido_dispara_para_alto():
    time.sleep(0.3)
    escolha3 = input('''
    Você dispara para o alto e pede que alguém se apresente.
    Um funcionário muito assustado diz que é o gerente da agência.
    Você pede que ele te leve até o cofre, mas sente que ele não sabe muito bem o que está fazendo.
    O que você faz? 

    A- Usa violência para intimidar o homem.
    B- Resolve fazer perguntas sobre o sistema de cofres do banco.

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você dá uma coronhada no homem e ameaça matá-lo caso ele te leve para a sala errada.
        Ele vira em uma sala e você vai atrás.
        Mas, lá dentro, você dá de cara com policiais e é rendido.

        O funcionário que você ignorou no início do jogo de fato acionou o alarme e chamou a polícia.

        Você perdeu.
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        ('''
        Você começa faz perguntas sobre os cofres do bando e percebe que o homem está improvisando as respostas.
        Você volta para o saguão do banco para pegar outra pessoa.
        Mas, ao chegar lá, dá de cara com vários policiais armados. 

        O funcionário que você ignorou no início do jogo de fato acionou o alarme e chamou a polícia.

        Você perdeu.
        ''')
        fim_do_jogo()
    else:
        bandido_dispara_para_alto()

#Função de terceira escolha do personagem assaltante - finais 7 e 8
def bandido_escolhe_funcionario():
    time.sleep(0.3)
    escolha3 = input('''
    Você escolhe um funcionário baseado nas suas percepções de como seria um gerente de banco.
    O homem começa a te levar para o cofre e demonstra segurança.
    Você, então, acredita que fez a escolha certa.
    Até, que, em um dos corredores do banco, o homem cai desmaiado.
    O que você faz? 

    A- Deixa ele pra lá e tenta achar o cofre sozinho.
    B- Tenta acordar o homem.

    Escolha A ou B
    ''').upper()
    if escolha3 == "A":
        time.sleep(0.3)
        print('''
        Você deixa o homem caído no chão e começa a abrir todas as portas que encontra no caminho.
        Sem sucesso, você decide voltar pelo corredor por onde veio. 
        Quando se vira, dá de cara com vários policiais armados. 

        O funcionário que você ignorou no início do jogo acionou o alarme e chamou a polícia.
        Você reage, mas é atingido primeiro.

        Você perdeu.
        ''')
        fim_do_jogo()
    elif escolha3 == "B":
        time.sleep(0.3)
        print('''
        Você vê um bebedouro próximo e resolve pegar um copo de água para jogar na cara do homem.
        Mesmo assim, ele permanece imóvel. 
        Convencido de que esse homem é o gerente, você insiste em tentar acordá-lo.
        Ajoelhado ao lado dele, você o sacode. De repente, escuta um clique.
        Quando se vira, dá de cara com a arma de um policial.

        O funcionário que você ignorou no início do jogo acionou o alarme.

        Você foi preso e perdeu o jogo.
        ''')
        fim_do_jogo()
    else:
        bandido_escolhe_funcionario()

#chamando a função que inicia o jogo
jogo()
