import os
from twilio.rest import Client
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import Levenshtein
from openai import OpenAI

client_openai = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

apbot = Flask(__name__)
def sendMessage(text : str, to: str, fromwwp: str):

    account_sid = "AC062b820202641a14ea00db8c5e94efff"
    auth_token = "1bb965f6da5c9aedae7eb64915a29c29"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_ ='whatsapp:+14155238886',
        body=text,
        to=to
        )
    print(message.sid)

    



@apbot.route("/test",methods = ["get","post"])
def test_completion():
    print("Eu vim aqui")
    msgt = "Como faco para usar meu assistente no Openai com esse codigo?"
    msgt = request.form.get("Body")
    chat_completion = client_openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msgt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    print("Chatgpt respondeu")

    msg = chat_completion.choices[0].message.content
    print(msg)
    print(chat_completion)

    return msg

    # return msg

@apbot.route("/sms",methods = ["get","post"])
def reply():
    valid_words = ["oi","ola","olá", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "sim", "não", "test drive", "bom dia", "boa tarde", "boa noite", "financeamento", "financiar", "quero financiar", "como financiar", "como financiar?", "parcelar", "quero parcelar", "como parcelar", "como parcelar?", "eu quero financiar", "eu quero parcelar", "juros", "negociar", "negociação", "eu quero negociar os juros", "quero negociar os juros", "quero negociar", "quero negociar juros", "quero reduzir os juros", "eu quero reduzir os juros", "como reduzir os juros?", "como diminuir os juros?", "eu quero diminuir os juros", "seguro", "vocês fazem seguro?", "quero seguro", "eu quero um seguro", "onde arranjo um seguro?", "atendente", "atendimento", "vendedor", "quero falar com um atendente", "eu quero falar com um atendente", "quero falar com o atendente", "quero falar com a atendente", "quero atendimento", "solicito atendimento", "eu preciso falar com um atendente", "eu preciso falar com uma atendente", "eu preciso falar com um vendedor", "eu quero falar com um vendedor", "como eu falo com um atendente?", "como eu falo com um vendedor?", "como eu falo com uma atendente?", "como eu falo com o atendente?", "quero ser atendido", "quero falar com alguem", "preciso falar com um atendente", "eu quero negociar as parcelas", "como negociar o financeamento", "eu quero negociar o financeamento", "preciso negociar as parcelas", "preciso de seguro", "preciso financiar", "preciso de financeamento", "setor de venda", "setor administrativo", "setor de vendas", "Hatch", "Sedã", "SUV", "Caminhonte", "Picape"]
    msgt = request.form.get("Body")
    msgt.lower()
    sen_num= request.form.get("From")
    me_num = request.form.get("To")
    print(msgt)
    print(sen_num)


    chat_completion = client_openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msgt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    print("Chatgpt respondeu")

    msg = chat_completion.choices[0].message.content

    sendMessage(msg, sen_num,me_num)
    
    
   
    # if(msgt == "1" or msgt == "2" or msgt == "3" or msgt == "4" or msgt == "5" or msgt == "6" or msgt == "7" or msgt == "8"):
    #         secondReply(msgt)
    # elif(msgt == "sim" or msgt == "Sim" or msgt == "s" or msgt == "ss" or msgt == "SIm" or msgt == "SIM" or msgt == "sIM" or msgt == "siM"):
    #        ajuda()
    
    # elif(msgt == "não" or msgt == "Não" or msgt == "nao" or msgt == "Nao" or msgt == "n" or msgt == "nn"):
    #         msg = "Muito obrigado por estar conosco!!"
    #         sendMessage(msg, sen_num, me_num)
    #         msg = "Se precisar de algo a mais so mandar um olá!"
    #         sendMessage(msg, sen_num, me_num)
    # elif(msgt == "Test" or msgt == "test" or msgt == "Test Drive" or msgt == "Test drive" or msgt == "test Drive" or msgt == "test drive" or msgt == "drive" or msgt == "Drive" or msgt == "testdrive" or msgt == "Testdrive" or msgt == "testDrive"):
    #      especifico(1)
    #      loop()
    # elif(msgt == "Financiamento" or msgt == "financeamento" or msgt == "parcelas" or msgt == "Parcelas" or msgt == "Parcelamento" or msgt == "parcelamento" or msgt == "Quero parcelar" or msgt == "quero parcelar" or msgt == "quero financiar" or msgt == "Quero financiar" or msgt == "Como parcelar" or msgt == "como parcelar" or msgt == "Como parcelar?" or msgt == "como parcelar?" or msgt == " Como financiar" or msgt == "como financiar" or msgt == "Como financiar?" or msgt == "como financiar?" or msgt == "financiar" or msgt == "Financiar" or msgt == "parcelar" or msgt == "Parcelar" or msgt == "eu quero financiar" or msgt == "eu quero parcelar" or msgt == "preciso financear"or msgt == "eu quero negociar as parcelas" or msgt == "eu quero negociar o financeamento" or msgt == "como negociar o financeamento"  or msgt == "preciso negociar as parcelas" or msgt == "preciso financiar" or msgt == "eu preciso parcelar" or msgt == "preciso de financiamento"):
    #       especifico(2)
    #       loop()
    # elif(msgt == "juros" or msgt == "Juros" or msgt == "Negociação" or msgt == "Negociacão" or msgt == "negociação" or msgt == "negociacão" or msgt == "negociaçao" or msgt == "Negociaçao" or msgt == "Quero negociar" or msgt == "quero negociar" or msgt == "quero reduzir os juros" or msgt == "Quero reduzir os juros" or msgt == "Quero reduzir" or msgt == "Reduzir" or msgt == "reduzir" or msgt == "diminuir" or msgt == "Diminuir" or msgt == "Negociar" or msgt == "negociar" or msgt == "Quero diminuir os juros" or msgt == "quero diminuir os juros" or msgt == "Quero diminuir" or msgt == "quero diminuir"or msgt == "como diminuir os juros?" or msgt == "quero negociar juros" or msgt == "quero reduzir os juros"or msgt == "eu quero reduzir os juros" or msgt == "como reduzir os juros?" or msgt == "como diminuir os juros?" or msgt == "eu quero diminuir os juros" or msgt == "eu quero negociar os juros" or msgt == "quero negociar os juros" or msgt == "quero saber sobre os juros" or msgt == "quero me informar sobre os juros" or msgt == "preciso de informação sobre os juros" or msgt == "preciso de informação dos juros" or msgt == "quero informações sobre juros" or msgt == "como funciona os juros?" or msgt == "como funciona os juros"):
    #      especifico(3)
    #      loop()
    # elif(msgt == "Seguro" or msgt == "seguro" or msgt =="vocês fazem seguro?" or msgt == "quero seguro" or msgt == "eu quero um seguro" or msgt == "onde arranjo um seguro?" or msgt == "preciso de seguro"):
    #      especifico(4)
    #      loop()
    # elif(msgt == "Falar com atendente" or msgt == "Atendente" or msgt == "atendente" or msgt == "Vendedor" or msgt == "vendedor" or msgt == "Falar com vendedor" or msgt == "atendimento" or msgt == "Atendimento" or msgt == "Quero atendimento" or msgt == "quero atendimento" or msgt == "Quero falar com o atendente" or msgt == "quero falar com o atendente" or msgt == "Quero falar com a atendente" or msgt == "quero falar com a atendente"  or msgt == "Quero falar com o vendedor" or msgt == "quero falar com o vendedor" or msgt == "Quero falar com a vendedora" or msgt == "quero falar com a vendedora" or msgt == "Quero atendimento" or msgt == "quero atendimento" or msgt == "quero ser atendido" or msgt == "Quero ser atendido" or msgt == "atendente" or msgt == "atendimento" or msgt == "vendedor" or msgt == "quero falar com um atedente" or msgt == "eu quero falar com um atendente" or msgt == "quero falar com o atendente" or msgt == "quero falar com a atendente" or msgt =="quero atendimento" or msgt == "solicito atendimento" or msgt == "eu preciso falar com um atendente" or msgt == "eu preciso falar com uma atendente" or msgt == "eu preciso falar com um vendedor" or msgt == "eu quero falar com um vendedor" or msgt == "como eu falo com um atendente?" or msgt == "como eu falo com um vendedor?" or msgt == "como eu falo com uma atendente?" or msgt == "como eu falo com o atendente?" or msgt == "quero ser atendido" or msgt =="quero falar com alguem" or msgt == "preciso falar com um atendente" or msgt == "quero falar com um atendente"):
    #     especifico(5)
    #     loop()
    # elif(msgt == "OI" or msgt == "Oi" or msgt == "oi" or msgt == "Olá" or msgt == "olá" or msgt == "Ola" or msgt == "ola" or msgt == "fala" or msgt == "opa" or msgt == "Fala" or msgt == "Opa" or msgt == "Bom dia" or msgt == "bom dia" or msgt == "bomdia" or msgt == "Boa tarde" or msgt == "boa tarde" or msgt == "boatarde" or msgt == "Bom tarde" or msgt == "bom tarde" or msgt == "bomtarde" or msgt == "Boa noite" or msgt == "boa noite" or msgt == "boanoite" or msgt == "Bom noite" or msgt == "bom noite" or msgt == "bomnoite" or msgt == "Boa dia" or msgt == "boa dia" or msgt == "boadia" or msgt == "Boadia" or msgt == "Bomtarde" or msgt == "Bomnoite" or msgt == "cuida" or msgt == "chama" or msgt == "agiliza" or msgt == "chama na alta" or msgt == "chama na alta garel" or msgt == "chama na alta garelzinho" or msgt == "garelzinho do mel"):
    #         intro()
    #         ajuda()
    
    # elif(msgt == "setor adminstrativo" or msgt == "administrativo"):
    #      msg = "Segue o contato do setor administrativo:\n(85)999999999999"
    #      sendMessage(msg,sen_num,me_num)
    #      loop()
    # elif(msgt == "setor rh" or msgt == "rh" or msgt == "setor do rh"):
    #      msg = "Segue o contato do setor RH:\n(85)888888888888"
    #      sendMessage(msg,sen_num,me_num)
    #      loop()
    # elif(msgt == "vendedor" or msgt == "vendedores" or msgt == "setor de vendedores" or msgt == "setor dos vendedores" or msgt == "setor de vendedor" or msgt == "setor dos vendedor" or msgt == "setor do vendedor" or msgt == "setor de vendas" or msgt == "setor de venda"):
    #       msg = "Segue o contato do setor de vendas:\n(85)77777777777"
    #       sendMessage(msg,sen_num,me_num)
    #       loop()
    # elif(msgt == "4.1" or msgt == "41" or msgt == "4,1" or msgt == "4 1"):
    #      msg = "Nós temos o limite de três carros por dia venha nos vistitar e fazer o seu test drive"
    #      sendMessage(msg,sen_num,me_num)
    #      loop()
    # elif(msgt == "4.2" or msgt == "42" or msgt == "4,2" or msgt == "4 2"):
    #      msg = "O nosso tempo limite é de 45 minutos por cada test drive"
    #      sendMessage(msg, sen_num, me_num)
    #      loop()
    # elif(msgt == "5.1" or msgt == "51" or msgt == "5,1" or msgt == "5 1"):
    #      msg = "Nos recomendamos o seguro ..."
    #      sendMessage(msg, sen_num,me_num)
    #      loop()
    # elif(msgt == "5.2" or msgt == "52" or msgt == "5,2" or msgt == "5 2"):
    #      msg = "Nós estamos focado completamente na venda de carros mas indicamos o seguro ... de extrema confiança!!"
    #      sendMessage(msg, sen_num,me_num)
    #      loop()
    # elif(msgt == "Hatch" or msgt == "hatch" or msgt == "Hatchs" or msgt == "hatchs"):
    #     msg = "Confira a listagem a seguir com todos os nossos Hatchs!!\n"
    #     sendMessage(msg, sen_num,me_num)
    #     hatchs()
    #     loop()
    # elif(msgt == "Sedã" or msgt == "sedã" or msgt == "seda" or msgt == "Seda" or msgt == "Sedan" or msgt == "sedan"):
    #     msg = "Confira a listagem a seguir com todos os nossos Sedãs!!\n"
    #     sendMessage(msg, sen_num,me_num)
    #     seda()
    #     loop()
    # elif(msgt == "Suv" or msgt == "SUv" or msgt == "SUV" or msgt == "suv" or msgt == "sUv" or msgt == "suV" or msgt == "sUV" or msgt == "Suvs" or msgt == "SUVs" or msgt == "SUVS" or msgt == "suvs"):
    #     msg = "Confira a listagem a seguir com todos os nossos SUVs!!\n"
    #     sendMessage(msg, sen_num,me_num)
    #     suv()
    #     loop()
    # elif(msgt == "picape" or msgt == "Picape" or msgt == "Caminhonete" or msgt == "caminhonete"):
    #     msg = "Confira a listagem a seguir com todos as nossas caminhonetes!!\n"
    #     sendMessage(msg, sen_num,me_num)
    #     picape()
    #     loop()
    
    # else:
    #     sugestion = find_closest_match(msgt, valid_words) 
    #     msg = 'Desculpa nao entendi a sua duvida, voce quis dizer "'+sugestion+'"?\n(se a palavra for essa, redigite-a)' 
    #     sendMessage(msg, sen_num, me_num)         

