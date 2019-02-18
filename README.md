# IbovespaWolf

Este repositório contém os códigos da equipe SEKMANDA, e tem como objetivo ser usada na competição da SEK na LARC 2018. O código foi desenvolvido para o Kit Lego Mindstorm NXT e utiliza como base a linguagem de programação NXC.

## Git Flow do Repositório

O Git Flow será um atributo de extrema importância para o nosso repositório, evitando que códigos errôneos sejam executados e que _builds_ funcionais não são perdidas na implementação de novas _features_.

### O que é um Git Flow?

Um Git Workflow, ou Git Flow é uma recomendação de como usar o Git para realizar o trabalho de maneira consistente e produtiva. Os fluxos de trabalho do Git incentivam os usuários a usar o Git de maneira efetiva e consistente. Dado o foco do Git em flexibilidade, não existe um processo padronizado de como interagir com o Git.

Ao trabalhar com uma equipe em um projeto gerenciado pelo Git, é importante garantir que a equipe esteja de acordo sobre como o fluxo de alterações será aplicado. Para garantir que a equipe esteja na mesma página, um fluxo de trabalho Git acordado deve ser desenvolvido ou selecionado.

### Descrição do nosso Git Flow

A Branch **dev** é a nossa branch principal e todos os merges requests devem ser feitos via Pull Request da branch feature que esta sendo desenvolvida para a dev. Quando uma versão da dev estiver usável, um Pull Request será submetido para a master.

## Desenvolvendo Novas Features

Novas funcionalidades devem ser desenvolvidas em branches únicas, **nenhuma feature deve ser desenvolvida na master e dev**.

Então como desenvolvo novas features? Com novas branches!

O intuito é que cada biblioteca seja construída em uma branch única. Por exemplo, se eu quero criar uma classe com novos indicadores econômicos, devo criá-la em uma biblioteca de movimentação, logo essa biblioteca deve ser construída em uma branch nova.

O comando para criar uma nova branch é :

```git
git branch nome_da_branch
```

Para visualizar todas as branches disponíveis:

```git
git branch
```

E para mudar seu ambiente de desenvolvimento para a branch desejada:
```git
git checkout nome_da_branch
````

Após ter adicionado mudanças e realizado o commit na sua branch, ao dar o push você pode se deparar com um possível erro. Este erro é porque sua branch ainda não existe no repositório remoto. Para corrigí-lo utilize o comando abaixo que realizará a ligação entre seu branch local e remoto.
````git
git push --set-upstream origin nome_da_branch
````

Quando todas as mudanças respectivas à branch estiverem prontas e testadas, solicite uma aprovação de pull request no repositório do Github.

## Modularização do Repositório

Por motivos de organização e divisões de tarefa, este repositório é organizado de forma modularizada. Na sua raiz, o repósitorio contem este arquivo README, e diretórios de exemplo, código fonte, e arquivos. No repositório de exemplos, devem conter arquivos apenas relacionados a testes individuais, de tarefas únicas, como teste do giroscópio ou de movimentação da garra. O repositório de arquivos deverá conter somente arquivos criados pelos códigos .nxc, onde o sistema principal realizará a devida leitura e escrita. O código fonte estará contido no diretório source.

Dentro do repositório _source_, existe duas pastas e os arquivos principais. A pasta _include_ deverá conter os arquivos de cabeçalho (headers), nestes arquivos deverá conter as definições das diretivas de pré-processamento e funções de cada biblioteca. A pasta _lib_ conterá as declaração das funções definidas em seu header. E os arquivos que deverão existir na pasta source devem ser somente o master.nxc, slave.nxc e conf.nxc

```
├── root
│   ├── exemplos
│   │   ├── pacman_bfs
│   ├── source
│   │   ├── include
│   │   │   ├── claw.h
│   │   ├── lib
│   │   │   ├── claw.nxc
│   │   └── master.nxc
│   └── arquivos
```
