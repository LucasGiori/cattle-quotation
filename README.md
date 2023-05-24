# Cattle Quotation

## Set up development environment

```shell
echo -e "TWILIO_ACCESS_ID={fillInHere}\nTWILIO_AUTH_TOKEN={fillInHere}\n\nFAKE_ACCESS_ID=123456\nFAKE_AUTH_TOKEN=98766" > .env.devlopment
```

## Run Application

```shell 
make run
```

#### Todo List

- [ ] Configurar container de dependências da aplicação
- [ ] Estruturar porta e formato default de logs para aplicação
- [ ] Avaliar SDK do Open Telemetry para python
- [ ] Adicionar validação para classes do comando
- [ ] Padronizar forma de realizar scraping, criar e incrementar algum tipo abstrato para extrair informações de forma mais simples sem precisar de manipulações repetitivas no response. See [scrapy](https://scrapy.org/)
- [ ] Adequar código as convenções do python. Estudar [Python Enhancement Proposals](https://peps.python.org/pep-0000/)