Ótimo, agora ficou bem claro! 🙌

## ✅ Resposta curta:

**Sim**, você pode deixar o script rodando dentro de um container Docker na sua VM Azure, e ele continuará executando **mesmo após você sair do container e da VM** — **desde que você execute o container corretamente em background**.

---

## 🧱 O que você precisa fazer:

### 🔹 1. Execute seu container em **modo "detached"** (`-d`)

Esse modo faz com que o container rode em segundo plano.

```bash
docker run -d --name meu_container nome_da_imagem
```

Se você quer rodar um script específico no container (e não o `CMD` da imagem), faça:

```bash
docker run -d --name meu_container nome_da_imagem python /caminho/para/meu_script.py
```

> ✅ Assim, o container continua executando o script mesmo se você sair do terminal, do container e da VM.

---

### 🔹 2. Ou, se já está **dentro do container**, você pode rodar o script com `nohup` ou `tmux`

**Dentro do container (já rodando):**

```bash
nohup python3 meu_script.py > saida.log 2>&1 &
exit
```

> Isso deixa o script rodando no fundo e você pode sair normalmente com `exit`.

---

### 🔹 3. Para containers que já estão criados e você quer reexecutar o script

Você pode usar `docker exec` para rodar um comando num container já ativo:

```bash
docker exec -d meu_container python3 /caminho/para/meu_script.py
```

* O `-d` aqui também é **"detached"**, ou seja, não precisa manter a sessão aberta.

---

## ✅ Verificar se o script ainda está rodando

Você pode usar:

```bash
docker ps  # Mostra containers em execução
docker logs meu_container  # Ver saída do script
docker exec -it meu_container bash  # Entrar de novo no container
```

---

## ⚠️ Atenção: cuidado com o `docker run` padrão

Se você rodar um container **sem o `-d`**, ele só roda enquanto sua **sessão estiver ativa**. Se você sair da VM ou do terminal, o container **pode parar** (a não ser que esteja com `nohup`, `tmux`, ou que o container esteja configurado como daemon).

---

## 🔄 Dica avançada (opcional)

Se seu script for longo e crítico, considere:

* **Montar um volume** para salvar o progresso ou logs.
* Usar um **process manager como supervisord** dentro do container.
* Configurar o container com `restart: always` para reiniciar se houver falhas.

---

Se você quiser, posso montar um `Dockerfile` ou comando exato com base no seu cenário. Me diga:

* Qual linguagem você está usando (Python, Node, etc)?
* Qual o script que você quer rodar?
* Você quer salvar logs ou dados em algum lugar específico?