def secondReply(msgtext):
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    
    if(msgtext == "1"):
        msg = "Nossa loja fica localizada na R. Eliseu Uchôa Beco, 63 - Guararapes, Fortaleza - CE, venha nos visitar!!"
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "2"):
        msg = "Me diga qual a sua preferencia:\n - Hatch \n - Sedan\n - SUV\n - Caminhonete"
        sendMessage(msg, sen_num, me_num)
        
    elif(msgtext == "3"):
        msg = "Para simular o seu financeamnto entre no nosso site www.urbanmotorsbr.com.br"
        sendMessage(msg, sen_num, me_num) 
        loop()
    elif(msgtext == "4"):
        msg = "Para acessar o nosso site basta clicar no link a seguir:\n www.urbanmotorsbr.com.br"
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "5"):
        msg = "Infelizmente ainda não oferecemos o serviço de seguro, mas podemos indicar parceiros confiaveis"
        sendMessage(msg, sen_num, me_num)
        msg = "Precisa de mais alguma ajuda?\n 5.1 - Porque não fazem seguro?"
        loop()
    elif(msgtext == "6"):
        msg = "Para agendar um test drive basta falar com um consultor e marcar o seu horario!"
        sendMessage(msg, sen_num, me_num)
        msg = "Precisa de mais alguma ajuda? \n 6.1 - Possui limite de tempo? \n 6.2 - Pode testar mais de um carro por dia?"
    elif(msgtext == "7"):
        msg = "Me diga qual o setor de sua preferencia:\n - Administrativo \n - Vendedores"
        sendMessage(msg, sen_num, me_num)
        loop()
        
    
