# Código Fonte LaTeX

Esta pasta contém o código fonte LaTeX do documento principal.

## Como compilar

Para gerar o PDF a partir do código fonte:
```bash
pdflatex coerencia_TRIOG.tex
pdflatex coerencia_TRIOG.tex  # Segunda vez para resolver referências
```

## Arquivos

- **coerencia_TRIOG.tex** - Código fonte principal
- **coerencia_TRIOG.pdf** - PDF compilado (também disponível em `/docs`)
- Outros arquivos (.aux, .log, etc.) são gerados automaticamente durante a compilação

## Pacotes LaTeX necessários

- `amsmath` - Equações matemáticas
- `amssymb` - Símbolos matemáticos especiais
- `siunitx` - Formatação de unidades
- `hyperref` - Links internos e externos
- `geometry` - Configuração de margens
