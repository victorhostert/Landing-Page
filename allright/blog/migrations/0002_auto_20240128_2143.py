# Generated by Django 5.0 on 2024-01-28 19:36

import os
from django.db import migrations
from django.core.files.base import ContentFile

def create_depoimentos(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Depoimento = apps.get_model('blog', 'Depoimento')
    Case = apps.get_model('blog', 'Case')
    Depoimento.objects.using(db_alias).create(
        autor='Antonino Assini, sócio fundador',
        conteudo='Ficamos bastante satisfeitos com o trabalho do Daniel da Allright Consultoria em nossa empresa. Podemos destacar a ética e honestidade nas suas ações, englobando os processos a tecnologia e as pessoas.',
        case=Case.objects.using(db_alias).get(pk=1),
    )
    Depoimento.objects.using(db_alias).create(
        autor='Juarez Castilho, Castilho, Paolin & Advogados Associados',
        conteudo=' O trabalho do Daniel da Allright vem ao encontro das necessidades do advogado, pois ele sabe identificar bem os requisitos e aplicações das demandas, facilitando muito o relacionamento entre empresa e setor jurídico.',
        case=Case.objects.using(db_alias).get(pk=1),
    )
    Depoimento.objects.using(db_alias).create(
        autor='Hugues Boritiyça, WA Solutions Brasil',
        conteudo='A transformação que o trabalho da Allright Consultoria proporcionou, em tão pouco tempo na Britagem Barracão, e ainda durante a pandemia da COVID-19, foi realmente surpreendente. Daniel buscou identificar e desenvolver talentos internos utilizando técnicas de gestão e incentivando a capacitação da equipe. Trazendo metodologia de vanguarda para a gestão de suprimentos colocou a Britagem Barracão um passo à frente da concorrência.',
        case=Case.objects.using(db_alias).get(pk=1),
    )
    Depoimento.objects.using(db_alias).create(
        autor='Mário José Schmitt, sócio fundador',
        conteudo='O Daniel tem uma visão bastante ampla dos negócios. A Allright efetuou um trabalho de muita qualidade e importância para a Ceramfix na organização e estruturação da empresa, permitindo o crescimento sustentado, redução de riscos e aumento dos resultados. Esse trabalho nos ajudou a fechar a importante parceria com o grupo alemão Ardex, multinacional referência mundial em produtos de alta tecnologia no mercado da construção civil.  ',
        case=Case.objects.using(db_alias).get(pk=2),
    )
    Depoimento.objects.using(db_alias).create(
        autor='Juarez Moyses, fundador da Handit Sistemas',
        conteudo='O Daniel nos abriu as portas da Ceramfix e dividiu conosco seus profundos conhecimentos e ferramentas aplicadas na elaboração do Plano Orçamentário Anual, estratégias estas implementadas por ele dentro das melhores práticas na busca pela excelência na gestão empresarial. Este processo foi de grande importância no desenvolvimento do sistema de planejamento orçamentário Handit Planning, hoje utilizado pela Ceramfix e por outras empresas de diversos segmentos. A visão estratégica e o amplo conhecimento em negócios fazem do Daniel um profissional focado na maximização dos resultados, na melhoria constante dos processos inerentes a todas as áreas e, em especial, no controle fino das despesas e custos das organizações. O Daniel nos trouxe a certeza de que "quem planeja tem futuro, quem não planeja tem destino."',
        case=Case.objects.using(db_alias).get(pk=2),
    )
    Depoimento.objects.using(db_alias).create(
        autor='Elton Soares, Dimensão Consultoria Organizacional',
        conteudo='Conheço o Daniel desde 2012 e desde então temos feito parcerias de sucesso. Em todas as empresas que tivemos oportunidade de juntos trabalharmos sempre percebi um alto grau de comprometimento, responsabilidade e busca constante de excelência. Trata-se de um profissional gabaritado e que realmente faz a diferença nos projetos assumidos. Seu conhecimento e experiência, somados a atitude proativa e foco nos resultados lhe garantem ilibada reputação.',
        case=Case.objects.using(db_alias).get(pk=2),
    )

def create_cases(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Case = apps.get_model('blog', 'Case')
    britagem_imagem = os.path.join('/home/app/web/assets/static/britagem_logo.png')
    ceramfix_imagem = os.path.join('/home/app/web/assets/static/ceramfix_logo.png')
    with open(britagem_imagem, 'rb') as f:
        britagem_image_data = f.read()
    with open(ceramfix_imagem, 'rb') as f:
        ceramfix_image_data = f.read()
    case_britagem = Case.objects.using(db_alias).create(
        titulo='CASE BRITAGEM BARRACÃO',
        introducao="""
        Em um diagnóstico inicial, analisamos a estrutura ideal e avaliamos os principais recursos humanos estratégicos disponíveis, providenciando algumas alterações e contratações necessárias. Avaliamos também os filhos e familiares, identificando e sugerindo o melhor aproveitamento individual. 
        No escopo dos trabalhos propusemos fazer a transição, de um empreendimento familiar, para uma empresa estruturada organizacionalmente num organograma profissional, com processos funcionais e sistemicamente integrados.  
        Identificamos os pontos fortes e as principais oportunidades de melhoria, organizando um plano de trabalho direcionado para agregar valor, reduzir riscos, e atingir a efetiva vocação da empresa. 
        """,
        trabalho_executado="""
            Estruturação do Financeiro com Fluxo de Caixa, renegociação do endividamento, alongando prazos e reduzindo taxas e parcelas, permitindo a conclusão de diversos investimentos inacabados, com importante retorno para o negócio. Implantação de um grupo de gestão com reuniões de trabalho semanais e área comercial proativa. Reimplantação do ERP Protheus/Totvs, estruturação do Supply Chain com PCP otimizado pela metodologia DDMRP e ferramenta WA Solutions, Estoques e Tecnologia da Informação. Implantação de Controladoria, reorganização da Contabilidade, análises de custos, preços de venda e rentabilidade. Análise e fechamento, por inviabilidade econômica, da empresa de transporte do grupo. Renegociação dos contratos, gerando ganhos importantes em custos e reposicionamento estratégico com os principais clientes. 
        """
    )
    case_ceramfix = Case.objects.using(db_alias).create(
        titulo='CASE CERAMFIX ',
        introducao="""
        Em crescimento constante, a empresa necessitava de uma estrutura adequada a essa realidade. Iniciamos um processo de integração sistêmica do negócio, estabelecendo os melhores fluxos e processos para a operação, utilizando ferramentas de lean manufactoring e dirigida pela demanda.  
        """,
        trabalho_executado="""
            Planejamento Estratégico, implantação do Plano Operacional (case principal da Handit Planning), compliance, Plano de Cargos e Salários, avaliação por competências e treinamento de lideranças. Reimplantação do ERP Logix/Totvs, implantação do PCP otimizado pela metodologia DDMRP, Controle de Estoques WMS e do Força de Vendas/CRM, otimizado com o Fluig/Totvs. Internalização da Contabilidade, implantação de Business intelligence (BI) e indicadores de performance (KPI’s). Análise de retorno de Investimentos, custos, preços de venda e rentabilidade. Estruturação das áreas de Tecnologia da Informação e Recursos Humanos, Manutenção de Ativos e trabalho estratégico comercial. Coordenação jurídico/tributária e da Due Diligence que resultou na Joint Venture com a multinacional Ardex, parceria firmada devido ao crescimento organizado e estratégico, que despertou o interesse de várias multinacionais.
        """
    )
    case_britagem.imagem.save('britagem_logo.png', ContentFile(britagem_image_data))
    case_ceramfix.imagem.save('ceramfix_logo.png', ContentFile(ceramfix_image_data))
    

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_cases),
        migrations.RunPython(create_depoimentos),
    ]