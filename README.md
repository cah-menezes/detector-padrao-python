# 🔍 Detector de Padrão

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LGPD](https://img.shields.io/badge/LGPD-Dados_Pessoais-E74C3C?style=flat)

Script em Python que detecta dados pessoais sensíveis em textos usando expressões regulares.

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

---

*Projeto desenvolvido como parte de uma trilha de automação aplicada à segurança da informação e GRC — com foco em identificação de dados pessoais sob a LGPD.*