msg = "Me diga qual a sua preferencia:\n - Hatch \n - Sedan\n - SUV\n - Caminhonete"

def ajuda():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    
    msg = " 1 - Onde fica localizado? \n 2 - Quero ver o estoque \n 3 - Simular financeamento \n 4 - Visitar site \n 5 - Vocês oferecem seguro?\n 6 - Quero agendar um test drive \n 7 - Falar com um consultar"
    sendMessage(msg, sen_num, me_num)

def intro():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = 'Olá, tudo bem?'
    sendMessage(msg, sen_num, me_num)
    msg = "Prazer eu sou o urbinho e estou aqui pra ajudar"
    msg = 'Qual serviço você deseja?'
    sendMessage(msg, sen_num, me_num)
    

def loop():
    
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = "Você precisa de mais alguma ajuda?\n (digite 'sim' ou 'não')"
    sendMessage(msg, sen_num, me_num)
    
def especifico(num):
     sen_num = request.form.get("From")
     me_num = request.form.get("To")

     if(num == 1):
          msg = "Os nossos testes drives possuem a duração de 45 minutos e você pode fazer ate dois test drives por dia!!"
          sendMessage(msg, sen_num, me_num)

     elif(num == 2):
          msg = "Sobre financeamento, primeiramente o banco tem que aprovar o seu finaceamento e depois negociamos a quantidade de parcelas que será mais agradavél para você"
          sendMessage(msg, sen_num, me_num)

     elif(num == 3):
          msg = "Infelizmente não conseguimos negociar sobre os juros do parcelamento, apenas informa-lo que quanto menor a quantidade de parcelas menores os juros"
          sendMessage(msg, sen_num, me_num)

     elif(num == 4):
          msg = "Nós não oferecemos serviços de seguro infelizmente"
          sendMessage(msg, sen_num, me_num)
         
     elif(num == 5):
          msg = "Me diga com qual setor você deseja falar:\n - Administrativo\n - RH\n - Vendedores\n"
          sendMessage(msg, sen_num, me_num)
          msg = "(digite uma das opções acima)"
          sendMessage(msg, sen_num, me_num)

