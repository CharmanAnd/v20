# ARQV30 Enhanced v2.0 - Guia de Produção

## 🚀 Correções Implementadas

### ✅ Problemas Resolvidos

1. **Google Search API Corrigida**
   - Validação robusta de chaves API
   - Detecção automática de quota/limite
   - Fallback inteligente para outros provedores
   - Cache para evitar requisições desnecessárias

2. **DuckDuckGo Scraping Robusto**
   - Headers anti-detecção aprimorados
   - Múltiplos seletores CSS para robustez
   - Tratamento de URLs redirecionadas
   - Delay anti-bot implementado

3. **Sistema de Cache Inteligente**
   - Cache SQLite para resultados de busca
   - Cache de conteúdo extraído
   - TTL configurável
   - Limpeza automática de entradas expiradas

4. **Encoding UTF-8 Garantido**
   - Detecção automática de encoding
   - Correção de caracteres corrompidos
   - Logging em UTF-8
   - Locale configurado corretamente

5. **Configuração de Produção**
   - FLASK_ENV=production
   - Debug desabilitado
   - Headers de segurança
   - Compressão GZIP
   - Service Worker para PWA

6. **Otimizações de Performance**
   - Busca paralela em múltiplos provedores
   - Rate limiting inteligente
   - Timeout configurável
   - Pool de conexões

## 🏭 Instalação para Produção

### 1. Instalação Automática
```bash
python install_production.py
```

### 2. Configuração Manual

#### Dependências
```bash
pip install -r requirements.txt
pip install gunicorn flask-compress redis psutil
```

#### Estrutura de Diretórios
```
ARQV30/
├── logs/           # Logs da aplicação
├── cache/          # Cache SQLite
├── src/uploads/    # Uploads temporários
├── backups/        # Backups do sistema
└── tmp/           # Arquivos temporários
```

#### Arquivo .env
```env
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-forte
HOST=0.0.0.0
PORT=5000

# APIs obrigatórias
SUPABASE_URL=sua-url-supabase
SUPABASE_ANON_KEY=sua-chave-anon
GEMINI_API_KEY=sua-chave-gemini

# APIs de busca (pelo menos uma)
GOOGLE_SEARCH_KEY=sua-chave-google
GOOGLE_CSE_ID=seu-cse-id
SERPER_API_KEY=sua-chave-serper
JINA_API_KEY=sua-chave-jina

# Configurações de produção
SEARCH_CACHE_ENABLED=true
CACHE_ENABLED=true
LOG_LEVEL=INFO
SECURE_HEADERS_ENABLED=true
GZIP_ENABLED=true
```

## 🚀 Execução

### Produção com Gunicorn (Recomendado)
```bash
python run_production.py
```

### Produção com Flask
```bash
cd src
python run.py
```

### Scripts de Inicialização
```bash
# Linux/Mac
./start.sh

# Windows
start.bat
```

## 📊 Monitoramento

### Status da Aplicação
```
GET /api/app_status
```

### Status dos Provedores de Busca
```
GET /api/status
```

### Limpeza de Cache
```
POST /api/clear_cache
```

### Reset de Provedores
```
POST /api/reset_providers
```

## 🔧 Configurações Avançadas

### Rate Limiting
```env
SEARCH_MAX_RETRIES=3
SEARCH_RETRY_DELAY=2
SEARCH_RATE_LIMIT_DELAY=1.5
```

### Cache
```env
SEARCH_CACHE_TTL=3600    # 1 hora
CACHE_TTL=1800           # 30 minutos
```

### Performance
```env
MAX_CONCURRENT_REQUESTS=10
REQUEST_TIMEOUT=60
DATABASE_POOL_SIZE=20
```

### Logging
```env
LOG_LEVEL=INFO
LOG_FILE_ENABLED=true
LOG_FILE_PATH=logs/arqv30.log
```

## 🛡️ Segurança

### Headers de Segurança (Automáticos)
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Strict-Transport-Security
- Referrer-Policy

### Rate Limiting
- 30 requisições por minuto por IP
- 500 requisições por hora por IP

### Validação de Entrada
- Sanitização automática de inputs
- Validação de tipos de arquivo
- Limite de tamanho de upload (16MB)

## 📈 Performance

### Otimizações Implementadas
1. **Cache Inteligente**: Evita requisições desnecessárias
2. **Busca Paralela**: Múltiplos provedores simultaneamente
3. **Compressão GZIP**: Reduz tamanho das respostas
4. **Service Worker**: Cache offline e PWA
5. **Pool de Conexões**: Reutilização de conexões DB

### Métricas de Performance
- Tempo médio de análise: 30-60 segundos
- Cache hit rate: >80%
- Uptime esperado: >99.9%

## 🔍 Troubleshooting

### Google Search Retorna 0 Resultados
1. Verifique se `GOOGLE_SEARCH_KEY` está correta
2. Verifique se `GOOGLE_CSE_ID` está correto
3. Verifique quota da API no Google Console
4. Execute: `POST /api/reset_providers`

### DuckDuckGo Falha
1. Verifique conectividade de internet
2. Pode estar temporariamente bloqueado
3. Sistema usa fallback automático

### Problemas de Encoding
1. Verifique se locale está configurado (pt_BR.UTF-8)
2. Logs mostrarão caracteres corretos
3. Sistema corrige automaticamente

### Performance Lenta
1. Verifique cache: `GET /api/app_status`
2. Limpe cache se necessário: `POST /api/clear_cache`
3. Verifique conectividade com APIs

## 📋 Checklist de Deploy

- [ ] Dependências instaladas
- [ ] Arquivo .env configurado
- [ ] Chaves de API válidas
- [ ] Diretórios criados
- [ ] Teste de instalação passou
- [ ] FLASK_ENV=production
- [ ] Logs funcionando
- [ ] Cache habilitado
- [ ] Headers de segurança ativos
- [ ] Service Worker funcionando

## 🆘 Suporte

### Logs Importantes
```bash
# Logs da aplicação
tail -f logs/arqv30.log

# Logs do Gunicorn
tail -f logs/gunicorn_error.log

# Status em tempo real
curl http://localhost:5000/api/app_status
```

### Comandos Úteis
```bash
# Verificar status
curl http://localhost:5000/api/health

# Limpar cache
curl -X POST http://localhost:5000/api/clear_cache

# Reset provedores
curl -X POST http://localhost:5000/api/reset_providers
```

## 🎯 Próximos Passos

1. Configure monitoramento (Prometheus/Grafana)
2. Implemente backup automático
3. Configure SSL/HTTPS
4. Implemente clustering se necessário
5. Configure CDN para assets estáticos

---

**ARQV30 Enhanced v2.0** - Sistema de Análise de Mercado Ultra-Robusto para Produção