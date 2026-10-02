import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

KAMUS_SAMPAH = {
    "sisa makanan": "Jenis: Organik. Bagus untuk dijadikan pupuk kompos rumah tangga.",
    "daun kering": "Jenis: Organik. Bisa dihancurkan untuk campuran kompos tanaman.",
    
    "plastik": "Jenis: Anorganik. Cuci bersih lalu bawa ke bank sampah untuk didaur ulang.",
    "kertas": "Jenis: Anorganik. Jaga tetap kering agar bisa didaur ulang menjadi kertas baru.",
    
    "baterai": "Jenis: B3. Mengandung kimia beracun, bawa ke tempat pembuangan khusus.",
    "lampu": "Jenis: B3. Mengandung merkuri, bungkus aman agar tidak pecah saat dibuang."
}


@bot.command()
async def pilah(ctx, *, barang: str):
    if barang in KAMUS_SAMPAH:
        await ctx.send(KAMUS_SAMPAH[barang])
    else:
        await ctx.send(f"Sampah {barang} tidak ditemukan. Coba ketik: plastik, kertas, sisa makanan, daun kering, baterai, atau lampu.")

bot.run("TOKEN_BOT_DISCORD_ANDA")