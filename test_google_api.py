#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Teste da Google Custom Search API
Script para testar e diagnosticar problemas com a Google API
"""

import os
import sys
import requests
import json
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def test_google_custom_search():
    """Testa a Google Custom Search API"""
    
    print("🔍 Testando Google Custom Search API...")
    print("=" * 50)
    
    # Verifica variáveis de ambiente
    api_key = os.getenv('GOOGLE_SEARCH_KEY')
    cse_id = os.getenv('GOOGLE_CSE_ID')
    
    print(f"API Key: {api_key[:10] if api_key else 'NÃO ENCONTRADA'}...{api_key[-5:] if api_key else ''}")
    print(f"CSE ID: {cse_id[:10] if cse_id else 'NÃO ENCONTRADO'}...{cse_id[-5:] if cse_id else ''}")
    print()
    
    if not api_key:
        print("❌ GOOGLE_SEARCH_KEY não encontrada no .env")
        return False
    
    if not cse_id:
        print("❌ GOOGLE_CSE_ID não encontrado no .env")
        return False
    
    # Teste básico da API
    url = "https://www.googleapis.com/customsearch/v1"
    
    # Query de teste simples
    test_query = "teste"
    
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': test_query,
        'num': 3,
        'lr': 'lang_pt',
        'gl': 'br'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    print(f"🌐 Fazendo requisição para: {test_query}")
    print(f"URL: {url}")
    print(f"Parâmetros: {json.dumps(params, indent=2)}")
    print()
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"📊 Headers: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            
            # Verifica se há erro na resposta
            if 'error' in data:
                error = data['error']
                print(f"❌ Erro na API:")
                print(f"   Código: {error.get('code', 'N/A')}")
                print(f"   Mensagem: {error.get('message', 'N/A')}")
                print(f"   Detalhes: {error.get('details', 'N/A')}")
                
                # Sugestões baseadas no erro
                if 'quota' in error.get('message', '').lower():
                    print("\n💡 Sugestões:")
                    print("   - Verifique se não atingiu o limite diário da API")
                    print("   - Acesse Google Cloud Console para verificar quotas")
                    print("   - Considere aumentar o limite ou aguardar reset")
                
                elif 'invalid' in error.get('message', '').lower():
                    print("\n💡 Sugestões:")
                    print("   - Verifique se a API Key está correta")
                    print("   - Verifique se o CSE ID está correto")
                    print("   - Confirme se a Custom Search API está habilitada")
                
                return False
            
            # Sucesso - analisa resultados
            items = data.get('items', [])
            search_info = data.get('searchInformation', {})
            
            print(f"✅ API funcionando!")
            print(f"📊 Resultados encontrados: {len(items)}")
            print(f"📊 Total disponível: {search_info.get('totalResults', 'N/A')}")
            print(f"📊 Tempo de busca: {search_info.get('searchTime', 'N/A')}s")
            print()
            
            if items:
                print("📋 Primeiros resultados:")
                for i, item in enumerate(items[:3], 1):
                    print(f"   {i}. {item.get('title', 'Sem título')}")
                    print(f"      URL: {item.get('link', 'Sem URL')}")
                    print(f"      Snippet: {item.get('snippet', 'Sem snippet')[:100]}...")
                    print()
            else:
                print("⚠️ Nenhum resultado retornado")
                print("💡 Isso pode ser normal para queries muito específicas")
            
            return True
            
        elif response.status_code == 403:
            print("❌ Erro 403 - Acesso Negado")
            print("💡 Possíveis causas:")
            print("   - API Key inválida ou expirada")
            print("   - Custom Search API não habilitada no projeto")
            print("   - Quota diária esgotada")
            print("   - Billing não configurado no Google Cloud")
            
        elif response.status_code == 400:
            print("❌ Erro 400 - Requisição Inválida")
            print("💡 Possíveis causas:")
            print("   - CSE ID inválido")
            print("   - Parâmetros da query inválidos")
            print("   - Formato da requisição incorreto")
            
        elif response.status_code == 429:
            print("❌ Erro 429 - Rate Limit Excedido")
            print("💡 Aguarde alguns minutos e tente novamente")
            
        else:
            print(f"❌ Erro HTTP {response.status_code}")
            print(f"Resposta: {response.text[:500]}")
        
        return False
        
    except requests.exceptions.Timeout:
        print("❌ Timeout na requisição")
        print("💡 Verifique sua conexão com a internet")
        return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de rede: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def test_cse_configuration():
    """Testa configuração do Custom Search Engine"""
    
    print("\n🔧 Testando configuração do CSE...")
    print("=" * 50)
    
    cse_id = os.getenv('GOOGLE_CSE_ID')
    
    if not cse_id:
        print("❌ CSE ID não encontrado")
        return False
    
    # Tenta acessar a configuração do CSE
    cse_url = f"https://cse.google.com/cse?cx={cse_id}"
    
    print(f"🌐 URL do CSE: {cse_url}")
    print("💡 Acesse esta URL para verificar a configuração do seu CSE")
    print()
    
    # Verifica formato do CSE ID
    if ':' in cse_id:
        parts = cse_id.split(':')
        print(f"📊 Formato do CSE ID: {len(parts)} partes")
        print(f"📊 Primeira parte: {parts[0]}")
        if len(parts) > 1:
            print(f"📊 Segunda parte: {parts[1]}")
    else:
        print("⚠️ CSE ID não contém ':' - formato pode estar incorreto")
    
    print("\n💡 Verificações recomendadas:")
    print("   1. CSE está configurado para buscar em toda a web")
    print("   2. CSE não está restrito a sites específicos")
    print("   3. CSE está ativo e público")
    print("   4. Billing está configurado no Google Cloud")
    
    return True

def main():
    """Função principal de teste"""
    
    print("🚀 ARQV30 Enhanced v2.0 - Diagnóstico Google API")
    print("=" * 60)
    
    # Teste 1: Configuração básica
    print("📋 TESTE 1: Configuração Básica")
    if not test_cse_configuration():
        print("❌ Falha na configuração básica")
        return
    
    # Teste 2: API funcionando
    print("\n📋 TESTE 2: Funcionalidade da API")
    if test_google_custom_search():
        print("✅ Google Custom Search API está funcionando!")
    else:
        print("❌ Google Custom Search API com problemas")
        print("\n🔧 PRÓXIMOS PASSOS:")
        print("1. Verifique as chaves no arquivo .env")
        print("2. Confirme que a Custom Search API está habilitada")
        print("3. Verifique quotas no Google Cloud Console")
        print("4. Confirme que o billing está ativo")
        print("5. Teste com uma query mais simples")
    
    print("\n" + "=" * 60)
    print("🏁 Diagnóstico concluído")

if __name__ == "__main__":
    main()