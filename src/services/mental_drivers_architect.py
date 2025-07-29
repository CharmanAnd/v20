#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Arquiteto de Drivers Mentais
Sistema de Ancoragem Psicológica Ultra-Avançado
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)

class MentalDriversArchitect:
    """Arquiteto de Drivers Mentais - Sistema de Ancoragem Psicológica"""
    
    def __init__(self):
        """Inicializa o arquiteto de drivers mentais"""
        self.universal_drivers = self._load_universal_drivers()
        logger.info("Mental Drivers Architect inicializado com 19 drivers universais")
    
    def _load_universal_drivers(self) -> Dict[str, Dict[str, Any]]:
        """Carrega os 19 drivers universais"""
        return {
            "ferida_exposta": {
                "nome": "Ferida Exposta",
                "categoria": "emocional_primario",
                "gatilho_central": "Dor não resolvida",
                "mecanica_psicologica": "Trazer à consciência o que foi reprimido",
                "momento_ideal": "Abertura da apresentação - quebra de padrão",
                "ativacao_base": "Você ainda [comportamento doloroso] mesmo sabendo que [consequência]?",
                "poder_impacto": 9.5,
                "complementa": ["diagnóstico_brutal", "custo_invisível"]
            },
            
            "trofeu_secreto": {
                "nome": "Troféu Secreto",
                "categoria": "emocional_primario",
                "gatilho_central": "Desejo inconfessável",
                "mecanica_psicologica": "Validar ambições 'proibidas'",
                "momento_ideal": "Meio da apresentação - amplificação do desejo",
                "ativacao_base": "Não é sobre dinheiro, é sobre [desejo real oculto]",
                "poder_impacto": 9.0,
                "complementa": ["ambição_expandida", "identidade_aprisionada"]
            },
            
            "inveja_produtiva": {
                "nome": "Inveja Produtiva",
                "categoria": "emocional_primario",
                "gatilho_central": "Comparação com pares",
                "mecanica_psicologica": "Transformar inveja em combustível",
                "momento_ideal": "Demonstração de resultados - prova social",
                "ativacao_base": "Enquanto você [situação atual], outros como você [resultado desejado]",
                "poder_impacto": 8.5,
                "complementa": ["ambiente_vampiro", "oportunidade_oculta"]
            },
            
            "relogio_psicologico": {
                "nome": "Relógio Psicológico",
                "categoria": "emocional_primario",
                "gatilho_central": "Urgência existencial",
                "mecanica_psicologica": "Tempo como recurso finito",
                "momento_ideal": "Antes da oferta - criação de urgência",
                "ativacao_base": "Quantos [período] você ainda vai [desperdício]?",
                "poder_impacto": 9.2,
                "complementa": ["custo_invisível", "decisão_binária"]
            },
            
            "identidade_aprisionada": {
                "nome": "Identidade Aprisionada",
                "categoria": "emocional_primario",
                "gatilho_central": "Conflito entre quem é e quem poderia ser",
                "mecanica_psicologica": "Expor a máscara social",
                "momento_ideal": "Desenvolvimento do problema - consciência",
                "ativacao_base": "Você não é [rótulo limitante], você é [potencial real]",
                "poder_impacto": 8.8,
                "complementa": ["ambição_expandida", "coragem_necessária"]
            },
            
            "custo_invisivel": {
                "nome": "Custo Invisível",
                "categoria": "emocional_primario",
                "gatilho_central": "Perda não percebida",
                "mecanica_psicologica": "Quantificar o preço da inação",
                "momento_ideal": "Agitação do problema - amplificação da dor",
                "ativacao_base": "Cada dia sem [solução] custa [perda específica]",
                "poder_impacto": 9.3,
                "complementa": ["relógio_psicológico", "diagnóstico_brutal"]
            },
            
            "ambicao_expandida": {
                "nome": "Ambição Expandida",
                "categoria": "emocional_primario",
                "gatilho_central": "Sonhos pequenos demais",
                "mecanica_psicologica": "Elevar o teto mental de possibilidades",
                "momento_ideal": "Visão do futuro - expansão de possibilidades",
                "ativacao_base": "Se o esforço é o mesmo, por que você está pedindo tão pouco?",
                "poder_impacto": 8.7,
                "complementa": ["troféu_secreto", "oportunidade_oculta"]
            },
            
            "diagnostico_brutal": {
                "nome": "Diagnóstico Brutal",
                "categoria": "emocional_primario",
                "gatilho_central": "Confronto com a realidade atual",
                "mecanica_psicologica": "Criar indignação produtiva com status quo",
                "momento_ideal": "Início - quebra de padrão e consciência",
                "ativacao_base": "Olhe seus números/situação. Até quando você vai aceitar isso?",
                "poder_impacto": 9.8,
                "complementa": ["ferida_exposta", "ambiente_vampiro"]
            },
            
            "ambiente_vampiro": {
                "nome": "Ambiente Vampiro",
                "categoria": "emocional_primario",
                "gatilho_central": "Consciência do entorno tóxico",
                "mecanica_psicologica": "Revelar como ambiente atual suga energia/potencial",
                "momento_ideal": "Identificação de obstáculos externos",
                "ativacao_base": "Seu ambiente te impulsiona ou te mantém pequeno?",
                "poder_impacto": 8.4,
                "complementa": ["mentor_salvador", "coragem_necessária"]
            },
            
            "mentor_salvador": {
                "nome": "Mentor Salvador",
                "categoria": "emocional_primario",
                "gatilho_central": "Necessidade de orientação externa",
                "mecanica_psicologica": "Ativar desejo por figura de autoridade que acredita neles",
                "momento_ideal": "Apresentação da solução - posicionamento de autoridade",
                "ativacao_base": "Você precisa de alguém que veja seu potencial quando você não consegue",
                "poder_impacto": 8.6,
                "complementa": ["ambiente_vampiro", "método_vs_sorte"]
            },
            
            "coragem_necessaria": {
                "nome": "Coragem Necessária",
                "categoria": "emocional_primario",
                "gatilho_central": "Medo paralisante disfarçado",
                "mecanica_psicologica": "Transformar desculpas em decisões corajosas",
                "momento_ideal": "Fechamento - superação de objeções",
                "ativacao_base": "Não é sobre condições perfeitas, é sobre decidir apesar do medo",
                "poder_impacto": 8.9,
                "complementa": ["decisão_binária", "identidade_aprisionada"]
            },
            
            "mecanismo_revelado": {
                "nome": "Mecanismo Revelado",
                "categoria": "racional_complementar",
                "gatilho_central": "Compreensão do 'como'",
                "mecanica_psicologica": "Desmistificar o complexo",
                "momento_ideal": "Demonstração da solução - prova de conceito",
                "ativacao_base": "É simplesmente [analogia simples], não [complicação percebida]",
                "poder_impacto": 7.8,
                "complementa": ["método_vs_sorte", "padrão_oculto"]
            },
            
            "prova_matematica": {
                "nome": "Prova Matemática",
                "categoria": "racional_complementar",
                "gatilho_central": "Certeza numérica",
                "mecanica_psicologica": "Equação irrefutável",
                "momento_ideal": "Validação da solução - dados concretos",
                "ativacao_base": "Se você fizer X por Y dias = Resultado Z garantido",
                "poder_impacto": 8.2,
                "complementa": ["mecanismo_revelado", "atalho_ético"]
            },
            
            "padrao_oculto": {
                "nome": "Padrão Oculto",
                "categoria": "racional_complementar",
                "gatilho_central": "Insight revelador",
                "mecanica_psicologica": "Mostrar o que sempre esteve lá",
                "momento_ideal": "Educação - revelação de insights",
                "ativacao_base": "Todos que conseguiram [resultado] fizeram [padrão específico]",
                "poder_impacto": 8.0,
                "complementa": ["exceção_possível", "oportunidade_oculta"]
            },
            
            "excecao_possivel": {
                "nome": "Exceção Possível",
                "categoria": "racional_complementar",
                "gatilho_central": "Quebra de limitação",
                "mecanica_psicologica": "Provar que regras podem ser quebradas",
                "momento_ideal": "Superação de crenças limitantes",
                "ativacao_base": "Diziam que [limitação], mas [prova contrária]",
                "poder_impacto": 7.9,
                "complementa": ["padrão_oculto", "ambição_expandida"]
            },
            
            "atalho_etico": {
                "nome": "Atalho Ético",
                "categoria": "racional_complementar",
                "gatilho_central": "Eficiência sem culpa",
                "mecanica_psicologica": "Validar o caminho mais rápido",
                "momento_ideal": "Apresentação do método - justificativa",
                "ativacao_base": "Por que sofrer [tempo longo] se existe [atalho comprovado]?",
                "poder_impacto": 8.1,
                "complementa": ["método_vs_sorte", "prova_matemática"]
            },
            
            "decisao_binaria": {
                "nome": "Decisão Binária",
                "categoria": "racional_complementar",
                "gatilho_central": "Simplificação radical",
                "mecanica_psicologica": "Eliminar zona cinzenta",
                "momento_ideal": "Fechamento - forçar decisão",
                "ativacao_base": "Ou você [ação desejada] ou aceita [consequência dolorosa]",
                "poder_impacto": 9.1,
                "complementa": ["relógio_psicológico", "coragem_necessária"]
            },
            
            "oportunidade_oculta": {
                "nome": "Oportunidade Oculta",
                "categoria": "racional_complementar",
                "gatilho_central": "Vantagem não percebida",
                "mecanica_psicologica": "Revelar demanda/chance óbvia mas ignorada",
                "momento_ideal": "Contextualização do mercado - timing",
                "ativacao_base": "O mercado está gritando por [solução] e ninguém está ouvindo",
                "poder_impacto": 8.3,
                "complementa": ["padrão_oculto", "ambição_expandida"]
            },
            
            "metodo_vs_sorte": {
                "nome": "Método vs Sorte",
                "categoria": "racional_complementar",
                "gatilho_central": "Caos vs sistema",
                "mecanica_psicologica": "Contrastar tentativa aleatória com caminho estruturado",
                "momento_ideal": "Diferenciação da solução - metodologia",
                "ativacao_base": "Sem método você está cortando mata com foice. Com método, está na autoestrada",
                "poder_impacto": 8.7,
                "complementa": ["mentor_salvador", "atalho_ético"]
            }
        }
    
    def analyze_avatar_for_drivers(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa avatar e identifica drivers mais eficazes"""
        
        # Extrai características do avatar
        dores = avatar_data.get('dores_viscerais', [])
        desejos = avatar_data.get('desejos_secretos', [])
        objecoes = avatar_data.get('objecoes_reais', [])
        perfil_psico = avatar_data.get('perfil_psicografico', {})
        
        # Identifica padrões emocionais
        emotional_patterns = self._identify_emotional_patterns(dores, desejos, perfil_psico)
        
        # Seleciona drivers mais eficazes
        selected_drivers = self._select_optimal_drivers(emotional_patterns, objecoes)
        
        # Customiza drivers para o avatar específico
        customized_drivers = self._customize_drivers_for_avatar(selected_drivers, avatar_data)
        
        return {
            "emotional_patterns": emotional_patterns,
            "selected_drivers": selected_drivers,
            "customized_drivers": customized_drivers,
            "sequencing_strategy": self._create_sequencing_strategy(customized_drivers),
            "implementation_guide": self._create_implementation_guide(customized_drivers)
        }
    
    def _identify_emotional_patterns(
        self, 
        dores: List[str], 
        desejos: List[str], 
        perfil_psico: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Identifica padrões emocionais do avatar"""
        
        patterns = {
            "dor_dominante": "frustração_estagnação",
            "desejo_primario": "liberdade_reconhecimento",
            "medo_central": "fracasso_público",
            "motivador_principal": "crescimento_pessoal",
            "bloqueio_mental": "perfeccionismo_paralisante",
            "gatilho_decisão": "urgência_oportunidade"
        }
        
        # Analisa dores para identificar padrão dominante
        dor_keywords = {
            "frustração_estagnação": ["estagnação", "não sair do lugar", "trabalhar muito", "sem crescimento"],
            "medo_fracasso": ["fracasso", "desmoronar", "perder tudo", "não conseguir"],
            "sobrecarga_tempo": ["tempo", "sobrecarregado", "não conseguir se desconectar", "12 horas"],
            "comparação_social": ["concorrência", "outros crescendo", "ficar para trás", "competidores"]
        }
        
        for pattern, keywords in dor_keywords.items():
            score = sum(1 for dor in dores for keyword in keywords if keyword.lower() in dor.lower())
            if score > 0:
                patterns["dor_dominante"] = pattern
                break
        
        # Analisa desejos para identificar motivação primária
        desejo_keywords = {
            "liberdade_reconhecimento": ["autoridade", "reconhecido", "liberdade", "legado"],
            "segurança_controle": ["segurança", "controle", "estabilidade", "previsibilidade"],
            "impacto_social": ["impactar", "ajudar", "transformar", "diferença"],
            "abundância_material": ["dinheiro", "riqueza", "abundância", "financeira"]
        }
        
        for pattern, keywords in desejo_keywords.items():
            score = sum(1 for desejo in desejos for keyword in keywords if keyword.lower() in desejo.lower())
            if score > 0:
                patterns["desejo_primario"] = pattern
                break
        
        return patterns
    
    def _select_optimal_drivers(
        self, 
        emotional_patterns: Dict[str, Any], 
        objecoes: List[str]
    ) -> List[str]:
        """Seleciona drivers mais eficazes baseado nos padrões emocionais"""
        
        # Mapeamento de padrões para drivers mais eficazes
        pattern_driver_map = {
            "frustração_estagnação": ["diagnóstico_brutal", "ambiente_vampiro", "relógio_psicológico"],
            "medo_fracasso": ["coragem_necessária", "mentor_salvador", "método_vs_sorte"],
            "sobrecarga_tempo": ["custo_invisível", "atalho_ético", "decisão_binária"],
            "comparação_social": ["inveja_produtiva", "ambição_expandida", "oportunidade_oculta"]
        }
        
        # Drivers essenciais que sempre devem estar presentes
        essential_drivers = ["diagnóstico_brutal", "ambição_expandida", "relógio_psicológico"]
        
        # Seleciona drivers baseado no padrão de dor dominante
        dor_dominante = emotional_patterns.get("dor_dominante", "frustração_estagnação")
        pattern_drivers = pattern_driver_map.get(dor_dominante, pattern_driver_map["frustração_estagnação"])
        
        # Combina drivers essenciais com específicos do padrão
        selected = list(set(essential_drivers + pattern_drivers))
        
        # Adiciona drivers complementares baseado em objeções
        if any("tempo" in obj.lower() for obj in objecoes):
            selected.append("atalho_ético")
        
        if any("dinheiro" in obj.lower() or "preço" in obj.lower() for obj in objecoes):
            selected.append("custo_invisível")
        
        if any("não funciona" in obj.lower() or "já tentei" in obj.lower() for obj in objecoes):
            selected.append("método_vs_sorte")
        
        # Limita a 7 drivers para não sobrecarregar
        return selected[:7]
    
    def _customize_drivers_for_avatar(
        self, 
        selected_drivers: List[str], 
        avatar_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Customiza drivers para o avatar específico"""
        
        customized = []
        
        for driver_key in selected_drivers:
            if driver_key not in self.universal_drivers:
                continue
                
            base_driver = self.universal_drivers[driver_key]
            
            # Customiza o driver
            customized_driver = {
                "nome": base_driver["nome"],
                "categoria": base_driver["categoria"],
                "gatilho_central": base_driver["gatilho_central"],
                "mecanica_psicologica": base_driver["mecanica_psicologica"],
                "momento_ideal": base_driver["momento_ideal"],
                "poder_impacto": base_driver["poder_impacto"],
                
                # Customizações específicas
                "definicao_visceral": self._create_visceral_definition(base_driver, avatar_data),
                "roteiro_ativacao": self._create_activation_script(base_driver, avatar_data),
                "frases_ancoragem": self._create_anchoring_phrases(base_driver, avatar_data),
                "prova_logica": self._create_logical_proof(base_driver, avatar_data),
                "loop_reforco": self._create_reinforcement_loop(base_driver, avatar_data),
                "implementacao_pratica": self._create_practical_implementation(base_driver, avatar_data)
            }
            
            customized.append(customized_driver)
        
        return customized
    
    def _create_visceral_definition(
        self, 
        base_driver: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> str:
        """Cria definição visceral customizada"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        dores = avatar_data.get('dores_viscerais', [])
        
        definitions = {
            "Diagnóstico Brutal": f"O momento devastador quando você percebe que está trabalhando como escravo no próprio negócio de {segmento}, gerando resultados medíocres enquanto vê outros com menos experiência alcançando o que você sempre sonhou.",
            
            "Ambição Expandida": f"A revelação de que você está subestimando drasticamente seu potencial no mercado de {segmento}, pedindo migalhas quando poderia estar dominando territórios inteiros.",
            
            "Relógio Psicológico": f"A consciência aterrorizante de que cada dia perdido em estratégias fracas no {segmento} é um dia a menos para construir o império que você merece.",
            
            "Custo Invisível": f"A hemorragia silenciosa de oportunidades, dinheiro e tempo que vaza do seu negócio de {segmento} enquanto você mantém processos obsoletos e mentalidade pequena.",
            
            "Ambiente Vampiro": f"O reconhecimento doloroso de que seu ambiente atual no {segmento} está sugando sua energia, criatividade e ambição, mantendo você preso em um ciclo de mediocridade.",
            
            "Método vs Sorte": f"A diferença brutal entre quem tem um sistema comprovado no {segmento} e quem está tentando na sorte, cortando mato com facão enquanto outros voam de helicóptero.",
            
            "Coragem Necessária": f"O momento de verdade onde você precisa escolher entre a segurança falsa da zona de conforto no {segmento} e a coragem de construir algo extraordinário."
        }
        
        return definitions.get(base_driver["nome"], f"Driver customizado para {segmento}")
    
    def _create_activation_script(
        self, 
        base_driver: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> Dict[str, str]:
        """Cria roteiro de ativação customizado"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        produto = avatar_data.get('produto', 'solução')
        dores = avatar_data.get('dores_viscerais', [])
        desejos = avatar_data.get('desejos_secretos', [])
        
        # Extrai dor principal
        dor_principal = dores[0] if dores else f"trabalhar muito em {segmento} sem ver resultados"
        desejo_principal = desejos[0] if desejos else f"ser reconhecido como autoridade em {segmento}"
        
        scripts = {
            "Diagnóstico Brutal": {
                "pergunta_abertura": f"Você está satisfeito com seus resultados atuais no {segmento}? Olhe seus números dos últimos 6 meses. Isso é tudo que você consegue produzir?",
                "historia_analogia": f"É como um piloto de Fórmula 1 dirigindo um Fusca 1970. Você tem o talento, a experiência, o conhecimento do mercado de {segmento}, mas está usando ferramentas e estratégias de 20 anos atrás. Enquanto isso, novatos com sistemas modernos estão te ultrapassando na curva.",
                "metafora_visual": f"Imagine um painel de controle onde cada métrica do seu negócio de {segmento} pisca verde. Onde cada processo funciona como um relógio suíço. Onde você acorda sabendo exatamente quanto vai faturar este mês.",
                "comando_acao": f"Pare de aceitar migalhas no {segmento}. Comece a construir o sistema que você merece ter."
            },
            
            "Ambição Expandida": {
                "pergunta_abertura": f"Se você pudesse multiplicar seus resultados no {segmento} por 10 com o mesmo esforço, você faria? Então por que está se contentando com tão pouco?",
                "historia_analogia": f"É como pedir um copo d'água quando você está na frente de uma cachoeira. O mercado de {segmento} tem potencial infinito, mas você está operando com mentalidade de escassez, limitando artificialmente suas possibilidades.",
                "metafora_visual": f"Visualize seu nome sendo anunciado como a maior autoridade em {segmento} do país. Imagine palestrando para milhares, sendo procurado pela mídia, tendo uma fila de clientes esperando para trabalhar com você.",
                "comando_acao": f"Expanda sua visão. Se o esforço é o mesmo, por que não dominar todo o mercado de {segmento}?"
            },
            
            "Relógio Psicológico": {
                "pergunta_abertura": f"Quantos anos você ainda vai desperdiçar tentando crescer no {segmento} sem um sistema que funciona?",
                "historia_analogia": f"É como plantar uma árvore. O melhor momento foi há 20 anos. O segundo melhor momento é agora. Cada dia que você adia implementar um sistema real no {segmento} é um dia a menos para colher os frutos da árvore que você poderia ter plantado.",
                "metafora_visual": f"Imagine olhar para trás daqui a 5 anos e perceber que você poderia ter construído um império no {segmento}, mas perdeu tempo com estratégias fracas e mentalidade pequena.",
                "comando_acao": f"O tempo não volta. Comece hoje a construir o futuro que você quer no {segmento}."
            }
        }
        
        return scripts.get(base_driver["nome"], {
            "pergunta_abertura": f"Como você se sente sobre sua situação atual no {segmento}?",
            "historia_analogia": f"É como navegar sem bússola no mercado de {segmento}.",
            "metafora_visual": f"Imagine ter total controle sobre seu negócio de {segmento}.",
            "comando_acao": f"Tome uma decisão que mude sua trajetória no {segmento}."
        })
    
    def _create_anchoring_phrases(
        self, 
        base_driver: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> List[str]:
        """Cria frases de ancoragem customizadas"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        
        phrases = {
            "Diagnóstico Brutal": [
                f"Mediocridade no {segmento} é uma escolha, não um destino",
                f"Seus resultados atuais no {segmento} são o reflexo das suas estratégias fracas",
                f"Enquanto você aceita migalhas, outros dominam o mercado de {segmento}",
                f"Talento sem sistema no {segmento} é desperdício de potencial",
                f"Você não está preso aos seus resultados atuais no {segmento}"
            ],
            
            "Ambição Expandida": [
                f"Se você vai sonhar com {segmento}, sonhe grande ou vá para casa",
                f"Pequenos planos no {segmento} não inflamam o sangue dos homens",
                f"Você nasceu para dominar o {segmento}, não para sobreviver nele",
                f"Mediocridade é o maior insulto ao seu potencial no {segmento}",
                f"O mercado de {segmento} está esperando por um líder. Por que não você?"
            ],
            
            "Relógio Psicológico": [
                f"Cada dia sem sistema no {segmento} é dinheiro jogado fora",
                f"O tempo perdido no {segmento} nunca volta, mas o futuro ainda pode ser construído",
                f"Procrastinação no {segmento} é o assassino silencioso dos sonhos",
                f"Enquanto você hesita no {segmento}, oportunidades viram pesadelos",
                f"O melhor momento para dominar o {segmento} foi ontem. O segundo melhor é agora"
            ]
        }
        
        return phrases.get(base_driver["nome"], [
            f"Transforme sua realidade no {segmento}",
            f"O poder está em suas mãos no {segmento}",
            f"Decida ser extraordinário no {segmento}"
        ])
    
    def _create_logical_proof(
        self, 
        base_driver: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> Dict[str, str]:
        """Cria prova lógica customizada"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        preco = avatar_data.get('preco', 997)
        
        proofs = {
            "Diagnóstico Brutal": {
                "estatistica": f"87% dos profissionais de {segmento} trabalham mais de 60 horas por semana mas faturam menos que deveriam",
                "caso_exemplo": f"João tinha 15 anos de experiência em {segmento} mas faturava R$ 8.000/mês. Após implementar um sistema, chegou a R$ 45.000/mês em 8 meses",
                "demonstracao": f"Compare seus resultados dos últimos 12 meses no {segmento} com o potencial real do seu mercado"
            },
            
            "Ambição Expandida": {
                "estatistica": f"O mercado brasileiro de {segmento} movimenta R$ 2,3 bilhões anuais, mas 95% dos profissionais capturam menos de 0,01% desse valor",
                "caso_exemplo": f"Maria expandiu sua visão no {segmento} de R$ 5.000/mês para R$ 50.000/mês simplesmente mudando sua estratégia de precificação",
                "demonstracao": f"Calcule: se você atendesse apenas 1% do seu mercado potencial em {segmento}, quanto faturaria?"
            },
            
            "Relógio Psicológico": {
                "estatistica": f"Profissionais que implementam sistemas no {segmento} recuperam o investimento em média 3,2 meses",
                "caso_exemplo": f"Carlos perdeu 2 anos tentando crescer sozinho no {segmento}. Com mentoria, alcançou em 6 meses o que não conseguiu em 24",
                "demonstracao": f"Cada mês de atraso no {segmento} custa em média R$ {preco * 3} em oportunidades perdidas"
            }
        }
        
        return proofs.get(base_driver["nome"], {
            "estatistica": f"Dados comprovam eficácia no {segmento}",
            "caso_exemplo": f"Casos reais de sucesso no {segmento}",
            "demonstracao": f"Resultados mensuráveis no {segmento}"
        })
    
    def _create_reinforcement_loop(
        self, 
        base_driver: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> str:
        """Cria loop de reforço customizado"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        
        loops = {
            "Diagnóstico Brutal": f"Toda vez que você olhar seus resultados no {segmento}, lembre: 'Isso é reflexo das minhas estratégias fracas, não do meu potencial'",
            "Ambição Expandida": f"Sempre que alguém perguntar sobre seus planos no {segmento}, responda com sua visão expandida, não com sua realidade atual",
            "Relógio Psicológico": f"A cada decisão adiada no {segmento}, calcule: 'Quanto isso está me custando em oportunidades perdidas?'",
            "Custo Invisível": f"Quando ver um processo manual no seu negócio de {segmento}, pense: 'Quanto dinheiro está vazando aqui?'",
            "Método vs Sorte": f"Antes de qualquer ação no {segmento}, pergunte: 'Isso é baseado em método comprovado ou estou tentando na sorte?'"
        }
        
        return loops.get(base_driver["nome"], f"Reforce constantemente a importância da transformação no {segmento}")
    
    def _create_practical_implementation(
        self, 
        base_driver: Dict[str, Any], 
        avatar_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria guia de implementação prática"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        
        return {
            "live_aquecimento": f"Como introduzir o driver durante live de aquecimento para {segmento}",
            "cpl_1": f"Como desenvolver o driver na primeira aula/conteúdo sobre {segmento}",
            "cpl_2": f"Como aprofundar o driver na segunda aula/conteúdo sobre {segmento}",
            "cpl_3": f"Como cristalizar o driver na terceira aula/conteúdo sobre {segmento}",
            "webinar_vendas": f"Como usar o driver durante webinar de vendas para {segmento}",
            "follow_up": f"Como reativar o driver em e-mails de follow-up sobre {segmento}",
            "objecoes": f"Como usar o driver para superar objeções específicas do {segmento}",
            "fechamento": f"Como usar o driver no fechamento de vendas para {segmento}"
        }
    
    def _create_sequencing_strategy(self, customized_drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria estratégia de sequenciamento dos drivers"""
        
        # Ordena drivers por momento ideal e poder de impacto
        sequenced = sorted(customized_drivers, key=lambda x: x["poder_impacto"], reverse=True)
        
        return {
            "fase_1_despertar": [d for d in sequenced if "diagnóstico" in d["nome"].lower() or "ferida" in d["nome"].lower()],
            "fase_2_desejo": [d for d in sequenced if "ambição" in d["nome"].lower() or "troféu" in d["nome"].lower()],
            "fase_3_decisao": [d for d in sequenced if "relógio" in d["nome"].lower() or "custo" in d["nome"].lower()],
            "fase_4_direcao": [d for d in sequenced if "método" in d["nome"].lower() or "coragem" in d["nome"].lower()],
            "sequencia_recomendada": [d["nome"] for d in sequenced],
            "timing_otimo": {
                "intervalo_entre_drivers": "3-5 minutos",
                "reforco_necessario": "A cada 15 minutos",
                "intensidade_crescente": "Aumentar 20% a cada driver"
            }
        }
    
    def _create_implementation_guide(self, customized_drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria guia completo de implementação"""
        
        return {
            "preparacao": {
                "estudo_avatar": "Memorize as 3 dores principais e 3 desejos secretos",
                "teste_drivers": "Teste cada driver com 5 pessoas do avatar antes de usar",
                "calibragem": "Ajuste intensidade baseado na reação da audiência",
                "backup_plan": "Tenha 2 drivers alternativos para cada momento"
            },
            
            "execucao": {
                "abertura": "Sempre comece com Diagnóstico Brutal para quebrar padrão",
                "desenvolvimento": "Use drivers emocionais para criar tensão",
                "climax": "Combine 2-3 drivers no momento da oferta",
                "fechamento": "Termine com Decisão Binária para forçar ação"
            },
            
            "monitoramento": {
                "sinais_positivos": ["Silêncio absoluto", "Perguntas específicas", "Linguagem corporal tensa"],
                "sinais_negativos": ["Dispersão", "Conversas paralelas", "Saídas da sala"],
                "ajustes_tempo_real": "Como modificar drivers baseado na reação",
                "escalation": "Quando e como intensificar drivers que não estão funcionando"
            },
            
            "otimizacao": {
                "teste_ab": "Como testar diferentes versões dos drivers",
                "metricas": "Taxa de engajamento, tempo de atenção, conversões",
                "refinamento": "Como melhorar drivers baseado nos resultados",
                "personalizacao": "Como adaptar drivers para diferentes segmentos do avatar"
            }
        }
    
    def generate_complete_drivers_system(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera sistema completo de drivers mentais customizados"""
        
        logger.info("🧠 Gerando sistema completo de drivers mentais...")
        
        # Analisa avatar para drivers
        driver_analysis = self.analyze_avatar_for_drivers(avatar_data)
        
        # Cria arsenal de emergência
        emergency_arsenal = self._create_emergency_arsenal(avatar_data, context_data)
        
        # Cria sistema anti-objeção
        anti_objection_system = self._create_anti_objection_system(avatar_data)
        
        # Cria pré-pitch invisível
        pre_pitch_system = self._create_pre_pitch_system(avatar_data, context_data)
        
        return {
            "drivers_customizados": driver_analysis["customized_drivers"],
            "sequenciamento_estrategico": driver_analysis["sequencing_strategy"],
            "guia_implementacao": driver_analysis["implementation_guide"],
            "arsenal_emergencia": emergency_arsenal,
            "sistema_anti_objecao": anti_objection_system,
            "pre_pitch_invisivel": pre_pitch_system,
            "metricas_eficacia": self._create_effectiveness_metrics(),
            "casos_uso_pratico": self._create_practical_use_cases(avatar_data),
            "troubleshooting": self._create_troubleshooting_guide()
        }
    
    def _create_emergency_arsenal(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> List[str]:
        """Cria arsenal de emergência para situações críticas"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        
        return [
            f"Se a audiência está dispersa: 'Quem aqui está satisfeito com seus resultados no {segmento}? Ninguém? Então me deem 5 minutos.'",
            f"Se há resistência: 'Eu sei que vocês já ouviram promessas sobre {segmento}. Eu também já fui enganado. Por isso vou mostrar dados, não promessas.'",
            f"Se questionam credibilidade: 'Vocês não precisam acreditar em mim. Acreditem nos números e nos resultados que vou mostrar sobre {segmento}.'",
            f"Se há objeções de preço: 'O caro não é investir em {segmento}. O caro é continuar perdendo dinheiro com estratégias fracas.'",
            f"Se há objeções de tempo: 'Vocês não têm tempo para implementar, mas têm tempo para continuar frustrados no {segmento}?'",
            f"Se questionam se funciona: 'Não funciona para quem não implementa. Para quem implementa no {segmento}, os resultados são inevitáveis.'",
            f"Se há comparação com concorrentes: 'A diferença não está no que ensinamos sobre {segmento}, mas em como garantimos que vocês implementem.'",
            f"Se há dúvidas sobre timing: 'O melhor momento para plantar uma árvore no {segmento} foi há 10 anos. O segundo melhor momento é agora.'",
            f"Se questionam necessidade: 'Vocês podem continuar como estão no {segmento}. A pergunta é: por quanto tempo mais?'",
            f"Se há medo de mudança: 'O maior risco no {segmento} não é mudar. É ficar parado enquanto o mercado evolui.'"
        ]
    
    def _create_anti_objection_system(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria sistema anti-objeção completo"""
        
        objecoes = avatar_data.get('objecoes_reais', [])
        segmento = avatar_data.get('segmento', 'negócios')
        
        # Objeções universais com contra-ataques
        universal_objections = {
            "preco_alto": {
                "objecao": "Está muito caro",
                "raiz_emocional": "Medo de perder dinheiro / Desvalorização própria",
                "contra_ataque": f"O caro não é investir em {segmento}. O caro é continuar perdendo R$ X por mês com estratégias fracas. Em 6 meses, você vai ter gastado mais tentando sozinho do que investindo na solução certa agora.",
                "prova_logica": f"Clientes que investiram recuperaram o valor em média em 3,2 meses no {segmento}",
                "reframe": "Não é gasto, é investimento com ROI comprovado"
            },
            
            "falta_tempo": {
                "objecao": "Não tenho tempo para implementar",
                "raiz_emocional": "Sobrecarga / Medo de mais trabalho",
                "contra_ataque": f"Você não tem tempo para implementar, mas tem tempo para continuar trabalhando 12 horas por dia no {segmento} pelos próximos 5 anos? O sistema economiza 20 horas por semana depois de implementado.",
                "prova_logica": f"Implementação leva 30 dias, economia de tempo dura para sempre no {segmento}",
                "reframe": "Não é sobre ter tempo, é sobre criar tempo"
            },
            
            "ja_tentei_antes": {
                "objecao": "Já tentei várias coisas e não funcionou",
                "raiz_emocional": "Frustração acumulada / Descrença",
                "contra_ataque": f"Exato! Você tentou várias coisas no {segmento} e não funcionou porque eram táticas isoladas, não um sistema completo. É como tentar construir uma casa comprando apenas tijolos, sem planta, sem fundação, sem arquiteto.",
                "prova_logica": f"92% das tentativas isoladas falham no {segmento}. 87% dos sistemas completos funcionam",
                "reframe": "Suas tentativas anteriores foram investimento em aprendizado"
            },
            
            "meu_nicho_diferente": {
                "objecao": f"Meu nicho em {segmento} é muito específico",
                "raiz_emocional": "Medo de não se encaixar / Necessidade de ser especial",
                "contra_ataque": f"Perfeito! Nichos específicos no {segmento} são onde estão as maiores oportunidades. Quanto mais específico, menos concorrência e maior margem. Você está na posição ideal.",
                "prova_logica": f"Nichos específicos no {segmento} têm 340% mais lucratividade que mercados gerais",
                "reframe": "Especificidade é vantagem competitiva, não limitação"
            },
            
            "preciso_pensar": {
                "objecao": "Preciso pensar / conversar com esposa",
                "raiz_emocional": "Medo de decisão errada / Procrastinação",
                "contra_ataque": f"Entendo. Mas me responda: há quanto tempo você está 'pensando' em crescer no {segmento}? 6 meses? 1 ano? 2 anos? Pensar sem agir é só uma forma sofisticada de procrastinar.",
                "prova_logica": f"Cada mês de 'pensamento' no {segmento} custa R$ X em oportunidades perdidas",
                "reframe": "A melhor decisão é a que você toma com informação suficiente, não perfeita"
            }
        }
        
        return {
            "objecoes_universais": universal_objections,
            "arsenal_emergencia": self._create_emergency_arsenal(avatar_data, {}),
            "tecnicas_avancadas": {
                "inversao_objecao": "Como transformar objeção em razão para comprar",
                "validacao_emocional": "Como validar a emoção por trás da objeção",
                "prova_social_direcionada": "Como usar casos específicos para cada objeção",
                "urgencia_genuina": "Como criar urgência real, não artificial"
            },
            "scripts_fechamento": self._create_closing_scripts(avatar_data)
        }
    
    def _create_pre_pitch_system(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria sistema de pré-pitch invisível"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        
        return {
            "orquestracao_emocional": {
                "sequencia_psicologica": [
                    {
                        "fase": "Quebra de Padrão",
                        "objetivo": "Interromper piloto automático mental",
                        "tempo": "Primeiros 2 minutos",
                        "tecnicas": ["Pergunta chocante", "Estatística surpreendente", "Afirmação controversa"],
                        "exemplo": f"Quem aqui está satisfeito com seus resultados no {segmento}? [Pausa] Ninguém? Então vocês estão no lugar certo."
                    },
                    {
                        "fase": "Validação Emocional",
                        "objetivo": "Criar conexão e confiança",
                        "tempo": "Minutos 3-7",
                        "tecnicas": ["História pessoal", "Vulnerabilidade controlada", "Espelhamento de dores"],
                        "exemplo": f"Eu também já trabalhei 14 horas por dia no {segmento} achando que esforço era sinônimo de resultado."
                    },
                    {
                        "fase": "Amplificação do Problema",
                        "objetivo": "Intensificar consciência da dor",
                        "tempo": "Minutos 8-15",
                        "tecnicas": ["Custo da inação", "Comparação social", "Projeção futura"],
                        "exemplo": f"Enquanto vocês hesitam, outros no {segmento} estão construindo impérios."
                    },
                    {
                        "fase": "Vislumbre da Solução",
                        "objetivo": "Plantar esperança e possibilidade",
                        "tempo": "Minutos 16-25",
                        "tecnicas": ["Casos de sucesso", "Demonstração", "Prova de conceito"],
                        "exemplo": f"Deixe-me mostrar como Maria transformou seu negócio de {segmento} em 90 dias."
                    },
                    {
                        "fase": "Autoridade e Credibilidade",
                        "objetivo": "Estabelecer posição de especialista",
                        "tempo": "Minutos 26-35",
                        "tecnicas": ["Resultados próprios", "Reconhecimento externo", "Metodologia única"],
                        "exemplo": f"Nos últimos 5 anos, ajudei 847 profissionais a dominarem o {segmento}."
                    },
                    {
                        "fase": "Urgência Genuína",
                        "objetivo": "Criar pressão temporal real",
                        "tempo": "Minutos 36-40",
                        "tecnicas": ["Oportunidade limitada", "Custo crescente", "Timing de mercado"],
                        "exemplo": f"O mercado de {segmento} está mudando. Quem não se adaptar agora, vai ficar para trás."
                    }
                ]
            },
            
            "ancoragem_de_valor": {
                "valor_percebido": f"Como fazer a audiência perceber o valor real da transformação no {segmento}",
                "comparacao_custos": f"Como contrastar custo da solução vs custo da inação no {segmento}",
                "roi_demonstrado": f"Como provar ROI através de casos reais no {segmento}",
                "investimento_vs_gasto": f"Como reposicionar preço como investimento no {segmento}"
            },
            
            "triggers_decisao": {
                "escassez_real": f"Como criar escassez genuína para {segmento}",
                "prova_social_massiva": f"Como usar depoimentos específicos do {segmento}",
                "autoridade_emprestada": f"Como usar credibilidade de terceiros no {segmento}",
                "reciprocidade_ativada": f"Como gerar obrigação moral no {segmento}"
            }
        }
    
    def _create_effectiveness_metrics(self) -> Dict[str, Any]:
        """Cria métricas de eficácia dos drivers"""
        
        return {
            "metricas_engajamento": {
                "atencao_sustentada": "Tempo médio de atenção durante ativação do driver",
                "interacao_verbal": "Número de perguntas/comentários após driver",
                "linguagem_corporal": "Mudanças posturais e expressões faciais",
                "participacao_ativa": "Nível de participação em exercícios"
            },
            
            "metricas_conversao": {
                "taxa_permanencia": "% que fica até o final da apresentação",
                "taxa_interesse": "% que faz perguntas sobre a solução",
                "taxa_conversao": "% que se torna cliente",
                "valor_medio": "Ticket médio dos convertidos"
            },
            
            "metricas_qualitativas": {
                "feedback_emocional": "Comentários sobre impacto emocional",
                "mudanca_perspectiva": "Relatos de mudança de visão",
                "urgencia_percebida": "Nível de urgência demonstrado",
                "confianca_gerada": "Grau de confiança estabelecido"
            },
            
            "benchmarks_industria": {
                "driver_mais_eficaz": "Diagnóstico Brutal (94% de engajamento)",
                "sequencia_otima": "Diagnóstico → Ambição → Relógio → Método",
                "timing_ideal": "3-5 minutos por driver com reforço a cada 15 minutos",
                "audiencia_ideal": "25-50 pessoas para máximo impacto"
            }
        }
    
    def _create_practical_use_cases(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria casos de uso práticos"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        
        return {
            "webinar_vendas": {
                "estrutura": "Como usar drivers em webinar de 90 minutos",
                "timing": "Quando ativar cada driver durante o webinar",
                "transicoes": "Como conectar drivers de forma fluida",
                "fechamento": "Como usar drivers no momento da oferta"
            },
            
            "live_aquecimento": {
                "abertura": f"Como usar Diagnóstico Brutal para abrir live sobre {segmento}",
                "desenvolvimento": f"Como desenvolver Ambição Expandida durante live de {segmento}",
                "engajamento": f"Como usar drivers para manter audiência engajada no {segmento}",
                "direcionamento": f"Como direcionar para próxima ação no {segmento}"
            },
            
            "sequencia_emails": {
                "email_1": f"Como usar Ferida Exposta no primeiro e-mail sobre {segmento}",
                "email_2": f"Como desenvolver Custo Invisível no segundo e-mail sobre {segmento}",
                "email_3": f"Como ativar Relógio Psicológico no terceiro e-mail sobre {segmento}",
                "email_4": f"Como usar Decisão Binária no e-mail de fechamento sobre {segmento}"
            },
            
            "vendas_individuais": {
                "descoberta": f"Como usar drivers durante descoberta de necessidades no {segmento}",
                "apresentacao": f"Como incorporar drivers na apresentação da solução para {segmento}",
                "objecoes": f"Como usar drivers para superar objeções no {segmento}",
                "fechamento": f"Como usar drivers no fechamento de vendas individuais no {segmento}"
            }
        }
    
    def _create_troubleshooting_guide(self) -> Dict[str, Any]:
        """Cria guia de solução de problemas"""
        
        return {
            "problemas_comuns": {
                "audiencia_resistente": {
                    "sintomas": ["Braços cruzados", "Expressões céticas", "Conversas paralelas"],
                    "causas": ["Overselling anterior", "Desconfiança", "Saturação de promessas"],
                    "solucoes": ["Começar com vulnerabilidade", "Usar dados, não promessas", "Validar ceticismo"]
                },
                
                "drivers_nao_funcionam": {
                    "sintomas": ["Falta de reação", "Dispersão", "Desinteresse"],
                    "causas": ["Avatar mal definido", "Timing incorreto", "Intensidade inadequada"],
                    "solucoes": ["Revisar avatar", "Ajustar sequência", "Aumentar intensidade gradualmente"]
                },
                
                "conversao_baixa": {
                    "sintomas": ["Alto engajamento, baixa conversão", "Interesse sem ação"],
                    "causas": ["Falta de urgência", "Preço mal ancorado", "Oferta confusa"],
                    "solucoes": ["Intensificar Relógio Psicológico", "Melhorar ancoragem de valor", "Simplificar oferta"]
                }
            },
            
            "ajustes_tempo_real": {
                "leitura_audiencia": "Como identificar sinais de engajamento/resistência",
                "modificacao_drivers": "Como ajustar drivers baseado na reação",
                "escalation": "Quando e como intensificar drivers",
                "backup_plans": "Drivers alternativos para situações específicas"
            },
            
            "otimizacao_continua": {
                "teste_ab": "Como testar diferentes versões dos drivers",
                "feedback_loop": "Como coletar e usar feedback para melhorar",
                "personalizacao": "Como adaptar drivers para diferentes segmentos",
                "evolucao": "Como evoluir drivers baseado em resultados"
            }
        }
    
    def _create_closing_scripts(self, avatar_data: Dict[str, Any]) -> Dict[str, str]:
        """Cria scripts de fechamento customizados"""
        
        segmento = avatar_data.get('segmento', 'negócios')
        preco = avatar_data.get('preco', 997)
        
        return {
            "fechamento_direto": f"Vocês têm duas opções no {segmento}: continuar como estão pelos próximos 5 anos ou transformar tudo nos próximos 90 dias. O que escolhem?",
            
            "fechamento_assumptivo": f"Quando vocês implementarem isso no {segmento}, vão perceber que era mais simples do que imaginavam. A pergunta não é se funciona, é quando vocês querem começar.",
            
            "fechamento_escassez": f"Só posso trabalhar com 20 pessoas por vez no {segmento}. Quem está pronto para ser uma delas?",
            
            "fechamento_urgencia": f"O mercado de {segmento} não vai esperar vocês se decidirem. Ou vocês agem agora ou assistem outros tomarem suas oportunidades.",
            
            "fechamento_valor": f"R$ {preco} é o que vocês gastam em 3 meses tentando sozinhos no {segmento}. Aqui vocês têm a solução completa e ainda sobra dinheiro."
        }

# Instância global
mental_drivers_architect = MentalDriversArchitect()