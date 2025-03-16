import discord
from discord.ext import commands
import random,os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


organik = ['daun', 'kulit pisang', 'makanan sisa',
           'sayur busuk', 'nasi basi', 'tulang ikan', 
           'ampas kopi', 'kulit telur', 'batang pisang', 
           'kotoran hewan', 'ranting kayu', 'serbuk kayu', 
           'rumput', 'teh celup bekas', 'tisu bekas', 
           'jerami', 'sabut kelapa', 'biji buah', 
           'cangkang udang', 'cangkang kepiting'
           ] 

anorganik =  [
    'plastik', 'botol plastik', 'kaca', 'kaleng', 'besi', 'aluminium', 
    'styrofoam', 'kardus bekas', 'baterai', 'kertas aluminium', 
    'sedotan', 'bungkus makanan', 'tutup botol', 'helm rusak', 
    'ban bekas', 'elektronik bekas', 'lampu neon', 'cd bekas', 
    'dvd bekas', 'kabel', 'paku', 'baut', 'pipa pvc'
    ]

b3 = [
    'oli bekas', 'aki bekas', 'obat kadaluarsa', 'cat tembok', 
    'deterjen', 'pestisida'
    ]


@bot.command()
async def sampah (ctx, * ,item : str = None):

    if item is None: #jika user tidak menyebut nama sampah
        await ctx.send('⚠️ Tolong sebut **nama sampah** setelah command ⚠️')
        await ctx.send('contoh : $sampah plastik')
        return

    #klasifikasi sampah
    if item.lower() in organik:
        await ctx.send(f'🍃{item} adalah **sampah organik** 🍃')
        await ctx.send(f'cara mengolah {item} adalah : ')
        await ctx.send('1.Mengolah Sampah Organik menjadi Pupuk Kompos\n'
        '2.Mengolah Sampah Organik menjadi Biopori')

    elif item.lower() in anorganik:
        await ctx.send(f'♻️{item} adalah **sampah anorganik** ♻️ ')
        await ctx.send(f'cara mengolah {item} adalah : ')
        await ctx.send('1. Recycle (Daur Ulang)\n'
        '2.Reuse (Mengolah Limbah Anorganik dengan Cara Menggunakan Kembali)\n'
        '3.Mengurangi penggunaan bahan anorganik yang sulit terurai')

    elif item.lower() in b3:
        await ctx.send(f'☣️{item} adalah **sampah b3** ☣️')
        await ctx.send(f'cara mengolah {item} adalah : ')
        await ctx.send('1.Daur Ulang\n'
        '2.Pemanfaatan Limbah B3 ')

    else:
        await ctx.send(f'❓{item} sepertinya bukan sampah❓')
