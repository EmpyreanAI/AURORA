# import pprint
import pymongo
import pandas
import glob
from datetime import datetime
import numpy as np

def create_market_type(stock_market):

    tpMerc = stock_market.TpMerc

    new_tpMercs = [{'_id': 10, 'desc': "Vista"},
                  {'_id': 12, 'desc': "Exercício de opções de compra"},
                  {'_id': 13, 'desc': "Exercício de opções de venda"},
                  {'_id': 17, 'desc': "Leilão"},
                  {'_id': 20, 'desc': "Fracionario"},
                  {'_id': 30, 'desc': "Termo"},
                  {'_id': 50, 'desc': "Futuro com retenção de ganho"},
                  {'_id': 60, 'desc': "Futuro com movimentação contínua"},
                  {'_id': 70, 'desc': "Opções de Venda"},
                  {'_id': 80, 'desc': "Opções de Compra"}]

    tpMerc.insert_many(new_tpMercs)

def create_bdi(stock_market):

    bdi = stock_market.BDI

    new_bdis = [{'_id': 2, 'desc': "LOTE PADRAO"},
                {'_id': 5, 'desc': "SANCIONADAS PELOS REGULAMENTOS BMFBOVESPA"},
                {'_id': 6, 'desc': "CONCORDATARIAS"},
                {'_id': 7, 'desc': "RECUPERACAO EXTRAJUDICIAL"},
                {'_id': 8, 'desc': "RECUPERAÇÃO JUDICIAL"},
                {'_id': 9, 'desc': "RAET - REGIME DE ADMINISTRACAO ESPECIAL TEMPORARIA"},
                {'_id': 10, 'desc': "DIREITOS E RECIBOS"},
                {'_id': 11, 'desc': "INTERVENCAO"},
                {'_id': 12, 'desc': "FUNDOS IMOBILIARIOS"},
                {'_id': 14, 'desc': "CERT.INVEST/TIT.DIV.PUBLICA"},
                {'_id': 18, 'desc': "OBRIGACÕES"},
                {'_id': 22, 'desc': "BÔNUS (PRIVADOS)"},
                {'_id': 26, 'desc': "APOLICES/BÔNUS/TITULOS PUBLICOS"},
                {'_id': 32, 'desc': "EXERCICIO DE OPCOES DE COMPRA DE INDICES"},
                {'_id': 33, 'desc': "EXERCICIO DE OPCOES DE VENDA DE INDICES"},
                {'_id': 38, 'desc': "EXERCICIO DE OPCOES DE COMPRA"},
                {'_id': 42, 'desc': "EXERCICIO DE OPCOES DE VENDA"},
                {'_id': 46, 'desc': "LEILAO DE NAO COTADOS"},
                {'_id': 48, 'desc': "LEILAO DE PRIVATIZACAO"},
                {'_id': 49, 'desc': "LEILAO DO FUNDO DE RECUPERACAO ECONOMICA ESPIRITO    SANTO"},
                {'_id': 50, 'desc': "LEILAO"},
                {'_id': 51, 'desc': "LEILAO FINOR"},
                {'_id': 52, 'desc': "LEILAO FINAM"},
                {'_id': 53, 'desc': "LEILAO FISET"},
                {'_id': 54, 'desc': "LEILAO DE ACOES EM MORA"},
                {'_id': 56, 'desc': "VENDAS POR ALVARA JUDICIAL"},
                {'_id': 58, 'desc': "OUTROS"},
                {'_id': 60, 'desc': "PERMUTA POR ACOES"},
                {'_id': 61, 'desc': "META"},
                {'_id': 62, 'desc': "MERCADO A TERMO"},
                {'_id': 66, 'desc': "DEBENTURES COM DATA DE VENCIMENTO ATE 3 ANOS"},
                {'_id': 68, 'desc': "DEBENTURES COM DATA DE VENCIMENTO MAIOR QUE 3 ANOS"},
                {'_id': 70, 'desc': "FUTURO COM RETENCAO DE GANHOS"},
                {'_id': 71, 'desc': "MERCADO DE FUTURO"},
                {'_id': 74, 'desc': "OPCOES DE COMPRA DE INDICES"},
                {'_id': 75, 'desc': "OPCOES DE VENDA DE INDICES"},
                {'_id': 78, 'desc': "OPCOES DE COMPRA"},
                {'_id': 82, 'desc': "OPCOES DE VENDA"},
                {'_id': 83, 'desc': "BOVESPAFIX"},
                {'_id': 84, 'desc': "SOMA FIX"},
                {'_id': 90, 'desc': "TERMO VISTA REGISTRADO"},
                {'_id': 96, 'desc': "MERCADO FRACIONARIO"},
                {'_id': 99, 'desc': "TOTAL GERAL"}]

    bdi.insert_many(new_bdis)