def find_closest_match(user_input, valid_words):
   
    closest_match = min(valid_words, key=lambda word: Levenshtein.distance(user_input, word))
    return closest_match

def simuOrca(valor, parcelas):
     sen_num = request.form.get("From")
     me_num = request.form.get("To")
     if(valor >= 0 and valor<=30000):
          if(parcelas > 15):
            msg = "Verificamos o o valor enviado e não conseguimos fazer o numero de parcelas pedido parcelamos em até 15 vezes"
            sendMessage(msg, sen_num, me_num)

          else:
            msg = "Verificamos o o valor enviado e conseguimos parcelar em" + parcelas+ "vezes!"
            sendMessage(msg, sen_num, me_num)
     if(valor > 30000 and valor <= 75000 ):
          if(parcelas > 30):
            msg = "Verificamos o o valor enviado e não conseguimos fazer o numero de parcelas pedido parcelamos em até 30 vezes"
            sendMessage(msg, sen_num, me_num)

          else:
            msg = "Verificamos o o valor enviado e conseguimos parcelar em" + parcelas+ "vezes!"
            sendMessage(msg, sen_num, me_num)
     if(valor > 75000 and valor <= 125000 ):
          if(parcelas > 45):
            msg = "Verificamos o o valor enviado e não conseguimos fazer o numero de parcelas pedido parcelamos em até 45 vezes"
            sendMessage(msg, sen_num, me_num)

          else:
            msg = "Verificamos o o valor enviado e conseguimos parcelar em" + parcelas+ "vezes!"
            sendMessage(msg, sen_num, me_num)

     if(valor > 125000 and valor <= 200000 ):
          if(parcelas > 60):
            msg = "Verificamos o o valor enviado e não conseguimos fazer o numero de parcelas pedido parcelamos em até 60 vezes"
            sendMessage(msg, sen_num, me_num)

          else:
            msg = "Verificamos o o valor enviado e conseguimos parcelar em" + parcelas+ "vezes!"
            sendMessage(msg, sen_num, me_num)


