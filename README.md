# 🔍 Detector de Padrão

Projeto 8 da trilha de Python — detecta dados pessoais sensíveis em textos usando expressões regulares.

## O que faz

Recebe um texto como input e varre procurando padrões de:
- 🪪 **CPF** (formato 000.000.000-00)
- 📧 **E-mail** (formato nome@dominio.com)

Se encontrar, informa qual dado foi detectado e onde. Conexão direta com LGPD e classificação de dados sensíveis.

## Como usar

```bash
python detector_padrao.py
```

Cole o texto quando solicitado. O programa retorna o que encontrou.

## Conceitos aplicados

- 🔎 `re` (expressões regulares) — busca de padrões em texto
- `re.search()` — localiza a primeira ocorrência do padrão
- 📦 Dicionário aninhado — organiza padrões e descrições por tipo de dado
- `def`, `for`, `if`, `f-string`

## Contexto

🛡️ Parte de uma trilha prática de Python com foco em GRC e Governança de TI.