def create_indopc(stock_market):
    indopc = stock_market.IndoPc

    new_indopcs = [{'_id': 1, 'desc': "CORREÇÃO PELA TAXA DO DÓLAR"},
                   {'_id': 2, 'desc': "CORREÇÃO PELA TJLP"},
                   {'_id': 8, 'desc': "CORREÇÃO PELO IGP-M - OPÇÕES PROTEGIDAS"},
                   {'_id': 9, 'desc': "CORREÇÃO PELA URV"}]

    indopc.insert_many(new_indopcs)

def create_especi(stock_market):
    especi = stock_market.Especi

    new_especis = [{'_id': 'BDR', 'desc': "BDR"},
                   {'_id': 'BNS', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES MISCELÂNEA"},
                   {'_id': 'BNS B/A', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS ORD', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES ORDINÁRIAS"},
                   {'_id': 'BNS P/A', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/B', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/C', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/D', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/E', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/F', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/G', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS P/H', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'BNS PRE', 'desc': "BÔNUS DE SUBSCRIÇÃO EM ACÕES PREFERÊNCIA"},
                   {'_id': 'CDA', 'desc': "CERTIFICADO DE DEPÓSITO DE ACÕES ORDINÁRIAS"},
                   {'_id': 'CI', 'desc': "FUNDO DE INVESTIMENTO"},
                   {'_id': 'CPA', 'desc': "CERTIF. DE POTENCIAL ADIC. DE CONSTRUÇÃO"},
                   {'_id': 'DIR', 'desc': "DIREITOS DE SUBSCRIÇÃO MISCELÂNEA (BÔNUS)"},
                   {'_id': 'DIR ORD', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES ORDINÁRIAS"},
                   {'_id': 'DIR P/A', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/B', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/C', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/D', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/E', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/F', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/G', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR P/H', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'DIR PR', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'DIR PRA', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'DIR PRB', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'DIR PRC', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'DIR PRE', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'LFT', 'desc': "LETRA FINANCEIRA DO TESOURO"},
                   {'_id': 'M1 REC', 'desc': "RECIBO DE SUBSCRIÇÃO DE MISCELÂNEAS"},
                   {'_id': 'ON', 'desc': "ACÕES ORDINÁRIAS NOMINATIVAS"},
                   {'_id': 'ON P', 'desc': "ACÕES ORDINÁRIAS NOMINATIVAS COM DIREITO"},
                   {'_id': 'ON REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES ORDINÁRIAS"},
                   {'_id': 'OR', 'desc': "ACÕES ORDINÁRIAS NOMINATIVAS RESGATÁVEIS"},
                   {'_id': 'OR P', 'desc': "ACÕES ORDINÁRIAS NOMINATIVAS RESGATÁVEIS"},
                   {'_id': 'PCD', 'desc': "POSIÇÃO CONSOLIDADA DA DIVIDA"},
                   {'_id': 'PN', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS"},
                   {'_id': 'PN P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS COM DIREITO"},
                   {'_id': 'PN REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNA', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE A"},
                   {'_id': 'PNA P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE A"},
                   {'_id': 'PNA REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNB', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE B"},
                   {'_id': 'PNB P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE B"},
                   {'_id': 'PNB REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNC', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE C"},
                   {'_id': 'PNC P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE C"},
                   {'_id': 'PNC REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PND', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE D"},
                   {'_id': 'PND P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE D"},
                   {'_id': 'PND REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNE', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE E"},
                   {'_id': 'PNE P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE E"},
                   {'_id': 'PNE REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNF', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE F"},
                   {'_id': 'PNF P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE F"},
                   {'_id': 'PNF REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNG', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE G"},
                   {'_id': 'PNG P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE G"},
                   {'_id': 'PNG REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNH', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE H"},
                   {'_id': 'PNH P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE H"},
                   {'_id': 'PNH REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PNR', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS RESGATÁVEIS"},
                   {'_id': 'PNV', 'desc': "ACÕES PREFERÊNCIAS NOMINATIVAS COM DIREITO"},
                   {'_id': 'PNV P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE V"},
                   {'_id': 'PNV REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES PREFERENCIAIS"},
                   {'_id': 'PR P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS RESGATÁVEIS"},
                   {'_id': 'PRA', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE A"},
                   {'_id': 'PRA P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE A"},
                   {'_id': 'PRA REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'PRB', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE B"},
                   {'_id': 'PRB P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE B"},
                   {'_id': 'PRB REC', 'desc': "DIREITOS DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'PRB REC2', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'PRC', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE C"},
                   {'_id': 'PRC P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE C"},
                   {'_id': 'PRC REC', 'desc': "RECIBO DE SUBSCRIÇÃO EM ACÕES RESGATÁVEIS"},
                   {'_id': 'PRD', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE D"},
                   {'_id': 'PRD P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE D"},
                   {'_id': 'PRE', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE E"},
                   {'_id': 'PRE P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE E"},
                   {'_id': 'PRF', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE F"},
                   {'_id': 'PRF P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE F"},
                   {'_id': 'PRG', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE G"},
                   {'_id': 'PRG P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE G"},
                   {'_id': 'PRH', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE H"},
                   {'_id': 'PRH P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS CLASSE H"},
                   {'_id': 'PRV', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS COM DIREITO"},
                   {'_id': 'PRV P', 'desc': "ACÕES PREFERÊNCIAIS NOMINATIVAS RESG. C/ DIREITO"},
                   {'_id': 'R', 'desc': "CESTA DE ACÕES NOMINATIVAS"},
                   {'_id': 'REC', 'desc': "RECIBO DE SUBSCRIÇÃO MISCELÂNEA"},
                   {'_id': 'REC PR', 'desc': "RECIBO DE SUBSCRIÇÃO EM PREF RESGATÁVEIS"},
                   {'_id': 'RON', 'desc': "CESTA DE ACÕES ORDINÁRIAS NOMINATIVAS"},
                   {'_id': 'TPR', 'desc': "TIT. PERPETUOS REMUN. VARIAV. ROYALTIES"},
                   {'_id': 'UNT', 'desc': "CERTIFICADO DE DEPÓSITO DE ACÕES - MISCELÂNEAS"},
                   {'_id': 'UNT 2', 'desc': "UNITS"},
                   {'_id': 'UP', 'desc': "PRECATÓRIO"},
                   {'_id': 'WRT', 'desc': "WARRANTS DE DEBÊNTURES"}]

    especi.insert_many(new_especis)

def create_market(path, stock_market):

    market = stock_market.Market

    files = glob.glob(path)

    for name in files:
        print(name)
        with open(name) as file:
            df = pandas.read_csv(file, low_memory=False)

        df = df.drop(df.index[-1])

        df['DATA'] = df['DATA'].astype(str)
        df['TIPREG'] = df['TIPREG'].astype(int)
        df['CODBDI'] = df['CODBDI'].astype(int)
        df['CODNEG'] = df['CODNEG'].astype(str)


        df['TPMERC'] = df['TPMERC'].astype(int)

        df['NOMRES'] = df['NOMRES'].astype(str)
        df['ESPECI'] = df['ESPECI'].astype(str)
        df['PRAZOT'] = df['PRAZOT'].astype(str)
        df['MODREF'] = df['MODREF'].astype(str)


        df['PREABE'] = (df['PREABE']/100).astype(float)
        df['PREMAX'] = (df['PREMAX']/100).astype(float)
        df['PREMIN'] = (df['PREMIN']/100).astype(float)
        df['PREMED'] = (df['PREMED']/100).astype(float)
        df['PREULT'] = (df['PREULT']/100).astype(float)
        df['PREOFC'] = (df['PREOFC']/100).astype(float)
        df['PREOFV'] = (df['PREOFV']/100).astype(float)

        df['TOTNEG'] = df['TOTNEG'].astype(int)
        df['QUATOT'] = df['QUATOT'].astype(np.int64)
        df['VOLTOT'] = df['VOLTOT'].astype(np.int64)
        df['PREEXE'] = (df['PREEXE']/100).astype(float)
        df['INDOPC'] = df['INDOPC'].astype(int)
        df['DATAEN'] = df['DATAEN'].astype(str)
        df['FATCOT'] = df['FATCOT'].astype(int)
        df['PTOEXE'] = df['PTOEXE'].astype(np.int64)
        df['CODISI'] = df['CODISI'].astype(str)
        df['DISMES'] = df['DISMES'].astype(int)


        dates = df['DATA'].unique()
        for date in dates:
            stocks_df = df[df['DATA'] == date]
            date = pandas.to_datetime(date)
            stocks_df = stocks_df.drop(['DATA'], axis=1)
            stocks_dict = stocks_df.to_dict(orient='records')
            new_market = {'_id': date, 'stocks': stocks_dict}
            market.insert_one(new_market)

def create_stocks_db():
    client = pymongo.MongoClient()

    stock_market = client.StockMarket

    data_path = '../../data/*.csv'
    create_market_type(stock_market)
    create_bdi(stock_market)
    create_indopc(stock_market)
    create_especi(stock_market)
    create_market(data_path, stock_market)


if __name__ == '__main__':
    create_stocks_db()
