import discord
import json
from discord import Option, slash_command
from discord.ui import Select,View
from discord.ext.commands import has_permissions,MissingPermissions

with open("configs.json","r") as f:
	data = json.load(f)
	TOKEN = data["token"]

with open("servers.json","r") as f:
	data = json.load(f)
	servidor_1 = data["servidor-1"]
	servidor_2 = data["servidor-2"]

bot = discord.Bot(debug_guilds=[servidor_1,servidor_2])


@bot.event
async def on_ready():
    print(f"{bot.user} está on-line!")


@has_permissions(manage_messages=True)
@bot.slash_command(name="calcular",description="calcula  os lançamentos do RP")
async def calcular(
	ctx,
	peso: Option(int,description="Peso do foguete"),
	reutilizavel: Option(str,description="Se o foguete é reutilizavel ou não"),
	destino: Option(int,description="Destino do foguete")

	):

	title = "Recompensa do usuario"
	description = "Bot em desenvolvimento"
	field_1 = "Valor a pagar:"
	field_2 = "Bot Alpha 0.0.2"

	if reutilizavel == "sim":
		n1 = (peso*20)
		n2 = (peso*destino)
		valors = abs((n1-n2))

		embed1 = discord.Embed(title=title,description=description,color= 0x00bfff)
		embed1.add_field(name=field_1,value=f"{valors}",inline=False)
		embed1.set_footer(text=field_2)

		await ctx.respond(embed=embed1)

	if reutilizavel == "não":
		n3 = (peso*60)
		n4 = (peso*destino) 
		valorn = abs((n3-n4))

		embed2 = discord.Embed(title=title,description=description,color= 0x00bfff)
		embed2.add_field(name=field_1,value=f"{valorn}",inline=False)
		embed2.set_footer(text=field_2)

		await ctx.respond(embed=embed2)

@calcular.error
async def calcular_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond(content="Você não possui a permissão de Gerenciar mensagens para executar esse comando!",ephemeral=True)

@bot.slash_command(name="ping",description="mostra a latencia do bot")
async def ping(ctx):
	await ctx.respond(f"Pong! meu ping é: \n{round (bot.latency*1000)}")


@bot.slash_command(name="info",description="informações sobre o Bot")
async def info(ctx):

	embed_info = discord.Embed(
		title="Informações",
		description="Informações sobre o bot",
		color= 0x00bfff
	)
	embed_info.add_field(name="Versão do bot:",value="O bot se encontra na versão Alpha 0.0.2")
	embed_info.add_field(name="Criador:",value="Tk#3615",inline=False)
	embed_info.add_field(name="Por que fui criado:",value="Para automatizar os pagamentos do lançamentos, pretendo ser utilizado para mais coisas em um futuro próximo",inline=False)
	embed_info.add_field(name="Ultimas atualizações:",value="Atualização de aparencia\n adicionado o comando /info",inline=False)
	
	await ctx.respond(embed=embed_info)


bot.run(TOKEN)
