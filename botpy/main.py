import os
from twilio.rest import Client
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import Levenshtein
from openai import OpenAI

client_openai = OpenAI(
    #defaults to os.environ.get("OPENAI_API_KEY")
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



@apbot.route("/sms",methods = ["get","post"])
def reply():
    valid_words = ["oi","ola","olá", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "sim", "não", "autoescola", "bom dia", "boa tarde", "boa noite", "valor", "gostaria", "quero fazer", "como fazer", "como fazer?", "horários", "horário", "como começar", "como começar?", "eu quero começar", "eu queria começar", "começar autoescola", "tirar carteira", "entrar autoescola", "eu quero começar a autoescolar", "quero tirar a carteira", "quero dirigir", "quero começar a dirigir", "quero entrar", "eu quero entrar na escola", "como entrar na autoescola?", "como tirar a carteira?", "eu gostaria de iniciar", "professores", "vocês fazem pra tirar a carteira A ou B?", "carteira A", "carteira B", "qual o valor", "atendente", "atendimento", "professor", "quero falar com um atendente", "eu quero falar com um atendente", "quero falar com o atendente", "quero falar com a atendente", "quero atendimento", "solicito atendimento", "eu preciso falar com um atendente", "eu preciso falar com uma atendente", "eu preciso falar com um professor", "eu quero falar com um professor", "como eu falo com um atendente?", "como eu falo com um responsável?", "como eu falo com uma atendente?", "como eu falo com o atendente?", "quero ser atendido", "quero falar com alguem", "preciso falar com um atendente", "eu quero desconto", "como negociar a carteira de motorista", "eu quero tirar a carteira A e B", "preciso tirar a habilitação", "preciso de habilitação", "preciso habilitar", "preciso de habilitação", "habilitação", "setor de habilitação", "setor finaceiro", "carro", "moto", "A", "B", "A e B"]
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

    print("Autoescola Ari")

    msg = chat_completion.choices[0].message.content

    sendMessage(msg, sen_num,me_num)
    
    
   
    if(msgt == "1" or msgt == "2" or msgt == "3" or msgt == "4" or msgt == "5" or msgt == "6" or msgt == "7" or msgt == "8"):
             secondReply(msgt)
    elif(msgt == "sim" or msgt == "Sim" or msgt == "s" or msgt == "ss" or msgt == "SIm" or msgt == "SIM" or msgt == "sIM" or msgt == "siM"):
            ajuda()
    
    elif(msgt == "não" or msgt == "Não" or msgt == "nao" or msgt == "Nao" or msgt == "n" or msgt == "nn"):
             msg = "Muito obrigado por estar conosco!!"
             sendMessage(msg, sen_num, me_num)
             msg = "Se precisar de algo a mais so mandar um olá!"
             sendMessage(msg, sen_num, me_num)
    elif(msgt == "experimental" or msgt == "test" or msgt == "Aula experimental" or msgt == "aula grátis" or msgt == "experimental grátis" or msgt == "teste grátis" or msgt == "aula de graça" or msgt == "Drive" or msgt == "teste experimental" or msgt == "aula teste" or msgt == "experimentar"):
          especifico(1)
          loop()
    elif(msgt == "Carteira tipo A" or msgt == "Carteira tipo B" or msgt == "A" or msgt == "B" or msgt == "Carteira tipo A e B" or msgt == "A e B" or msgt == "Quero tirar a carteira de carro" or msgt == "quero tirar a carteira de moto" or msgt == "carro" or msgt == "moto" or msgt == "Como tirar a carteira" or msgt == "como dirigir" or msgt == "Como entrar?" or msgt == "como começar?" or msgt == " Como iniciar" or msgt == "como começar" or msgt == "Como começo?"):
           especifico(2)
           loop()
    elif(msgt == "Seguro" or msgt == "seguro" or msgt =="vocês fazem seguro?" or msgt == "quero seguro" or msgt == "eu quero um seguro" or msgt == "onde arranjo um seguro?" or msgt == "preciso de seguro"):
          especifico(4)
          loop()
    elif(msgt == "Falar com atendente" or msgt == "Atendente" or msgt == "atendente" or msgt == "Vendedor" or msgt == "vendedor" or msgt == "Falar com vendedor" or msgt == "atendimento" or msgt == "Atendimento" or msgt == "Quero atendimento" or msgt == "quero atendimento" or msgt == "Quero falar com o atendente" or msgt == "quero falar com o atendente" or msgt == "Quero falar com a atendente" or msgt == "quero falar com a atendente"  or msgt == "Quero falar com o vendedor" or msgt == "quero falar com o vendedor" or msgt == "Quero falar com a vendedora" or msgt == "quero falar com a vendedora" or msgt == "Quero atendimento" or msgt == "quero atendimento" or msgt == "quero ser atendido" or msgt == "Quero ser atendido" or msgt == "atendente" or msgt == "atendimento" or msgt == "vendedor" or msgt == "quero falar com um atedente" or msgt == "eu quero falar com um atendente" or msgt == "quero falar com o atendente" or msgt == "quero falar com a atendente" or msgt =="quero atendimento" or msgt == "solicito atendimento" or msgt == "eu preciso falar com um atendente" or msgt == "eu preciso falar com uma atendente" or msgt == "eu preciso falar com um vendedor" or msgt == "eu quero falar com um vendedor" or msgt == "como eu falo com um atendente?" or msgt == "como eu falo com um vendedor?" or msgt == "como eu falo com uma atendente?" or msgt == "como eu falo com o atendente?" or msgt == "quero ser atendido" or msgt =="quero falar com alguem" or msgt == "preciso falar com um atendente" or msgt == "quero falar com um atendente"):
         especifico(5)
         loop()
    elif(msgt == "OI" or msgt == "Oi" or msgt == "oi" or msgt == "Olá" or msgt == "olá" or msgt == "Ola" or msgt == "ola" or msgt == "fala" or msgt == "opa" or msgt == "Fala" or msgt == "Opa" or msgt == "Bom dia" or msgt == "bom dia" or msgt == "bomdia" or msgt == "Boa tarde" or msgt == "boa tarde" or msgt == "boatarde" or msgt == "Bom tarde" or msgt == "bom tarde" or msgt == "bomtarde" or msgt == "Boa noite" or msgt == "boa noite" or msgt == "boanoite" or msgt == "Bom noite" or msgt == "bom noite" or msgt == "bomnoite" or msgt == "Boa dia" or msgt == "boa dia" or msgt == "boadia" or msgt == "Boadia" or msgt == "Bomtarde" or msgt == "Bomnoite" or msgt == "cuida" or msgt == "chama" or msgt == "agiliza" or msgt == "chama na alta" or msgt == "chama na alta garel" or msgt == "chama na alta garelzinho" or msgt == "garelzinho do mel"):
             intro()
             ajuda()
    
    elif(msgt == "setor adminstrativo" or msgt == "administrativo"):
          msg = "Segue o contato do setor administrativo:\n +55 85 99957-7909"
          sendMessage(msg,sen_num,me_num)
          loop()
    elif(msgt == "setor rh" or msgt == "rh" or msgt == "setor do rh"):
          msg = "Segue o contato do setor RH:\+55 85 99957-7909"
          sendMessage(msg,sen_num,me_num)
          loop()
    elif(msgt == "vendedor" or msgt == "vendedores" or msgt == "setor de vendedores" or msgt == "setor dos vendedores" or msgt == "setor de vendedor" or msgt == "setor dos vendedor" or msgt == "setor do vendedor" or msgt == "setor de vendas" or msgt == "setor de venda"):
           msg = "Segue o contato do setor de vendas:\+55 85 99957-7909"
           sendMessage(msg,sen_num,me_num)
           loop()
    elif(msgt == "4.1" or msgt == "41" or msgt == "4,1" or msgt == "4 1"):
          msg = "Nós temos o limite de três carros por dia venha nos vistitar e fazer o seu test drive"
          sendMessage(msg,sen_num,me_num)
          loop()
    elif(msgt == "4.2" or msgt == "42" or msgt == "4,2" or msgt == "4 2"):
          msg = "O nosso tempo limite é de 45 minutos por cada test drive"
          sendMessage(msg, sen_num, me_num)
          loop()
    elif(msgt == "5.1" or msgt == "51" or msgt == "5,1" or msgt == "5 1"):
          msg = "Nos recomendamos o seguro ..."
          sendMessage(msg, sen_num,me_num)
          loop()
    elif(msgt == "5.2" or msgt == "52" or msgt == "5,2" or msgt == "5 2"):
          msg = "Nós estamos focado completamente na venda de carros mas indicamos o seguro ... de extrema confiança!!"
          sendMessage(msg, sen_num,me_num)
          loop()
    
    else:
         sugestion = find_closest_match(msgt, valid_words) 
         msg = 'Desculpa nao entendi a sua duvida, voce quis dizer "'+sugestion+'"?\n(se a palavra for essa, redigite-a)' 
         sendMessage(msg, sen_num, me_num)         

def secondReply(msgtext):
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    
    if(msgtext == "1"):
        msg = "Possuímos 4 unidades: Av. Desembargador Gonzaga, 752  – Cidade dos Funcionários, Fortaleza – CE, 60823-000 ; R. Paulo Roberto Pinheiro, 70 – Guararapes, Fortaleza – CE, 60810-100 ; Av. Bernardo Manuel, 9380 – Itaperi, Fortaleza – CE, 60410-234 ; Av. Prof. Fco. Oscar Rodrigues, 379 – Jereissati II, Maracanaú – CE, 61901-090  "
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "2"):
        msg = "Me diga qual a sua preferencia:\n - tipo A \n - tipo B\n - A e B"
        sendMessage(msg, sen_num, me_num)
        
    elif(msgtext == "3"):
        msg = "Para mais informações sobre a Autoescola, acesse nosso site: autoescolaari.com/"
        sendMessage(msg, sen_num, me_num) 
        loop()
    elif(msgtext == "4"):
        msg = "Para acessar o nosso site basta clicar no link a seguir:\n autoescolaari.com/"
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "5"):
        msg = "Certo. logo um atentende irá vir lhe ajudar."
        sendMessage(msg, sen_num, me_num)
        msg = "Precisa de mais alguma ajuda?"
        loop()
    elif(msgtext == "6"):
        msg = "Para agendar uma aula prática basta falar com um consultor e marcar o seu horario!"
        sendMessage(msg, sen_num, me_num)
        msg = "Precisa de mais alguma ajuda?"
    elif(msgtext == "7"):
        msg = "Me diga qual o setor de sua preferencia:\n - Administrativo \n - Professores"
        sendMessage(msg, sen_num, me_num)
        loop()
        