def hatchs():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")
    msg = """FIAT: 

MOBI 1.0 LIKE  22/23 Cinza  0 KM  59.900,00 R$
MOBI 1.0 LIKE  22/23 Vermelho 13673 KM
PALIO ATTRACTIVE 1.0 8V (FLEX)  16/16 Branco 84385 KM

CITRÕEN:

C4 CACTUS 1.6 FEEL (AUT)  22/22 Vermelho 48772 KM N 82.900,00 R$

CHEVROLET:

ONIX 1.0 LS SPE/4 15/15 Preto 95826 KM 44.900,00 R$
ONIX 1.0TAT LT1 FLEX 4P  20/21 Prata 42516 KM 86.000,00 R$

HONDA:

FIT 1.5 LX CVT (FLEX) 18/19 Branco 20147 KM 85.900,00 R$
FIT DX 1.4 (FLEX)  11/12 Prata 118000 KM S 43.900,00 R$

HYUNDAI:

HB20 1.0 VISION  22/22 Branco 0 KM 65.900,00 R$
HB20 1.0 VISION  22/22 Branco 0 KM 65.900,00 R$

NISSAN:

 MARCH 1.0 12V SV (FLEX)  14/15 Prata 82445 KM 42.900,00 R$

RENAULT:

SANDERO AUTHENTIQUE 1.0 16V  19/20 Prata 0 KM 50.900,00 R$

VOLKSWAGEN:

GOL 1.0 MPI (FLEX)  22/23 Cinza 28651 KM 59.900,00 R$"""
    sendMessage(msg, sen_num, me_num)

def seda():
     sen_num = request.form.get("From")
     me_num = request.form.get("To")
     msg = """FIAT:

CRONOS 1.3 DRIVE (FLEX)  22/22 Cinza 0 KM 74.900,00 R$

CHEVROLET:

PRISMA 1.4 LTZ SPE/4  18/19 Branco 60368 KM 69.900,00 R$

HONDA:

CIVIC EXR 2.0 I-VTEC (AUT) (FLEX) 15/16 Branco 48200 KM 79.900,00 R$

TOYOTA:

COROLLA 2.0 XEI CVT 18/19 Branco 46000 KM 124.900,00 R$

VOLKSWAGEN:

2x VOYAGE 1.0 MPI (FLEX) 22/23 Branco 0 KM 68.900,00 R$"""
     sendMessage(msg, sen_num, me_num)