def ajuda():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    
    msg = " 1 - Onde fica localizado? \n 2 - Solicitar Habilitação \n 3 - Autoescola \n 4 - Visitar site \n 5 - Atendimento?\n 6 - Quero agendar uma aula prática \n 7 - Falar com um consultar"
    sendMessage(msg, sen_num, me_num)

def intro():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = 'Olá, tudo bem?'
    sendMessage(msg, sen_num, me_num)
    msg = "Prazer eu sou o Ari e estou aqui pra ajudar"
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
          msg = "A nossas aulas práticas são diárias e você pode solicitá-las com um atendente."
          sendMessage(msg, sen_num, me_num)
         
     elif(num == 5):
          msg = "Me diga com qual setor você deseja falar:\n - Administrativo\n - RH\n - Professores\n"
          sendMessage(msg, sen_num, me_num)
          msg = "(digite uma das opções acima)"
          sendMessage(msg, sen_num, me_num)

def find_closest_match(user_input, valid_words):
   
    closest_match = min(valid_words, key=lambda word: Levenshtein.distance(user_input, word))
    return closest_match

    sendMessage(msg, sen_num, me_num)
if(__name__=="__main__"):
    port = int(os.environ.get("PORT", 5000))
    apbot.run(host='0.0.0.0', port=port)