def suv():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")
    msg = """CAOA CHERY:

TIGGO 8 1.6 TGDI GASOLINA TXS D 21/22 Branco 44000 KM 159.900,00 R$
TIGGO 8 1.6 TGDI GASOLINA TXS D 21/22 Branco 36555 KM 159.900,00 R$

CITRÕEN:

C4 CACTUS 1.6 FEEL (AUT)  22/22 Vermelho 48772 KM N 82.900,00 R$

HYUNDAI:

CRETA 1.6 ACTION (AUT) 21/22 Branco 0 KM 110.900,00 R$

JAGUAR:

 E-PACE 2.0 P250 4WD 18/18 Branco 70610 KM 259.900,00 R$

JEEP:

COMPASS 2.0 LONGITUDE (AUT) 18/18 Branco 52255 KM 119.900,00 R$
COMPASS 2.0 SPORT U 20/21 Prata 26834 KM 117.000,00 R$
COMPASS S 2.0 DIESEL LIMITED 4 22/22 Preto 0 KM 220.900,00 R$
RENEGADE 1.8 LONGITUDE (AUT) 20/21 Branco 38127 KM 88.000,00 R$
RENEGADE 1.8 LONGITUDE (AUT) 16/16 Preto 68660 KM 65.900,00 R$
RENEGADE SPORT 2.0 MULTIJET T 16/16 Prata 86000 KM 82.900,00 R$
RENEGADE SPORT 2.0 TDI 4WD 16/17 Branco 0 KM 98.900,00 R$

LAND ROVER:

DISCOVERY SPORT 2.0 P250 SE FL 19/19 Cinza 36907 KM 179.900,00 R$
RANGE ROVER SPORT HSE 3.0 V6 19/20 Preto 54039 KM 479.900,00 R$

MITSUBISHI: 

PAJERO SPORT 3.0 HPE 4X4 V6 24 08/09 Prata 111048 KM 59.900,00 R$

NISSAN:

KICKS 1.6 ADVANCE CVT 22/22 Vermelho 0 KM 109.900,00 R$
KICKS 1.6 EXCLUSIVE CVT 22/22 Preto 0 KM 114.900,00 R$
KICKS 1.6 SENSE 22/22 Branco 45786 KM 82.900,00 R$
KICKS 1.6 SV CVT (FLEX) 19/20 Branco 73000 KM 94.900,00 R$

RENAULT:

CAPTUR 1.3 TCE ICONIC CVT 21/22 Prata 0 KM 109.900,00 R$

SSANGYONG:

KYRON 2.0 XDI 200KY 4X4 16V TUR 10/11 Branco 175780 KM 50.900,00 R$

VOLKSWAGEN:

TIGUAN ALLSPACE 1.4 250 TSI CO 18/18 Preto 0 KM 145.900,00 R$"""
    sendMessage(msg, sen_num, me_num)

def picape():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")
    msg = """FIAT:

TORO 1.3 TURBO 270 FLEX ENDUR 21/22 Prata 0 KM 119.900,00 R$
TORO 2.0 TDI ENDURANCE 4WD (A 22/22 Branco 42258 KM 145.900,00 R$
TORO FREEDOM 1.8 AT6 4X2 (FLEX) 17/18 Prata 79210 KM 95.900,00 R$
STRADA WORKING 1.4 (FLEX) 15/15 Branco 95507 KM 65.900,00 R$

CHEVROLET:

S10 2.8 LT 4X4 CD 16V TURBO DIE 18/19 Branco 86318 KM 169.900,00 R$

MITSUBISHI:

L200 TRITON SPORT 2.4 DID-H GL 22/23 Branco 0 KM 185.900,00 R$

NISSAN:

FRONTIER ATTACK 4X4 (AUT) 18/19 Branco 48750 KM 163.900,00 R$
FRONTIER AX 4X4 3.2 22/23 Branco 48181 KM 174.900,00 R$

TOYOTA:

HILUX (CABINE DUPLA) 3.0 TDI 4X4 12/12 Preto 125.900,00 R$
HILUX 2.8 D-4D TURBO DIESEL CD 19/20 Branco 205.900,00 R$
HILUX 2.8 D-4D TURBO DIESEL CD U 22/22 Prata 250.900,00 R$

VOLKSWAGEN:

SAVEIRO 1.6 MI CLI CS 8V GASOLI 97/97 41900 KM 35.900,00 R$"""
    sendMessage(msg, sen_num, me_num)
if(__name__=="__main__"):
    port = int(os.environ.get("PORT", 5000))
    apbot.run(host='0.0.0.0', port=port)